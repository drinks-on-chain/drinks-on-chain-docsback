"""Comprueba los enlaces relativos de los documentos Markdown del repositorio.

Para cada archivo *.md (fuera de .git) busca enlaces en línea `[texto](destino)`,
imágenes `![alt](destino)` y definiciones de referencia `[id]: destino`, ignorando
los bloques de código y el código en línea. Para cada destino relativo comprueba:
  1. que el archivo o la carpeta existe (relativo al documento que enlaza);
  2. si lleva ancla (`#seccion`) y apunta a un Markdown, que el ancla existe
     con el mismo algoritmo que usa GitHub para los títulos.
Los enlaces absolutos (http, https, mailto, tel) no se comprueban.

Uso: python scripts/comprobar_enlaces.py [raíz]   (por defecto, la raíz del repositorio)
Sale con código 1 si encuentra algún enlace roto.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote

RAIZ = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
EXTERNO = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.I)
BLOQUE_CODIGO = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.S | re.M)
CODIGO_EN_LINEA = re.compile(r"(`+)(?:(?!\1).)+?\1", re.S)
COMENTARIO_HTML = re.compile(r"<!--.*?-->", re.S)
ENLACE = re.compile(r"!?\[(?:[^\[\]]|\[[^\]]*\])*\]\(\s*(<[^>]*>|[^\s()]*(?:\([^\s()]*\)[^\s()]*)*)(?:\s+[\"'(].*?[\"')])?\s*\)")
REFERENCIA = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]*>|\S+)", re.M)
TITULO = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$", re.M)
ANCLA_HTML = re.compile(r"<a\s[^>]*(?:id|name)=[\"']([^\"']+)[\"']", re.I)


def sin_codigo(texto: str) -> str:
    texto = BLOQUE_CODIGO.sub("", texto)
    texto = COMENTARIO_HTML.sub("", texto)
    return CODIGO_EN_LINEA.sub("", texto)


def slug_github(titulo: str) -> str:
    titulo = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", titulo)  # enlaces → su texto
    titulo = re.sub(r"<[^>]+>", "", titulo)  # etiquetas HTML
    titulo = titulo.replace("`", "").strip().lower()
    titulo = re.sub(r"[^\w\- ]", "", titulo)
    return titulo.replace(" ", "-")


_anclas: dict[Path, set[str]] = {}


def anclas(doc: Path) -> set[str]:
    if doc not in _anclas:
        texto = BLOQUE_CODIGO.sub("", doc.read_text(encoding="utf-8"))
        vistos: dict[str, int] = {}
        resultado = set(ANCLA_HTML.findall(texto))
        for _, titulo in TITULO.findall(texto):
            base = slug_github(titulo)
            n = vistos.get(base, 0)
            resultado.add(base if n == 0 else f"{base}-{n}")
            vistos[base] = n + 1
        _anclas[doc] = resultado
    return _anclas[doc]


def comprobar(doc: Path) -> list[str]:
    errores = []
    texto = sin_codigo(doc.read_text(encoding="utf-8"))
    destinos = ENLACE.findall(texto) + REFERENCIA.findall(texto)
    for destino in destinos:
        destino = destino.strip().strip("<>")
        if not destino or EXTERNO.match(destino):
            continue
        ruta, _, ancla = destino.partition("#")
        ruta = unquote(ruta.split("?", 1)[0])
        objetivo = (doc.parent / ruta).resolve() if ruta else doc
        relativo = doc.relative_to(RAIZ).as_posix()
        if not objetivo.exists():
            errores.append(f"{relativo}: no existe «{destino}»")
            continue
        if ancla and objetivo.is_file() and objetivo.suffix.lower() == ".md":
            if unquote(ancla).lower() not in anclas(objetivo):
                errores.append(f"{relativo}: no existe el ancla «#{ancla}» en «{ruta or doc.name}»")
    return errores


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    documentos = sorted(p for p in RAIZ.rglob("*.md") if ".git" not in p.relative_to(RAIZ).parts and "node_modules" not in p.parts)
    errores = [e for doc in documentos for e in comprobar(doc)]
    for error in errores:
        print(error)
    print(f"{len(documentos)} documentos revisados, {len(errores)} enlaces rotos")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
