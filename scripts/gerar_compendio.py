name: Gerar Compêndio

on:
  push:
    branches:
      - main

jobs:
  gerar:
    # Não executa quando o próprio bot gera o compêndio
    if: github.actor != 'github-actions[bot]'

    runs-on: ubuntu-latest

    permissions:
      contents: write

    steps:
      - name: Baixar repositório
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Executar script
        run: python scripts/gerar_compendio.py

      - name: Commit automático
        run: |
          git config user.name "github-actions"
          git config user.email "github-actions@github.com"

          git add Prisioneiros-do-Tempo-Compendio.md

          if git diff --cached --quiet; then
            echo "Nenhuma alteração."
            exit 0
          fi

          git commit -m "Atualiza compêndio automaticamente [skip ci]"

          git pull --rebase origin main

          git push origin HEAD:main
