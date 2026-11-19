"""zero_defects in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh zero_defects_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "zd_es"
NAME = "zero_defects_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Zero Defects": "sírou dífects",
    "Poka Yoke": "Poka Yoke",
    "Crosby": "Crósbi",
    "Jidoka": "Yidoka",
    "Andon": "Andon",
    "PFMEA": "pe efe eme e a",
    "DPMO": "de pe eme o",
    "Cpk": "ce pe ka",
    "PPM": "pe pe eme",
    "FPY": "efe pe ye",
    "SOP": "ese o pe",
    "SKU": "ese ka u",
    "Cp": "ce pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Un conector, mal asentado. Pasó todas las revisiones visuales. Luego cuatrocientos "
    "teléfonos regresaron a retrabajo. ¿Te suena familiar? En esta lección aprenderás Zero "
    "Defects. Verás cómo medir la calidad con honestidad, y cómo hacer imposibles errores "
    "como ese. Seguiremos a Priya, ingeniera de línea en una línea de ensamble de teléfonos "
    "celulares, mientras hace justo eso."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Previene los defectos, no solo los inspecciones. Mide con "
    "honestidad, con definiciones claras. Y cuando algo falle, corrige el sistema, no a la "
    "persona. Esta es tu acción para esta semana. Elige un defecto que sigue regresando en tu "
    "línea, y pregúntate cómo hacerlo imposible. Excelente trabajo al completar esta lección, "
    "y todo el curso, de la A a la Z. Ahora ve y haz una mejora en tu línea."
)

# Each page: title, 2-5 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Significado y filosofía",
        "points": [("Todo defecto se puede prevenir", "trata cada defecto como prevenible"),
                   ("Bien a la primera", "Buscas hacer"),
                   ("Diseña y controla el proceso", "Diseñando y controlando"),
                   ("Una disciplina, no una promesa", "Es una disciplina")],
        "example": "La línea de Priya: una estación ahora confirma que el conector está asentado antes de la "
                   "prueba eléctrica.",
        "example_cue": "En la línea de Priya",
        "script": "Esta es la idea central. Zero Defects trata cada defecto como prevenible, no como un "
                  "costo normal del negocio. Buscas hacer cada unidad bien a la primera. ¿Cómo? Diseñando y "
                  "controlando bien el proceso. Es una disciplina, no una promesa de que nada saldrá mal "
                  "nunca. En la línea de Priya, una estación ahora confirma que el conector está asentado "
                  "antes de la prueba eléctrica. ¿Y de dónde vino esta idea?",
    },
    {
        "key": "p02", "num": 2, "title": "Historia y valor para el negocio",
        "points": [("Crosby, años 1960: calidad = cumplir los requisitos", "Philip Crosby hizo"),
                   ("Lean agrega calidad integrada y a prueba de errores", "El Lean moderno agrega"),
                   ("Corrige el sistema, no a la persona", "corriges el sistema"),
                   ("Los líderes quitan barreras; los operadores paran y reaccionan", "Los líderes quitan las barreras")],
        "example": "Para ganarte el apoyo de los líderes, necesitas mostrar el dinero.",
        "example_cue": "Pero para ganarte ese apoyo",
        "script": "Philip Crosby hizo famoso a Zero Defects en los años sesenta. Su definición es simple. "
                  "Calidad significa cumplir requisitos claramente definidos. El Lean moderno agrega "
                  "calidad integrada, trabajo estándar y dispositivos a prueba de errores. Este es el "
                  "cambio clave. Cuando pasa un defecto, corriges el sistema, no culpas a la persona. Los "
                  "líderes quitan las barreras, y se confía en que los operadores paren y reaccionen. Pero "
                  "para ganarte ese apoyo, necesitas mostrar el dinero.",
    },
    {
        "key": "p03", "num": 3, "title": "El costo de la mala calidad",
        "points": [("Falla interna: desecho, retrabajo, reprueba", "Las fallas internas incluyen"),
                   ("Falla externa: garantía, devoluciones", "Las fallas externas incluyen"),
                   ("Ocultos: retrasos, manejo, capacidad perdida", "Luego vienen los costos ocultos"),
                   ("Prevenir cuesta mucho menos", "Prevenir cuesta mucho menos")],
        "example": "La línea de Priya: 400 teléfonos retrabajados = ₹32,000 de retrabajo directo — antes de "
                   "un solo embarque tarde.",
        "example_cue": "El mes pasado, la línea de Priya",
        "script": "La mala calidad cuesta más de lo que crees. Las fallas internas incluyen desecho, "
                  "retrabajo y reprueba. Las fallas externas incluyen reclamos de garantía y devoluciones. "
                  "Luego vienen los costos ocultos, como retrasos, manejo extra y capacidad perdida. El mes "
                  "pasado, la línea de Priya retrabajó cuatrocientos teléfonos. Son treinta y dos mil "
                  "rupias de retrabajo directo, antes de un solo embarque tarde. Prevenir cuesta mucho "
                  "menos. ¿Y cómo mides dónde se pierde la calidad?",
    },
    {
        "key": "p04", "num": 4, "title": "FTR, FPY y RTY",
        "points": [("Bien a la primera: sin ninguna corrección", "Bien a la primera significa"),
                   ("Rendimiento a la primera: pasar un paso a la primera", "El rendimiento a la primera es"),
                   ("Rendimiento acumulado: multiplica cada paso", "El rendimiento acumulado multiplica")],
        "example": "Tres etapas de 98% cada una dan solo unos 94% juntas.",
        "example_cue": "Tres etapas de noventa y ocho",
        "script": "Empieza con tres medidas de rendimiento. Bien a la primera significa cumplir los "
                  "requisitos sin ninguna corrección. El rendimiento a la primera es la parte de las "
                  "unidades que pasa un paso a la primera. El rendimiento acumulado multiplica los "
                  "rendimientos de cada paso. Aquí está la trampa. Tres etapas de noventa y ocho por ciento "
                  "cada una suena muy bien. Juntas, dan solo unos noventa y cuatro por ciento. ¿Qué paso de "
                  "tu línea baja el total en silencio?",
    },
    {
        "key": "p05", "num": 5, "title": "PPM, DPMO y metas",
        "points": [("PPM: unidades defectuosas por millón", "El PPM cuenta"),
                   ("DPMO: defectos por millón de oportunidades", "El DPMO cuenta"),
                   ("Reporta el tamaño de muestra y el alcance", "Reporta siempre tu muestra"),
                   ("Nunca compares PPM con DPMO", "Y nunca compares")],
        "example": "Priya encontró 25 teléfonos malos en 50,000 = 500 PPM.",
        "example_cue": "Priya encontró veinticinco",
        "script": "Las tasas de defectos necesitan un denominador preciso. El PPM cuenta las unidades "
                  "defectuosas por millón. El DPMO cuenta los defectos por millón de oportunidades. Así que "
                  "primero debes definir las oportunidades en cada unidad. Priya encontró veinticinco "
                  "teléfonos malos en cincuenta mil. Son quinientos PPM. Reporta siempre tu muestra y tu "
                  "alcance. Y nunca compares un PPM con un DPMO. Ahora, ¿cómo evitas que los defectos "
                  "siquiera se hagan?",
    },
    {
        "key": "p06", "num": 6, "title": "Calidad en el origen",
        "points": [("Cada operación es dueña de su trabajo", "cada operación es dueña"),
                   ("Siguiente estación = tu cliente", "Trata a la siguiente estación"),
                   ("Revisa entradas y ajuste, sigue el SOP", "Revisa tus entradas"),
                   ("¿Algo mal? Para, separa, escala", "Si algo se ve mal")],
        "example": "Línea de decodificadores: los operadores revisan la almohadilla térmica y el torque de "
                   "los tornillos antes de que una unidad avance.",
        "example_cue": "En la línea de decodificadores",
        "script": "Calidad en el origen significa que cada operación es dueña de su propio trabajo. Trata a "
                  "la siguiente estación como tu cliente. Revisa tus entradas y tu ajuste primero, y luego "
                  "sigue el SOP vigente. Si algo se ve mal, para, separa y escala. No lo pases. En la línea "
                  "de decodificadores de al lado, los operadores revisan la almohadilla térmica y el torque "
                  "de los tornillos antes de que una unidad avance. La inspección posterior no puede "
                  "rescatar un proceso inestable. ¿Pero qué pasa si la gente todavía se equivoca?",
    },
    {
        "key": "p07", "num": 7, "title": "Poka Yoke",
        "points": [("Poka Yoke = a prueba de errores", "Significa a prueba de errores"),
                   ("Haz los errores imposibles, o atrápalos", "Formas, interbloqueos y sensores"),
                   ("Prevenir le gana a una etiqueta de advertencia", "Prevenir le gana a una advertencia"),
                   ("Pon a prueba con muestras buenas y malas", "Pon a prueba cada dispositivo")],
        "example": "El fixture del conector de batería de Priya solo entra de una forma; el teléfono no "
                   "avanza hasta que se registra la revisión.",
        "example_cue": "Priya agregó un fixture",
        "script": "Ahí entra el Poka Yoke. Significa a prueba de errores. Formas, interbloqueos y sensores "
                  "hacen un error imposible, o lo atrapan al instante. Prevenir le gana a una advertencia, "
                  "porque las advertencias dependen de la memoria. Priya agregó un fixture para el conector "
                  "de batería que solo entra de una forma. El teléfono no avanza hasta que se registra la "
                  "revisión. Pon a prueba cada dispositivo con muestras buenas y malas, en cada turno. ¿Y "
                  "qué pasa cuando algo todavía sale mal?",
    },
    {
        "key": "p08", "num": 8, "title": "Jidoka, Andon y respuesta",
        "points": [("Jidoka: el proceso se detiene solo", "Jidoka significa"),
                   ("El Andon hace visible el problema", "Una señal de Andon"),
                   ("Criterios de paro claros, un responsable nombrado", "Necesitas criterios de paro claros"),
                   ("Vuelve a arrancar solo cuando la causa esté controlada", "vuelves a arrancar solo cuando")],
        "example": "Un probador de audio marca un desbalance de canal repetido: la línea se detiene y se "
                   "retienen las unidades sospechosas.",
        "example_cue": "Imagina un probador de audio",
        "script": "Jidoka significa que el proceso detecta una anormalidad y se detiene solo. Una señal de "
                  "Andon hace visible el problema, para que las personas correctas respondan rápido. "
                  "Necesitas criterios de paro claros, y un responsable nombrado para cada llamada de "
                  "Andon. Imagina un probador de audio que marca un desbalance de canal repetido. La línea "
                  "se detiene, y se retienen las unidades sospechosas. Se revisa el fixture, y vuelves a "
                  "arrancar solo cuando la causa esté controlada. Parar no es fallar. Esconder el problema "
                  "sí lo es.",
    },
    {
        "key": "p09", "num": 9, "title": "Trabajo estándar y auditorías",
        "points": [("Trabajo estándar: el mejor método y el más seguro", "Con el trabajo estándar"),
                   ("Verifica la primera unidad después del cambio de modelo", "verifica la primera unidad"),
                   ("Las auditorías por capas confirman los controles", "Luego las auditorías por capas"),
                   ("Audita los controles, no el papeleo", "Audita los controles")],
        "example": "Liberar firmware necesita la imagen aprobada, que coincida la receta y una suma de "
                   "verificación.",
        "example_cue": "En una estación de firmware",
        "script": "Ahora, ¿cómo mantienes estables los buenos resultados? Con el trabajo estándar. Es el "
                  "mejor método y el más seguro de hoy, con revisiones, ajustes y trazabilidad. Mantenlo "
                  "visible, y verifica la primera unidad después de cada cambio de modelo. Luego las "
                  "auditorías por capas del proceso confirman que tus controles críticos siguen "
                  "funcionando. Audita los controles, no el papeleo. En una estación de firmware, liberar "
                  "necesita la imagen aprobada, que coincida la receta y una suma de verificación. ¿Pero "
                  "qué tan estable es el proceso mismo?",
    },
    {
        "key": "p10", "num": 10, "title": "SPC y capacidad del proceso",
        "points": [("SPC: variación normal contra señales reales", "Separa la variación normal"),
                   ("Cp: dispersión contra especificación", "El Cp compara"),
                   ("Cpk: también revisa el centrado", "El Cpk también revisa"),
                   ("Solo con un proceso estable y un calibrador calibrado", "Los dos solo significan algo")],
        "example": "Torque de tornillos en la línea de Priya: variación cerrada y centrada da un Cpk ≈ 1.33. "
                   "Eso es capaz.",
        "example_cue": "Toma el torque de los tornillos",
        "script": "El control estadístico del proceso responde eso. Separa la variación normal de las "
                  "señales reales que necesitan acción. El Cp compara la dispersión de tu proceso con la "
                  "especificación. El Cpk también revisa si el proceso está centrado. Los dos solo "
                  "significan algo cuando el proceso es estable y el calibrador está calibrado. Toma el "
                  "torque de los tornillos en la línea de Priya. Con una variación cerrada y centrada, el "
                  "Cpk da alrededor de uno punto tres tres. Eso es capaz. ¿Pero cómo ves venir los riesgos?",
    },
    {
        "key": "p11", "num": 11, "title": "PFMEA y planes de control",
        "points": [("PFMEA: cómo puede fallar cada paso, y por qué", "Pregunta cómo cada paso"),
                   ("El plan de control lo convierte en revisiones reales", "Luego el plan de control"),
                   ("Método · frecuencia · responsable · reacción", "Cada revisión tiene un método"),
                   ("Actualiza los dos tras fallas reales", "Actualiza los dos cada vez")],
        "example": "Una almohadilla aislante faltante puede causar un corto → interbloqueo de presencia + "
                   "regla de parar y retener.",
        "example_cue": "En un equipo de audio",
        "script": "Usas un análisis de modos de falla del proceso. Pregunta cómo cada paso puede fallar, "
                  "por qué, y qué lo previene o lo detecta. Luego el plan de control lo convierte en "
                  "revisiones reales. Cada revisión tiene un método, una frecuencia, un responsable y una "
                  "reacción. En un equipo de audio, una almohadilla aislante faltante puede causar un "
                  "corto. Así que el análisis lleva a un interbloqueo de presencia y a una regla clara de "
                  "parar y retener. Actualiza los dos cada vez que una falla real te enseñe algo.",
    },
    {
        "key": "p12", "num": 12, "title": "Análisis de causa raíz",
        "points": [("Define el problema con precisión", "empieza por definir"),
                   ("Contén primero el inventario sospechoso", "Contén el inventario sospechoso"),
                   ("Hechos, cinco porqués, pruebas controladas", "Luego usa hechos"),
                   ("¿Por qué pasó? ¿Por qué no se detuvo?", "Tu solución debe responder")],
        "example": "El equipo de Priya rastreó sus fallas de carga hasta un conector mal asentado.",
        "example_cue": "El equipo de Priya rastreó",
        "script": "Y las fallas te van a enseñar, si escarbas bien. El análisis de causa raíz empieza por "
                  "definir el problema con precisión. Contén el inventario sospechoso primero. Luego usa "
                  "hechos, cinco porqués y pruebas controladas, nunca suposiciones. Tu solución debe "
                  "responder dos preguntas. ¿Por qué pasó el defecto? ¿Y por qué nuestros controles no lo "
                  "detuvieron? El equipo de Priya rastreó sus fallas de carga hasta un conector mal "
                  "asentado. Veamos qué hicieron después.",
    },
    {
        "key": "p13", "num": 13, "title": "Caso práctico: teléfono celular",
        "points": [("1,200 de 40,000 fallaron: 3%", "Mil doscientos de cuarenta"),
                   ("Datos separados por lote, fixture, estación, turno", "El equipo separó los datos"),
                   ("Fixture con guía + revisión automática del asentado", "Así que probaron"),
                   ("FMEA y SOP actualizados", "Actualizaron el análisis de modos de falla")],
        "example": "Las fallas bajaron a 0.5% — una reducción de 83%.",
        "example_cue": "Las fallas bajaron a medio",
        "script": "Este es el caso de Priya. Mil doscientos de cuarenta mil teléfonos fallaron la primera "
                  "prueba de carga. Es una tasa de falla del tres por ciento. El equipo separó los datos "
                  "por lote de conectores, fixture, estación y turno. El patrón apuntaba al fixture. Así "
                  "que probaron un fixture con guía y una revisión automática del asentado. Las fallas "
                  "bajaron a medio por ciento. Es una reducción del ochenta y tres por ciento. ¿Y qué hizo "
                  "que se quedara? Actualizaron el análisis de modos de falla y el SOP.",
    },
    {
        "key": "p14", "num": 14, "title": "Decodificador y audio",
        "points": [("El mismo pensamiento, controles a la medida", "Solo ajustas los controles"),
                   ("Decodificador: firmware que coincida con el SKU", "Así que haz coincidir el firmware"),
                   ("Audio: conectores con guía, unidades patrón", "Los conectores con guía y las revisiones con unidades patrón"),
                   ("Empaque: número de serie que coincida con la caja", "En empaque")],
        "example": "Decodificador: firmware, energía, etiquetas. Audio: polaridad, sellado, balance de "
                   "canales.",
        "example_cue": "Los defectos de los decodificadores muchas veces",
        "script": "El mismo pensamiento funciona en cada familia de productos. Solo ajustas los controles. "
                  "Los defectos de los decodificadores muchas veces tienen que ver con el firmware, la "
                  "energía y las etiquetas. Así que haz coincidir el firmware con el SKU, y bloquea la "
                  "carga equivocada. Los equipos de audio fallan en la polaridad de la bocina, el sellado y "
                  "el balance de canales. Los conectores con guía y las revisiones con unidades patrón "
                  "manejan eso. En empaque, el sistema compara cada número de serie con su caja. ¿Qué "
                  "protegerías primero en tu línea?",
    },
    {
        "key": "p15", "num": 15, "title": "KPI y ruta de 90 días",
        "points": [("Atrasados: FPY, PPM, costo de la mala calidad", "Vigila tus resultados atrasados"),
                   ("Adelantados: pruebas de reto, puntajes de auditoría", "Vigila también los controles adelantados"),
                   ("Días 1–30: base y contención", "En los primeros treinta días"),
                   ("Días 31–60: causas raíz, piloto de Poka Yoke", "En los siguientes treinta"),
                   ("Días 61–90: verificar ganancias, extender a todas partes", "En los últimos treinta")],
        "example": "Últimos 30 días: verifica las ganancias y extiéndelas a cada línea.",
        "example_cue": "En los últimos treinta",
        "script": "Por último, hazlo parte de la gestión diaria. Vigila tus resultados atrasados, como el "
                  "FPY, el PPM y el costo de la mala calidad. Vigila también los controles adelantados, "
                  "como las pruebas de reto de los interbloqueos y los puntajes de auditoría. Este es un "
                  "plan simple de noventa días. En los primeros treinta días, mide la base y contén. En los "
                  "siguientes treinta, encuentra las causas raíz y haz un piloto de Poka Yoke. En los "
                  "últimos treinta, verifica las ganancias y extiéndelas a cada línea.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Todo defecto se puede prevenir", "icon": "shield", "with": 0},
        {"label": "Bien a la primera", "icon": "check", "tone": "good", "with": 1},
        {"label": "Diseña el proceso", "icon": "gear", "with": 2},
        {"label": "Una disciplina", "icon": "clipboard", "with": 3}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "¿Conector asentado?", "icon": "sensor", "with": "example"},
            {"label": "Luego la prueba eléctrica", "icon": "test", "tone": "good", "with": "example"}]}},
    "p02": {"type": "timeline", "items": [
        {"label": "Calidad = cumplir los requisitos", "sub": "Crosby, 1960s", "icon": "clipboard", "with": 0},
        {"label": "Calidad integrada, a prueba de errores", "sub": "Lean moderno", "icon": "key", "with": 1},
        {"label": "Corrige el sistema, no a la persona", "sub": "Hoy", "icon": "gear", "with": 2}]},
    "p03": {"type": "icons", "items": [
        {"label": "Interna", "sub": "Desecho, retrabajo, reprueba", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "Externa", "sub": "Garantía, devoluciones", "icon": "box", "tone": "bad", "with": 1},
        {"label": "Oculta", "sub": "Retrasos, manejo, capacidad", "icon": "clock", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 32000, "prefix": "₹", "icon": "wrench", "label": "de retrabajo directo",
                 "unit": "400 teléfonos retrabajados en un mes", "with": "example"}},
    "p04": {"type": "icons", "items": [
        {"label": "Bien a la primera", "sub": "Sin ninguna corrección", "icon": "check", "with": 0},
        {"label": "Rendimiento a la primera", "sub": "Pasar un paso a la primera", "icon": "test", "with": 1},
        {"label": "Rendimiento acumulado", "sub": "Multiplica cada paso", "icon": "sequence", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "98% × 98% × 98% ≈ 94%", "suffix": "%", "with": "example", "items": [
            {"label": "Etapa 1", "value": 98, "with": "example"},
            {"label": "Etapa 2", "value": 98, "with": "example"},
            {"label": "Etapa 3", "value": 98, "with": "example"},
            {"label": "Juntas", "value": 94, "tone": "bad", "with": "example"}]}},
    "p05": {"type": "versus", "items": [
        {"label": "PPM", "sub": "Unidades defectuosas por millón", "icon": "count", "with": 0},
        {"label": "DPMO", "sub": "Defectos por millón de oportunidades", "icon": "search", "with": 1}],
        "then": {"type": "stat", "value": 500, "suffix": " PPM", "icon": "count", "label": "25 teléfonos malos en 50,000",
                 "unit": "Reporta siempre el tamaño de muestra y el alcance", "with": "example"}},
    "p06": {"type": "flow", "items": [
        {"label": "Sé dueño de tu trabajo", "icon": "hand", "with": 0},
        {"label": "Siguiente estación = cliente", "icon": "person", "with": 1},
        {"label": "Entradas, ajuste, SOP", "icon": "clipboard", "with": 2},
        {"label": "Para, separa, escala", "icon": "warning", "tone": "bad", "with": 3}]},
    "p07": {"type": "ladder", "top": "LO MÁS FUERTE", "bottom": "LO MÁS DÉBIL", "items": [
        {"label": "Hazlo imposible", "icon": "key", "with": 1},
        {"label": "Atrápalo al instante", "icon": "sensor", "with": 1},
        {"label": "Etiqueta de advertencia", "icon": "warning", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "El fixture entra de una forma", "icon": "shape", "with": "example"},
            {"label": "Revisión registrada", "icon": "clipboard", "with": "example"},
            {"label": "Solo entonces avanza el teléfono", "icon": "check", "tone": "good", "with": "example"}]}},
    "p08": {"type": "flow", "items": [
        {"label": "Anormalidad detectada", "sub": "Jidoka", "icon": "sensor", "with": 0},
        {"label": "Andon: hazlo visible", "icon": "warning", "with": 1},
        {"label": "Para, retén los sospechosos", "icon": "lock", "tone": "bad", "with": "example"},
        {"label": "Arranca cuando esté controlado", "icon": "check", "tone": "good", "with": 3}]},
    "p09": {"type": "doc", "items": [
        {"label": "Trabajo estándar · Estación de firmware", "icon": "label", "with": 0},
        {"label": "Primera unidad verificada tras el cambio", "icon": "check", "with": 1},
        {"label": "Imagen aprobada + receta coincidente", "icon": "chip", "with": "example"},
        {"label": "Suma de verificación antes de liberar", "icon": "lock", "with": "example"},
        {"label": "Auditoría por capas: controles, no papeleo", "icon": "search", "with": 3}]},
    "p10": {"type": "icons", "items": [
        {"label": "Ruido contra señal real", "icon": "wave", "with": 0},
        {"label": "Cp: dispersión contra especificación", "icon": "scale", "with": 1},
        {"label": "Cpk: también centrado", "icon": "pin", "with": 2},
        {"label": "Proceso estable, calibrador calibrado", "icon": "gear", "with": 3}],
        "then": {"type": "stat", "value": 1.33, "decimals": 2, "icon": "screw", "label": "Cpk del torque de tornillos",
                 "unit": "Variación cerrada y centrada: capaz", "with": "example"}},
    "p11": {"type": "flow", "items": [
        {"label": "PFMEA: cómo puede fallar", "icon": "search", "with": 0},
        {"label": "Plan de control: revisiones reales", "icon": "clipboard", "with": 1},
        {"label": "Método · frecuencia · responsable · reacción", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Almohadilla aislante faltante", "sub": "Puede causar un corto", "icon": "warning", "tone": "bad", "with": "example"},
            {"label": "Interbloqueo de presencia", "icon": "sensor", "with": "example"},
            {"label": "Regla de parar y retener", "icon": "lock", "tone": "good", "with": "example"}]}},
    "p12": {"type": "flow", "items": [
        {"label": "Define con precisión", "icon": "clipboard", "with": 0},
        {"label": "Contén el inventario sospechoso", "icon": "lock", "with": 1},
        {"label": "Hechos, cinco porqués, pruebas", "icon": "test", "with": 2},
        {"label": "¿Por qué se hizo? ¿Por qué no se detuvo?", "icon": "search", "tone": "good", "with": 3}]},
    "p13": {"type": "stat", "value": 3, "suffix": "%", "icon": "power", "label": "fallaron la primera prueba de carga",
            "unit": "1,200 de 40,000 teléfonos", "with": 0,
            "then": {"type": "compare", "before": {"label": "Antes", "value": 3}, "after": {"label": "Después", "value": 0.5},
                     "decimals": 1, "suffix": "%", "unit": "teléfonos que fallan la primera prueba de carga",
                     "note": "Una reducción de 83%", "with": "example"}},
    "p14": {"type": "icons", "items": [
        {"label": "Decodificador", "sub": "Firmware que coincide con el SKU", "icon": "chip", "with": 1},
        {"label": "Audio", "sub": "Conectores con guía, unidades patrón", "icon": "wave", "with": 2},
        {"label": "Empaque", "sub": "Número de serie que coincide con la caja", "icon": "barcode", "with": 3}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Base y contención", "sub": "Días 1–30", "icon": "lock", "with": 2},
        {"label": "Causas raíz, piloto de Poka Yoke", "sub": "31–60", "icon": "search", "with": 3},
        {"label": "Verificar ganancias, extender a todas partes", "sub": "61–90", "icon": "chartUp", "with": 4}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "970 de 1,000 unidades pasan la primera prueba sin retrabajo. ¿Cuál es el rendimiento a "
                    "la primera?",
        "options": ["3%", "97%", "9.7 por unidad"],
        "correct": 1,
        "explanation": "FPY = aceptadas a la primera ÷ total = 970 ÷ 1,000 = 97%. Solo cuenta las unidades que "
                       "pasaron a la primera, sin retrabajo.",
        "q_script": "Prueba rápida. Novecientas setenta de mil unidades pasan la primera prueba, sin "
                    "retrabajo. ¿Cuál es el rendimiento a la primera? Tómate unos segundos.",
        "a_script": "Es noventa y siete por ciento. El rendimiento a la primera solo cuenta las unidades que "
                    "pasaron a la primera, divididas entre el total.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Una línea de audio encuentra la polaridad de la bocina invertida en 30 unidades este "
                    "turno. ¿Qué debe hacer PRIMERO el equipo?",
        "options": ["Volver a entrenar al operador y seguir", "Parar, contener las unidades sospechosas, y luego encontrar la causa raíz",
                    "Agregar una etiqueta de advertencia a la bocina", "Aumentar la inspección final"],
        "correct": 1,
        "explanation": "Primero contén: para y retén las unidades sospechosas hasta el último punto bueno. Luego "
                       "encuentra la causa raíz y prevénla, por ejemplo con un conector de polaridad con guía. "
                       "Culpar, poner etiquetas y más inspección no evitan que se repita.",
        "q_script": "Una más, y esta es un escenario. Una línea de audio encuentra la polaridad de la bocina "
                    "invertida en treinta unidades este turno. ¿Qué debe hacer primero el equipo? Piénsalo.",
        "a_script": "Para y contén primero las unidades sospechosas. Luego encuentra la causa raíz, y "
                    "prevénla, por ejemplo con un conector de polaridad con guía. Culpar, poner etiquetas y "
                    "más inspección no evitarán que regrese.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
