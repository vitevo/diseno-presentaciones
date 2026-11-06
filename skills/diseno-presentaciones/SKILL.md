---
name: diseno-presentaciones
description: Diseña presentaciones nuevas y diagnostica o rediseña presentaciones existentes aplicando los principios de diseño de diapositivas de Nancy Duarte (Guía HBR, sección «Las diapositivas») — prueba del vistazo de tres segundos, una idea por diapositiva, guion gráfico con pósits, tipos de diapositiva, orden visual, contraste, espacio en blanco, jerarquía, unidad, datos claros y honestos, conversión de viñetas en diagramas, número de diapositivas y animación con sentido. Úsalo siempre que el usuario pida crear, planificar, mejorar, revisar, auditar, "limpiar" o rediseñar un deck, una presentación, diapositivas o un PowerPoint (.pptx), convertir un texto o informe en diapositivas, transformar viñetas en un diagrama, elegir el gráfico adecuado para unos datos en una diapositiva, o dar feedback sobre diapositivas de estudiantes o colegas, aunque no mencione a Duarte. No usar para redactar el discurso hablado sin diapositivas ni para pósters impresos.
---

# Diseño de presentaciones (principios de Duarte)

Este skill convierte los principios de la sección «Las diapositivas» de Duarte (*Guía HBR: Presentaciones persuasivas*) en un método de trabajo. Tiene dos modos que comparten los mismos criterios:

- **Crear**: de un tema, guion, informe o datos a un deck terminado.
- **Revisar**: de un deck existente a un diagnóstico con propuestas «antes / después» y, si se pide, la versión rediseñada.

La idea de fondo que conviene no perder de vista: el público tiene un solo canal de atención. Si lee, no escucha. Por eso la diapositiva acompaña al orador; no es el documento. Casi todas las decisiones de abajo se derivan de eso.

## Principios núcleo (resumen operativo)

1. **Prueba del vistazo (3 segundos).** Cada diapositiva debe captarse en unos tres segundos, como una valla publicitaria que se mira de reojo al conducir. Si exige leer, compite con el orador.
   - Cálculo útil para justificarlo ante el usuario: a ~250 palabras/minuto de lectura, una diapositiva de ~80 palabras roba ~20 s de atención; multiplicado por todas las diapositivas, el público pierde una fracción grande de la charla leyendo.
2. **Una idea por diapositiva.** Las diapositivas no cuestan nada; si una contiene un gráfico, una cita, una lista y un diagrama, se parte en varias y se elimina lo que sobra.
3. **Empezar en blanco.** Nada de plantillas por defecto con «Haz clic para añadir texto». Cada elemento (logo, franjas, ondas decorativas) entra solo si aporta significado.
4. **Texto mínimo y grande.** Frases cortas, tipografía tan grande como se pueda para que se lea desde el fondo de la sala.
5. **Coherencia visual.** Una tipografía (dos como máximo), paleta de tres colores complementarios más uno o dos neutros, fotos que parezcan del mismo fotógrafo, ilustraciones del mismo estilo.
6. **Tamaño = importancia.** El público interpreta lo más grande como lo más importante; alinear y dimensionar con intención.
7. **Pensar como diseñador**, no como redactor de documentos: elegir elementos visuales que transmitan significado y evitar clichés visuales (diana para «objetivos», apretón de manos sobre el globo para «alianza», candado para «seguridad»). Descartar las primeras ideas que vienen a la mente: suelen ser las de todos.

Los detalles de cada bloque están en `references/`:

| Archivo | Cuándo leerlo |
|---|---|
| `references/tipos-diapositiva.md` | Al planificar la secuencia o asignar un tipo a cada diapositiva |
| `references/organizacion-visual.md` | Al componer cada diapositiva (orden, contraste, espacio en blanco, jerarquía, unidad) y al decidir número de diapositivas y animaciones |
| `references/datos-y-diagramas.md` | Cuando haya cifras, gráficos, tablas o listas de viñetas relacionadas que convenga diagramar |
| `references/checklist-revision.md` | En el modo Revisar, y como control final en el modo Crear |

## Modo Crear

### 1. Entender el encargo
Antes de diseñar, aclarar (preguntando solo lo que falte y cambie el resultado):
- Público, contexto (sala, virtual, se enviará por correo, se publicará en línea) y duración.
- El mensaje central: qué debe recordar o hacer el público al salir.
- Material disponible: texto, datos, imágenes, identidad visual institucional.

El contexto decide la densidad. Para una charla en vivo se aplica la prueba del vistazo con todo rigor. Si el deck se leerá sin orador (enviado por correo), puede llevar algo más de texto, pero conviene sugerir separar «diapositivas para proyectar» y «documento de apoyo» en lugar de abarrotar las diapositivas. Algunas situaciones piden cero diapositivas (brindis, homenaje, anuncio delicado, charla breve e informal): dilo si es el caso.

### 2. Guion gráfico antes que diapositivas
Como un cineasta que dibuja sus planos antes de rodar: primero se esboza, luego se produce. Entregar al usuario una tabla de guion gráfico (storyboard) para validar el flujo antes de construir:

| N.º | Tipo | Idea única (una frase) | Elemento visual | Notas del orador |
|---|---|---|---|---|

- Una fila = una idea. Si una idea no cabe en una frase corta o en un boceto pequeño (el equivalente a un pósit), es demasiado compleja: dividirla o buscar otra forma de decirla.
- Asignar a cada fila un tipo de `references/tipos-diapositiva.md` (entrada, título, navegación, viñetas, palabra en grande, cita, datos, diagrama, imagen conceptual, vídeo, salida).
- Lo que no cabe en la diapositiva va a las notas del orador, no se pierde.
- Variar el ritmo: alternar tipos para que no haya diez diapositivas de viñetas seguidas.

Si el usuario tiene prisa o pidió el deck directo, presentar el guion brevemente junto con el primer borrador en lugar de esperar aprobación.

### 3. Construir
- **Formato de salida**: si la sesión ofrece un tipo de artefacto de diapositivas (Slides), usarlo; si el usuario pide un PowerPoint/.pptx, cargar el skill `pptx` y seguirlo. En ambos casos estos principios mandan sobre las plantillas por defecto.
- Tamaños para proyección en sala: títulos ≥ 32 pt, texto ≥ 24 pt (nunca < 18 pt), etiquetas de diagrama ≥ 18 pt. Si otro skill (p. ej. `pptx`) sugiere cuerpos de 14–16 pt, aquí manda la legibilidad a distancia: recortar texto antes que achicar letra.
- Definir una sola vez el sistema visual (tipografía, 3 colores + neutros, tratamiento de imagen, rejilla de alineación) y aplicarlo a todo el deck.
- Datos → `references/datos-y-diagramas.md` (destacar lo importante, ejes y rejillas en gris claro, sin 3D, escalas honestas, el gráfico correcto o ningún gráfico).
- Listas de ideas relacionadas → intentar convertirlas en diagrama.
- Imágenes: elegir metáforas frescas, no clichés. No inventes datos, citas ni fuentes; si una cita no tiene autor y fuente verificables, márcala como pendiente.
- Escribir notas del orador con lo que se dirá; así la diapositiva puede quedarse en lo esencial.

### 4. Verificar
Pasar `references/checklist-revision.md` sobre el deck terminado. Si es un .pptx, ejecutar el script de auditoría (abajo) y corregir lo que marque.

## Modo Revisar

1. **Inventario.** Si es .pptx, ejecutar:
   ```bash
   python scripts/auditar_pptx.py ruta/al/deck.pptx            # informe legible
   python scripts/auditar_pptx.py ruta/al/deck.pptx --json     # para procesar
   ```
   El script cuenta palabras y viñetas (cuadros con 3+ párrafos) por diapositiva, estima segundos de lectura, detecta tamaños de letra pequeños, número de tipografías y colores de texto, gráficos 3D y diapositivas con muchos elementos. Es un detector de síntomas, no un juez: confirmar visualmente (renderizar a imagen si se puede, p. ej. con LibreOffice → PDF → PNG) antes de concluir.
   Si es PDF o imágenes, inspeccionar visualmente cada diapositiva.
2. **Diagnóstico** con `references/checklist-revision.md`. Para cada problema: diapositiva, principio que incumple, por qué afecta al público y propuesta concreta.
3. **Entregar** en este orden:
   - **Veredicto general** (3–5 líneas): qué funciona, los 2–3 problemas que más pesan.
   - **Tabla de diagnóstico**: `Diap. | Problema | Principio | Propuesta`.
   - **Antes / después** de las 2–4 diapositivas más críticas: describir la versión actual y la rediseñada (tipo de diapositiva, texto exacto que quedaría, elemento visual, qué pasa a notas del orador). Si una diapositiva de viñetas se convierte en diagrama, nombrar el tipo de diagrama (red, segmento, unión, flujo, pila) y su variante.
   - Si el usuario pidió el rediseño completo, construir la nueva versión con el modo Crear (paso 3) conservando el contenido sustantivo del original.
4. Tono: directo y útil. Si el deck es para docencia o feedback a estudiantes, formular las observaciones como criterios aprendibles («esta diapositiva no pasa la prueba del vistazo porque…»), no como juicios.

## Errores frecuentes al aplicar este skill
- Reducir texto hasta dejar la diapositiva vacía de sentido: menos texto no es menos mensaje; lo que se quita va a notas del orador o al diagrama.
- Añadir iconos o fotos decorativas para «rellenar»: viola el espacio en blanco y la regla de añadir solo con razón.
- Convertir todo en diagrama: solo cuando las viñetas tienen una relación real (proceso, partes de un todo, jerarquía, interdependencia).
- Animaciones por adorno: solo para mostrar cómo funciona algo, crear contraste tras muchas diapositivas estáticas, o dosificar viñetas.

## Fuente
Duarte, N. (2012). *HBR Guide to Persuasive Presentations*, Sección 5 «Las diapositivas» (ed. en español: *Guía HBR: Presentaciones persuasivas*). Los criterios de este skill están parafraseados; no reproducir el texto del libro en las salidas, citar la fuente si el usuario necesita referenciarla.
