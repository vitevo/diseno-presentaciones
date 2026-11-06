# Diseño de presentaciones · Agent Skill

Skill para Claude que diseña presentaciones nuevas y diagnostica o rediseña presentaciones existentes con los principios de diseño de diapositivas de **Nancy Duarte** (*HBR Guide to Persuasive Presentations*, sección «Las diapositivas»).

> El público tiene un solo canal de atención: si lee, no escucha. La diapositiva acompaña al orador; no es el documento.

## Qué hace

| Modo | Entrada | Salida |
|---|---|---|
| **Crear** | Tema, guion, informe o datos | Guion gráfico (storyboard) → deck terminado con notas del orador |
| **Revisar** | Deck existente (.pptx, PDF o imágenes) | Veredicto, tabla de diagnóstico, propuestas «antes / después» y, si se pide, el rediseño |

Criterios que aplica: prueba del vistazo de tres segundos, una idea por diapositiva, empezar en blanco, guion gráfico con pósits, tipos de diapositiva, orden visual, contraste, espacio en blanco, jerarquía, unidad, datos claros y honestos, conversión de viñetas en diagramas, número de diapositivas y animación con sentido.

## Estructura

```
skills/diseno-presentaciones/
├── SKILL.md                         # Instrucciones principales (modos Crear y Revisar)
├── references/
│   ├── tipos-diapositiva.md         # Entrada, título, navegación, viñetas, cita, datos…
│   ├── organizacion-visual.md       # Orden, contraste, espacio, jerarquía, unidad, animación
│   ├── datos-y-diagramas.md         # Gráficos honestos y de viñetas a diagramas
│   └── checklist-revision.md        # Lista de control para diagnosticar un deck
└── scripts/
    └── auditar_pptx.py              # Detector automático de síntomas en un .pptx
```

## Instalación

### Claude.ai (web, escritorio)
1. Descarga `diseno-presentaciones.skill` desde la sección **Releases** (o genéralo con `tools/empaquetar.sh`).
2. En Claude: **Configuración → Capacidades → Skills → Subir skill**.

### Claude Code — como plugin
```bash
/plugin marketplace add vitevo/diseno-presentaciones
/plugin install diseno-presentaciones@diseno-presentaciones
```

### Claude Code — copia manual
```bash
git clone https://github.com/vitevo/diseno-presentaciones.git
cp -r diseno-presentaciones/skills/diseno-presentaciones ~/.claude/skills/
```

## Uso

No hace falta nombrar el skill; se activa con pedidos como:

- «Convierte este informe en una presentación de 15 minutos para el consejo de facultad».
- «Revisa este PowerPoint de mis estudiantes y dame feedback».
- «Transforma estas viñetas en un diagrama».
- «¿Qué gráfico uso para mostrar estos datos en una diapositiva?»

### Script de auditoría (independiente)

```bash
pip install -r requirements.txt
python skills/diseno-presentaciones/scripts/auditar_pptx.py deck.pptx            # informe legible
python skills/diseno-presentaciones/scripts/auditar_pptx.py deck.pptx --json     # salida JSON
python skills/diseno-presentaciones/scripts/auditar_pptx.py deck.pptx --max-palabras 25 --min-pt 20
```

Detecta palabras y viñetas por diapositiva, segundos estimados de lectura, letra pequeña, número de tipografías y colores, gráficos 3D o circulares, diapositivas saturadas, placeholders vacíos y diapositivas sin notas del orador. Son **síntomas**, no veredictos: conviene confirmar visualmente.

## Desarrollo

```bash
pip install -r requirements.txt
python tests/test_auditar.py     # prueba de humo del script
bash tools/empaquetar.sh         # genera dist/diseno-presentaciones.skill
```

Al publicar una etiqueta `v*` (p. ej. `git tag v1.0.0 && git push --tags`), GitHub Actions valida el skill y adjunta el `.skill` al release.

## Fuente

Duarte, N. (2012). *HBR Guide to Persuasive Presentations*. Harvard Business Review Press. (Ed. en español: *Guía HBR: Presentaciones persuasivas*.)

Los criterios del skill están parafraseados; el repositorio no reproduce el texto del libro.

## Autor

**Victor Omar Vite León** — Pontificia Universidad Católica del Perú (PUCP)
ORCID: [0000-0002-0206-5858](https://orcid.org/0000-0002-0206-5858)

## Licencia

[MIT](LICENSE).
