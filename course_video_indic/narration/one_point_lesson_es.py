"""one_point_lesson in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh one_point_lesson_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "op_es"
NAME = "one_point_lesson_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "One Point Lesson": "uán póint léson",
    "Poka Yoke": "Poka Yoke",
    "Kaizen": "Káizen",
    "Gemba": "Guemba",
    "OPL": "o pe ele",
    "SOP": "ese o pe",
    "PCB": "pe ce be",
    "AOI": "a o i",
    "ESD": "e ese de",
    "TPM": "te pe eme",
    "5S": "cinco eses",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Turno de noche. Un operador nuevo coloca un conector al revés, y lo estrella. El turno "
    "de día conocía el truco. Nadie lo había compartido. ¿Te suena familiar? En esta lección "
    "aprenderás la One Point Lesson. Es una forma visual, de una sola hoja, de enseñar bien "
    "una sola cosa, justo en la estación de trabajo. Seguiremos a Ravi, supervisor de turno "
    "en una línea de grabadoras de video, mientras hace las primeras."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Un tema, un punto claro, y un buen apoyo visual. Enséñala "
    "en el Gemba, y confírmala observando el trabajo. Y contrólala, para que siempre coincida "
    "con el estándar vigente. Esta es tu acción para esta semana. Elige un error que se sigue "
    "repitiendo, y haz un borrador de una One Point Lesson para él. Excelente trabajo al "
    "completar esta lección. Ahora aprenderás Poka Yoke, a prueba de errores."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es una One Point Lesson",
        "points": [("Una cosa, en una hoja", "enseña una sola cosa en una"),
                   ("Corta: se aprende en minutos", "Es corta"),
                   ("Visual: ejemplos buenos y malos", "Es visual"),
                   ("Se enseña en el lugar de trabajo", "se enseña justo en el lugar de trabajo")],
        "example": "La primera OPL de Ravi, inserción del conector: el agarre correcto, el agarre "
                   "incorrecto, y el clic que hay que escuchar.",
        "example_cue": "La primera de Ravi",
        "script": "Esta es la idea central. Una One Point Lesson, u OPL, enseña una sola cosa en una sola "
                  "hoja. Es corta, así que la aprendes en unos minutos. Es visual, con fotos y ejemplos "
                  "claros de lo bueno y lo malo. Y se enseña justo en el lugar de trabajo. La primera de "
                  "Ravi trató la inserción del conector. Una foto del agarre correcto, una del agarre "
                  "incorrecto, y el clic que hay que escuchar. ¿Qué crees que nunca debe reemplazar?",
    },
    {
        "key": "p02", "num": 2, "title": "Lo que una OPL no es",
        "points": [("Nunca reemplaza tu SOP", "Una OPL nunca reemplaza tu SOP"),
                   ("Ningún tema grande metido en una hoja", "Tampoco mete"),
                   ("Refuerza un punto crítico", "refuerza un punto crítico")],
        "example": "La lección del conector de Ravi va junto al SOP y señala el paso exacto que apoya.",
        "example_cue": "La lección del conector de Ravi",
        "script": "Una OPL nunca reemplaza tu SOP. No es una instrucción de trabajo, ni una especificación "
                  "completa, ni una certificación. Tampoco mete un tema grande en una hoja saturada. En "
                  "cambio, refuerza un punto crítico, para que la gente lo recuerde. La lección del "
                  "conector de Ravi va justo junto al SOP. Señala el paso exacto que apoya. Así el estándar "
                  "sigue siendo el principal, y la OPL hace que se quede. ¿Por qué vale la pena el "
                  "esfuerzo?",
    },
    {
        "key": "p03", "num": 3, "title": "Por qué las OPL valen la pena",
        "points": [("Cierra brechas de habilidad entre turnos", "Las OPL cierran brechas de habilidad"),
                   ("La gente nueva aprende más rápido", "La gente nueva aprende más rápido"),
                   ("Las lecciones de los defectos se comparten rápido", "Las lecciones de los defectos"),
                   ("Los operadores hábiles se vuelven instructores", "tus operadores hábiles")],
        "example": "El turno de noche estrellaba 14 conectores por semana; el de día, 2. Mismo SOP, distinto "
                   "saber hacer.",
        "example_cue": "El turno de noche de Ravi estrellaba",
        "script": "Las OPL cierran brechas de habilidad entre personas y turnos. El turno de noche de Ravi "
                  "estrellaba catorce conectores por semana. El turno de día estrellaba dos. Mismo SOP, "
                  "pero distinto saber hacer. Una One Point Lesson reparte ese saber hacer en minutos. La "
                  "gente nueva aprende más rápido. Las lecciones de los defectos y las descomposturas se "
                  "comparten rápido. Y tus operadores hábiles se vuelven instructores, lo que crea un "
                  "verdadero sentido de dueño. La recompensa aparece en calidad, seguridad y costo. ¿Y qué "
                  "tipos puedes hacer?",
    },
    {
        "key": "p04", "num": 4, "title": "Tipos de OPL",
        "points": [("Conocimiento básico, p. ej. manejo ESD", "Una lección de conocimiento básico"),
                   ("Problema: defecto, causa y solución", "Una lección de problema"),
                   ("Mejora: un método mejor salido de un Kaizen", "Una lección de mejora"),
                   ("Seguridad · Calidad · Mantenimiento", "Luego están las de seguridad")],
        "example": "La lección del conector estrellado de Ravi es de tipo problema.",
        "example_cue": "La lección del conector estrellado de Ravi",
        "script": "Hay seis tipos comunes. Una lección de conocimiento básico enseña algo que todos deben "
                  "saber, como el manejo ESD. Una lección de problema explica un defecto, su causa y su "
                  "solución. Una lección de mejora comparte un método mejor salido de un Kaizen. Luego "
                  "están las de seguridad, calidad y mantenimiento. La lección del conector estrellado de "
                  "Ravi es de tipo problema. Los nombres pueden variar en tu planta. La regla no. Un punto "
                  "claro. ¿Y cuándo debes hacer una?",
    },
    {
        "key": "p05", "num": 5, "title": "Cuándo crear una",
        "points": [("Un defecto repetido recién resuelto", "Un defecto repetido se acaba"),
                   ("Producto, máquina o plantilla nuevos", "Un producto nuevo"),
                   ("Un paso que se sigue malentendiendo", "Un paso del SOP"),
                   ("Un casi accidente o el truco de alguien hábil", "Un casi accidente")],
        "example": "El disparador de Ravi: se encontró la causa de los conectores estrellados — ahora la "
                   "solución tenía que llegar a cada turno.",
        "example_cue": "Para Ravi, el disparador",
        "script": "Haz una cuando un pequeño conocimiento puede cambiar el comportamiento. Un defecto "
                  "repetido se acaba de resolver. Llega un producto nuevo, una máquina o una plantilla. Un "
                  "paso del SOP se sigue malentendiendo. Un casi accidente revela una brecha. O una persona "
                  "hábil conoce un truco que nadie más sabe. Para Ravi, el disparador era claro. Se "
                  "encontró la causa de los conectores estrellados. Ahora la solución tenía que llegar a "
                  "cada turno. ¿Qué va en la hoja?",
    },
    {
        "key": "p06", "num": 6, "title": "Estructura de una buena OPL",
        "points": [("Número, título, revisión, fecha", "Empieza con un número"),
                   ("Por qué importa + el único punto clave", "Luego di por qué importa"),
                   ("Imágenes, pasos, precaución", "Agrega las imágenes"),
                   ("Responsable, aprobación, registro de entrenamiento", "Termina con el responsable")],
        "example": "La hoja debe entenderse de un vistazo — ¿tu operador más nuevo podría leerla en un "
                   "minuto?",
        "example_cue": "La hoja debe entenderse",
        "script": "Cada OPL sigue el mismo formato, para que la gente sepa dónde mirar. Empieza con un "
                  "número, un título corto, la revisión y la fecha. Luego di por qué importa, y escribe el "
                  "único punto clave. Agrega las imágenes y los pasos simples. Incluye una precaución donde "
                  "haya un riesgo. Termina con el responsable, la aprobación y el registro de "
                  "entrenamiento. La hoja debe entenderse de un vistazo. ¿Tu operador más nuevo podría leer "
                  "la tuya en un minuto?",
    },
    {
        "key": "p07", "num": 7, "title": "Cómo prepararla",
        "points": [("Define un objetivo de aprendizaje", "definir un objetivo de aprendizaje"),
                   ("Ve al Gemba, verifica el estándar", "Luego ve al Gemba"),
                   ("Palabras simples, fotos reales, bueno contra malo", "Después, ponla"),
                   ("Revisa, luego aprueba", "Luego pide que Calidad")],
        "example": "Ravi fotografió el conector real, en la estación real.",
        "example_cue": "Ravi fotografió",
        "script": "Empieza por definir un objetivo de aprendizaje. Luego ve al Gemba, y observa el trabajo "
                  "real. Verifica el estándar aprobado y la causa raíz. Después, ponla en las palabras "
                  "simples que usan tus operadores. Agrega fotos reales, flechas y ejemplos buenos y malos. "
                  "Haz el borrador en la plantilla estándar. Luego pide que Calidad o Ingeniería la revise, "
                  "y la apruebe. Ravi fotografió el conector real, en la estación real. ¿Y cómo haces que "
                  "funcionen las imágenes?",
    },
    {
        "key": "p08", "num": 8, "title": "Comunicación visual",
        "points": [("Fotos reales, flechas en el punto exacto", "Usa fotos reales"),
                   ("Bueno y malo lado a lado", "Pon lo bueno y lo malo"),
                   ("Letra grande, mucho espacio", "Usa letra grande"),
                   ("Nunca uses el color como única señal", "nunca uses el color")],
        "example": "La OPL de Ravi muestra una paloma, una cruz, y las palabras bien y no está bien.",
        "example_cue": "Ravi agregó una paloma",
        "script": "Lo visual es el corazón de una OPL. Quien aprende debe captar el punto antes de leer una "
                  "sola frase. Usa fotos reales, con flechas y círculos en el punto exacto. Pon lo bueno y "
                  "lo malo lado a lado. Usa letra grande y mucho espacio. Evita párrafos largos y palabras "
                  "técnicas. Y nunca uses el color como única señal. Ravi agregó una paloma, una cruz, y "
                  "las palabras bien y no está bien. ¿Y cómo la enseñas de verdad?",
    },
    {
        "key": "p09", "num": 9, "title": "Enseñar en el Gemba",
        "points": [("Explica por qué importa", "Explica por qué importa"),
                   ("Muestra, demuestra, compara", "Muestra la pieza real"),
                   ("Haz preguntas, déjalos intentar", "Haz preguntas cortas"),
                   ("Una firma sola no prueba nada", "Una firma sola")],
        "example": "Ravi enseña cada lección en 5 minutos al inicio del turno, y luego observa a cada "
                   "operador hacerlo.",
        "example_cue": "Ravi enseña cada lección",
        "script": "Enséñala donde pasa el trabajo. Explica por qué importa, en términos de calidad o "
                  "seguridad. Muestra la pieza real. Demuéstralo despacio, y luego compara lo bueno y lo "
                  "malo. Haz preguntas cortas para revisar que se entendió. Deja que quien aprende lo "
                  "intente, y corrige los errores en el momento. Ravi enseña cada lección en cinco minutos "
                  "al inicio del turno. Luego observa a cada operador hacerlo. Una firma sola no prueba "
                  "nada. ¿Dónde más pueden ayudar las OPL?",
    },
    {
        "key": "p10", "num": 10, "title": "OPL para ensamble final y calidad",
        "points": [("Tarjetas: llamada falsa del AOI contra defecto real", "En tarjetas"),
                   ("Ensamble: secuencia de tornillos, seguro del conector", "En ensamble"),
                   ("Prueba: revisión de la versión de firmware", "En prueba"),
                   ("Empaque: revisión de etiqueta y accesorios", "En empaque")],
        "example": "Evitar el PCB equivocado: dónde leer el número de la tarjeta, cómo comparar el modelo, "
                   "qué hacer si no coincide.",
        "example_cue": "La siguiente lección de Ravi",
        "script": "Casi cada proceso tiene un buen tema de OPL. En tarjetas, enseña a distinguir una "
                  "llamada falsa del AOI de un defecto real. En ensamble, enseña la secuencia de tornillos "
                  "y el seguro del conector. En prueba, enseña la revisión de la versión de firmware. En "
                  "empaque, enseña la revisión de etiqueta y accesorios. La siguiente lección de Ravi fue "
                  "evitar el PCB equivocado. Dónde leer el número de la tarjeta, cómo comparar el modelo, y "
                  "qué hacer si no coincide. ¿Qué tema te ayudaría más?",
    },
    {
        "key": "p11", "num": 11, "title": "Las OPL y otras herramientas Lean",
        "points": [("Después de un Kaizen: el método nuevo", "Después de un Kaizen"),
                   ("Después de un Poka Yoke: qué significa su alarma", "Después de instalar un Poka Yoke"),
                   ("Estándares de 5S y cuidado de máquinas", "Enseña los estándares de 5S"),
                   ("Lecciones del análisis de causa raíz", "Comparte las lecciones")],
        "example": "Fixture nuevo → una OPL sobre cómo cargarlo, y qué significa la luz roja.",
        "example_cue": "El equipo de Ravi instaló",
        "script": "Las OPL ayudan a que otras herramientas Lean funcionen en el piso. Después de un Kaizen, "
                  "una OPL enseña el método nuevo. Después de instalar un Poka Yoke, explica cómo funciona "
                  "el dispositivo, y qué significa su alarma. Enseña los estándares de 5S, y el cuidado "
                  "básico de máquinas para el TPM. Comparte las lecciones del análisis de causa raíz. El "
                  "equipo de Ravi instaló un fixture nuevo. Su OPL enseñó cómo cargarlo, y qué significa la "
                  "luz roja. ¿Pero cómo mantienes correctas las OPL?",
    },
    {
        "key": "p12", "num": 12, "title": "Control y revisiones",
        "points": [("Número, responsable, aprobador", "Dale un número único"),
                   ("Ligada al SOP que apoya", "Lígala al SOP"),
                   ("Revisada cada vez que algo cambia", "Revísala cada vez"),
                   ("Copias viejas retiradas de la línea", "Y retira las copias viejas")],
        "example": "Cuando cambió el proveedor del conector, Ravi revisó la lección y retiró cada copia "
                   "vieja.",
        "example_cue": "Cuando cambió el proveedor del conector de Ravi",
        "script": "Una OPL es un documento controlado, aunque sea corta. Dale un número único, un "
                  "responsable y un aprobador. Lígala al SOP que apoya. Revísala cada vez que cambie el "
                  "producto, el proceso o el estándar. Y retira las copias viejas de la línea. Cuando "
                  "cambió el proveedor del conector de Ravi, él revisó la lección, y retiró cada copia "
                  "vieja. Esta es la regla de oro. Una OPL nunca debe contradecir tu estándar vigente. ¿Y "
                  "funcionó?",
    },
    {
        "key": "p13", "num": 13, "title": "Medir la efectividad",
        "points": [("El resultado es el cambio de comportamiento", "El cambio de comportamiento es"),
                   ("Revisa el conocimiento con preguntas", "Así que revisa el conocimiento"),
                   ("Observa el método días después", "Luego observa el método"),
                   ("Sigue el defecto objetivo", "Y sigue el defecto")],
        "example": "Turno de noche: de 14 conectores estrellados por semana → 1 por semana, seis semanas "
                   "después de la lección.",
        "example_cue": "El turno de noche de Ravi estrellaba",
        "script": "Esta es la prueba real. Completar el entrenamiento no es el resultado. El cambio de "
                  "comportamiento es el resultado. Así que revisa el conocimiento con unas preguntas. Luego "
                  "observa el método en el Gemba, días después. Y sigue el defecto que querías atacar. El "
                  "turno de noche de Ravi estrellaba catorce conectores por semana. Seis semanas después de "
                  "la lección, estrellaron uno. Si un problema sigue, no solo vuelvas a entrenar. Revisa "
                  "también el estándar y el proceso. ¿Qué errores debes evitar?",
    },
    {
        "key": "p14", "num": 14, "title": "Errores comunes",
        "points": [("Demasiado contenido → divídelo", "Demasiado contenido"),
                   ("Solo texto → agrega fotos reales", "Solo texto"),
                   ("Solo firma → demuestra y observa", "Solo firmas"),
                   ("Versión vieja en la pared → control de revisiones", "Una versión vieja")],
        "example": "El primer borrador de Ravi cubría cuatro temas. Lo dividió en cuatro lecciones.",
        "example_cue": "El primer borrador de Ravi",
        "script": "Cuidado con algunos errores clásicos. ¿Demasiado contenido en una hoja? Divídelo. ¿Solo "
                  "texto? Agrega fotos reales. ¿Solo firmas? Demuestra, pregunta y observa. ¿Una versión "
                  "vieja en la pared? Usa control de revisiones. ¿Nadie revisa si funcionó? Sigue el "
                  "defecto. Y nunca uses una OPL para culpar a alguien. El primer borrador de Ravi cubría "
                  "cuatro temas. Lo dividió en cuatro lecciones. ¿Listo para extender las tuyas?",
    },
    {
        "key": "p15", "num": 15, "title": "Ruta y lista del creador",
        "points": [("Planea la plantilla, la numeración, la aprobación", "Planea tu plantilla"),
                   ("Piloto en los defectos o riesgos más grandes", "Haz un piloto con unas lecciones"),
                   ("Entrena a los instructores, úsalas en el Gemba", "Entrena a los supervisores"),
                   ("Mide el efecto, arma una biblioteca", "Mide el efecto")],
        "example": "Antes de liberar, pregunta: ¿Es correcta? ¿El punto es obvio?",
        "example_cue": "Antes de liberar cualquier lección",
        "script": "Extiéndelo en fases simples. Planea tu plantilla, la numeración y el flujo de "
                  "aprobación. Haz un piloto con unas lecciones sobre tus defectos o riesgos de seguridad "
                  "más grandes. Entrena a los supervisores y a los operadores hábiles para enseñarlas. "
                  "Luego úsalas en las juntas de turno y en el Gemba. Mide el efecto, y arma una biblioteca "
                  "controlada. Antes de liberar cualquier lección, pregúntate. ¿Es correcta? ¿El punto es "
                  "obvio? Enseña bien un punto, y mantenlo vigente.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Una cosa", "icon": "check"}, {"label": "Minutos para aprender", "icon": "clock"},
        {"label": "Visual", "icon": "camera"}, {"label": "En el lugar de trabajo", "icon": "wrench"}]},
    "p02": {"type": "versus", "items": [
        {"label": "Reemplazar el SOP", "sub": "o meter un tema grande", "icon": "cross", "with": 0},
        {"label": "Junto al SOP", "sub": "Señala el paso exacto", "icon": "clipboard", "with": 2}]},
    "p03": {"type": "compare", "before": {"label": "Turno de noche", "value": 14}, "after": {"label": "Turno de día", "value": 2},
            "unit": "conectores estrellados por semana", "note": "Mismo SOP, distinto saber hacer", "with": "example"},
    "p04": {"type": "icons", "items": [
        {"label": "Conocimiento básico", "icon": "chip", "with": 0}, {"label": "Problema", "icon": "warning", "with": 1},
        {"label": "Mejora", "icon": "chartUp", "with": 2}, {"label": "Seguridad", "icon": "shield", "with": 3},
        {"label": "Calidad", "icon": "check", "with": 3}, {"label": "Mantenimiento", "icon": "wrench", "with": 3}]},
    "p05": {"type": "icons", "items": [
        {"label": "Defecto repetido resuelto", "icon": "check"}, {"label": "Producto o plantilla nuevos", "icon": "box"},
        {"label": "Paso malentendido", "icon": "search"}, {"label": "Casi accidente, o un truco", "icon": "warning"}]},
    "p06": {"type": "doc", "items": [
        {"label": "OPL-012 · Inserción del conector · Rev B", "icon": "label", "with": 0},
        {"label": "Punto clave: empuja hasta que haga clic", "icon": "key", "with": 1},
        {"label": "", "icon": "goodbad", "with": 2},
        {"label": "Precaución: nunca lo fuerces", "icon": "warning", "with": 2},
        {"label": "Responsable · aprobada · entrenados", "icon": "person", "with": 3}]},
    "p07": {"type": "flow", "items": [
        {"label": "Un objetivo de aprendizaje", "icon": "search"},
        {"label": "Ve al Gemba", "sub": "Verifica el estándar", "icon": "walk"},
        {"label": "Palabras simples, fotos reales", "icon": "camera"},
        {"label": "Revisa, luego aprueba", "icon": "check", "tone": "good"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Fotos reales, flechas", "icon": "camera", "with": 0},
        {"label": "Bueno y malo lado a lado", "icon": "shape", "with": 1},
        {"label": "Letra grande, espacio", "icon": "label", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Solo color", "sub": "No todos lo ven", "icon": "warning"},
            {"label": "Paloma, cruz + palabras", "sub": "Bien / no está bien", "icon": "check"}]}},
    "p09": {"type": "flow", "items": [
        {"label": "Explica por qué importa", "icon": "person"},
        {"label": "Muestra, demuestra, compara", "icon": "camera"},
        {"label": "Pregunta, luego déjalos intentar", "icon": "hand"},
        {"label": "Una firma no prueba nada", "icon": "cross", "tone": "bad"}]},
    "p10": {"type": "flow", "items": [
        {"label": "Tarjetas", "sub": "Llamada falsa del AOI contra defecto real", "icon": "chip"},
        {"label": "Ensamble", "sub": "Secuencia de tornillos, seguro del conector", "icon": "screw"},
        {"label": "Prueba", "sub": "Revisión de la versión de firmware", "icon": "test"},
        {"label": "Empaque", "sub": "Etiqueta y accesorios", "icon": "label"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Kaizen", "icon": "chartUp"}, {"label": "Poka Yoke", "icon": "key"},
        {"label": "5S + TPM", "icon": "tray"}, {"label": "Causa raíz", "icon": "search"}]},
    "p12": {"type": "flow", "items": [
        {"label": "Número, responsable, aprobador", "icon": "label"},
        {"label": "Ligada a su SOP", "icon": "clipboard"},
        {"label": "Revisada en cada cambio", "icon": "sequence"},
        {"label": "Copias viejas retiradas", "icon": "trash", "tone": "good"}]},
    "p13": {"type": "icons", "items": [
        {"label": "Cambio de comportamiento", "icon": "person", "with": 0},
        {"label": "Unas preguntas", "icon": "search", "with": 1},
        {"label": "Observar, días después", "icon": "clock", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Antes", "value": 14}, "after": {"label": "6 semanas después", "value": 1},
                 "unit": "conectores estrellados por semana, turno de noche", "note": "La lección cambió el comportamiento", "with": "example"}},
    "p14": {"type": "icons", "items": [
        {"label": "¿Demasiado?", "sub": "Divídelo", "icon": "stack"},
        {"label": "¿Solo texto?", "sub": "Agrega fotos reales", "icon": "camera"},
        {"label": "¿Solo firma?", "sub": "Observa el trabajo", "icon": "hand"},
        {"label": "¿Versión vieja?", "sub": "Control de revisiones", "icon": "sequence"}]},
    "p15": {"type": "steps", "items": [
        {"label": "Plantilla + numeración", "with": 0}, {"label": "Piloto en defectos grandes", "with": 1},
        {"label": "Entrenar a los instructores", "with": 2}, {"label": "Usarlas en el Gemba", "with": 2},
        {"label": "Medir el efecto", "with": 3}, {"label": "Armar una biblioteca", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un borrador de OPL cubre inserción del conector, torque de tornillos, revisión de "
                    "etiquetas y ESD en una hoja. ¿Cuál es el problema?",
        "options": ["Necesita más texto", "Tiene demasiados puntos — divídelo en varias OPL",
                    "Debería ir solo a color"],
        "correct": 1,
        "explanation": "Una OPL enseña UN punto. Cuatro temas en una hoja diluyen el mensaje — mejor haz cuatro "
                       "OPL enfocadas.",
        "q_script": "Prueba rápida. Un borrador de lección cubre inserción del conector, torque de tornillos, "
                    "revisión de etiquetas y ESD, todo en una hoja. ¿Cuál es el problema? Tómate unos "
                    "segundos.",
        "a_script": "Tiene demasiados puntos. Una One Point Lesson enseña una sola cosa. Divídela en cuatro "
                    "lecciones enfocadas.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Todos firmaron la OPL hace dos semanas, pero el mismo defecto regresó. ¿Qué debe hacer "
                    "PRIMERO el supervisor?",
        "options": ["Hacer que todos vuelvan a firmar", "Observar el trabajo y revisar el estándar, el método y la lección",
                    "Culpar a los operadores que firmaron", "Quitar la OPL de la línea"],
        "correct": 1,
        "explanation": "Las firmas no prueban el aprendizaje. Ve a observar: ¿se sigue el método, el estándar "
                       "está bien, la OPL es clara? Luego corrige la causa.",
        "q_script": "Una más, y esta es un escenario. Todos firmaron la lección hace dos semanas, pero el "
                    "mismo defecto regresó. ¿Qué debe hacer primero el supervisor? Piénsalo.",
        "a_script": "Ve a observar el trabajo. Revisa el método, el estándar y la lección misma. Una firma no "
                    "prueba el aprendizaje, así que encuentra la causa real.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
