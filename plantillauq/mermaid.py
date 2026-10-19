"""Pre-renderiza los diagramas Mermaid de una presentación Marp a SVG incrustado.

Uso (lo invoca tema/render.sh; no suele llamarse a mano):
  python3 tema/mermaid.py <entrada.md> <salida.md> <carpeta-temporal>

Reconoce los dos modos de escribir un diagrama en las presentaciones del curso:

  <div class="mermaid" style="…">   …código…   </div>      (el que usan los decks)
  ```mermaid                        …código…   ```          (el de los documentos)

Cada bloque se renderiza con Mermaid CLI (`mmdc`, o la variable MMDC) y el SVG se incrusta
tal cual en el Markdown de salida, conservando el `style` del div original (los
`transform: scale(…)` con los que se ajustan los diagramas a la diapositiva siguen aplicando).
Al incrustarlo no quedan archivos sueltos ni dependencias de red: sirve igual para pdf, pptx y html.

Si existe `tema/mermaid.json` se usa como configuración de Mermaid (tema, colores, tipografía).
"""

import os
import re
import subprocess
import sys
from pathlib import Path

MMDC = os.environ.get("MMDC", "mmdc")
TEMA = Path(__file__).resolve().parent
CONFIG = TEMA / "mermaid.json"

# <div class="mermaid" …>código</div>  y  ```mermaid\ncódigo\n```
BLOQUES = re.compile(
    r'<div\s+class="mermaid"([^>]*)>(.*?)</div>|^```mermaid[ \t]*\n(.*?)^```[ \t]*$',
    re.S | re.M,
)
ESTILO = re.compile(r'style="([^"]*)"')


def codigo(bloque: str) -> str:
    """Devuelve el código Mermaid listo para `mmdc`: entidades HTML y saltos de línea resueltos."""
    texto = bloque.strip()
    for entidad, caracter in (("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&amp;", "&")):
        texto = texto.replace(entidad, caracter)
    # Las etiquetas de los decks parten línea con `\n`. Mermaid 11 solo lo respeta en algunos
    # tipos de diagrama (en los de secuencia lo imprime tal cual); `<br/>` funciona en todos.
    return texto.replace("\\n", "<br/>")


def svg(fuente: str, tmp: Path, n: int) -> str:
    """Renderiza un diagrama y devuelve el SVG como texto (con un id único por diagrama)."""
    entrada, salida = tmp / f"mermaid-{n}.mmd", tmp / f"mermaid-{n}.svg"
    entrada.write_text(fuente, encoding="utf-8")
    orden = [MMDC, "-q", "-i", str(entrada), "-o", str(salida), "-b", "transparent",
             "-I", f"diagrama-{n}"]
    if CONFIG.exists():
        orden += ["-c", str(CONFIG)]
    try:
        subprocess.run(orden, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit(f"❌ No se encontró Mermaid CLI ('{MMDC}'). Instálelo con: npm i -g @mermaid-js/mermaid-cli")
    except subprocess.CalledProcessError as e:
        sys.exit(f"❌ Error al renderizar el diagrama {n}:\n{e.stderr or e.stdout}")
    texto = salida.read_text(encoding="utf-8")
    return re.sub(r"^<\?xml[^>]*\?>\s*", "", texto)  # Marp no necesita la declaración XML.


def main():
    origen, destino, tmp = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    md = origen.read_text(encoding="utf-8")
    n = 0

    def reemplazo(m: re.Match) -> str:
        nonlocal n
        n += 1
        atributos, cuerpo = (m.group(1), m.group(2)) if m.group(2) is not None else ("", m.group(3))
        estilo = ESTILO.search(atributos or "")
        estilo = estilo.group(1) if estilo else "text-align: center;"
        # La clase cambia a `mermaid-svg`: el diagrama ya está dibujado y nada debe reprocesarlo.
        return f'<div class="mermaid-svg" style="{estilo}">{svg(codigo(cuerpo), tmp, n)}</div>'

    destino.write_text(BLOQUES.sub(reemplazo, md), encoding="utf-8")
    if n:
        print(f"🎨 {n} diagrama(s) Mermaid renderizado(s)")


if __name__ == "__main__":
    main()
