"""why_why in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh why_why_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ww_es"
NAME = "why_why_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "X-Matrix": "équis mátrix",
    "Why-Why": "juái juái",
    "Pareto": "Pareto",
    "Gemba": "Guemba",
    "5W2H": "cinco doble u dos hache",
    "FMEA": "efe eme e a",
    "HDMI": "hache de eme i",
    "SOP": "ese o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Veintiún teléfonos fallaron la carga en la prueba final. La primera respuesta llegó "
    "rápido. Error del operador. Dos días después, volvió a pasar. ¿Te suena familiar? En "
    "esta lección aprenderás el análisis Why-Why, también llamado los cinco porqués. Verás "
    "cómo ir más allá de la respuesta fácil, hasta una causa que puedas comprobar y "
    "controlar. Seguiremos a Neha, ingeniera de calidad en una línea de teléfonos celulares, "
    "mientras hace justo eso."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Empieza con un problema preciso, y protege primero a tu "
    "cliente. Respalda cada porqué con evidencia, y pruébalo antes de llamarlo causa raíz. Y "
    "corrige cómo pasó, y también por qué se escapó. Esta es tu acción para esta semana. Toma "
    "un defecto repetido, y escribe su planteamiento 5W2H. Excelente trabajo al completar "
    "esta lección. Ahora aprenderás la X-Matrix, que une la estrategia con la acción."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es Why-Why",
        "points": [("Pregunta por qué, una y otra vez, con hechos", "El análisis Why-Why significa"),
                   ("Cinco no es una regla", "pero cinco no es una regla"),
                   ("Detente en una causa que puedas comprobar y controlar", "Te detienes cuando")],
        "example": "La falla de carga es el síntoma: el asentado del conector, un daño en la tarjeta, el "
                   "contacto del fixture o el ajuste del probador podrían causarla.",
        "example_cue": "En la línea de Neha",
        "script": "Esta es la idea central. El análisis Why-Why significa preguntar por qué pasó un "
                  "problema, una y otra vez, con hechos detrás de cada respuesta. Muchos lo llaman los "
                  "cinco porqués, pero cinco no es una regla. Te detienes cuando llegas a una causa que "
                  "puedes comprobar y controlar. En la línea de Neha, la falla de carga es el síntoma. "
                  "Podría ser el asentado del conector, un daño en la tarjeta, el contacto del fixture, o "
                  "el ajuste del probador. Ninguna es la causa raíz hasta que se prueba. ¿Y cómo encaja "
                  "esto con otras herramientas?",
    },
    {
        "key": "p02", "num": 2, "title": "Why-Why y el análisis de causa raíz",
        "points": [("Una herramienta dentro del análisis de causa raíz", "Why-Why es una herramienta"),
                   ("Ve al lugar real, mira el producto real", "Ve al lugar real"),
                   ("¿Qué evidencia respalda este porqué?", "pregunta qué evidencia"),
                   ("La acción humana es una pista, no la respuesta", "Y trata la acción humana")],
        "example": "Tornillos faltantes en una línea de audio: 'el operador olvidó' no bastaba — el equipo "
                   "revisó el alimentador y la secuencia.",
        "example_cue": "Cuando faltaron tornillos",
        "script": "Why-Why es una herramienta dentro del análisis de causa raíz. La espina de pescado, las "
                  "gráficas de Pareto y los experimentos van junto a ella. Funciona mejor para una cadena "
                  "clara de causa y efecto. Ve al lugar real, y mira el producto real. En cada paso, "
                  "pregunta qué evidencia respalda este porqué. Y trata la acción humana como una pista, no "
                  "como la respuesta final. Cuando faltaron tornillos en una línea de audio, el operador "
                  "olvidó no bastaba. El equipo revisó el alimentador y la secuencia. ¿Y por dónde "
                  "empiezas?",
    },
    {
        "key": "p03", "num": 3, "title": "Paso 1: definir con 5W2H",
        "points": [("Un planteamiento preciso del problema", "Empieza con un planteamiento preciso"),
                   ("5W2H: qué, dónde, cuándo, cómo se encontró, cuántos", "Usa el 5W2H"),
                   ("Incluye el último estado bueno conocido", "Incluye el último estado bueno")],
        "example": "Línea 2: 21 de 700 teléfonos (3%) fallaron la carga después del cambio de fixture de las "
                   "11; el turno anterior estaba abajo de 0.5%.",
        "example_cue": "En la Línea dos",
        "script": "Empieza con un planteamiento preciso del problema. Un problema vago recibe respuestas "
                  "vagas. Usa el 5W2H. Qué falló, dónde, cuándo, cómo se encontró, y cuántos. Incluye el "
                  "último estado bueno conocido. Este es el planteamiento de Neha. En la Línea dos, "
                  "veintiún de setecientos teléfonos fallaron la carga. Es el tres por ciento, justo "
                  "después de un cambio de fixture a las once. El turno anterior estaba abajo de medio por "
                  "ciento. Nota cuánto te dice eso ya. ¿Pero qué pasa con los teléfonos que ya se armaron?",
    },
    {
        "key": "p04", "num": 4, "title": "Paso 2: primero contener",
        "points": [("Protege primero a tu cliente", "protege a tu cliente"),
                   ("Encuentra el último punto bueno conocido", "Encuentra el último punto bueno"),
                   ("Retén el inventario físicamente y en el sistema", "Retén ese inventario"),
                   ("Cuadra cada unidad", "Luego cuadra cada unidad")],
        "example": "Separar el 100% protege al cliente — no prueba que eliminaste la causa.",
        "example_cue": "Separar el cien por ciento",
        "script": "Antes de analizar, protege a tu cliente. La contención limita el riesgo mientras corre "
                  "la investigación. Encuentra el último punto bueno conocido, y cada número de serie o "
                  "lote armado desde entonces. Retén ese inventario físicamente, y también en el sistema. "
                  "Luego cuadra cada unidad. Revisada, con falla, retrabajada, liberada o pendiente. Neha "
                  "retuvo cada teléfono armado desde el cambio de fixture. Pero aquí hay una trampa. "
                  "Separar el cien por ciento protege al cliente. No prueba que eliminaste la causa. ¿Y qué "
                  "sigue?",
    },
    {
        "key": "p05", "num": 5, "title": "Paso 3: hechos en el Gemba",
        "points": [("Compara unidades con falla contra buenas conocidas", "compara las unidades con falla"),
                   ("Revisa ajustes, fixtures, versiones, lotes", "Revisa los ajustes"),
                   ("Conserva la evidencia antes de ajustar", "Conserva la evidencia"),
                   ("Vi · fuente · podría significar", "Lleva tres columnas")],
        "example": "Neha fotografió y etiquetó cada teléfono con falla por número de serie, y luego sacó los "
                   "registros del probador y de mantenimiento.",
        "example_cue": "Neha fotografió",
        "script": "Tu análisis es tan bueno como tu evidencia. Ve al Gemba, y compara las unidades con "
                  "falla con unas buenas conocidas. Revisa los ajustes, los fixtures, la calibración, las "
                  "versiones de software y los lotes del proveedor. Conserva la evidencia antes de que "
                  "alguien ajuste algo. Neha fotografió y etiquetó cada teléfono con falla por número de "
                  "serie. Luego sacó los registros del probador y los de mantenimiento. Lleva tres "
                  "columnas. Lo que viste, de dónde salió, y qué podría significar. Ahora estás listo para "
                  "preguntar por qué.",
    },
    {
        "key": "p06", "num": 6, "title": "Paso 4: armar la cadena",
        "points": [("Empieza por el evento observado", "Escribe el evento observado"),
                   ("Cada flecha es una afirmación que puedes revisar", "Cada flecha es una afirmación"),
                   ("Hechos, no 'descuido'", "Usa hechos específicos"),
                   ("Ramifica cuando las causas se combinan", "Ramifica la cadena")],
        "example": "Etiqueta de caja equivocada → trabajo de impresión viejo → el software lo permitió → la "
                   "impresora no estaba ligada al producto escaneado.",
        "example_cue": "Una etiqueta de caja equivocada",
        "script": "Escribe el evento observado arriba. Pregunta por qué pasó. Luego pregunta por qué "
                  "existía esa condición. Cada flecha es una afirmación que debes poder revisar. Pregunta "
                  "por qué ocurrió el defecto, nunca a quién culpar. Usa hechos específicos, no etiquetas "
                  "como descuido. Este es un ejemplo de empaque. Una etiqueta de caja equivocada venía de "
                  "un trabajo de impresión viejo. El software lo permitió, porque la impresora no estaba "
                  "ligada al producto escaneado. Ramifica la cadena cada vez que contribuyó más de una "
                  "causa.",
    },
    {
        "key": "p07", "num": 7, "title": "Ocurrencia, fuga y sistema",
        "points": [("Ocurrencia: cómo se hizo el defecto", "La causa de ocurrencia"),
                   ("Fuga: por qué nadie lo atrapó", "La causa de fuga"),
                   ("Sistema: por qué los controles no vieron el riesgo", "Y la causa de sistema"),
                   ("Cada una necesita su propia solución", "Cada una necesita")],
        "example": "El fixture permite un asentado parcial de la batería (ocurrencia); la prueba final no "
                   "vio el contacto intermitente (fuga).",
        "example_cue": "En la línea de Neha",
        "script": "Un análisis completo normalmente tiene más de una cadena. La causa de ocurrencia explica "
                  "cómo se hizo el defecto. La causa de fuga explica por qué nadie lo atrapó. Y la causa de "
                  "sistema explica por qué tus controles no vieron el riesgo desde el principio. En la "
                  "línea de Neha, un fixture podía permitir un asentado parcial de la batería. Esa es la "
                  "ocurrencia. La prueba final no revisaba el contacto intermitente. Esa es la fuga. Cada "
                  "una necesita su propia solución. ¿Pero qué pasa si hay muchas causas posibles?",
    },
    {
        "key": "p08", "num": 8, "title": "Espina de pescado y Pareto",
        "points": [("Espina de pescado: 6 grupos de causas", "Una espina de pescado agrupa"),
                   ("Pareto: ordena por frecuencia", "Una gráfica de Pareto ordena"),
                   ("Los riesgos de seguridad raros todavía importan", "Pero un riesgo de seguridad raro"),
                   ("Una espina de pescado son suposiciones, no prueba", "una espina de pescado es una lista")],
        "example": "Los dos tipos de defecto principales de Neha sumaban el 65% del total — ahí se enfocó "
                   "primero.",
        "example_cue": "Los dos tipos principales de Neha",
        "script": "Cuando hay muchas causas posibles, empieza a lo ancho. Una espina de pescado agrupa las "
                  "ideas en personas, máquina, método, material, medición y medio ambiente. Una gráfica de "
                  "Pareto ordena los defectos por qué tan seguido pasan. Los dos tipos principales de Neha "
                  "sumaban el sesenta y cinco por ciento del total. Ahí se enfocó primero. Pero un riesgo "
                  "de seguridad raro todavía importa, aunque su conteo sea bajo. Y recuerda, una espina de "
                  "pescado es una lista de suposiciones, no una prueba. ¿Y cómo compruebas una causa?",
    },
    {
        "key": "p09", "num": 9, "title": "Comprobar la causa",
        "points": [("Predice qué debería cambiar", "Antes de la prueba"),
                   ("Mantén fijos los demás factores", "Mantén fijos los demás factores"),
                   ("Prueba lo bueno y lo malo, en varios turnos", "Prueba las condiciones buenas y malas")],
        "example": "Pines de fixture buenos contra gastados, con las mismas piezas: las fallas siguieron a "
                   "los pines gastados.",
        "example_cue": "Neha sospechaba",
        "script": "Una cadena lógica no basta. Tienes que probarla. Antes de la prueba, escribe qué debería "
                  "cambiar si tu causa es cierta. Mantén fijos los demás factores, como el lote de material "
                  "y la versión del programa. Prueba las condiciones buenas y malas, en varios turnos. Neha "
                  "sospechaba de un pin del fixture gastado. Probó pines buenos y pines gastados, con las "
                  "mismas piezas. Las fallas siguieron a los pines gastados. ¿Qué habría probado que estaba "
                  "equivocada? Fallas que se quedaran con los pines buenos.",
    },
    {
        "key": "p10", "num": 10, "title": "Acción correctiva y Poka Yoke",
        "points": [("Corrige la causa, no el síntoma", "Ahora corrige la causa"),
                   ("La prevención de ingeniería le gana a los recordatorios", "La prevención de ingeniería"),
                   ("Corrige la ocurrencia + una revisión independiente de la fuga", "Corrige la ocurrencia"),
                   ("Actualiza el FMEA, el SOP, el entrenamiento", "Luego actualiza el FMEA")],
        "example": "Etiquetas de audio equivocadas: la impresora ahora necesita primero un escaneo de serie "
                   "que coincida. Volver a entrenar depende de la memoria.",
        "example_cue": "Para las etiquetas equivocadas",
        "script": "Ahora corrige la causa, no solo el síntoma. La prevención de ingeniería le gana a los "
                  "recordatorios. Piensa en fixtures con guía, interbloqueos por código de barras y "
                  "sensores de presencia. Corrige la ocurrencia, y agrega una revisión independiente para "
                  "la fuga. Luego actualiza el FMEA, el SOP y el entrenamiento. Para las etiquetas "
                  "equivocadas en equipos de audio, la impresora ahora necesita primero un escaneo de serie "
                  "que coincida. ¿Por qué volver a entrenar suele ser una solución débil? Porque depende de "
                  "la memoria, y la memoria falla. ¿Cómo sabes que tu solución funcionó?",
    },
    {
        "key": "p11", "num": 11, "title": "Verificar y cerrar",
        "points": [("Terminado ≠ comprobado", "Terminar una acción"),
                   ("Reto: muestras buenas, malas, en el límite", "Reta al nuevo control"),
                   ("Vigila la repetición y el rendimiento", "Vigila la repetición"),
                   ("Sin paros nuevos ni rechazos falsos", "Revisa que no hayas")],
        "example": "La regla de cierre de Neha: cero repeticiones en 10 días de producción, pruebas de reto "
                   "aprobadas, cada unidad sospechosa ubicada.",
        "example_cue": "Neha fijó una regla de cierre",
        "script": "Terminar una acción no es lo mismo que comprobar que funciona. Reta al nuevo control con "
                  "muestras buenas conocidas, malas conocidas y en el límite. Vigila la repetición y el "
                  "rendimiento a la primera en varios turnos, modelos y cambios de modelo. Revisa que no "
                  "hayas creado paros nuevos ni rechazos falsos. Neha fijó una regla de cierre con su "
                  "planta. Cero repeticiones en diez días de producción, pruebas de reto aprobadas, y cada "
                  "unidad sospechosa ubicada. Tu planta debe fijar su propia regla. Luego Calidad la firma.",
    },
    {
        "key": "p12", "num": 12, "title": "KPI de Why-Why",
        "points": [("Mide la rapidez y los resultados", "Mide la rapidez"),
                   ("Adelantados: contención rápida, acciones verificadas", "Las medidas adelantadas"),
                   ("Atrasados: tasa de defectos, repetición", "Las medidas atrasadas"),
                   ("Mantén estables las definiciones", "Mantén estables las definiciones")],
        "example": "50 → 15 defectos = una baja de 70%. Costo de ₹1.2 lakh, ₹30,000 ahorrados al mes = "
                   "recuperación en 4 meses.",
        "example_cue": "Los defectos de Neha bajaron",
        "script": "Mide la rapidez y los resultados. Las medidas adelantadas incluyen la contención rápida "
                  "y las acciones verificadas. Las medidas atrasadas incluyen la tasa de defectos y la "
                  "repetición. Mantén estables las definiciones, para que nadie mejore un número "
                  "cambiándolo. Los defectos de Neha bajaron de cincuenta a quince, con el mismo volumen. "
                  "Es una baja del setenta por ciento. Su solución costó ciento veinte mil rupias, y ahorra "
                  "treinta mil al mes. Así que se paga en cuatro meses. ¿Cuáles de estas sigue tu equipo "
                  "hoy?",
    },
    {
        "key": "p13", "num": 13, "title": "Caso práctico: falla de carga",
        "points": [("¿Teléfono o probador? Pruébalo primero", "¿La falla estaba en el teléfono"),
                   ("Se volvieron a probar en un segundo probador: siguieron fallando", "Volvió a probar los teléfonos con falla"),
                   ("Pin gastado en el fixture de ensamble", "El conector de la batería quedaba"),
                   ("Solución: pines nuevos, límites de vida, revisión de ajuste", "Su solución fue")],
        "example": "Los teléfonos con falla volvieron a fallar en un segundo probador: los teléfonos sí "
                   "estaban mal.",
        "example_cue": "También fallaron ahí",
        "script": "Así se armó el caso de Neha. ¿La falla estaba en el teléfono, o en el probador? Volvió a "
                  "probar los teléfonos con falla en un segundo probador. También fallaron ahí, así que los "
                  "teléfonos sí estaban mal. La cadena fue así. El conector de la batería quedaba medio "
                  "asentado, porque un pin de resorte gastado en el nuevo fixture de ensamble no lo "
                  "empujaba hasta el fondo. Estaba gastado porque no existía un intervalo de cambio. Su "
                  "solución fue pines nuevos, límites de vida, y una revisión de ajuste. ¿Tú habrías "
                  "revisado primero el probador?",
    },
    {
        "key": "p14", "num": 14, "title": "Decodificador y audio",
        "points": [("Productos distintos, evidencia distinta", "Productos distintos necesitan"),
                   ("Decodificador: soldadura HDMI, firmware, probador", "En un decodificador"),
                   ("Audio: rastrear el kit, la secuencia de empaque, los escaneos", "En un equipo de audio"),
                   ("Extiende las soluciones comprobadas a líneas parecidas", "Cuando una solución está comprobada")],
        "example": "Control remoto faltante: el kit no lo incluyó, y luego la caja se cerró sin escanear el "
                   "control.",
        "example_cue": "El kit no incluyó el control",
        "script": "Productos distintos necesitan evidencia distinta. En un decodificador sin imagen, "
                  "revisarías la soldadura HDMI, el firmware y los ajustes del probador. Y preguntarías por "
                  "qué la revisión de imagen al final de la línea no lo vio. En un equipo de audio sin su "
                  "control remoto, rastrearías el kit, la secuencia de empaque y los escaneos. El kit no "
                  "incluyó el control. Luego la caja se cerró sin escanear el control. Cuando una solución "
                  "está comprobada, extiéndela también a líneas parecidas. ¿Listo para el plan de "
                  "implementación?",
    },
    {
        "key": "p15", "num": 15, "title": "Implementación en 90 días",
        "points": [("Línea piloto + unos facilitadores", "Empieza con una línea piloto"),
                   ("Días 1–30: disparadores, puestos, plantillas", "En los primeros treinta días"),
                   ("Días 31–60: investigar, probar hipótesis", "En los siguientes treinta"),
                   ("Días 61–90: retar, actualizar, extender", "En los últimos treinta")],
        "example": "Audita que haya muestras reales y eslabones verificados — no formatos bonitos.",
        "example_cue": "Audita que haya muestras reales",
        "script": "Haz del Why-Why parte de la gestión diaria. Empieza con una línea piloto de alto riesgo, "
                  "y entrena a unos facilitadores. En los primeros treinta días, define disparadores, "
                  "puestos y plantillas. En los siguientes treinta, haz investigaciones reales y prueba tus "
                  "hipótesis. En los últimos treinta, pon a prueba las soluciones, actualiza los controles, "
                  "y extiende las lecciones. Audita que haya muestras reales y eslabones verificados, no "
                  "formatos bonitos. Recuerda, pregunta por qué hasta que puedas comprobar la causa. Luego "
                  "haz imposible que se repita.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "¿Por qué?", "sub": "Respaldado por un hecho", "icon": "search", "with": 0},
        {"label": "¿Por qué otra vez?", "sub": "Cinco no es una regla", "icon": "count", "with": 1},
        {"label": "Una causa que puedes comprobar y controlar", "icon": "key", "tone": "good", "with": 2}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Asentado del conector", "icon": "pin", "with": "example"},
            {"label": "Daño en la tarjeta", "icon": "chip", "with": "example"},
            {"label": "Contacto del fixture", "icon": "wrench", "with": "example"},
            {"label": "Ajuste del probador", "icon": "test", "with": "example"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Why-Why", "sub": "Una herramienta entre muchas", "icon": "search", "tone": "good", "with": 0},
        {"label": "Lugar real, producto real", "icon": "walk", "with": 1},
        {"label": "Evidencia para cada porqué", "icon": "clipboard", "with": 2},
        {"label": "Las personas son una pista", "icon": "person", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "El operador olvidó", "sub": "No basta", "icon": "person", "with": "example"},
            {"label": "Revisa el alimentador y la secuencia", "sub": "Hechos", "icon": "search", "with": "example"}]}},
    "p03": {"type": "doc", "items": [
        {"label": "Planteamiento del problema · Línea 2", "icon": "label", "with": 0},
        {"label": "Qué: falla de carga en la prueba final", "icon": "power", "with": 1},
        {"label": "Cuándo: después del cambio de fixture de las 11", "icon": "clock", "with": 1},
        {"label": "Cuántos: 21 de 700 teléfonos (3%)", "icon": "count", "with": 1},
        {"label": "Último estado bueno: abajo de 0.5%", "icon": "check", "with": 2}]},
    "p04": {"type": "flow", "items": [
        {"label": "Protege al cliente", "icon": "shield", "with": 0},
        {"label": "Encuentra el último punto bueno", "icon": "search", "with": 1},
        {"label": "Retén el inventario: piso y sistema", "icon": "lock", "with": 2},
        {"label": "Cuadra cada unidad", "icon": "count", "tone": "good", "with": 3}]},
    "p05": {"type": "icons", "items": [
        {"label": "Con falla contra buenas conocidas", "icon": "scale", "with": 0},
        {"label": "Ajustes, versiones, lotes", "icon": "gear", "with": 1},
        {"label": "Conserva la evidencia", "icon": "camera", "with": 2},
        {"label": "Vi · fuente · significado", "icon": "clipboard", "with": 3}]},
    "p06": {"type": "icons", "items": [
        {"label": "Empieza por el evento", "icon": "search", "with": 0},
        {"label": "Cada flecha: una afirmación para revisar", "icon": "check", "with": 1},
        {"label": "Hechos, no etiquetas", "icon": "cross", "tone": "bad", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Etiqueta de caja equivocada", "icon": "label", "tone": "bad", "with": "example"},
            {"label": "Trabajo de impresión viejo", "icon": "sequence", "with": "example"},
            {"label": "El software lo permitió", "icon": "chip", "with": "example"},
            {"label": "La impresora no estaba ligada al escaneo", "icon": "barcode", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Ocurrencia", "sub": "Cómo se hizo", "icon": "wrench", "with": 0},
        {"label": "Fuga", "sub": "Por qué nadie lo atrapó", "icon": "search", "with": 1},
        {"label": "Sistema", "sub": "Por qué los controles no lo vieron", "icon": "gear", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "El fixture permite un asentado parcial", "sub": "Ocurrencia", "icon": "pin", "tone": "bad", "with": "example"},
            {"label": "La prueba final no ve el contacto intermitente", "sub": "Fuga", "icon": "test", "tone": "bad", "with": "example"},
            {"label": "Una solución para cada una", "icon": "check", "tone": "good", "with": 3}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Espina de pescado: 6 grupos", "icon": "gear", "with": 0},
        {"label": "Pareto: ordenar por conteo", "icon": "chartUp", "with": 1},
        {"label": "Riesgos de seguridad raros", "icon": "warning", "tone": "bad", "with": 2},
        {"label": "Suposiciones, no prueba", "icon": "search", "with": 3}],
        "then": {"type": "bars", "label": "", "note": "Los dos principales = 65% de los defectos", "with": "example", "items": [
            {"label": "Tipo 1", "value": 40, "tone": "bad", "with": "example"},
            {"label": "Tipo 2", "value": 25, "tone": "bad", "with": "example"},
            {"label": "Tipo 3", "value": 15, "with": "example"},
            {"label": "Tipo 4", "value": 12, "with": "example"},
            {"label": "Otros", "value": 8, "with": "example"}]}},
    "p09": {"type": "steps", "items": [
        {"label": "Predice el cambio", "with": 0}, {"label": "Fija los demás factores", "with": 1},
        {"label": "Prueba lo bueno y lo malo", "with": 2}, {"label": "En varios turnos", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Pines gastados", "sub": "Las fallas los siguieron", "icon": "pin", "with": "example"},
            {"label": "Pines buenos", "sub": "Las mismas piezas pasaron", "icon": "check", "with": "example"}]}},
    "p10": {"type": "ladder", "top": "LO MÁS FUERTE", "bottom": "LO MÁS DÉBIL", "items": [
        {"label": "Fixture con guía, interbloqueo", "icon": "key", "with": 1},
        {"label": "Sensor de presencia", "icon": "sensor", "with": 1},
        {"label": "Revisión independiente de la fuga", "icon": "search", "with": 2},
        {"label": "Volver a entrenar, recordatorios", "icon": "warning", "tone": "bad", "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Buena conocida", "icon": "check", "tone": "good", "with": 1},
        {"label": "Mala conocida", "icon": "cross", "tone": "bad", "with": 1},
        {"label": "Muestras en el límite", "icon": "scale", "with": 1},
        {"label": "Repetición y rendimiento", "icon": "chartUp", "with": 2}],
        "then": {"type": "doc", "with": "example", "items": [
            {"label": "Regla de cierre · Línea 2", "icon": "label", "with": "example"},
            {"label": "Cero repeticiones en 10 días de producción", "icon": "calendar", "with": "example"},
            {"label": "Pruebas de reto aprobadas", "icon": "test", "with": "example"},
            {"label": "Cada unidad sospechosa ubicada", "icon": "count", "with": "example"},
            {"label": "Calidad la firma", "icon": "person", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Rapidez y resultados", "icon": "clock", "with": 0},
        {"label": "Adelantado: contención rápida", "icon": "shield", "with": 1},
        {"label": "Atrasado: defectos, repeticiones", "icon": "chartDown", "with": 2},
        {"label": "Definiciones estables", "icon": "scale", "with": 3}],
        "then": {"type": "compare", "before": {"label": "Antes", "value": 50}, "after": {"label": "Después", "value": 15},
                 "unit": "defectos de carga, mismo volumen", "note": "Una baja de 70% · recuperación en 4 meses", "with": "example"}},
    "p13": {"type": "flow", "items": [
        {"label": "¿Teléfono o probador?", "icon": "search", "with": 0},
        {"label": "Segundo probador: siguió fallando", "icon": "test", "with": 1},
        {"label": "Pin del fixture de ensamble gastado, sin intervalo de cambio", "icon": "pin", "tone": "bad", "with": 2},
        {"label": "Pines nuevos, límites de vida, revisión de ajuste", "icon": "check", "tone": "good", "with": 3}]},
    "p14": {"type": "icons", "items": [
        {"label": "Decodificador", "sub": "HDMI, firmware, probador", "icon": "chip", "with": 1},
        {"label": "Equipo de audio", "sub": "Kit, secuencia, escaneos", "icon": "wave", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "El kit no incluyó el control", "icon": "tray", "tone": "bad", "with": "example"},
            {"label": "La caja se cerró sin escanear el control", "icon": "box", "tone": "bad", "with": "example"},
            {"label": "Extiende la solución comprobada", "icon": "sequence", "tone": "good", "with": 3}]}},
    "p15": {"type": "timeline", "items": [
        {"label": "Disparadores, puestos, plantillas", "sub": "Días 1–30", "icon": "clipboard", "with": 1},
        {"label": "Investigar, probar hipótesis", "sub": "31–60", "icon": "search", "with": 2},
        {"label": "Retar, actualizar, extender", "sub": "61–90", "icon": "chartUp", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "La prueba final no detectó un conector de batería medio asentado. ¿Qué tipo de causa es "
                    "esa?",
        "options": ["Causa de ocurrencia", "Causa de fuga", "Causa de sistema"],
        "correct": 1,
        "explanation": "El defecto se hizo antes (ocurrencia). La causa de fuga explica por qué la barrera de "
                       "detección — aquí, la prueba final — no lo atrapó.",
        "q_script": "Prueba rápida. La prueba final no detectó un conector de batería medio asentado. ¿Qué "
                    "tipo de causa es esa? Tómate unos segundos.",
        "a_script": "Es una causa de fuga. El defecto se hizo antes. La fuga explica por qué nuestras "
                    "revisiones no lo atraparon.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "30 cajas salieron con etiquetas equivocadas y alguien dice “error del operador”. ¿Qué "
                    "debe hacer PRIMERO el equipo?",
        "options": ["Volver a entrenar al operador y cerrarlo", "Contener las cajas sospechosas, y luego preguntar por qué el proceso lo permitió",
                    "Poner un letrero de recordatorio en empaque"],
        "correct": 1,
        "explanation": "Primero contén, luego averigua por qué el proceso permitió una etiqueta equivocada. "
                       "Volver a entrenar o un letrero dependen de la memoria, así que casi nunca evitan que se "
                       "repita.",
        "q_script": "Una más, y esta es un escenario. Treinta cajas salieron con etiquetas equivocadas, y "
                    "alguien dice error del operador. ¿Qué debe hacer primero el equipo? Piénsalo.",
        "a_script": "Primero contén las cajas sospechosas. Luego pregunta por qué el proceso permitió una "
                    "etiqueta equivocada. Volver a entrenar o un letrero dependen de la memoria, así que casi "
                    "nunca evitan que se repita.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
