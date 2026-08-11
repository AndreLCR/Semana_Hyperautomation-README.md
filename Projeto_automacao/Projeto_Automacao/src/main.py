"""
Robô de Cadastro - Portal Fake

Fluxo:
Acessar e-mail -> Encontrar mensagens "cadastro portal fake" ->
Baixar anexos -> Validar documentos -> Mover para documentos_ok ou
documentos_pendentes
"""
from email_reader import buscar_solicitacoes_cadastro, ConexaoEmailError
from validator import validar_documentacao, classificar_arquivos


def processar_cadastros():
    try:
        solicitacoes = buscar_solicitacoes_cadastro()
    except ConexaoEmailError as e:
        print(f"[ERRO] {e}")
        return

    print(f"{len(solicitacoes)} solicitação(ões) de cadastro encontrada(s).")

    for s in solicitacoes:
        remetente, anexos = s["remetente"], s["anexos"]

        completo, faltantes = validar_documentacao(anexos)
        pasta_destino = classificar_arquivos(remetente, anexos, completo)

        if completo:
            print(f"[OK] {remetente} -> documentação completa ({pasta_destino})")
        else:
            print(f"[PENDENTE] {remetente} -> faltando: {', '.join(faltantes)} ({pasta_destino})")


if __name__ == "__main__":
    processar_cadastros()
