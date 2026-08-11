# Robô de Cadastro — Portal Fake

Automação individual que acessa uma caixa de e-mail, identifica
solicitações de cadastro (assunto **"cadastro portal fake"**), baixa os
documentos anexados, valida se a documentação está completa (ficha de
cadastro, documento com foto e comprovante de residência) e organiza os
arquivos em `documentos_ok` ou `documentos_pendentes` de acordo com o
resultado.

## Arquivos

| Arquivo | Responsabilidade |
|---|---|
| `config.py` | Configurações e regras de negócio (assunto alvo, documentos obrigatórios, pastas) |
| `email_reader.py` | Conecta no e-mail via IMAP, filtra pelo assunto e baixa os anexos |
| `validator.py` | Valida a documentação e move os arquivos para a pasta correta |
| `main.py` | Orquestra o fluxo completo |
| `PDD.md` | PDD simplificado do processo |
| `GITFLOW.md` | Passo a passo de GitFlow para versionar o projeto |

## Setup

1. Ative o IMAP na conta do Gmail (Configurações → Encaminhamento e
   POP/IMAP).
2. Gere uma senha de app (Conta Google → Segurança → Senhas de app).
3. Exporte as credenciais:
   ```bash
   export CADASTRO_EMAIL="seuemail@gmail.com"
   export CADASTRO_EMAIL_SENHA="sua_senha_de_app"
   ```

## Uso

```bash
python main.py
```

O robô processa os e-mails não lidos com assunto "cadastro portal fake" e
organiza os documentos automaticamente.
