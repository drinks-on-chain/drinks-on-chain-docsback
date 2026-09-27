"""Extrae los diagramas Mermaid de los documentos y los deja listos para Mermaid Live.

Para cada bloque ```mermaid de los documentos NN-*.md:
  1. escribe diagramas/NN-KK-titulo.mmd con el código puro (sin las marcas de Markdown),
     que se puede pegar tal cual en https://mermaid.live;
  2. añade (o actualiza) debajo del bloque un enlace que abre el diagrama en Mermaid Live
     y otro al archivo .mmd;
  3. regenera diagramas/README.md con el índice.

Uso: python diagramas/generar.py   (desde la raíz del repositorio)
Vuelve a ejecutarlo cada vez que cambie un diagrama.
"""

import base64
import json
import re
import unicodedata
import zlib
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIAGRAMAS = RAIZ / "diagramas"
BLOQUE = re.compile(r"```mermaid\n(.*?)```\n(?:\n?<sub>\[Abrir en Mermaid Live\].*?</sub>\n)?", re.S)
TITULO = re.compile(r"^#{2,4} (.+)$", re.M)


def slug(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    texto = re.sub(r"^[\d.\s·]+", "", texto)
    return re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")[:50] or "diagrama"


def enlace_mermaid_live(codigo: str) -> str:
    estado = {
        "code": codigo,
        "mermaid": json.dumps({"theme": "neutral"}),
        "autoSync": True,
        "updateDiagram": True,
    }
    comprimido = zlib.compress(json.dumps(estado).encode("utf-8"), 9)
    return "https://mermaid.live/edit#pako:" + base64.urlsafe_b64encode(comprimido).decode().rstrip("=")


def main() -> None:
    for viejo in DIAGRAMAS.glob("*.mmd"):
        viejo.unlink()

    indice = []
    for doc in sorted(RAIZ.glob("[0-9][0-9]-*.md")):
        texto = doc.read_text(encoding="utf-8")
        numero = doc.name[:2]
        contador = 0

        def reemplazar(m: re.Match) -> str:
            nonlocal contador
            contador += 1
            codigo = m.group(1)
            titulos = TITULO.findall(texto[: m.start()])
            titulo = titulos[-1].strip() if titulos else doc.stem
            nombre = f"{numero}-{contador:02d}-{slug(titulo)}.mmd"
            (DIAGRAMAS / nombre).write_text(codigo, encoding="utf-8", newline="\n")
            indice.append((doc.name, titulo, nombre, enlace_mermaid_live(codigo)))
            return (
                f"```mermaid\n{codigo}```\n\n"
                f"<sub>[Abrir en Mermaid Live]({enlace_mermaid_live(codigo)}) · "
                f"[código](diagramas/{nombre})</sub>\n"
            )

        nuevo = BLOQUE.sub(reemplazar, texto)
        doc.write_text(nuevo, encoding="utf-8", newline="\n")

    lineas = [
        "# Diagramas",
        "",
        "Código Mermaid puro de cada diagrama de los documentos, generado por `generar.py`.",
        "Para verlo: abre el enlace, o copia el contenido del archivo `.mmd` y pégalo en",
        "[Mermaid Live](https://mermaid.live). No hace falta copiar las líneas `` ```mermaid ``",
        "de los documentos: Mermaid Live no las reconoce.",
        "",
        "| Documento | Sección | Archivo | Ver |",
        "|---|---|---|---|",
    ]
    for doc, titulo, nombre, url in indice:
        lineas.append(f"| {doc} | {titulo} | [{nombre}]({nombre}) | [Mermaid Live]({url}) |")
    (DIAGRAMAS / "README.md").write_text("\n".join(lineas) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(indice)} diagramas")


if __name__ == "__main__":
    main()
