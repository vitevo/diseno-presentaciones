#!/usr/bin/env python3
"""Prueba de humo: crea un deck con problemas conocidos y verifica que el script los detecte."""
import subprocess
import sys
import tempfile
from pathlib import Path

from pptx import Presentation
from pptx.util import Pt

SCRIPT = Path(__file__).resolve().parent.parent / "skills/diseno-presentaciones/scripts/auditar_pptx.py"

with tempfile.TemporaryDirectory() as d:
    deck = Path(d) / "prueba.pptx"
    prs = Presentation()
    s = prs.slides.add_slide(prs.slide_layouts[1])
    s.shapes.title.text = "Diapositiva saturada"
    tf = s.placeholders[1].text_frame
    tf.text = "palabra " * 40
    for i in range(5):
        r = tf.add_paragraph().add_run()
        r.text = f"viñeta {i}"
        r.font.size = Pt(14)
    prs.save(deck)

    out = subprocess.run([sys.executable, str(SCRIPT), str(deck)],
                         capture_output=True, text=True, check=True).stdout
    for esperado in ("A1 vistazo", "A10 viñetas", "A4 letra pequeña", "Sin notas del orador"):
        assert esperado in out, f"No se detectó: {esperado}\n{out}"
print("✓ auditar_pptx.py detecta los síntomas esperados")
