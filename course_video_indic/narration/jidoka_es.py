"""jidoka in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh jidoka_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "jd_es"
NAME = "jidoka_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Sakichi Toyoda": "Sakichi Toyoda",
    "Poka Yoke": "Poka Yoke",
    "Jidoka": "Yidoka",
    "Kaizen": "Káizen",
    "Andon": "Andon",
    "PFMEA": "pe efe eme e a",
    "SOP": "ese o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "El dosificador trabajó perfecto toda la noche. Excepto que su boquilla estaba medio "
    "tapada. Para la mañana, ciento cuarenta monitores de pacientes tenían un sello delgado. "
    "¿Te suena familiar? En esta lección aprenderás Jidoka, la automatización con toque "
    "humano. Verás cómo hacer que un proceso detecte un problema, se detenga solo, y pida "
    "ayuda, antes de que se acumulen los defectos. Seguiremos a Anjali, ingeniera de procesos "
    "en una línea de monitores de pacientes."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Define primero lo normal, para que el proceso sepa cómo se "
    "ve lo anormal. Detecta, detén y contén en el origen, y nunca pases un defecto. Y trata "
    "cada paro como una lección, corrigiendo la causa raíz para que no se repita. Esta es tu "
    "acción para esta semana. Elige un proceso automático, y anota qué debería hacer que se "
    "detenga. Excelente trabajo al completar esta lección. Ahora aprenderás Kaizen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es Jidoka",
        "points": [("Detectar una anormalidad", "detecta una condición anormal"),
                   ("Detener o contener", "detiene o contiene"),
                   ("Corregir, luego prevenir", "Luego las personas corrigen")],
        "example": "El dosificador de Anjali sella el bisel frontal de cada monitor de pacientes.",
        "example_cue": "El reto de Anjali",
        "script": "A Jidoka muchos lo llaman automatización con toque humano. Significa un proceso que "
                  "detecta una condición anormal por sí mismo. Detiene o contiene el trabajo, para que "
                  "ningún defecto avance. Luego las personas corrigen, y evitan que vuelva a pasar. El reto "
                  "de Anjali era un dosificador de adhesivo. Sella el bisel frontal de cada monitor de "
                  "pacientes. ¿Y qué cambia cuando agregas Jidoka?",
    },
    {
        "key": "p02", "num": 2, "title": "Sin Jidoka y con él",
        "points": [("Los defectos viajan contra atrapados en el origen", "Sin Jidoka, un defecto"),
                   ("Dudas contra reglas de paro claras", "la gente duda"),
                   ("Inspección contra calidad integrada", "la calidad depende")],
        "example": "Sin él: 140 sellos delgados, encontrados en la prueba de fugas a la mañana siguiente.",
        "example_cue": "Sin él",
        "script": "Sin Jidoka, un defecto puede viajar por muchas estaciones antes de que alguien lo vea. "
                  "La gente duda en parar, porque nadie le dijo que podía. Separar piezas se vuelve rutina, "
                  "y la calidad depende de la inspección final. Con Jidoka, se atrapa cerca del origen. Las "
                  "reglas de paro son claras, y la calidad está integrada en el proceso. Sin él, Anjali "
                  "encontró ciento cuarenta sellos delgados a la mañana siguiente. ¿Dónde empezó esta idea?",
    },
    {
        "key": "p03", "num": 3, "title": "De dónde vino",
        "points": [("El telar automático de Sakichi Toyoda", "Viene del telar de Sakichi Toyoda"),
                   ("Se detenía cuando se rompía un hilo", "se detenía solo"),
                   ("Uno de los dos pilares del TPS", "dos pilares")],
        "example": "Just-in-Time mueve bien el material. Jidoka asegura que no mueva bien los defectos.",
        "example_cue": "Esta es la conexión",
        "script": "Viene del telar de Sakichi Toyoda. La parte ingeniosa no era la velocidad. El telar se "
                  "detenía solo cada vez que se rompía un hilo, en lugar de tejer tela mala. Esa idea se "
                  "volvió uno de los dos pilares del Sistema de Producción Toyota. Esta es la conexión. "
                  "Justo a tiempo mueve el material con eficiencia. Jidoka asegura que no muevas defectos "
                  "con eficiencia. ¿Eso significa menos personas?",
    },
    {
        "key": "p04", "num": 4, "title": "Las personas siguen importando",
        "points": [("Las máquinas vigilan, las personas piensan", "Las máquinas vigilan"),
                   ("Una persona puede atender varias máquinas", "una persona puede"),
                   ("Criterio, reparación, mejora", "en criterio")],
        "example": "La operadora de Anjali miraba el cordón todo el turno. Ahora atiende dos estaciones.",
        "example_cue": "La operadora de Anjali",
        "script": "No. Jidoka no quita personas. Las máquinas vigilan, y las personas piensan. Como la "
                  "máquina avisa cuando necesita ayuda, una persona puede atender varias máquinas. Su "
                  "tiempo se va en criterio, reparación, estándares y mejora. La operadora de Anjali miraba "
                  "el cordón de adhesivo todo el turno. Ahora atiende dos estaciones, y resuelve problemas. "
                  "¿Cómo funciona el ciclo?",
    },
    {
        "key": "p05", "num": 5, "title": "Paso 1: detectar",
        "points": [("Primero define lo normal", "definir lo normal"),
                   ("Luego detecta la desviación", "detectas cuando"),
                   ("Sensores, revisiones, pruebas, monitores", "Sensores, visión")],
        "example": "Cordón normal: de 2.0 a 2.4 mm de ancho, sin huecos.",
        "example_cue": "Para Anjali",
        "script": "El ciclo tiene cuatro pasos. Detectar, detener, corregir y prevenir. La detección "
                  "necesita algo primero. Debes definir lo normal. No puedes detectar lo anormal hasta "
                  "saber cómo se ve lo bueno. Luego detectas cuando el proceso se aleja de eso. Sensores, "
                  "visión, pruebas, monitores de torque y revisiones del operador pueden hacerlo. Para "
                  "Anjali, lo normal era un cordón de dos a dos punto cuatro milímetros de ancho, sin "
                  "huecos. ¿Qué sigue?",
    },
    {
        "key": "p06", "num": 6, "title": "Pasos 2 a 4: detener, corregir, prevenir",
        "points": [("Detén o contén según el riesgo", "Detén o contén"),
                   ("Corregir: restablecer el estándar", "Corregir significa"),
                   ("Prevenir: eliminar la causa raíz", "Prevenir significa")],
        "example": "Corregir no es lo mismo que prevenir. Una boquilla limpia se puede volver a tapar.",
        "example_cue": "Recuerda esto",
        "script": "Detén o contén, de una forma que corresponda al riesgo. Puede ser un paro de máquina, un "
                  "bloqueo de estación, una unidad retenida, o una transacción bloqueada. Corregir "
                  "significa restablecer el estándar aprobado, y encontrar el producto afectado. Prevenir "
                  "significa eliminar la causa raíz, y actualizar el estándar. Recuerda esto. Corregir no "
                  "es prevenir. Una boquilla limpia se puede volver a tapar mañana. ¿Y en qué se diferencia "
                  "de la automatización?",
    },
    {
        "key": "p07", "num": 7, "title": "Jidoka contra automatización simple",
        "points": [("La automatización hace el trabajo", "La automatización simple"),
                   ("Jidoka además juzga el trabajo", "Jidoka agrega"),
                   ("Máquinas rápidas hacen defectos rápidos", "una máquina rápida")],
        "example": "El dosificador de Anjali: totalmente automático, pero ciego. Siguió dosificando toda la "
                   "noche.",
        "example_cue": "El dosificador de Anjali",
        "script": "La automatización simple hace el trabajo. Jidoka agrega criterio sobre el trabajo. Una "
                  "máquina normal sigue corriendo, a menos que algo se atore físicamente. Una máquina con "
                  "Jidoka se detiene cuando ve una anormalidad definida, y llama a una persona. Y aquí está "
                  "el peligro. Una máquina rápida hace defectos rápido. El dosificador de Anjali era "
                  "totalmente automático, pero ciego. Dosificó cordones delgados toda la noche. ¿Qué "
                  "principios deben guiarte?",
    },
    {
        "key": "p08", "num": 8, "title": "Principios clave",
        "points": [("Ningún defecto avanza", "Ningún defecto avanza"),
                   ("Ninguna anormalidad escondida", "Ninguna anormalidad escondida"),
                   ("Ninguna repetición aceptada sin acción", "Ningún problema repetido")],
        "example": "Tres preguntas: ¿qué es lo normal? ¿Cómo detectamos una desviación? ¿Qué pasa después?",
        "example_cue": "Haz tres preguntas",
        "script": "Recuerda tres reglas cortas. Ningún defecto avanza. Ninguna anormalidad escondida. "
                  "Ningún problema repetido se acepta sin acción. Usa juntos la detección de la máquina y "
                  "el criterio humano. Y nunca solo reinicies sin aprender algo. Cada paro debe dejar el "
                  "proceso un poco más fuerte. Haz tres preguntas sobre cualquier proceso. ¿Qué es lo "
                  "normal? ¿Cómo detectaremos una desviación? ¿Y qué pasa exactamente después de "
                  "detectarla? ¿Puedes responderlas para tu línea?",
    },
    {
        "key": "p09", "num": 9, "title": "Andon",
        "points": [("Verde: normal", "Verde significa"),
                   ("Amarillo: se necesita ayuda", "Amarillo significa"),
                   ("Rojo: detener, contener, escalar", "Rojo significa")],
        "example": "La regla de Anjali: el líder de equipo responde un amarillo en menos de dos minutos.",
        "example_cue": "En la línea de Anjali",
        "script": "El Andon hace visibles los problemas, con luces, sonidos o pantallas. Verde significa "
                  "normal, así que sigue trabajando al estándar. Amarillo significa que se necesita ayuda, "
                  "y un líder llega rápido. Rojo significa una anormalidad crítica. Detente de forma "
                  "segura, contén, y escala. Luego encuentra la última unidad buena conocida. En la línea "
                  "de Anjali, el líder de equipo responde cualquier amarillo en menos de dos minutos. ¿Qué "
                  "tan rápido llega la ayuda a tu línea?",
    },
    {
        "key": "p10", "num": 10, "title": "Una cultura de Andon",
        "points": [("Una llamada es información útil", "Una llamada real de Andon"),
                   ("Nunca castigues un paro", "Nunca castigues"),
                   ("Las llamadas pueden subir al principio", "las llamadas suelen subir")],
        "example": "Las llamadas de Andon se duplicaron el primer mes, y bajaron a la mitad para el tercero.",
        "example_cue": "En la línea de Anjali",
        "script": "El Andon solo funciona si la gente confía en él. Una llamada real de Andon es "
                  "información útil, no una molestia. Nunca castigues un paro, o la gente esconderá los "
                  "problemas para proteger la producción. Y espera una sorpresa. Cuando los problemas se "
                  "vuelven visibles, las llamadas suelen subir al principio. En la línea de Anjali, las "
                  "llamadas de Andon se duplicaron el primer mes. Para el tercer mes, habían bajado a la "
                  "mitad, porque se corregían las causas. ¿Tu equipo llamaría?",
    },
    {
        "key": "p11", "num": 11, "title": "Primero los controles más fuertes",
        "points": [("Eliminar, o prevenir por diseño", "Primero, elimina"),
                   ("Detectar y detener de inmediato", "Después, detecta"),
                   ("Advertencias e inspección al final", "Las advertencias van")],
        "example": "Un buen Poka Yoke: simple, cerca del origen, difícil de brincar, fácil de poner a "
                   "prueba.",
        "example_cue": "Un buen Poka Yoke",
        "script": "Usa el control más fuerte que puedas. Primero, elimina la posibilidad de error, o "
                  "prevénla por diseño. Después, detecta el error y detente de inmediato. Las advertencias "
                  "van después de eso, y la inspección posterior solo como defensa extra. Un buen Poka Yoke "
                  "es simple, está cerca del origen, y es difícil de brincar. Y es fácil de poner a prueba "
                  "en cada turno. ¿Y qué construyó Anjali?",
    },
    {
        "key": "p12", "num": 12, "title": "La estación Jidoka de Anjali",
        "points": [("Un sensor mide cada cordón", "mide cada cordón"),
                   ("Fuera de límites: el dosificador se detiene", "el dosificador se detiene"),
                   ("Andon, y retención hasta la última unidad buena", "El Andon llama")],
        "example": "Primer paro real: un monitor afectado, no 140.",
        "example_cue": "Su primer paro real",
        "script": "Agregó un sensor de visión que mide cada cordón, justo después de dosificar. Si el ancho "
                  "sale de los límites, el dosificador se detiene, y la unidad se retiene. El Andon llama "
                  "al líder de equipo. Todo lo hecho desde la última unidad buena se revisa. Su primer paro "
                  "real llegó dos semanas después. Hubo un monitor afectado, no ciento cuarenta. ¿Pero por "
                  "qué se tapó la boquilla?",
    },
    {
        "key": "p13", "num": 13, "title": "Causa raíz después del paro",
        "points": [("Detener revela; analizar mejora", "Detener revela"),
                   ("Pregunta por qué, con evidencia", "Por qué se tapó la boquilla"),
                   ("Corrígelo, luego estandariza", "Así que agregó")],
        "example": "El adhesivo se curaba en la boquilla durante los descansos. No había paso de purga en el "
                   "estándar.",
        "example_cue": "El adhesivo se curaba",
        "script": "Detener revela un problema. El análisis de causa raíz lo convierte en una mejora. ¿Por "
                  "qué se tapó la boquilla? El adhesivo se curaba dentro de ella durante los descansos. "
                  "¿Por qué? No había un paso de purga después de una pausa. ¿Por qué? El estándar nunca "
                  "cubrió los descansos. Así que agregó una purga automática después de cualquier pausa, y "
                  "un monitor de presión. También se actualizaron el PFMEA y el SOP. ¿Cómo medirías el "
                  "éxito?",
    },
    {
        "key": "p14", "num": 14, "title": "Medir lo correcto",
        "points": [("Rendimiento a la primera y fugas al cliente", "Vigila el rendimiento a la primera"),
                   ("Tiempo de respuesta del Andon", "Tiempo de respuesta del Andon"),
                   ("Anormalidades repetidas", "anormalidades repetidas")],
        "example": "Rendimiento a la primera: 97.5% → 99.0%. Fugas: cero en 90 días.",
        "example_cue": "Los resultados de Anjali",
        "script": "Mide la respuesta y la repetición, no solo el número de paros. Vigila el rendimiento a "
                  "la primera, y las fugas al cliente. Sigue el tiempo de respuesta del Andon, desde la "
                  "llamada hasta que llega la ayuda. Y vigila las anormalidades repetidas. Deben bajar con "
                  "el tiempo. Los resultados de Anjali fueron claros. El rendimiento a la primera subió "
                  "punto y medio, a noventa y nueve por ciento. Ni un solo sello malo se escapó en noventa "
                  "días. ¿Quién hace que todo funcione?",
    },
    {
        "key": "p15", "num": 15, "title": "Puestos y tu ruta",
        "points": [("Los operadores detectan, llaman y detienen", "Los operadores detectan"),
                   ("Los líderes responden y restablecen", "Los líderes responden"),
                   ("Un arranque de 30-60-90 días", "Arráncalo")],
        "example": "Días 0–30: define lo anormal. 31–60: detecta y entrena. 61–90: corrige las repeticiones "
                   "principales.",
        "example_cue": "En los primeros treinta días",
        "script": "Cada quien tiene un papel. Los operadores detectan, llaman, detienen y dan hechos. Los "
                  "líderes responden rápido, y restablecen el estándar. Mantenimiento mantiene funcionando "
                  "sensores e interbloqueos, y la gerencia protege el derecho a parar. Arráncalo en noventa "
                  "días. En los primeros treinta días, define lo anormal y elige un piloto. Luego construye "
                  "la detección y entrena. Por último, corrige las causas repetidas principales. ¿Dónde vas "
                  "a empezar?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Detectar", "icon": "sensor", "with": 0},
        {"label": "Detener", "icon": "lock", "with": 1},
        {"label": "Corregir", "icon": "wrench", "with": 2},
        {"label": "Prevenir", "icon": "shield", "tone": "good", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Sin Jidoka", "sub": "Los defectos viajan, se encuentran tarde", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Con Jidoka", "sub": "Atrapado en el origen", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 140, "icon": "warning", "label": "sellos delgados para la mañana",
                 "unit": "encontrados en la prueba de fugas", "with": "example"}},
    "p03": {"type": "timeline", "items": [
        {"label": "El telar se detiene si se rompe un hilo", "sub": "Principios de 1900", "icon": "gear", "with": 0},
        {"label": "Pilar del TPS", "sub": "TPS", "icon": "stack", "with": 2},
        {"label": "Ningún defecto avanza", "sub": "Hoy", "icon": "shield", "tone": "good", "with": "example"}]},
    "p04": {"type": "versus", "items": [
        {"label": "Vigilar una máquina", "sub": "Todo el turno", "icon": "search", "tone": "bad", "with": 0},
        {"label": "Atiende dos estaciones", "sub": "Y resuelve problemas", "icon": "person", "tone": "good", "with": "example"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Definir lo normal", "icon": "clipboard", "with": 0},
        {"label": "Detectar la desviación", "icon": "sensor", "with": 1},
        {"label": "Pruebas, monitores", "icon": "test", "with": 2}],
        "then": {"type": "stat", "value": 2.0, "decimals": 1, "suffix": "–2.4 mm", "icon": "pin", "label": "ancho normal del cordón",
                 "unit": "sin huecos", "with": "example"}},
    "p06": {"type": "steps", "items": [
        {"label": "Detener o contener", "with": 0},
        {"label": "Corregir", "with": 1},
        {"label": "Prevenir", "with": 2}]},
    "p07": {"type": "versus", "items": [
        {"label": "Automatización simple", "sub": "Dosificó toda la noche", "icon": "gear", "tone": "bad", "with": 0},
        {"label": "Jidoka", "sub": "Se detiene y llama", "icon": "sensor", "tone": "good", "with": 1}]},
    "p08": {"type": "icons", "items": [
        {"label": "Ningún defecto avanza", "icon": "lock", "with": 0},
        {"label": "Ninguna anormalidad escondida", "icon": "search", "with": 1},
        {"label": "Ninguna repetición sin acción", "icon": "key", "tone": "good", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Verde: normal", "sub": "Sigue el estándar", "icon": "check", "tone": "good", "with": 0},
        {"label": "Amarillo: ayuda", "sub": "El líder llega rápido", "icon": "person", "with": 1},
        {"label": "Rojo: detener", "sub": "Contener, escalar", "icon": "warning", "tone": "bad", "with": 2}]},
    "p10": {"type": "bars", "label": "", "note": "Llamadas de Andon por semana", "with": 2, "items": [
        {"label": "Antes", "value": 10, "with": 2},
        {"label": "Mes 1", "value": 20, "with": "example"},
        {"label": "Mes 3", "value": 10, "tone": "good", "with": "example"}]},
    "p11": {"type": "ladder", "top": "LO MÁS FUERTE", "bottom": "LO MÁS DÉBIL", "items": [
        {"label": "Eliminar o prevenir", "icon": "shape", "with": 0},
        {"label": "Detectar y detener", "icon": "sensor", "with": 1},
        {"label": "Advertir", "icon": "warning", "with": 2},
        {"label": "Inspeccionar después", "icon": "search", "with": 2}]},
    "p12": {"type": "flow", "items": [
        {"label": "El sensor revisa cada cordón", "icon": "sensor", "with": 0},
        {"label": "El dosificador se detiene", "icon": "lock", "with": 1},
        {"label": "Andon, retener hasta la última buena", "icon": "warning", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Antes", "value": 140}, "after": {"label": "Con Jidoka", "value": 1},
                 "unit": "monitores afectados por problema de boquilla", "with": "example"}},
    "p13": {"type": "steps", "items": [
        {"label": "Boquilla tapada", "with": 1},
        {"label": "Adhesivo curado en descansos", "with": "example"},
        {"label": "Sin paso de purga", "with": "example"},
        {"label": "Purga automática + monitor de presión", "with": 2}]},
    "p14": {"type": "compare", "before": {"label": "Antes", "value": 97.5}, "after": {"label": "Después", "value": 99.0},
            "decimals": 1, "suffix": "%", "unit": "rendimiento a la primera", "note": "Cero fugas en 90 días", "with": "example"},
    "p15": {"type": "timeline", "items": [
        {"label": "Definir lo anormal, piloto", "sub": "Días 0–30", "icon": "clipboard", "with": 2},
        {"label": "Detectar, entrenar", "sub": "31–60", "icon": "sensor", "with": 2},
        {"label": "Corregir las repeticiones principales", "sub": "61–90", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "¿Qué hace a Jidoka distinto de la automatización común?",
        "options": ["Corre más rápido",
                    "Detecta una anormalidad definida, se detiene, y llama a una persona",
                    "No necesita a nadie"],
        "correct": 1,
        "explanation": "La automatización hace el trabajo; Jidoka además lo juzga. Se detiene ante una "
                       "anormalidad definida y pide ayuda humana, para que los defectos no se multipliquen.",
        "q_script": "Prueba rápida. ¿Qué hace a Jidoka distinto de la automatización común? Tómate unos "
                    "segundos.",
        "a_script": "Es el segundo. Detecta una anormalidad definida, se detiene solo, y llama a una persona. "
                    "Así los defectos no se multiplican.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Una operadora ve un sello anormal, pero la línea va atrasada. ¿Qué debe hacer?",
        "options": ["Seguir y reportarlo al final del turno",
                    "Llamar al Andon y retener la unidad, como dicen las reglas de paro",
                    "Corregirlo ella misma en silencio y seguir"],
        "correct": 1,
        "explanation": "Ningún defecto avanza, ninguna anormalidad escondida. Llamar al Andon y retener la "
                       "unidad protege al cliente, aunque la producción vaya atrasada.",
        "q_script": "Una más, y esta es un escenario. Una operadora ve un sello anormal, pero la línea va "
                    "atrasada. ¿Qué debe hacer? Piénsalo.",
        "a_script": "Llamar al Andon, y retener la unidad, tal como dicen las reglas de paro. Ningún defecto "
                    "avanza, y ninguna anormalidad se esconde, aunque la producción vaya atrasada.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
