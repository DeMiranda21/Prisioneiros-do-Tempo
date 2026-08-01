from pathlib import Path

# Ordem dos arquivos que formarão o compêndio
arquivos = [
    "README.md",
    "01 - Regras e Mecânicas.md",
    "02 - Personagens.md",
    "03 - Mapas.md",
    "04 - Lore.md",
    "05 - Backlog.md",
]

saida = Path("Prisioneiros-do-Tempo-Compendio.md")

with saida.open("w", encoding="utf-8") as compendio:

    compendio.write("# Prisioneiros do Tempo\n")
    compendio.write("## Compêndio Automático\n\n")
    compendio.write("---\n\n")

    for arquivo in arquivos:

        caminho = Path(arquivo)

        if not caminho.exists():
            print(f"{arquivo} não encontrado.")
            continue

        compendio.write(f"\n\n---\n\n")
        compendio.write(f"<!-- INÍCIO {arquivo} -->\n\n")

        compendio.write(caminho.read_text(encoding="utf-8"))

        compendio.write(f"\n\n<!-- FIM {arquivo} -->\n")
