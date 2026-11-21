"""low_cost_automation in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh low_cost_automation_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "lc_es"
NAME = "low_cost_automation_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Low Cost Automation": "lóu cost otoméishon",
    "Gemba": "Guemba",
    "Muda": "Muda",
    "Mura": "Mura",
    "Muri": "Muri",
    "ECRS": "e ce erre ese",
    "LCA": "ele ce a",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Cada rejilla de bocina en la línea de Gaurav se asentaba con un mazo de hule. "
    "Cuatrocientos golpes por hora, por operador. Muñecas adoloridas, y rejillas flojas que "
    "vibraban en la prueba. ¿Te suena familiar? En esta lección aprenderás Low Cost "
    "Automation. Verás cómo dispositivos simples y seguros pueden eliminar trabajo repetitivo "
    "y errores, sin comprar una línea completa de robots. Seguiremos a Gaurav, ingeniero de "
    "procesos en una línea de bocinas Bluetooth."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Primero simplifica, y nunca automatices el desperdicio. "
    "Elige la solución segura más simple que haga el trabajo, con la seguridad como primer "
    "filtro. Y comprueba el beneficio real, luego dale mantenimiento como a cualquier otra "
    "máquina. Esta es tu acción para esta semana. Busca un movimiento repetitivo en tu línea, "
    "y pregúntate si se puede eliminar antes de automatizarlo. Excelente trabajo al completar "
    "esta lección. Ahora aprenderás Muda, Mura y Muri."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es Low Cost Automation",
        "points": [("Dispositivos simples, confiables y económicos", "simples, confiables"),
                   ("Eliminar trabajo repetitivo y errores", "para eliminar trabajo repetitivo"),
                   ("Sin necesidad de automatizar todo", "sin saltar")],
        "example": "El objetivo de Gaurav: asentar la rejilla, a mano con un mazo de hule.",
        "example_cue": "El objetivo de Gaurav",
        "script": "Low Cost Automation, o LCA, significa usar dispositivos simples, confiables y "
                  "económicos. Los usas para eliminar trabajo repetitivo, evitar errores y mejorar la "
                  "seguridad. Y lo haces sin saltar directo a una línea totalmente automática. Piensa en "
                  "prensas de sujeción, guías, sensores y pequeños cilindros de aire. El objetivo de Gaurav "
                  "era asentar la rejilla, que todavía se hacía a mano con un mazo de hule. ¿Qué ideas "
                  "guían el LCA?",
    },
    {
        "key": "p02", "num": 2, "title": "La filosofía central",
        "points": [("Automatiza la necesidad, no la complejidad", "Automatiza la necesidad"),
                   ("Simplifica antes de automatizar", "Simplifica antes"),
                   ("Mantén a las personas en el ciclo", "Mantén a las personas"),
                   ("Mídelo, dale mantenimiento", "Y mide")],
        "example": "Cotizaron un robot sofisticado en ₹18 lakh. Gaurav preguntó: ¿qué necesita de verdad el "
                   "trabajo?",
        "example_cue": "Cotizaron un robot",
        "script": "Algunas ideas guían todo buen LCA. Automatiza la necesidad, no la complejidad. Empieza "
                  "por el problema, y la función que requieres. Simplifica antes de automatizar cualquier "
                  "cosa. Mantén a las personas en el ciclo, para que las anormalidades sigan visibles. Y "
                  "mide el beneficio, luego dale mantenimiento. Cotizaron un robot en un millón ochocientas "
                  "mil rupias. Gaurav hizo una pregunta. ¿Qué necesita de verdad este trabajo?",
    },
    {
        "key": "p03", "num": 3, "title": "Cuándo tiene sentido el LCA",
        "points": [("Movimientos frecuentes y repetitivos", "se repite en cada ciclo"),
                   ("Riesgo ergonómico o de seguridad", "lastima a las personas"),
                   ("Pasos olvidados o hechos al revés", "se olvidan pasos"),
                   ("Cuello de botella, pero sin justificar un robot", "un cuello de botella")],
        "example": "Asentar la rejilla: cada ciclo, tensión en la muñeca, y asentado disparejo. Cumple las "
                   "cuatro.",
        "example_cue": "Asentar la rejilla cumplía",
        "script": "El LCA tiene sentido cuando un movimiento se repite en cada ciclo, muchas veces por "
                  "turno. Cuando el trabajo lastima a las personas, o crea un riesgo de seguridad. Cuando "
                  "se olvidan pasos, se hacen al revés o en otro lugar. Y cuando hay un cuello de botella, "
                  "pero automatizar todo no vale el dinero. También sirve para productos con volumen "
                  "incierto. Asentar la rejilla cumplía con todo. ¿Pero qué nunca debe significar bajo "
                  "costo?",
    },
    {
        "key": "p04", "num": 4, "title": "Bajo costo, nunca baja seguridad",
        "points": [("La seguridad es el primer filtro del diseño", "La seguridad es el primer"),
                   ("Guardas, paros, evaluación de riesgos", "Guardas, paros de emergencia"),
                   ("Un sensor normal no es un dispositivo de seguridad", "un sensor común")],
        "example": "La regla de Gaurav: ningún dispositivo corre hasta que el equipo de seguridad firma la "
                   "evaluación de riesgos.",
        "example_cue": "La regla de Gaurav",
        "script": "Bajo costo nunca debe significar baja seguridad, ni mala ingeniería. La seguridad es el "
                  "primer filtro del diseño, antes que el costo o la velocidad. Guardas, paros de "
                  "emergencia, evaluación de riesgos y normas eléctricas siguen aplicando. Y recuerda, un "
                  "sensor común o un controlador no es automáticamente un dispositivo de seguridad. La "
                  "regla de Gaurav era simple. Ningún dispositivo corre hasta que el equipo de seguridad "
                  "firma la evaluación de riesgos. ¿Qué tipos de LCA existen?",
    },
    {
        "key": "p05", "num": 5, "title": "Niveles de LCA",
        "points": [("Mecánico: gravedad, resortes, guías", "Las ayudas mecánicas"),
                   ("Neumático: prensas, sujetadores, pinzas", "Las ayudas neumáticas"),
                   ("Sensores y controles simples", "Los sensores detectan"),
                   ("Elige el nivel más bajo que funcione", "Elige el nivel más bajo")],
        "example": "Manual → asistido → semiautomático → automático.",
        "example_cue": "Piensa en una escalera",
        "script": "Hay varios niveles. Las ayudas mecánicas usan gravedad, resortes, palancas y guías, sin "
                  "nada de energía. Las ayudas neumáticas usan pequeños cilindros de aire para sujetar o "
                  "presionar. Los sensores detectan presencia, posición o secuencia, y controles simples "
                  "corren los pasos. Piensa en una escalera, de manual a totalmente automático. Elige el "
                  "nivel más bajo que cumpla tu necesidad con seguridad. ¿Por dónde empiezas?",
    },
    {
        "key": "p06", "num": 6, "title": "El método LCA",
        "points": [("Observar y medir", "Observa el trabajo real"),
                   ("Simplificar, luego definir la función", "simplifícalo"),
                   ("Concepto, revisión de riesgos, prototipo", "haz un boceto del concepto"),
                   ("Validar, estandarizar, replicar", "valídalo")],
        "example": "La base de Gaurav: ciclo de 28 s, 18 rejillas flojas por cada 1,000 bocinas.",
        "example_cue": "La base de Gaurav",
        "script": "Sigue un método claro. Observa el trabajo real, y mide el tiempo, el movimiento, los "
                  "defectos y el riesgo. Luego simplifícalo, y define exactamente qué función debe cumplir "
                  "el dispositivo. Después, haz un boceto del concepto, revisa sus riesgos, y construye un "
                  "prototipo. Por último, valídalo, estandarízalo, y cópialo donde encaje. La base de "
                  "Gaurav era un ciclo de veintiocho segundos, y dieciocho rejillas flojas por cada mil. "
                  "¿Qué va primero?",
    },
    {
        "key": "p07", "num": 7, "title": "ECRS antes de automatizar",
        "points": [("Eliminar, combinar, reordenar, simplificar", "Eliminar, combinar"),
                   ("Solo entonces automatiza", "Solo entonces"),
                   ("El desperdicio automatizado sigue siendo desperdicio", "El desperdicio automatizado")],
        "example": "Gaurav eliminó un paso aparte de golpe de prueba: la nueva prensa confirmaría el "
                   "asentado por sí misma.",
        "example_cue": "Gaurav encontró",
        "script": "Primero simplifica, con ECRS. Eliminar, combinar, reordenar y simplificar. Solo entonces "
                  "automatiza lo que queda. ¿Por qué? Porque el desperdicio automatizado sigue siendo "
                  "desperdicio. Solo es más rápido, más caro, y más difícil de cambiar después. Gaurav "
                  "encontró un paso que eliminar antes que nada. Los operadores volvían a golpear cada "
                  "rejilla, solo para revisarla. Una prensa bien diseñada podía confirmar el asentado por "
                  "sí misma. ¿Qué vio en el Gemba?",
    },
    {
        "key": "p08", "num": 8, "title": "La oportunidad de Gaurav",
        "points": [("Movimiento repetido en cada ciclo", "el mismo movimiento"),
                   ("Fuerza dispareja, asentado disparejo", "fuerza dispareja"),
                   ("Tensión en la muñeca, cada turno", "tensión en la muñeca")],
        "example": "Rejillas flojas: 18 por cada 1,000 bocinas, todas encontradas en la prueba de vibración.",
        "example_cue": "Las rejillas flojas",
        "script": "En el Gemba, vio el mismo movimiento, en cada ciclo. Tomar el mazo, golpear alrededor de "
                  "la rejilla, revisarla, dejar el mazo. Cada operador usaba fuerza dispareja, así que el "
                  "asentado variaba. Algunas rejillas quedaban flojas, y vibraban en la prueba. Y los "
                  "operadores reportaban tensión en la muñeca a media jornada. Las rejillas flojas llegaban "
                  "a dieciocho por cada mil bocinas. ¿Qué tecnología elegirías?",
    },
    {
        "key": "p09", "num": 9, "title": "Elegir tecnología simple",
        "points": [("Ajusta la tecnología a la función", "Elige por función"),
                   ("Las menos piezas, piezas estándar", "Usa las menos piezas"),
                   ("Fácil de limpiar, ajustar y reparar", "Hazlo fácil")],
        "example": "La elección de Gaurav: un pequeño cilindro de aire, un nido de ubicación y un sensor de "
                   "presencia.",
        "example_cue": "Gaurav eligió",
        "script": "Elige por función, no porque algo se vea avanzado. Piensa en la precisión, el tiempo de "
                  "ciclo, el ambiente, y quién le dará mantenimiento. Usa las menos piezas, y piezas "
                  "estándar donde puedas. Hazlo fácil de limpiar, ajustar y reparar. Y que su estado se vea "
                  "de un vistazo. Gaurav eligió un pequeño cilindro de aire, un nido de ubicación y un "
                  "sensor de presencia. ¿Cómo lo haces seguro?",
    },
    {
        "key": "p10", "num": 10, "title": "Diseñarlo seguro",
        "points": [("Busca puntos de atrapamiento y energía acumulada", "Busca puntos de atrapamiento"),
                   ("Guardas y arranque a dos manos", "Agrega guardas"),
                   ("Paro seguro, rearranque seguro", "Después de un paro")],
        "example": "Un arranque a dos manos mantiene ambas manos fuera de la zona de la prensa. La presión "
                   "de aire se libera al parar.",
        "example_cue": "La prensa de Gaurav",
        "script": "Busca puntos de atrapamiento, aplastamiento, partes móviles, y presión de aire "
                  "acumulada. Agrega guardas, y una forma de arranque que mantenga las manos lejos del "
                  "peligro. Después de un paro o una pérdida de aire, el dispositivo debe volver a un "
                  "estado seguro, no arrancar solo. La prensa de Gaurav usa un arranque a dos manos, así "
                  "ambas manos quedan libres. La presión de aire se libera en cualquier paro. ¿Tus fixtures "
                  "actuales pasarían esa prueba?",
    },
    {
        "key": "p11", "num": 11, "title": "La prensa de Gaurav",
        "points": [("El nido ubica la bocina", "Un nido ubica"),
                   ("El sensor confirma que la rejilla está", "Un sensor confirma"),
                   ("Fuerza controlada, lámpara de OK o no OK", "fuerza controlada")],
        "example": "Sin rejilla, no hay prensado. Posición incorrecta, no hay prensado. Asentada: lámpara "
                   "verde.",
        "example_cue": "Sin rejilla",
        "script": "Esto es lo que construyó. Un nido ubica la bocina de la misma forma cada vez. Un sensor "
                  "confirma que la rejilla está presente y en posición. Luego el cilindro presiona con "
                  "fuerza controlada, y una lámpara muestra si está bien o no. Sin rejilla, no hay "
                  "prensado. Posición incorrecta, no hay prensado. Bien asentada, luz verde. El operador "
                  "carga y descarga, y la prensa hace el resto. ¿Qué tanto más rápido fue?",
    },
    {
        "key": "p12", "num": 12, "title": "Contar la ganancia real",
        "points": [("Tiempo de ciclo: de 28 s a 22 s", "El tiempo de ciclo bajó"),
                   ("Producción teórica: unas 35 más por hora", "unas treinta y cinco"),
                   ("Incluye paros y recuperación", "Incluye la carga")],
        "example": "Revisión en la realidad: dos atoramientos cortos por turno, de un minuto cada uno. La "
                   "ganancia se mantuvo.",
        "example_cue": "Gaurav midió",
        "script": "El tiempo de ciclo bajó de veintiocho segundos a veintidós. En teoría, son unas treinta "
                  "y cinco bocinas más por hora. Pero no confíes solo en la teoría. Una estación rápida que "
                  "se para seguido puede frenar toda la línea. Incluye la carga, la descarga, los paros "
                  "menores, los atoramientos y la recuperación de fallas. Gaurav midió la producción real "
                  "durante dos semanas. Hubo dos atoramientos cortos por turno, de un minuto cada uno. La "
                  "ganancia se mantuvo. ¿Pero valió el dinero?",
    },
    {
        "key": "p13", "num": 13, "title": "Costo y recuperación",
        "points": [("Costo total de propiedad", "Cuenta el costo total"),
                   ("Beneficio neto, validado", "Cuenta solo los beneficios"),
                   ("Recuperación = inversión ÷ beneficio mensual", "La recuperación es")],
        "example": "₹1.2 lakh invertidos ÷ ₹30,000 de beneficio neto al mes = recuperación en 4 meses.",
        "example_cue": "La prensa de Gaurav costó",
        "script": "Cuenta el costo total de propiedad. Eso es diseño, piezas, instalación, entrenamiento, "
                  "aire, refacciones y mantenimiento. Cuenta solo los beneficios que puedas validar, como "
                  "menos retrabajo y tiempo de mano de obra liberado. La recuperación es la inversión, "
                  "dividida entre el beneficio neto mensual. La prensa de Gaurav costó ciento veinte mil "
                  "rupias. Ahorraba treinta mil al mes. Es una recuperación en cuatro meses. ¿Cómo la "
                  "mantienes funcionando?",
    },
    {
        "key": "p14", "num": 14, "title": "Validar y mantener",
        "points": [("Prueba en todos los modelos y turnos", "Pruébalo"),
                   ("Mantenimiento preventivo y refacciones", "Dale un plan de mantenimiento"),
                   ("Códigos de falla y recuperación claros", "Escribe códigos de falla claros")],
        "example": "Rejillas flojas: de 18 a 2 por cada 1,000. Quejas de muñeca: ninguna en 60 días.",
        "example_cue": "Las rejillas flojas bajaron",
        "script": "Pruébalo en varios modelos y turnos, antes de darlo por terminado. Revisa la seguridad, "
                  "la calidad, la velocidad, la confiabilidad y qué tan fácil se recuperan los operadores "
                  "de una falla. Dale un plan de mantenimiento, refacciones críticas, y revisiones de "
                  "sensores. Escribe códigos de falla claros, para que los técnicos lo reparen rápido. Las "
                  "rejillas flojas bajaron de dieciocho a dos por cada mil. Y no hubo quejas de muñeca en "
                  "sesenta días. ¿Qué errores debes evitar?",
    },
    {
        "key": "p15", "num": 15, "title": "Errores y tu siguiente paso",
        "points": [("Automatizar un proceso que no entiendes", "Automatizar un proceso"),
                   ("Elegir primero la tecnología", "Elegir la tecnología"),
                   ("Olvidar el mantenimiento y las refacciones", "Olvidar")],
        "example": "La prensa de Gaurav ahora corre en tres líneas, copiada después de revisar que encaja en "
                   "cada una.",
        "example_cue": "La prensa de Gaurav ahora",
        "script": "Cuidado con los errores comunes. Automatizar un proceso que no entiendes. Elegir la "
                  "tecnología antes de definir el problema. Olvidar el mantenimiento, las refacciones y la "
                  "recuperación de fallas. Reclamar ahorros teóricos que nunca validaste. E ignorar lo que "
                  "te dicen los operadores. Y no actualizar los estándares después. La prensa de Gaurav "
                  "ahora corre en tres líneas, copiada solo después de revisar que encaja en cada una. ¿Qué "
                  "trabajo repetitivo vas a revisar primero?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Dispositivos simples", "icon": "gear", "with": 0},
        {"label": "Menos repetición, menos errores", "icon": "check", "with": 1},
        {"label": "Sin línea completa de robots", "icon": "scale", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 400, "icon": "hand", "label": "golpes de mazo por hora",
                 "unit": "por operador", "with": "example"}},
    "p02": {"type": "icons", "items": [
        {"label": "Necesidad, no complejidad", "icon": "key", "with": 0},
        {"label": "Primero simplificar", "icon": "shape", "with": 1},
        {"label": "Personas en el ciclo", "icon": "person", "with": 2},
        {"label": "Medir, mantener", "icon": "wrench", "tone": "good", "with": 3}]},
    "p03": {"type": "icons", "items": [
        {"label": "Repetitivo", "icon": "sequence", "with": 0},
        {"label": "Riesgo ergonómico", "icon": "warning", "with": 1},
        {"label": "Pasos olvidados", "icon": "cross", "with": 2},
        {"label": "Cuello de botella", "icon": "clock", "with": 3}]},
    "p04": {"type": "flow", "items": [
        {"label": "Primero el filtro de seguridad", "icon": "shield", "tone": "good", "with": 0},
        {"label": "Guardas, paros de emergencia, revisión de riesgos", "icon": "lock", "with": 1},
        {"label": "Firmado antes de correr", "icon": "clipboard", "with": "example"}]},
    "p05": {"type": "ladder", "top": "AUTOMÁTICO", "bottom": "MANUAL", "items": [
        {"label": "Sensores y controles simples", "icon": "sensor", "with": 2},
        {"label": "Ayuda neumática", "icon": "gear", "with": 1},
        {"label": "Ayuda mecánica", "icon": "shape", "with": 0},
        {"label": "Manual", "icon": "hand", "with": 3}]},
    "p06": {"type": "steps", "items": [
        {"label": "Observar, medir", "with": 0}, {"label": "Simplificar, definir", "with": 1},
        {"label": "Concepto, riesgo, prototipo", "with": 2}, {"label": "Validar, estandarizar, copiar", "with": 3}]},
    "p07": {"type": "steps", "items": [
        {"label": "Eliminar", "with": 0}, {"label": "Combinar", "with": 0},
        {"label": "Reordenar", "with": 0}, {"label": "Simplificar", "with": 0},
        {"label": "Luego automatizar", "with": 1}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Volver a golpear cada rejilla", "sub": "Eliminado", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "La prensa confirma el asentado", "sub": "Integrado", "icon": "check", "tone": "good", "with": "example"}]}},
    "p08": {"type": "flow", "items": [
        {"label": "El mismo movimiento cada ciclo", "icon": "hand", "tone": "bad", "with": 0},
        {"label": "Fuerza dispareja", "icon": "scale", "tone": "bad", "with": 1},
        {"label": "Tensión en la muñeca", "icon": "warning", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 18, "icon": "wave", "label": "rejillas flojas por cada 1,000",
                 "unit": "encontradas en la prueba de vibración", "with": "example"}},
    "p09": {"type": "icons", "items": [
        {"label": "Cilindro de aire", "icon": "gear", "with": "example"},
        {"label": "Nido de ubicación", "icon": "shape", "with": "example"},
        {"label": "Sensor de presencia", "icon": "sensor", "with": "example"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Puntos de atrapamiento", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Arranque a dos manos", "icon": "hand", "with": 1},
        {"label": "Aire liberado al parar", "icon": "lock", "tone": "good", "with": 2}]},
    "p11": {"type": "flow", "items": [
        {"label": "El nido ubica", "icon": "shape", "with": 0},
        {"label": "El sensor confirma", "icon": "sensor", "with": 1},
        {"label": "Prensado controlado", "icon": "gear", "with": 2},
        {"label": "Verde: asentada", "icon": "check", "tone": "good", "with": "example"}]},
    "p12": {"type": "compare", "before": {"label": "Mazo", "value": 28}, "after": {"label": "Prensa", "value": 22},
            "suffix": " s", "unit": "tiempo de ciclo por bocina", "note": "Unas 35 más por hora, en teoría", "with": 0},
    "p13": {"type": "bars", "label": "", "note": "Ahorro acumulado, miles de ₹: recuperado en el mes 4", "with": "example", "items": [
        {"label": "Mes 1", "value": 30, "with": "example"},
        {"label": "Mes 2", "value": 60, "with": "example"},
        {"label": "Mes 3", "value": 90, "with": "example"},
        {"label": "Mes 4", "value": 120, "tone": "good", "with": "example"}]},
    "p14": {"type": "compare", "before": {"label": "Mazo", "value": 18}, "after": {"label": "Prensa", "value": 2},
            "unit": "rejillas flojas por cada 1,000 bocinas", "note": "Sin quejas de muñeca en 60 días", "with": "example"},
    "p15": {"type": "icons", "items": [
        {"label": "Automatizar lo desconocido", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Primero la tecnología", "icon": "gear", "tone": "bad", "with": 1},
        {"label": "Sin refacciones, sin PM", "icon": "wrench", "tone": "bad", "with": 2},
        {"label": "Copiada a 3 líneas", "icon": "check", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Antes de agregar automatización a un paso manual, ¿qué debes hacer primero?",
        "options": ["Comprar la máquina más rápida que haya",
                    "Simplificarlo con ECRS, y eliminar el desperdicio",
                    "Pedirles a los operadores que trabajen más rápido"],
        "correct": 1,
        "explanation": "Primero simplifica: eliminar, combinar, reordenar y simplificar. El desperdicio "
                       "automatizado sigue siendo desperdicio, solo más rápido y más difícil de cambiar.",
        "q_script": "Prueba rápida. Antes de automatizar un paso manual, ¿qué debes hacer primero? Tómate "
                    "unos segundos.",
        "a_script": "Simplificarlo con ECRS, y eliminar el desperdicio. El desperdicio automatizado sigue "
                    "siendo desperdicio, solo más rápido y más difícil de cambiar.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Una estación LCA nueva ahorra 6 segundos en papel, pero se atora diez veces por turno. "
                    "¿Qué debe hacer el equipo?",
        "options": ["Extenderla: el tiempo de ciclo es mejor",
                    "Medir la producción real con los paros, y corregir primero la confiabilidad",
                    "Quitar el sensor para que se atore menos"],
        "correct": 1,
        "explanation": "El tiempo de ciclo teórico no es capacidad real. Incluye los atoramientos y la "
                       "recuperación, corrige la confiabilidad, y solo entonces extiéndela. Quitar un sensor "
                       "debilitaría el control de calidad.",
        "q_script": "Una más, y esta es un escenario. Una estación nueva ahorra seis segundos en papel. Pero "
                    "se atora diez veces por turno. ¿Qué debe hacer el equipo? Piénsalo.",
        "a_script": "Mide la producción real, incluyendo los paros, y corrige primero la confiabilidad. La "
                    "teoría no es capacidad, y quitar el sensor solo debilitaría la calidad.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
