from pathlib import Path
from datetime import datetime
import subprocess

# ==============================
# CONFIGURAÇÕES
# ==============================

ARQUIVO_SAIDA = "Prisioneiros-do-Tempo-Compendio.md"

IGNORAR_PASTAS = {
    ".git",
    ".github",
    "scripts",
}

IGNORAR_ARQUIVOS = {
    ARQUIVO_SAIDA,
}

# ==============================
# BUSCA DOS DOCUMENTOS
# ==============================

arquivos = []

for arquivo in Path(".").glob("*.md"):

    if arquivo.name in IGNORAR_ARQUIVOS:
        continue

    arquivos.append(arquivo)

arquivos.sort(key=lambda a: a.name.lower())

# ==============================
# INFORMAÇÕES DO REPOSITÓRIO
# ==============================

try:
    commit = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        text=True
    ).strip()
except Exception:
    commit = "desconhecido"

data = datetime.now().strftime("%d/%m/%Y %H:%M")

# ==============================
# GERAÇÃO DO COMPÊNDIO
# ==============================

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as out:

    out.write("# Prisioneiros do Tempo\n\n")

    out.write("## Compêndio Oficial\n\n")

    out.write(
        "Este documento é gerado automaticamente pelo GitHub Actions.\n\n"
    )

    out.write(
        "Sempre que houver conflito entre este documento e qualquer conversa, "
        "este documento deve ser considerado a fonte oficial do projeto.\n\n"
    )

    out.write("---\n\n")

    out.write(f"**Gerado em:** {data}\n\n")

    out.write(f"**Commit:** `{commit}`\n\n")

    out.write(f"**Quantidade de documentos:** {len(arquivos)}\n\n")

    out.write("---\n\n")

    out.write("# Índice\n\n")

    for arquivo in arquivos:

        titulo = arquivo.stem

        ancora = (
            titulo
            .lower()
            .replace(" ", "-")
            .replace(".", "")
        )

        out.write(f"- [{titulo}](#{ancora})\n")

    out.write("\n\n---\n")

    for arquivo in arquivos:

        titulo = arquivo.stem

        out.write("\n\n")
        out.write("=" * 70)
        out.write("\n\n")

        out.write(f"# {titulo}\n\n")

        out.write(
            arquivo.read_text(
                encoding="utf-8"
            )
        )

        out.write("\n\n")
