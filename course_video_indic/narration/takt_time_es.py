"""takt_time in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh takt_time_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "tt_es"
NAME = "takt_time_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Uniform Production": "iúniform prodákshon",
    "Yamazumi": "Yamazumi",
    "Heijunka": "Jeiyunka",
    "Kanban": "Kanban",
    "SMED": "esméd",
    "TAKT": "takt",
    "UPPH": "u pe pe hache",
    "UPH": "u pe hache",
    "WIP": "doble u i pe",
    "SOP": "ese o pe",
    "A": "a",
    "B": "be",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Cada máquina en la línea de cámaras de Rohan se veía ocupada. Las estaciones del inicio "
    "iban a toda velocidad. Aun así, embarques seguía perdiendo el camión. ¿Cómo puede una "
    "línea ocupada llegar tarde? En esta lección aprenderás el tiempo TAKT, el compás que "
    "marca tu cliente. Verás cómo calcularlo bien, y usarlo para balancear, asignar personal "
    "y correr tu línea. Seguiremos a Rohan, ingeniero de planeación en una planta de cámaras."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. El TAKT es el tiempo neto disponible dividido entre la "
    "demanda del cliente. Es el ritmo que necesitas, no el tiempo que de verdad tarda una "
    "estación. Y planea con las pérdidas reales, como los paros y el rendimiento, no con la "
    "velocidad teórica. Esta es tu acción para esta semana. Calcula el TAKT de una de tus "
    "líneas, y compáralo con tu estación más lenta. Excelente trabajo al completar esta "
    "lección. Ahora aprenderás Uniform Production."
)

# One story thread: Rohan's network-camera plant. 7,200 good cameras/day, 1,200 net
# minutes/day over three shifts -> TAKT 10 s; final test 18 s per unit is the constraint.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es el tiempo TAKT",
        "points": [("Takt: en alemán, compás o ritmo", "El TAKT viene"),
                   ("El ritmo que cumple la demanda del cliente", "Es el ritmo"),
                   ("TAKT = tiempo neto disponible ÷ demanda", "Divide tu tiempo neto")],
        "example": "420 minutos netos ÷ 840 cámaras = una cámara cada 30 segundos.",
        "example_cue": "Digamos que un turno tiene",
        "script": "Esta es la idea central. El TAKT viene de la palabra alemana para compás, o ritmo. Es el "
                  "ritmo al que debes terminar unidades para cumplir la demanda del cliente. La fórmula es "
                  "simple. Divide tu tiempo neto disponible entre la demanda. Digamos que un turno tiene "
                  "cuatrocientos veinte minutos. El cliente necesita ochocientas cuarenta cámaras. Es una "
                  "cámara cada treinta segundos. ¿Es el tiempo que de verdad tarda un operador? No.",
    },
    {
        "key": "p02", "num": 2, "title": "Por qué importa el TAKT",
        "points": [("Une a tu cliente con el piso de producción", "El TAKT une a tu cliente"),
                   ("Sin un ritmo común → sobreproducción, WIP", "Sin un ritmo común"),
                   ("Planear personal, balancear el trabajo, dar ritmo a los materiales", "El TAKT te ayuda a planear")],
        "example": "El ensamble de Rohan armó 1,000 cámaras de más antes de la prueba. La utilización se "
                   "veía muy bien; los camiones igual salían tarde.",
        "example_cue": "Su ensamble armó",
        "script": "El TAKT une a tu cliente con el piso de producción. Sin un ritmo común, las primeras "
                  "estaciones sobreproducen, y el WIP se amontona. Los faltantes se esconden, y embarques "
                  "se vuelve una carrera. Eso es justo lo que le pasó a Rohan. Su ensamble armó mil cámaras "
                  "de más antes de la prueba. La utilización se veía muy bien. Pero los camiones igual "
                  "salían tarde. El TAKT te ayuda a planear el personal, balancear el trabajo, y dar ritmo "
                  "a los materiales. Pero primero necesitas los números correctos. ¿Por dónde empiezas?",
    },
    {
        "key": "p03", "num": 3, "title": "Tiempo neto disponible",
        "points": [("Empieza con la duración del turno", "Toma la duración de tu turno"),
                   ("Resta descansos planeados, juntas, limpieza", "Luego resta los descansos planeados"),
                   ("Aquí no restes los paros imprevistos", "no restes los paros imprevistos"),
                   ("Anota tus supuestos", "anota tus supuestos")],
        "example": "Turno de 480 min − descansos − una junta corta = 420 minutos netos.",
        "example_cue": "Un turno de ocho horas",
        "script": "Empieza con el tiempo neto disponible. Toma la duración de tu turno. Luego resta los "
                  "descansos planeados, las juntas y la limpieza planeada. Un turno de ocho horas son "
                  "cuatrocientos ochenta minutos. Quita los descansos y una junta corta, y te quedan "
                  "cuatrocientos veinte. Pero aquí no restes los paros imprevistos. Esa es una pérdida que "
                  "manejas cuando revisas la capacidad. Sé consistente, y anota tus supuestos. ¿Y la otra "
                  "mitad de la fórmula?",
    },
    {
        "key": "p04", "num": 4, "title": "Demanda del cliente",
        "points": [("Demanda y tiempo: el mismo periodo", "La demanda debe cubrir"),
                   ("Unidades buenas necesarias, no unidades iniciadas", "Usa las unidades buenas"),
                   ("Varios modelos: revisa cada uno", "En una línea de varios modelos"),
                   ("Recalcula cuando cambien la demanda o los turnos", "recalcula cada vez")],
        "example": "Demanda diaria con el tiempo de un turno = sin sentido.",
        "example_cue": "Mezclar la demanda diaria",
        "script": "La demanda debe cubrir el mismo periodo que tu tiempo. Si usas la demanda diaria, usa "
                  "también el tiempo neto diario. Mezclar la demanda diaria con el tiempo de un turno no "
                  "tiene sentido. Usa las unidades buenas que tu cliente necesita, no las unidades que "
                  "inicias. En una línea de varios modelos, el TAKT total es una guía. Pero cada modelo "
                  "todavía necesita su propia revisión de capacidad. Y recalcula cada vez que cambien la "
                  "demanda o los turnos. ¿Y en qué se diferencia el TAKT del tiempo de ciclo?",
    },
    {
        "key": "p05", "num": 5, "title": "TAKT contra tiempo de ciclo y tiempo de entrega",
        "points": [("TAKT: el ritmo que necesitas", "El TAKT es el ritmo que necesitas"),
                   ("Tiempo de ciclo: lo que tarda una estación", "El tiempo de ciclo es"),
                   ("Tiempo de entrega: todo el recorrido", "El tiempo de entrega es"),
                   ("Ciclo > TAKT = no puede seguir el paso", "Si tu tiempo de ciclo")],
        "example": "Una de las líneas de Rohan: prueba final de 38 s contra un TAKT de 30 s. Necesitaba "
                   "mejorar, o un segundo probador.",
        "example_cue": "En una de las líneas de Rohan",
        "script": "Esta es la confusión más común. El TAKT es el ritmo que necesitas. El tiempo de ciclo es "
                  "lo que de verdad tarda una estación, medido en el piso. El tiempo de entrega es todo el "
                  "recorrido, con esperas y movimientos. Si tu tiempo de ciclo es más largo que el TAKT, "
                  "esa estación no puede seguir el paso. En una de las líneas de Rohan, la prueba final "
                  "tardaba treinta y ocho segundos, contra un TAKT de treinta. Necesitaba mejorar, o un "
                  "segundo probador. Siempre define primero tus puntos de inicio y fin.",
    },
    {
        "key": "p06", "num": 6, "title": "Pitch, UPH y UPPH",
        "points": [("UPH: el ritmo por hora que necesitas", "Unidades por hora"),
                   ("Pitch: el tiempo para llenar un empaque", "El pitch es"),
                   ("UPPH: producción buena por hora-persona", "El UPPH mide"),
                   ("La teoría no es producción", "la teoría no es producción")],
        "example": "TAKT de 24 s → 150 unidades por hora. Empaque de 20 → un pitch de 8 minutos.",
        "example_cue": "Con un TAKT de",
        "script": "El TAKT se liga a otros números útiles. Unidades por hora, o UPH, es el ritmo por hora "
                  "que necesitas. El pitch es el tiempo para llenar un empaque estándar. Con un TAKT de "
                  "veinticuatro segundos, necesitas ciento cincuenta unidades por hora. Un empaque de "
                  "veinte da un pitch de ocho minutos. El UPPH mide la producción buena por hora-persona. "
                  "Pero recuerda, la teoría no es producción. La salida real depende del tiempo en marcha y "
                  "del rendimiento. ¿Y cómo balanceas el trabajo?",
    },
    {
        "key": "p07", "num": 7, "title": "Balancear con Yamazumi",
        "points": [("Mide el tiempo de cada elemento de trabajo", "Divide cada trabajo"),
                   ("Apila el trabajo de cada operador como una barra", "Apila el trabajo de cada operador"),
                   ("Traza la línea del TAKT de lado a lado", "Luego traza la línea del TAKT"),
                   ("Mueve o rediseña dentro de la seguridad y la habilidad", "Así que mueves o rediseñas")],
        "example": "TAKT de 40 s: el operador A tiene 52 s de trabajo, el operador B solo 25 s.",
        "example_cue": "En una de las celdas de Rohan",
        "script": "Usas una gráfica Yamazumi. Divide cada trabajo en elementos repetibles, y mide su "
                  "tiempo. Apila el trabajo de cada operador como una barra. Luego traza la línea del TAKT "
                  "de lado a lado. Cualquier barra arriba de la línea está sobrecargada. En una de las "
                  "celdas de Rohan, el TAKT era de cuarenta segundos. El operador A tenía cincuenta y dos "
                  "segundos de trabajo. El operador B tenía solo veinticinco. Así que mueves o rediseñas "
                  "tareas, dentro de los límites de seguridad y habilidad. ¿Cuántas personas necesitas?",
    },
    {
        "key": "p08", "num": 8, "title": "Mínimo de operadores",
        "points": [("Contenido de trabajo ÷ TAKT, redondea hacia arriba", "Divide el contenido total de trabajo manual"),
                   ("Solo un punto de partida", "tómalo como un punto de partida"),
                   ("Usa un estudio de tiempos estable", "Usa un estudio de tiempos estable")],
        "example": "310 s de trabajo ÷ TAKT de 40 s = 7.75 → al menos 8 operadores.",
        "example_cue": "La celda de Rohan tenía",
        "script": "Esta es una estimación rápida. Divide el contenido total de trabajo manual entre el "
                  "TAKT, y redondea hacia arriba. La celda de Rohan tenía trescientos diez segundos de "
                  "trabajo por cámara. Con un TAKT de cuarenta, da siete punto setenta y cinco. Así que "
                  "necesitas al menos ocho operadores. Pero tómalo como un punto de partida. Las caminatas, "
                  "el surtido, las revisiones de calidad y los niveles de habilidad importan. Usa un "
                  "estudio de tiempos estable, no un solo ciclo en el mejor caso. ¿Qué limita tu "
                  "producción?",
    },
    {
        "key": "p09", "num": 9, "title": "Cuellos de botella y estaciones en paralelo",
        "points": [("El cuello de botella limita la producción buena", "Es el paso que limita"),
                   ("Capacidad = 3,600 ÷ tiempo de ciclo", "La capacidad por hora de una estación"),
                   ("Aplica el tiempo en marcha y el rendimiento a la primera", "Aplica el tiempo en marcha"),
                   ("Evidencia antes de comprar una máquina", "Revisa la evidencia")],
        "example": "Dos probadores de 50 s = 144 intentos por hora → unas 127 unidades buenas tras el tiempo "
                   "en marcha y el rendimiento.",
        "example_cue": "Dos probadores de cincuenta",
        "script": "El cuello de botella. Es el paso que limita tu producción buena. La capacidad por hora "
                  "de una estación es tres mil seiscientos segundos, divididos entre su tiempo de ciclo. "
                  "Dos probadores de cincuenta segundos cada uno dan ciento cuarenta y cuatro intentos por "
                  "hora. Pero los probadores se paran, y algunas unidades fallan. Aplica el tiempo en "
                  "marcha y el rendimiento a la primera, y te quedan unas ciento veintisiete unidades "
                  "buenas. Revisa la evidencia antes de comprar otra máquina. ¿Y los modelos mezclados?",
    },
    {
        "key": "p10", "num": 10, "title": "Modelos mezclados y Heijunka",
        "points": [("Un solo TAKT no le queda a todos los modelos", "Un solo TAKT"),
                   ("Revisa los tiempos de estación de cada modelo", "Así que revisa los tiempos de cada modelo"),
                   ("Heijunka: nivela el volumen y la mezcla", "Usa el Heijunka"),
                   ("SMED: reduce las pérdidas por cambio de modelo", "usa el SMED")],
        "example": "60% Modelo A, 40% Modelo B con una prueba más larga: programa todos los B juntos y la "
                   "prueba se ahoga.",
        "example_cue": "Digamos que el sesenta por ciento",
        "script": "Un solo TAKT no garantiza que todos los modelos quepan. Digamos que el sesenta por "
                  "ciento de la demanda de Rohan es el Modelo A, y el cuarenta por ciento es el Modelo B. "
                  "El Modelo B necesita una prueba más larga. Si el plan programa todos los B juntos, la "
                  "prueba se ahoga, aunque el promedio se vea bien. Así que revisa los tiempos de cada "
                  "modelo. Usa el Heijunka para nivelar el volumen y la mezcla. Y usa el SMED para reducir "
                  "tus pérdidas por cambio de modelo. ¿Y los materiales?",
    },
    {
        "key": "p11", "num": 11, "title": "Flujo de materiales y Kanban",
        "points": [("El TAKT marca el ritmo de los materiales", "El TAKT también marca"),
                   ("Kanban: tiempo de entrega, tamaño del contenedor", "Las cantidades del Kanban"),
                   ("Límites de WIP entre procesos", "Fija límites de WIP"),
                   ("No liberes trabajo solo para estar ocupado", "No liberes nuevo trabajo")],
        "example": "TAKT de 30 s, caja de 40 → dura 20 minutos; el surtido debe llegar antes.",
        "example_cue": "Con un TAKT de treinta segundos",
        "script": "El TAKT también marca el ritmo de los materiales. Con un TAKT de treinta segundos, una "
                  "caja de cuarenta piezas dura veinte minutos. Así que el surtido debe llegar antes de que "
                  "se acabe, con algo de protección para la variación. Las cantidades del Kanban también "
                  "dependen del tiempo de entrega y del tamaño del contenedor. Fija límites de WIP entre "
                  "procesos. Y esta es una regla dura. No liberes nuevo trabajo solo para mantener ocupada "
                  "cada estación. ¿Y cómo corres el día?",
    },
    {
        "key": "p12", "num": 12, "title": "Plan contra real cada hora",
        "points": [("Planeado = segundos netos ÷ TAKT", "Las unidades planeadas son"),
                   ("Compara lo real con el plan", "Digamos que haces"),
                   ("Registra por qué: paros, rechazos, material", "Ahora registra por qué"),
                   ("No culpes a la velocidad del operador", "No culpes cada faltante")],
        "example": "TAKT de 30 s → 120 planeadas por hora. Hechas 108 = 90%, una brecha de 12.",
        "example_cue": "Con un TAKT de treinta segundos",
        "script": "Usa un tablero de plan contra real cada hora. Las unidades planeadas son los segundos "
                  "netos de la hora, divididos entre el TAKT. Con un TAKT de treinta segundos, planeas "
                  "ciento veinte cámaras buenas. Digamos que haces ciento ocho. Es el noventa por ciento, y "
                  "una brecha de doce. Ahora registra por qué. Paros, rechazos, material, o personal. No "
                  "culpes cada faltante a la velocidad del operador. ¿Listo para el caso completo de Rohan?",
    },
    {
        "key": "p13", "num": 13, "title": "Caso práctico: planta de cámaras",
        "points": [("7,200 cámaras buenas al día, 1,200 min netos", "La planta de Rohan debe embarcar"),
                   ("TAKT = 10 segundos", "Así que el TAKT es de diez segundos"),
                   ("La prueba tarda 18 s — la restricción", "Pero la prueba tarda"),
                   ("Dos probadores ≈ 353 buenas/hora contra 360", "Dos probadores dan")],
        "example": "2 probadores = 400 intentos/hora en papel → ≈ 353 buenas con el tiempo en marcha y el "
                   "rendimiento reales. Meta: 360.",
        "example_cue": "Con el tiempo en marcha",
        "script": "La planta de Rohan debe embarcar siete mil doscientas cámaras buenas al día. Tiene mil "
                  "doscientos minutos netos, en tres turnos. Así que el TAKT es de diez segundos. Las "
                  "estaciones de lente y ensamble son más rápidas que eso. Pero la prueba tarda dieciocho "
                  "segundos. Dos probadores dan cuatrocientos intentos por hora en papel. Con el tiempo en "
                  "marcha y el rendimiento reales, son unas trescientas cincuenta y tres unidades buenas. "
                  "La meta es trescientas sesenta. ¿Qué harías tú?",
    },
    {
        "key": "p14", "num": 14, "title": "Errores comunes",
        "points": [("SÍ usa la demanda aprobada y el tiempo neto", "Usa la demanda aprobada"),
                   ("SÍ actualiza el TAKT cuando algo cambie", "Actualiza el TAKT"),
                   ("NO lo confundas con el tiempo de ciclo", "No lo confundas"),
                   ("NO te saltes pruebas, pasos ni descansos", "nunca persigas la velocidad saltándote pruebas, pasos del SOP")],
        "example": "Rohan mejoró el tiempo en marcha del probador y recortó el ciclo de prueba antes de "
                   "comprar un tercer probador.",
        "example_cue": "Rohan mejoró el tiempo en marcha",
        "script": "Rohan mejoró el tiempo en marcha del probador, y recortó el ciclo de prueba, antes de "
                  "comprar un tercer probador. Ahora, cuidado con los errores comunes. Usa la demanda "
                  "aprobada y el tiempo neto correcto. Actualiza el TAKT cuando cambien la demanda o los "
                  "turnos. No lo confundas con el tiempo de ciclo. No uses las horas brutas del turno. Y "
                  "nunca persigas la velocidad saltándote pruebas, pasos del SOP o descansos. ¿Tus líderes "
                  "pueden explicar los números detrás del TAKT de tu tablero?",
    },
    {
        "key": "p15", "num": 15, "title": "Ruta de 90 días",
        "points": [("Días 1–30: demanda, tiempo neto, tiempos de ciclo", "En los primeros treinta días"),
                   ("Días 31–60: Yamazumi, tableros por hora", "En los siguientes treinta"),
                   ("Días 61–90: verifica producción y rendimiento, crece", "En los últimos treinta"),
                   ("Meta: producción buena confiable", "Recuerda la meta")],
        "example": "Producción buena confiable al ritmo del cliente — no mantener ocupada cada estación.",
        "example_cue": "Es producción buena confiable",
        "script": "Empieza con una línea representativa de tu planta. En los primeros treinta días, reúne "
                  "la demanda, el tiempo neto y los tiempos de ciclo reales, y mapea el balance actual. En "
                  "los siguientes treinta, haz un piloto de Yamazumi, trabajo estándar y tableros por hora. "
                  "Ataca el cuello de botella. En los últimos treinta, verifica la producción y el "
                  "rendimiento, entrena respaldos, y crece. Recuerda la meta. Es producción buena confiable "
                  "al ritmo del cliente. No mantener ocupada cada estación.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Takt = compás", "icon": "wave", "with": 0}, {"label": "El ritmo que marca la demanda", "icon": "clock", "with": 1},
        {"label": "Tiempo neto ÷ demanda", "icon": "count", "with": 2}],
        "then": {"type": "stat", "value": 30, "suffix": " s", "icon": "camera", "label": "una cámara cada 30 segundos",
                 "unit": "420 minutos netos ÷ 840 cámaras", "with": "example"}},
    "p02": {"type": "versus", "items": [
        {"label": "1,000 armadas antes de la prueba", "sub": "Estaciones ocupadas, camiones tarde", "icon": "stack", "with": "example"},
        {"label": "Un ritmo común", "sub": "Personal, balance, materiales", "icon": "clock", "with": 2}]},
    "p03": {"type": "flow", "items": [
        {"label": "Turno de 480 min", "icon": "clock", "with": 0},
        {"label": "− descansos, junta, limpieza", "icon": "calendar", "with": 1},
        {"label": "= 420 minutos netos", "sub": "Los paros imprevistos no se restan aquí", "icon": "check", "tone": "good", "with": "example"}]},
    "p04": {"type": "versus", "items": [
        {"label": "Demanda diaria ÷ un turno", "sub": "No tiene sentido", "icon": "cross", "with": "example"},
        {"label": "El mismo periodo para los dos", "sub": "Unidades buenas, no unidades iniciadas", "icon": "calendar", "with": 0}]},
    "p05": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "El ritmo que necesitas", "icon": "clock", "with": 0},
        {"label": "Tiempo de ciclo", "sub": "Lo que tarda una estación", "icon": "gear", "with": 1},
        {"label": "Tiempo de entrega", "sub": "Todo el recorrido", "icon": "sequence", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "La prueba no sigue el paso: mejórala, o agrega un probador", "unit": "segundos por cámara", "with": "example", "items": [
            {"label": "TAKT", "value": 30, "tone": "good", "with": "example"},
            {"label": "Prueba final", "value": 38, "tone": "bad", "with": "example"}]}},
    "p06": {"type": "icons", "items": [
        {"label": "UPH", "sub": "Ritmo por hora necesario", "icon": "chartUp", "with": 0},
        {"label": "Pitch", "sub": "Tiempo para llenar un empaque", "icon": "box", "with": 1},
        {"label": "UPPH", "sub": "Producción buena por hora-persona", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "TAKT 24 s", "icon": "clock", "with": "example"},
            {"label": "= 150 unidades por hora", "icon": "chartUp", "with": "example"},
            {"label": "Empaque de 20 = pitch de 8 min", "icon": "box", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Mide cada elemento", "icon": "clock"}, {"label": "Apila cada operador", "icon": "stack"},
        {"label": "Traza la línea del TAKT", "icon": "sequence"}, {"label": "Mueve trabajo, con seguridad", "icon": "person"}],
        "then": {"type": "bars", "label": "TAKT", "value": 40, "suffix": " s", "note": "A está sobrecargado", "unit": "segundos de trabajo por operador", "with": "example", "items": [
            {"label": "Operador A", "value": 52, "tone": "bad", "with": "example"},
            {"label": "Operador B", "value": 25, "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Trabajo ÷ TAKT, redondea hacia arriba", "icon": "count", "with": 0},
        {"label": "Un punto de partida", "icon": "sequence", "with": 1},
        {"label": "Estudio de tiempos estable", "icon": "clock", "with": 2}],
        "then": {"type": "stat", "value": 8, "icon": "person", "label": "operadores, al menos",
                 "unit": "310 s de trabajo ÷ TAKT de 40 s = 7.75, redondeado hacia arriba", "with": "example"}},
    "p09": {"type": "icons", "items": [
        {"label": "El cuello de botella", "icon": "warning", "tone": "bad"}, {"label": "3,600 ÷ tiempo de ciclo", "icon": "count"},
        {"label": "Tiempo en marcha × rendimiento", "icon": "chartUp"}, {"label": "Primero la evidencia", "icon": "search"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "2 probadores de 50 s", "icon": "test", "with": "example"},
            {"label": "144 intentos por hora", "icon": "count", "with": "example"},
            {"label": "≈ 127 buenas tras tiempo en marcha y rendimiento", "icon": "check", "tone": "good", "with": "example"}]}},
    "p10": {"type": "versus", "items": [
        {"label": "Todos los B juntos", "sub": "La prueba se ahoga", "icon": "stack", "with": "example"},
        {"label": "Nivela la mezcla", "sub": "Heijunka + SMED", "icon": "sequence", "with": 2}]},
    "p11": {"type": "stat", "value": 20, "suffix": " min", "icon": "box", "label": "una caja de 40 piezas dura",
            "unit": "con un TAKT de 30 s: el surtido debe llegar antes", "with": "example"},
    "p12": {"type": "bars", "label": "", "note": "90%: una brecha de 12. Registra por qué.", "unit": "cámaras buenas en una hora, TAKT de 30 s", "items": [
        {"label": "Planeado", "value": 120, "with": "example"},
        {"label": "Hecho", "value": 108, "tone": "bad", "with": "example"}]},
    "p13": {"type": "stat", "value": 10, "suffix": " s", "icon": "clock", "label": "TAKT para 7,200 cámaras buenas al día",
            "unit": "1,200 minutos netos ÷ 7,200 cámaras", "with": 1,
            "then": {"type": "bars", "label": "Meta", "value": 360, "unit": "cámaras buenas por hora, dos probadores", "with": 3, "items": [
                {"label": "En papel", "value": 400, "with": 3},
                {"label": "Real", "value": 353, "tone": "bad", "with": 3}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Demanda aprobada + tiempo neto", "icon": "check", "tone": "good"},
        {"label": "Actualizar cuando algo cambie", "icon": "sequence", "tone": "good"},
        {"label": "No es tiempo de ciclo", "icon": "cross", "tone": "bad"},
        {"label": "Nunca saltarse pruebas ni descansos", "icon": "warning", "tone": "bad"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Demanda, tiempo neto, tiempos de ciclo", "sub": "Días 1–30", "icon": "clipboard", "with": 0},
        {"label": "Yamazumi, tableros por hora", "sub": "31–60", "icon": "stack", "with": 1},
        {"label": "Verificar producción y rendimiento, crecer", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un turno tiene 25,200 segundos netos y el cliente necesita 840 unidades. ¿Cuál es el "
                    "tiempo TAKT?",
        "options": ["20 segundos", "30 segundos", "40 segundos"],
        "correct": 1,
        "explanation": "TAKT = tiempo neto disponible ÷ demanda = 25,200 ÷ 840 = 30 segundos por unidad.",
        "q_script": "Prueba rápida. Un turno tiene veinticinco mil doscientos segundos netos. El cliente "
                    "necesita ochocientas cuarenta unidades. ¿Cuál es el tiempo TAKT? Tómate unos segundos.",
        "a_script": "Son treinta segundos. El TAKT es el tiempo neto disponible dividido entre la demanda. "
                    "Así que una unidad cada treinta segundos.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "La prueba final tarda 38 s por unidad, pero el TAKT es de 30 s. Un gerente dice: \"Diles "
                    "a los probadores que vayan más rápido.\" ¿Qué debe hacer PRIMERO el equipo?",
        "options": ["Saltarse parte de la prueba para ahorrar tiempo", "Analizar las pérdidas y la capacidad de la estación de prueba",
                    "Armar inventario extra antes", "Recalcular el TAKT con el tiempo bruto del turno"],
        "correct": 1,
        "explanation": "Un tiempo de ciclo arriba del TAKT es un problema de capacidad. Estudia las pérdidas, el "
                       "ciclo y el tiempo en marcha de la estación, y luego mejórala o agrega capacidad "
                       "verificada. Saltarse pruebas o esconderlo con inventario crea problemas nuevos.",
        "q_script": "Una más, y esta es un escenario. La prueba final tarda treinta y ocho segundos, pero el "
                    "TAKT es de treinta. Un gerente dice, diles a los probadores que vayan más rápido. ¿Qué "
                    "debe hacer primero el equipo? Piénsalo.",
        "a_script": "Analiza primero la estación de prueba. Estudia sus pérdidas, su ciclo y su tiempo en "
                    "marcha, y luego mejórala, o agrega capacidad comprobada. Saltarse pruebas o armar "
                    "inventario solo crea problemas nuevos.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
