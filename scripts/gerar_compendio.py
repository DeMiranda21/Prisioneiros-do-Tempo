from pathlib import Path
from datetime import datetime
import subprocess

# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

ARQUIVO_SAIDA = "Prisioneiros-do-Tempo-Compendio.md"

IGNORAR_PASTAS = {
    ".git",
    ".github",
    "scripts",
    "__pycache__",
    ".venv",
}

IGNORAR_ARQUIVOS = {
    ARQUIVO_SAIDA,
}

# ==========================================================
# LOCALIZA TODOS OS MARKDOWN DO PROJETO
# ==========================================================

arquivos = []

for arquivo in Path(".").rglob("*.md"):

    if arquivo.name in IGNORAR_ARQUIVOS:
        continue

    if any(parte in IGNORAR_PASTAS for parte in arquivo.parts):
        continue

    arquivos.append(arquivo)

arquivos.sort(key=lambda p: str(p).lower())

# ==========================================================
# INFORMAÇÕES DO REPOSITÓRIO
# ==========================================================

try:
    commit = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        text=True
    ).strip()
except Exception:
    commit = "desconhecido"

data = datetime.now().strftime("%d/%m/%Y %H:%M UTC")

# ==========================================================
# GERAÇÃO DO COMPÊNDIO
# ==========================================================

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as out:

    out.write("# Prisioneiros do Tempo\n\n")

    out.write("## Compêndio Oficial\n\n")

    out.write(
        "Este documento é gerado automaticamente pelo GitHub Actions.\n\n"
    )

    out.write("---\n\n")

    out.write("# Contexto Oficial para IA\n\n")

    out.write(
        "Este documento representa a documentação oficial do projeto "
        "**Prisioneiros do Tempo**.\n\n"
    )

    out.write(
        "Sempre que houver conflito entre este documento e qualquer "
        "conversa anterior, este documento prevalece.\n\n"
    )

    out.write(
        "Novas ideias discutidas em conversa somente passam a fazer parte "
        "do projeto após aprovação do autor e atualização da documentação "
        "oficial.\n\n"
    )

    out.write("---\n\n")

    out.write(f"**Gerado em:** {data}\n\n")
    out.write(f"**Commit:** `{commit}`\n\n")
    out.write(f"**Quantidade de documentos:** {len(arquivos)}\n\n")

    out.write("---\n\n")

    out.write("# Índice\n\n")

    for arquivo in arquivos:

        caminho = arquivo.as_posix()

        ancora = (
            caminho
            .lower()
            .replace("/", "")
            .replace("\\", "")
            .replace(".", "")
            .replace(" ", "-")
        )

        out.write(f"- [{caminho}](#{ancora})\n")

    out.write("\n\n---\n")

    # ======================================================
    # DOCUMENTOS
    # ======================================================

    for arquivo in arquivos:

        caminho = arquivo.as_posix()

        ancora = (
            caminho
            .lower()
            .replace("/", "")
            .replace("\\", "")
            .replace(".", "")
            .replace(" ", "-")
        )

        out.write("\n\n")
        out.write("=" * 80)
        out.write("\n\n")

        out.write(f'<a id="{ancora}"></a>\n\n')

        out.write(f"# {caminho}\n\n")

        out.write(
            f"*Arquivo original:* `{caminho}`\n\n"
        )

        out.write("---\n\n")

        out.write(
            arquivo.read_text(
                encoding="utf-8"
            )
        )

        out.write("\n\n")
