#!/usr/bin/env python3
"""Valida el frontmatter de SKILL.md y que existan los archivos que referencia."""
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "diseno-presentaciones"
md = (SKILL / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", md, re.S)
errores = []
if not m:
    errores.append("SKILL.md sin frontmatter YAML")
else:
    fm = m.group(1)
    nombre = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not nombre or nombre.group(1).strip() != SKILL.name:
        errores.append("name no coincide con el nombre de la carpeta")
    if not desc:
        errores.append("falta description")
    elif len(desc.group(1)) > 1024:
        errores.append(f"description supera 1024 caracteres ({len(desc.group(1))})")
for ref in sorted(set(re.findall(r"`((?:references|scripts)/[\w\-./]+)`", md))):
    if not (SKILL / ref).exists():
        errores.append(f"archivo referenciado no existe: {ref}")
if errores:
    print("\n".join(f"✗ {e}" for e in errores))
    sys.exit(1)
print("✓ SKILL.md válido")
