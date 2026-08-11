# Guia de GitFlow — passo a passo

O GitFlow usa 3 tipos de branch (ramificação):

- **`main`** — só recebe código pronto e testado (versão "final")
- **`develop`** — onde o desenvolvimento acontece, antes de ir pra `main`
- **`feature/nome-da-feature`** — onde você trabalha em UMA funcionalidade
  por vez, sem mexer direto na `develop`

## 1. Iniciar o repositório (só na primeira vez)

```bash
cd atividade_individual_cadastro
git init
git add .
git commit -m "chore: estrutura inicial do projeto"
```

## 2. Criar a branch `main` e a `develop`

Se você já criou o repositório no GitHub, sua branch padrão provavelmente
já se chama `main`. Agora crie a `develop` a partir dela:

```bash
git branch -M main
git checkout -b develop
```

## 3. Criar a branch da feature

Todo o código do robô deve ser desenvolvido dentro de uma branch
`feature/`, nunca direto na `develop` ou na `main`:

```bash
git checkout -b feature/processo-cadastro
```

## 4. Trabalhar e commitar

Vá commitando em pedaços pequenos e com mensagens claras, por exemplo:

```bash
git add config.py
git commit -m "feat: adiciona configurações do robo"

git add email_reader.py
git commit -m "feat: adiciona leitura de e-mails via IMAP"

git add validator.py
git commit -m "feat: adiciona validacao e classificacao de documentos"

git add main.py
git commit -m "feat: adiciona orquestracao do fluxo principal"
```

## 5. Enviar a branch para o GitHub

```bash
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin feature/processo-cadastro
```

(se o `origin` já estiver configurado, pule o `git remote add`)

## 6. Abrir o Pull Request

No GitHub, abra um Pull Request de `feature/processo-cadastro` para
`develop`. Revise as mudanças e faça o merge.

## 7. Atualizar sua develop local

```bash
git checkout develop
git pull origin develop
```

## 8. Quando o processo estiver pronto para entrega

Faça o merge da `develop` na `main` (pode ser direto, ou via outro Pull
Request `develop -> main`, dependendo do que o professor pedir):

```bash
git checkout main
git merge develop
git push origin main
```

## Resumo visual

```
feature/processo-cadastro
        ↓ (Pull Request)
     develop
        ↓ (merge quando pronto)
       main
```

## Dicas rápidas

- `git status` — mostra em qual branch você está e o que mudou
- `git branch` — lista todas as branches locais
- `git log --oneline` — mostra o histórico de commits de forma resumida
- Nunca trabalhe direto na `main`; sempre passe pela `feature/` e depois
  pela `develop`
