"""ishikawa in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh ishikawa_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ik_es"
NAME = "ishikawa_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Kaoru Ishikawa": "Kaoru Ishikawa",
    "Ishikawa": "Ishikawa",
    "Pareto": "Pareto",
    "Jidoka": "Yidoka",
    "Gemba": "Guemba",
    "PFMEA": "pe efe eme e a",
    "SOP": "ese o pe",
    "ESD": "e ese de",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Las fallas en la prueba de puertos de la línea de switches se multiplicaron por seis en "
    "una semana. La primera junta duró dos horas. Terminó con una sola decisión. Comprar un "
    "probador nuevo. ¿Te suena familiar? En esta lección aprenderás el diagrama de Ishikawa, "
    "también llamado espina de pescado. Verás cómo buscar causas a lo ancho, y luego "
    "comprobar las reales antes de gastar una rupia. Seguiremos a Nikhil, ingeniero de "
    "calidad en una línea de switches de red."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Empieza con un efecto preciso y medible en la cabeza. Busca "
    "a lo ancho en las seis M, sin culpar. Y trata cada espina como una suposición hasta que "
    "la evidencia la compruebe. Esta es tu acción para esta semana. Dibuja una espina de "
    "pescado para un problema que se repite, y elige las tres causas que probarás primero. "
    "Excelente trabajo al completar esta lección. Ahora aprenderás Jidoka."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es una espina de pescado",
        "points": [("Un problema en la cabeza", "Un problema va"),
                   ("Las posibles causas en las espinas", "posibles causas"),
                   ("Una herramienta para pensar en equipo", "Es una herramienta de equipo")],
        "example": "El problema de Nikhil: switches de red que fallan la prueba de enlace de puertos.",
        "example_cue": "El problema de Nikhil",
        "script": "Un diagrama de Ishikawa parece el esqueleto de un pescado. Un problema va en la cabeza. "
                  "Todas las posibles causas salen de las espinas, ordenadas en familias. Es una "
                  "herramienta de equipo, para que todos vean toda la búsqueda en una página. Evita que "
                  "saltes a la primera idea. El problema de Nikhil eran switches de red que fallaban la "
                  "prueba de enlace de puertos. ¿De dónde vino esta herramienta?",
    },
    {
        "key": "p02", "num": 2, "title": "Origen, y sus límites",
        "points": [("Kaoru Ishikawa, pionero de la calidad", "Kaoru Ishikawa"),
                   ("Una de las siete herramientas básicas de calidad", "siete herramientas básicas de calidad"),
                   ("Muestra posibles causas, no prueba nada", "no prueba")],
        "example": "Comprar un probador nuevo era una suposición. La espina de pescado la volvería una "
                   "suposición entre muchas.",
        "example_cue": "Comprar un probador nuevo",
        "script": "La hizo popular Kaoru Ishikawa, un experto japonés en calidad. Es una de las siete "
                  "herramientas básicas de calidad. Pero esto es lo clave. Muestra posibles causas, y no "
                  "prueba ninguna. La prueba viene después, de la observación, la medición y los ensayos. "
                  "Comprar un probador nuevo era solo una suposición. La espina de pescado la volvería una "
                  "suposición entre muchas. ¿Y cómo se ve el pescado?",
    },
    {
        "key": "p03", "num": 3, "title": "Anatomía del pescado",
        "points": [("Cabeza: el efecto", "La cabeza es"),
                   ("Columna y espinas mayores: familias de causas", "La columna une"),
                   ("Espinas menores: causas específicas", "Las espinas menores llevan")],
        "example": "Escribe una causa como “sospechosa” hasta que se compruebe.",
        "example_cue": "La regla de Nikhil",
        "script": "Léelo de izquierda a derecha. La cabeza es el efecto, el problema que quieres resolver. "
                  "La columna une todo con ella. Las espinas mayores son familias de causas, como máquina o "
                  "método. Las espinas menores llevan posibles causas específicas, y las espinas más chicas "
                  "van todavía más hondo. La regla de Nikhil era simple. Cada causa es sospechosa, hasta "
                  "que se compruebe. ¿Qué va en la cabeza?",
    },
    {
        "key": "p04", "num": 4, "title": "Un efecto preciso",
        "points": [("Qué, dónde, cuándo, cuánto", "Di qué está fallando"),
                   ("Una base y un denominador", "Agrega una base"),
                   ("Un modo de defecto a la vez", "Limítalo a un solo modo")],
        "example": "“Las fallas de enlace de puertos en la Línea 3 de switches subieron de 5 a 32 por cada "
                   "1,000 esta semana.”",
        "example_cue": "Nikhil escribió",
        "script": "Una cabeza vaga te da un pescado vago. La calidad está mal no ayuda a nadie. Di qué está "
                  "fallando, dónde, cuándo, y cuánto. Agrega una base, y un denominador claro. Limítalo a "
                  "un solo modo de defecto a la vez. Nikhil escribió una frase. Las fallas de enlace de "
                  "puertos en la línea tres de switches subieron de cinco a treinta y dos por cada mil esta "
                  "semana. ¿Ves qué tanto más precisa es?",
    },
    {
        "key": "p05", "num": 5, "title": "Las 6M: personas, máquina, método",
        "points": [("Personas: habilidad, carga, entrega de turno", "Personas cubre"),
                   ("Máquina: desgaste, ajustes, mantenimiento", "Máquina cubre"),
                   ("Método: secuencia, SOP, cambio de modelo", "Método cubre")],
        "example": "Usa las familias como guía, no como cajas rígidas.",
        "example_cue": "Úsalas como guía",
        "script": "La mayoría de los equipos usa seis familias, llamadas las seis M. Personas cubre "
                  "habilidad, entrenamiento, carga de trabajo y entregas de turno. Máquina cubre el "
                  "desgaste del fixture, los ajustes, el mantenimiento y el software. Método cubre la "
                  "secuencia, el SOP, los cambios de modelo y las revisiones de ajuste. Para cada familia, "
                  "hazle a tu equipo una pregunta. ¿Esto podría explicar nuestro efecto? Úsalas como guía, "
                  "no como cajas rígidas. Una causa puede tocar dos familias. ¿Y las otras tres M?",
    },
    {
        "key": "p06", "num": 6, "title": "Material, medición, medio ambiente",
        "points": [("Material: proveedor, lote, manejo", "Material cubre"),
                   ("Medición: calibradores, límites de prueba, rechazos falsos", "Medición cubre"),
                   ("Medio ambiente: ESD, humedad, polvo, calor", "Medio ambiente cubre")],
        "example": "La medición es la que los equipos olvidan. ¿El probador mismo dice la verdad?",
        "example_cue": "La medición es la que",
        "script": "Material cubre la variación del proveedor, el lote equivocado, y el daño por manejo. "
                  "Medición cubre calibradores, límites de prueba, calibración y rechazos falsos. Medio "
                  "ambiente cubre ESD, humedad, polvo, luz y calor. La medición es la que los equipos "
                  "olvidan más. ¿El probador mismo te dice la verdad? Ten presente esa pregunta. Un fixture "
                  "de prueba gastado puede rechazar unidades buenas todo el día. Antes de dibujar, ¿qué "
                  "debes reunir?",
    },
    {
        "key": "p07", "num": 7, "title": "Primero reúne evidencia",
        "points": [("Un Pareto de tipos de defecto", "un Pareto"),
                   ("Separa por turno, lote, estación, probador", "Separa los datos"),
                   ("Compara unidades buenas con malas", "Compara unidades buenas")],
        "example": "Las fallas se juntaban en dos de las cuatro estaciones de prueba.",
        "example_cue": "La primera separación de Nikhil",
        "script": "Lleva algunos datos a la sala. Empieza con un Pareto de tipos de defecto, para trabajar "
                  "en el más grande. Separa los datos por turno, lote, estación y probador. Compara "
                  "unidades buenas con malas, lado a lado. La primera separación de Nikhil fue una "
                  "sorpresa. La mayoría de las fallas venía de solo dos de las cuatro estaciones de prueba. "
                  "¿Qué sospecharías, solo con eso?",
    },
    {
        "key": "p08", "num": 8, "title": "Construirlo: ocho pasos",
        "points": [("Define el efecto, reúne al equipo", "Define el efecto"),
                   ("Dibuja las espinas, lluvia de ideas, sin culpa", "Dibuja la cabeza"),
                   ("Pregunta por qué, junta, prioriza", "Pregunta por qué podría"),
                   ("Asigna responsables para probar causas", "Asigna un responsable")],
        "example": "El equipo de Nikhil: producción, calidad, pruebas, mantenimiento y almacén.",
        "example_cue": "El equipo de Nikhil",
        "script": "Constrúyelo en ocho pasos. Define el efecto, y reúne a un equipo de varias áreas. Dibuja "
                  "la cabeza, la columna y las familias. Haz una lluvia de causas sin debate y sin culpa. "
                  "Pregunta por qué podría pasar esto, para ir más hondo. Junta los duplicados, y prioriza "
                  "con datos. Asigna un responsable para probar cada causa. El equipo de Nikhil mezcló "
                  "producción, calidad, pruebas, mantenimiento y almacén. ¿Por qué incluir al almacén?",
    },
    {
        "key": "p09", "num": 9, "title": "La espina de pescado de Nikhil",
        "points": [("Máquina: deriva en la altura del prensado", "Máquina tenía"),
                   ("Medición: cables de prueba gastados", "Medición tenía"),
                   ("Material, método, personas, medio ambiente", "Otras espinas")],
        "example": "Veintitrés posibles causas en cuarenta minutos.",
        "example_cue": "En cuarenta minutos",
        "script": "Porque los problemas de material muchas veces empiezan en el almacén. Esto es lo que "
                  "encontró el equipo. Máquina tenía una herramienta de prensado cuyo tope de altura podía "
                  "desviarse. Medición tenía cables de prueba de retorno, conectados miles de veces. Otras "
                  "espinas tenían un lote nuevo de puertos del proveedor, una revisión de acople faltante, "
                  "un equipo temporal y los registros ESD. En cuarenta minutos, tenían veintitrés posibles "
                  "causas. ¿Cuál pruebas primero?",
    },
    {
        "key": "p10", "num": 10, "title": "Espina de pescado, luego cinco porqués",
        "points": [("La espina de pescado va a lo ancho", "La espina de pescado va a lo ancho"),
                   ("Los cinco porqués van a lo hondo", "Los cinco porqués van a lo hondo"),
                   ("Nunca te detengas en error del operador", "nunca te detengas")],
        "example": "¿Por qué los cables gastados? No había límite de cambio. ¿Por qué? Los cables no estaban "
                   "en el plan de mantenimiento.",
        "example_cue": "Toma los cables de prueba",
        "script": "Usa dos herramientas juntas. La espina de pescado va a lo ancho, para encontrar "
                  "candidatas. Los cinco porqués van a lo hondo, por un camino elegido. Toma los cables de "
                  "prueba. ¿Por qué estaban gastados? Nadie los cambiaba. ¿Por qué? No estaban en ningún "
                  "plan de mantenimiento. Y nunca te detengas en error del operador. Pregunta qué hizo "
                  "posible el error. Pero una cadena convincente todavía no es prueba. ¿Cómo compruebas una "
                  "causa?",
    },
    {
        "key": "p11", "num": 11, "title": "Compruébalo: la escalera de evidencia",
        "points": [("Obsérvalo en el Gemba", "Observa la condición en el Gemba"),
                   ("Rastrea y mide", "Rastrea las fallas"),
                   ("Experimenta, luego repite", "Haz un experimento controlado")],
        "example": "Los votos no cuentan. Un solo ensayo bueno tampoco es prueba.",
        "example_cue": "Los votos no cuentan",
        "script": "Sube una escalera de evidencia. Observa la condición en el Gemba. Rastrea las fallas "
                  "hasta lotes, turnos, estaciones y equipos. Mide con instrumentos calibrados. Haz un "
                  "experimento controlado, cambiando un factor a la vez. Luego repítelo, para mostrar que "
                  "el efecto de verdad desaparece. Los votos no cuentan como evidencia. Y un solo ensayo "
                  "bueno tampoco es prueba. ¿Y qué comprobó Nikhil?",
    },
    {
        "key": "p12", "num": 12, "title": "Dos causas, las dos reales",
        "points": [("Cables gastados: fallas falsas", "Los cables nuevos eliminaron"),
                   ("Deriva en la altura del prensado: fallas reales", "el tope del prensado"),
                   ("Las causas pueden coexistir", "Dos causas")],
        "example": "Reprueba con cables nuevos: 6 de 10 switches 'con falla' pasaron. Los otros 4 tenían "
                   "puertos poco profundos.",
        "example_cue": "Volvió a probar",
        "script": "Volvió a probar diez switches con falla, con cables totalmente nuevos. Seis de ellos "
                  "pasaron. Los cables nuevos eliminaron de inmediato las fallas falsas. Los otros cuatro "
                  "sí fallaban. Sus puertos quedaban poco profundos, porque el tope del prensado se había "
                  "desviado. Dos causas, las dos reales, al mismo tiempo. Eso pasa más seguido de lo que "
                  "crees. Corregir solo una dejaría la mitad del problema. Un probador nuevo no habría "
                  "corregido ninguna. ¿Y qué acciones tomarías?",
    },
    {
        "key": "p13", "num": 13, "title": "Acciones correctivas fuertes",
        "points": [("Elimina por diseño antes de volver a entrenar", "Elimina la causa por diseño"),
                   ("Bloqueos, interbloqueos, contadores", "Usa bloqueos"),
                   ("Actualiza el SOP, el PFMEA, el plan de control", "actualiza el SOP")],
        "example": "Contador de inserciones del cable con un límite de cambio. Revisión y bloqueo de la "
                   "altura del prensado al inicio de cada turno.",
        "example_cue": "El equipo de Nikhil agregó",
        "script": "Elimina la causa por diseño, antes de depender de recordatorios o de volver a entrenar. "
                  "Usa bloqueos, interbloqueos, contadores y fixtures. Luego actualiza el SOP, el PFMEA, el "
                  "plan de control y el entrenamiento, todo junto. El equipo de Nikhil agregó un contador "
                  "de inserciones a cada cable de prueba, con un límite de cambio. Y la altura del prensado "
                  "se revisaba y se bloqueaba al inicio de cada turno. ¿Cómo sabrías que funcionó?",
    },
    {
        "key": "p14", "num": 14, "title": "Comprobar que funcionó",
        "points": [("Fija la meta antes de empezar", "Fija tu meta"),
                   ("Una ventana fija y un tamaño de muestra", "una ventana fija"),
                   ("32 → 4 por cada 1,000, sostenido 30 días", "Las fallas bajaron")],
        "example": "Cero fallas falsas por cables gastados, en 30 días de producción.",
        "example_cue": "Y ni una sola",
        "script": "Fija tu meta antes del cambio, no después de ver los resultados. Decide una ventana fija "
                  "y un tamaño de muestra. Nikhil eligió treinta días de producción. También retó al "
                  "contador con un cable gastado, para comprobar que bloqueaba su uso. Las fallas bajaron "
                  "de treinta y dos por cada mil a cuatro, y ahí se quedaron. Y ni una sola falla falsa "
                  "vino de un cable gastado. El presupuesto del probador regresó al cajón. ¿Qué errores "
                  "debes evitar?",
    },
    {
        "key": "p15", "num": 15, "title": "Errores y buenas prácticas",
        "points": [("Efectos vagos y defectos mezclados", "Un efecto vago"),
                   ("Faltan áreas en la sala", "Dejar fuera"),
                   ("Sin validación después de la sesión", "Detenerse después")],
        "example": "Deja las causas descartadas en la gráfica, con la evidencia que las descartó.",
        "example_cue": "Deja las causas descartadas",
        "script": "Cuidado con algunos errores. Un efecto vago, o varios defectos mezclados. Dejar fuera a "
                  "mantenimiento, pruebas o almacén. Escribir descuido del operador en lugar de mirar el "
                  "sistema. Detenerse después de la lluvia de ideas, sin pruebas y sin responsables. Deja "
                  "las causas descartadas en la gráfica, con la evidencia que las descartó. Tu próximo "
                  "equipo te lo agradecerá. ¿Qué error has visto?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Posibles causas", "icon": "search", "with": 1},
        {"label": "Familias de causas", "icon": "stack", "with": 1},
        {"label": "El problema", "sub": "En la cabeza", "icon": "warning", "tone": "bad", "with": 0}]},
    "p02": {"type": "versus", "items": [
        {"label": "Prueba", "sub": "No sale de la espina de pescado", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Posibles causas", "sub": "Lo que muestra", "icon": "search", "tone": "good", "with": 2}]},
    "p03": {"type": "icons", "items": [
        {"label": "Cabeza", "sub": "El efecto", "icon": "warning", "with": 0},
        {"label": "Espinas mayores", "sub": "Familias de causas", "icon": "stack", "with": 1},
        {"label": "Espinas menores", "sub": "Causas específicas", "icon": "search", "with": 2}]},
    "p04": {"type": "versus", "items": [
        {"label": "“La calidad está mal”", "sub": "Vago", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "5 → 32 por cada 1,000", "sub": "Línea 3, enlace de puertos, esta semana", "icon": "check", "tone": "good", "with": "example"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Personas", "icon": "person", "with": 0},
        {"label": "Máquina", "icon": "gear", "with": 1},
        {"label": "Método", "icon": "clipboard", "with": 2}]},
    "p06": {"type": "icons", "items": [
        {"label": "Material", "icon": "box", "with": 0},
        {"label": "Medición", "icon": "scale", "tone": "bad", "with": 1},
        {"label": "Medio ambiente", "icon": "wave", "with": 2}]},
    "p07": {"type": "bars", "label": "", "note": "Fallas de enlace de puertos por estación de prueba", "with": "example", "items": [
        {"label": "T1", "value": 14, "tone": "bad", "with": "example"},
        {"label": "T2", "value": 3, "with": "example"},
        {"label": "T3", "value": 12, "tone": "bad", "with": "example"},
        {"label": "T4", "value": 3, "with": "example"}]},
    "p08": {"type": "steps", "items": [
        {"label": "Definir, equipo", "with": 0}, {"label": "Dibujar, lluvia de ideas", "with": 1},
        {"label": "¿Por qué? Juntar, ordenar", "with": 2}, {"label": "Los responsables prueban", "with": 3}]},
    "p09": {"type": "icons", "items": [
        {"label": "Máquina", "sub": "Deriva en la altura del prensado", "icon": "gear", "with": 0},
        {"label": "Medición", "sub": "Cables de prueba gastados", "icon": "scale", "with": 1},
        {"label": "Material", "sub": "Lote nuevo de puertos", "icon": "box", "with": 2},
        {"label": "Método", "sub": "Sin revisión de acople", "icon": "clipboard", "with": 2},
        {"label": "Personas", "sub": "Equipo temporal", "icon": "person", "with": 2},
        {"label": "Medio ambiente", "sub": "Registros ESD", "icon": "wave", "with": 2}],
        "then": {"type": "stat", "value": 23, "icon": "search", "label": "posibles causas en 40 minutos",
                 "unit": "cada una sigue siendo una suposición", "with": "example"}},
    "p10": {"type": "steps", "items": [
        {"label": "Cables gastados", "with": "example"},
        {"label": "Nunca se cambiaron", "with": "example"},
        {"label": "No están en el plan de mantenimiento", "with": "example"}]},
    "p11": {"type": "ladder", "top": "LO MÁS FUERTE", "bottom": "LO MÁS DÉBIL", "items": [
        {"label": "Repetir", "icon": "check", "with": 2},
        {"label": "Experimentar", "icon": "test", "with": 2},
        {"label": "Rastrear y medir", "icon": "scale", "with": 1},
        {"label": "Observar", "icon": "search", "with": 0}]},
    "p12": {"type": "bars", "label": "", "note": "10 switches con falla reprobados con cables nuevos: 6 pasaron, 4 tenían puertos poco "
                                                 "profundos", "with": "example", "items": [
        {"label": "Fallas falsas", "value": 6, "with": "example"},
        {"label": "Fallas reales", "value": 4, "tone": "bad", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Contador de inserciones del cable", "icon": "count", "with": "example"},
        {"label": "Bloqueo de la altura del prensado", "icon": "lock", "with": "example"},
        {"label": "SOP, PFMEA, plan de control", "icon": "clipboard", "tone": "good", "with": 2}]},
    "p14": {"type": "compare", "before": {"label": "Antes", "value": 32}, "after": {"label": "Después", "value": 4},
            "unit": "fallas de enlace de puertos por cada 1,000 switches", "note": "Sostenido 30 días de producción", "with": 2},
    "p15": {"type": "icons", "items": [
        {"label": "Efecto vago", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Faltan áreas", "icon": "person", "tone": "bad", "with": 1},
        {"label": "Sin validación", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Conserva las causas descartadas", "icon": "clipboard", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "¿Cuál es el mejor efecto para la cabeza de una espina de pescado?",
        "options": ["“Problemas de calidad en la línea de switches”",
                    "“Las fallas de enlace de puertos en la Línea 3 subieron de 5 a 32 por cada 1,000 esta "
                    "semana”",
                    "“El probador está mal”"],
        "correct": 1,
        "explanation": "Una buena cabeza nombra un defecto, el lugar, el periodo y el tamaño, con una base. “El "
                       "probador está mal” ya es una causa.",
        "q_script": "Prueba rápida. ¿Cuál de estos es el mejor efecto para la cabeza de una espina de "
                    "pescado? Tómate unos segundos.",
        "a_script": "Es el segundo. Nombra un defecto, el lugar, el periodo y el tamaño. El último ya es una "
                    "causa.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Después de la lluvia de ideas, el equipo vota “descuido del operador” como la causa "
                    "principal. ¿Qué sigue?",
        "options": ["Volver a entrenar a los operadores: el equipo estuvo de acuerdo",
                    "Preguntar qué hizo posible el error, y probar las causas con evidencia",
                    "Poner un letrero de advertencia en la estación"],
        "correct": 1,
        "explanation": "Un voto no es evidencia, y el descuido no es una causa controlable. Pregunta qué "
                       "condición del proceso hizo posible el error, y luego compruébala.",
        "q_script": "Una más, y esta es un escenario. Después de la lluvia de ideas, el equipo vota descuido "
                    "del operador como la causa principal. ¿Qué debe pasar después? Piénsalo.",
        "a_script": "Pregunta qué hizo posible el error, y prueba cada causa con evidencia. Un voto no es "
                    "prueba, y el descuido no es una causa que puedas controlar.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
