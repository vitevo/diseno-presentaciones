#!/usr/bin/env python3
"""Auditoría rápida de un .pptx con los criterios de diseño de diapositivas de Duarte.

Detecta síntomas (no emite juicios definitivos):
  - palabras y viñetas por diapositiva, segundos estimados de lectura (250 ppm)
  - tamaños de letra pequeños (< 18 pt por defecto, ajustable con --min-pt)
  - número de tipografías y colores de texto en todo el deck
  - gráficos 3D y gráficos circulares
  - diapositivas con muchos elementos
  - placeholders vacíos de plantilla

Uso:
    python auditar_pptx.py deck.pptx [--json] [--max-palabras 30]
"""
import argparse
import json
import re
import sys
from collections import Counter

try:
    from pptx import Presentation
    from pptx.util import Pt
    from pptx.enum.shapes import MSO_SHAPE_TYPE
except ImportError:
    sys.exit("Falta python-pptx: pip install python-pptx")

PPM = 250  # palabras por minuto de lectura


def iter_shapes(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from iter_shapes(sh.shapes)
        else:
            yield sh


def color_of(run):
    try:
        c = run.font.color
        if c and c.type is not None and c.rgb is not None:
            return str(c.rgb)
    except (AttributeError, TypeError):
        pass
    return None


def is_title(shape):
    try:
        if shape.is_placeholder:
            return shape.placeholder_format.type in (1, 3)  # TITLE, CENTER_TITLE
    except (AttributeError, ValueError):
        pass
    return False


def chart_info(shape):
    try:
        ch = shape.chart
    except (AttributeError, ValueError):
        return None
    xml = ch._chartSpace.xml
    tipos = re.findall(r"<c:(\w+Chart)>", xml)
    tipos = [t for t in tipos if t != "plotArea"]
    return {"tipos": tipos, "3d": any("3D" in t for t in tipos)}


def auditar(path, max_palabras=30, min_pt=18):
    prs = Presentation(path)
    fuentes = Counter()
    colores = Counter()
    diapos = []
    for i, slide in enumerate(prs.slides, start=1):
        palabras = 0
        palabras_titulo = 0
        vinetas = 0
        tam_pequenos = set()
        graficos = []
        n_elem = 0
        vacios = 0
        imagenes = 0
        titulo = ""
        primer_texto = ""
        for sh in iter_shapes(slide.shapes):
            # elemento = bloque de contenido (texto, imagen, gráfico, tabla), no formas decorativas vacías
            tiene_texto = getattr(sh, "has_text_frame", False) and sh.text_frame.text.strip()
            if tiene_texto or sh.shape_type == MSO_SHAPE_TYPE.PICTURE or getattr(sh, "has_chart", False) \
                    or getattr(sh, "has_table", False):
                n_elem += 1
            if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
                imagenes += 1
            ci = chart_info(sh) if getattr(sh, "has_chart", False) else None
            if ci:
                graficos.append(ci)
            if not getattr(sh, "has_text_frame", False):
                continue
            texto = sh.text_frame.text.strip()
            if not texto:
                if getattr(sh, "is_placeholder", False):
                    vacios += 1
                continue
            tit = is_title(sh)
            n = len(texto.split())
            if tit:
                palabras_titulo += n
                titulo = titulo or texto.replace("\n", " ")[:80]
            else:
                palabras += n
                primer_texto = primer_texto or texto.replace("\n", " ")[:80]
            parrafos = [p for p in sh.text_frame.paragraphs if p.text.strip()]
            # viñetas = párrafos dentro de un mismo cuadro con 3+ párrafos (no etiquetas de diagrama sueltas)
            if not tit and len(parrafos) >= 3:
                vinetas += len(parrafos)
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if r.font.name:
                        fuentes[r.font.name] += 1
                    c = color_of(r)
                    if c:
                        colores[c] += 1
                    if r.font.size and not tit and r.font.size < Pt(min_pt) and r.text.strip():
                        tam_pequenos.add(round(r.font.size.pt))
        total = palabras + palabras_titulo
        seg = round(total / PPM * 60)
        alertas = []
        if total > max_palabras:
            alertas.append(f"A1 vistazo: {total} palabras (~{seg} s de lectura)")
        if vinetas >= 5:
            alertas.append(f"A10 viñetas: {vinetas} párrafos/viñetas")
        if tam_pequenos:
            alertas.append(f"A4 letra pequeña: {sorted(tam_pequenos)} pt")
        if n_elem >= 10:
            alertas.append(f"A7 espacio: {n_elem} bloques de contenido (en diagramas puede ser normal)")
        for g in graficos:
            if g["3d"]:
                alertas.append(f"B3 gráfico 3D: {g['tipos']}")
            if any(t.startswith("pie") or t.startswith("doughnut") for t in g["tipos"]):
                alertas.append(f"B4 circular: revisar si comunica ({g['tipos']})")
        if len(graficos) > 1:
            alertas.append(f"A2 una idea: {len(graficos)} gráficos en la diapositiva")
        # agrupar alertas repetidas (p. ej., varios gráficos 3D)
        cnt = Counter(alertas)
        alertas = [a if n == 1 else f"{a} ×{n}" for a, n in cnt.items()]
        if vacios:
            alertas.append(f"A3 plantilla: {vacios} placeholder(s) vacíos")
        diapos.append({
            "diapositiva": i, "titulo": titulo or primer_texto, "palabras": total,
            "segundos_lectura": seg, "vinetas": vinetas, "elementos": n_elem,
            "imagenes": imagenes, "graficos": graficos,
            "notas_orador": bool(slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip()),
            "alertas": alertas,
        })
    deck_alertas = []
    if len(fuentes) > 2:
        deck_alertas.append(f"C1 unidad: {len(fuentes)} tipografías explícitas {list(fuentes)}")
    if len(colores) > 5:
        deck_alertas.append(f"C1 unidad: {len(colores)} colores de texto explícitos")
    seg_total = sum(d["segundos_lectura"] for d in diapos)
    return {
        "archivo": path, "n_diapositivas": len(diapos),
        "palabras_totales": sum(d["palabras"] for d in diapos),
        "minutos_lectura_totales": round(seg_total / 60, 1),
        "diapos_sin_notas": [d["diapositiva"] for d in diapos if not d["notas_orador"]],
        "tipografias": dict(fuentes), "colores_texto": dict(colores),
        "alertas_deck": deck_alertas, "diapositivas": diapos,
    }


def imprimir(r):
    print(f"Auditoría: {r['archivo']}")
    print(f"Diapositivas: {r['n_diapositivas']} · palabras proyectadas: {r['palabras_totales']}"
          f" · lectura total estimada: {r['minutos_lectura_totales']} min (tiempo que el público no escucha)")
    if r["tipografias"]:
        print(f"Tipografías explícitas: {', '.join(r['tipografias'])}")
    for a in r["alertas_deck"]:
        print(f"  ! {a}")
    print()
    for d in r["diapositivas"]:
        cab = f"[{d['diapositiva']:>2}] {d['titulo'] or '(sin título)'} — {d['palabras']} pal., {d['elementos']} elem."
        print(cab)
        for a in d["alertas"]:
            print(f"     ! {a}")
    sin = r["diapos_sin_notas"]
    if sin:
        print(f"\nSin notas del orador: {sin}")
    print("\nNota: son síntomas automáticos; confirmar visualmente antes de concluir.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--max-palabras", type=int, default=30)
    ap.add_argument("--min-pt", type=int, default=18, help="tamaño mínimo aceptable (pt) fuera de títulos")
    a = ap.parse_args()
    res = auditar(a.pptx, a.max_palabras, a.min_pt)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        imprimir(res)
