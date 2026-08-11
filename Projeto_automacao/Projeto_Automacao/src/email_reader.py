"""
Responsável por: acessar o e-mail, encontrar as mensagens de cadastro
(assunto "cadastro portal fake") e baixar os anexos.
"""
import imaplib
import email
from email.header import decode_header
import os

import config


class ConexaoEmailError(Exception):
    """Erro ao conectar ou logar na caixa de e-mail."""
    pass


def conectar_imap():
    try:
        imap = imaplib.IMAP4_SSL(config.IMAP_SERVER)
        imap.login(config.EMAIL_USER, config.EMAIL_PASS)
        imap.select("inbox")
        return imap
    except (imaplib.IMAP4.error, OSError) as e:
        raise ConexaoEmailError(f"Não foi possível conectar/logar no e-mail: {e}")


def buscar_solicitacoes_cadastro():
    """Retorna uma lista de dicts: {remetente, assunto, anexos: [caminhos]}
    apenas para e-mails cujo assunto contenha 'cadastro portal fake'."""
    imap = conectar_imap()
    status, mensagens = imap.search(None, "UNSEEN")
    solicitacoes = []

    for num in mensagens[0].split():
        try:
            status, dados = imap.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(dados[0][1])

            assunto = _decodificar_assunto(msg.get("Subject") or "")
            if config.ASSUNTO_ALVO not in assunto.lower():
                continue  # não é um e-mail de cadastro, ignora

            remetente = email.utils.parseaddr(msg.get("From"))[1]
            anexos = _baixar_anexos(msg, remetente)

            solicitacoes.append({
                "remetente": remetente,
                "assunto": assunto,
                "anexos": anexos,
            })
        except Exception as e:
            # um e-mail com problema não pode travar o processamento dos demais
            print(f"[AVISO] Erro ao processar um e-mail, pulando para o próximo: {e}")
            continue

    imap.close()
    imap.logout()
    return solicitacoes


def _decodificar_assunto(assunto_raw):
    trecho, encoding = decode_header(assunto_raw)[0]
    if isinstance(trecho, bytes):
        trecho = trecho.decode(encoding or "utf-8", errors="ignore")
    return trecho


def _baixar_anexos(msg, remetente):
    pasta_cliente = os.path.join(config.PASTA_DOWNLOADS, remetente.split("@")[0])
    os.makedirs(pasta_cliente, exist_ok=True)

    caminhos = []
    for parte in msg.walk():
        if parte.get_content_disposition() != "attachment":
            continue

        nome_arquivo = parte.get_filename()
        if not nome_arquivo:
            continue

        try:
            conteudo = parte.get_payload(decode=True)
            if not conteudo:
                continue  # anexo vazio/corrompido, ignora

            caminho = os.path.join(pasta_cliente, nome_arquivo)
            with open(caminho, "wb") as f:
                f.write(conteudo)
            caminhos.append(caminho)
        except OSError as e:
            print(f"[AVISO] Não foi possível salvar o anexo {nome_arquivo}: {e}")

    return caminhos
