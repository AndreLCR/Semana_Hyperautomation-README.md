import os

# ==== Credenciais (defina como variáveis de ambiente, NUNCA no código) ====
# No Gmail é preciso gerar uma "senha de app" (App Password) em
# Conta Google > Segurança > Senhas de app — a senha normal não funciona
# com IMAP.
EMAIL_USER = os.getenv("CADASTRO_EMAIL", "alcarvalho407@gmail.com")
EMAIL_PASS = os.getenv("CADASTRO_EMAIL_SENHA", "andrecarvalho")

IMAP_SERVER = "imap.gmail.com"

# ==== Regra de negócio: assunto que identifica um e-mail de cadastro ====
ASSUNTO_ALVO = "cadastro portal fake"

# ==== Regra de negócio: documentos obrigatórios ====
# Um documento é considerado presente se essa palavra aparecer no nome do
# arquivo anexado (case-insensitive).
DOCUMENTOS_OBRIGATORIOS = ["ficha_cadastro", "documento_foto", "comprovante_residencia"]

# ==== Pastas locais ====
PASTA_DOWNLOADS = "documentos_recebidos"
PASTA_OK = "documentos_ok"
PASTA_PENDENTES = "documentos_pendentes"
