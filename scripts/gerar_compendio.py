from pathlib import Path
from datetime import datetime
import subprocess

# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

PASTA_SAIDA = Path("generated")
PASTA_SAIDA.mkdir(exist_ok=True)

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

    out.write("=" * 80 + "\n")
    out.write("PRISIONEIROS DO TEMPO\n")
    out.write("CONTEXTO OFICIAL DO PROJETO\n")
    out.write("=" * 80 + "\n\n")

    out.write("INSTRUÇÕES PARA A IA\n")
    out.write("-" * 80 + "\n\n")

    out.write(
        "Este arquivo foi gerado automaticamente a partir da documentação "
        "oficial do repositório GitHub.\n\n"
    )

    out.write(
        "Ao responder qualquer pergunta sobre o projeto, siga rigorosamente "
        "as instruções abaixo.\n\n"
    )

    out.write("1. Este documento é a única fonte oficial do projeto.\n\n")

    out.write(
        "2. Caso exista qualquer conflito entre este documento, memória da "
        "conversa ou conhecimento do modelo, este documento prevalece.\n\n"
    )

    out.write(
        "3. Nunca apresente inferências como fatos documentados.\n\n"
    )

    out.write(
        "4. Caso determinada informação não esteja documentada, informe isso "
        "explicitamente.\n\n"
    )

    out.write(
        "5. Toda nova mecânica, personagem, mapa ou regra discutida deve ser "
        "tratada apenas como PROPOSTA até aprovação explícita do autor.\n\n"
    )

    out.write(
        "6. Após aprovação, a proposta somente passa a fazer parte oficial do "
        "projeto quando for incorporada à documentação do repositório.\n\n"
    )

    out.write(
        "7. Preserve a consistência entre regras, personagens, mapas, lore e "
        "filosofia de design.\n\n"
    )

    out.write(
        "8. Evite aumentar a complexidade sem ganho claro de jogabilidade.\n\n"
    )

    out.write(
        "9. Sempre que sugerir uma alteração, identifique claramente se ela "
        "é uma regra oficial ou apenas uma proposta de design.\n\n"
    )

    out.write(
        "10. Quando possível, fundamente as respostas indicando em qual "
        "documento a informação está registrada.\n\n"
    )

    out.write("-" * 80 + "\n\n")

    out.write(f"Gerado em: {data}\n")
    out.write(f"Commit: {commit}\n")
    out.write(f"Documentos encontrados: {len(arquivos)}\n\n")

    out.write("=" * 80 + "\n")
    out.write("ÍNDICE\n")
    out.write("=" * 80 + "\n\n")

    # ======================================================
    # DOCUMENTOS
    # ======================================================

    for arquivo in arquivos:

        caminho = arquivo.as_posix()

        out.write("\n\n")
        out.write("=" * 80 + "\n")
        out.write(f"ARQUIVO: {caminho}\n")
        out.write("=" * 80 + "\n\n")

        conteudo = arquivo.read_text(encoding="utf-8")

        out.write(conteudo)

        if not conteudo.endswith("\n"):
            out.write("\n")

        out.write("\n")
