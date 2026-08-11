"""
Responsável por: validar se os documentos obrigatórios estão presentes e
mover os arquivos para documentos_ok ou documentos_pendentes.
"""
import os
import shutil

import config


def validar_documentacao(anexos):
    """Verifica se todos os documentos obrigatórios estão presentes.

    Regra de negócio: cada documento obrigatório (ficha_cadastro,
    documento_foto, comprovante_residencia) precisa aparecer no nome de
    pelo menos um arquivo anexado, sem diferenciar maiúsculas/minúsculas.
    """
    nomes = [os.path.basename(a).lower() for a in anexos]
    faltantes = [
        doc for doc in config.DOCUMENTOS_OBRIGATORIOS
        if not any(doc in nome for nome in nomes)
    ]
    return len(faltantes) == 0, faltantes


def classificar_arquivos(remetente, anexos, completo):
    """Move os arquivos para documentos_ok ou documentos_pendentes, em uma
    subpasta com o nome do remetente."""
    destino_base = config.PASTA_OK if completo else config.PASTA_PENDENTES
    pasta_destino = os.path.join(destino_base, remetente.split("@")[0])
    os.makedirs(pasta_destino, exist_ok=True)

    for caminho in anexos:
        try:
            destino = os.path.join(pasta_destino, os.path.basename(caminho))
            shutil.move(caminho, destino)
        except OSError as e:
            print(f"[AVISO] Não foi possível mover o arquivo {caminho}: {e}")

    return pasta_destino
