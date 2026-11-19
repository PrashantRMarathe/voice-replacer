"""hancho in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh hancho_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "hc_es"
NAME = "hancho_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Ishikawa": "Ishikawa",
    "Hancho": "Jancho",
    "Gemba": "Guemba",
    "TAKT": "takt",
    "SOP": "ese o pe",
    "LED": "led",
    "TV": "te ve",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "El mes pasado, la línea produjo veinte TV menos por hora, durante todo un turno. Nadie "
    "lo notó hasta el reporte de la mañana siguiente. Para entonces, la pérdida ya era "
    "historia. ¿Te suena familiar? En esta lección aprenderás Hancho, el liderazgo justo en "
    "el piso de producción. Verás cómo un líder de equipo detecta una brecha en la primera "
    "hora, y la corrige antes de que termine el turno. Seguiremos a Sunita, una nueva Hancho "
    "en una línea de TV LED."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Dirige desde el Gemba, comparando el estándar con lo que de "
    "verdad está pasando. Haz visible cada brecha, cada hora, y reacciona en el mismo turno. "
    "Y desarrolla a tu gente, para que la línea no dependa de ti. Esta es tu acción para esta "
    "semana. Escribe tu propio trabajo estándar de líder, para un turno. Excelente trabajo al "
    "completar esta lección. Ahora aprenderás el diagrama de Ishikawa."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es un Hancho",
        "points": [("En japonés: líder de equipo", "significa en japonés"),
                   ("Un sistema de liderazgo, no una herramienta", "No es una herramienta"),
                   ("Dirige donde se crea el valor", "que dirige justo")],
        "example": "Sunita: doce operadores, una línea de TV LED, los resultados de cada turno.",
        "example_cue": "Sunita dirige a doce operadores en una línea de pantallas LED",
        "script": "Hancho significa en japonés líder de equipo, o líder de primera línea. No es una "
                  "herramienta que llenas. Es un sistema de liderazgo, construido alrededor de una persona "
                  "que dirige justo donde se crea el valor. Cerca de los operadores, cerca del proceso, y "
                  "cerca de los problemas. Sunita dirige a doce operadores en una línea de pantallas LED. "
                  "Es dueña de los resultados de cada turno, y de cada TV. ¿Y cómo piensa un Hancho?",
    },
    {
        "key": "p02", "num": 2, "title": "La mentalidad del Hancho",
        "points": [("¿Cuál es el estándar? ¿Qué es lo real?", "Cuál es el estándar"),
                   ("¿Dónde está la brecha, y por qué?", "Dónde está la brecha"),
                   ("Actúa ya, y luego evita que se repita", "Qué hacemos ahora mismo")],
        "example": "Sunita lleva estas preguntas en una tarjeta en su bolsillo.",
        "example_cue": "Sunita lleva",
        "script": "Un Hancho hace las mismas preguntas, cada vez. ¿Cuál es el estándar? ¿Qué está pasando "
                  "de verdad? ¿Dónde está la brecha, y qué la causó? ¿Qué hacemos ahora mismo, y qué debe "
                  "cambiar para que nunca se repita? Nota que en ninguna hay culpa. Solo estándar, real, "
                  "brecha y acción. Sunita lleva estas preguntas en una tarjeta pequeña en su bolsillo. "
                  "¿Por qué una línea necesita este puesto?",
    },
    {
        "key": "p03", "num": 3, "title": "Por qué las líneas necesitan un Hancho",
        "points": [("Las brechas pequeñas crecen cuando los líderes están lejos", "Cuando los líderes están lejos"),
                   ("Respuesta más rápida, responsabilidad clara", "Un Hancho significa"),
                   ("Kaizen diario, no solo proyectos", "Y la mejora pasa")],
        "example": "El mes pasado: una brecha de 20 TV por hora, encontrada a la mañana siguiente.",
        "example_cue": "Recuerda la brecha",
        "script": "Cuando los líderes están lejos del proceso, las brechas pequeñas crecen. Un fixture "
                  "flojo se vuelve un paro. Unos cuantos defectos se vuelven una queja del cliente. Un "
                  "Hancho significa respuesta más rápida, y responsabilidad clara en cada turno. Los "
                  "estándares se siguen, porque alguien los revisa. Y la mejora pasa todos los días, no "
                  "solo en proyectos especiales. Recuerda la brecha del mes pasado, encontrada a la mañana "
                  "siguiente. ¿De qué es dueño exactamente un Hancho?",
    },
    {
        "key": "p04", "num": 4, "title": "De qué es dueño un Hancho",
        "points": [("Seguridad y calidad", "La seguridad va primero"),
                   ("Entrega y costo", "La entrega significa"),
                   ("Las personas y el proceso", "Y las personas")],
        "example": "La regla de Sunita: resuélvelo, pide apoyo, o escala. Sabe cuál.",
        "example_cue": "Sunita aprendió",
        "script": "Un Hancho es dueño de seis áreas. La seguridad va primero, luego la calidad, protegiendo "
                  "el estándar y conteniendo los defectos. La entrega significa seguir el plan contra lo "
                  "real, cada hora. El costo significa reducir desecho, retrabajo y paros. Y las personas, "
                  "y el proceso, con entrenamiento, trabajo estándar y una línea lista. Sunita aprendió una "
                  "cosa más. Saber cuándo resolverlo, cuándo pedir apoyo, y cuándo escalar. ¿Cómo empieza "
                  "su día?",
    },
    {
        "key": "p05", "num": 5, "title": "Antes de que empiece el turno",
        "points": [("Revisión de preparación antes del turno", "Primero, la preparación"),
                   ("Una junta breve con el equipo", "Luego una junta breve"),
                   ("Revisiones de arranque y de primera pieza", "Luego las revisiones de arranque")],
        "example": "La junta de hoy: un cambio de modelo a la TV de 43 pulgadas a las 10 en punto.",
        "example_cue": "La junta de hoy",
        "script": "El día de Sunita empieza antes que la línea. Primero, la preparación. ¿Están listos las "
                  "personas, los materiales, las máquinas, las herramientas y los documentos? Luego una "
                  "junta breve. La meta, las alertas de calidad, los puntos de seguridad, y lo que aprendió "
                  "el turno anterior. Luego las revisiones de arranque, incluida la primera pieza. La junta "
                  "de hoy tenía un punto grande. Un cambio de modelo a la TV de cuarenta y tres pulgadas a "
                  "las diez en punto. ¿Qué pasa cuando la línea ya corre?",
    },
    {
        "key": "p06", "num": 6, "title": "Durante y después del turno",
        "points": [("Plan contra real cada hora", "Cada hora"),
                   ("Reacciona a cada anormalidad", "Reacciona"),
                   ("Entrena en el proceso", "Entrena"),
                   ("Una entrega de turno con hechos", "Al final")],
        "example": "Nota de entrega: pendientes, WIP, estado de calidad, acciones y responsables.",
        "example_cue": "Su entrega de turno",
        "script": "Cada hora, compara el plan con lo real. Producción, rendimiento a la primera, paros y "
                  "trabajo en proceso. Reacciona a cada anormalidad, y la registra. Entrena a los "
                  "operadores en el proceso, no en una sala de juntas. Al final, entrega al siguiente turno "
                  "con hechos, no con recuerdos. Su entrega de turno cubre los pendientes, el estado de "
                  "calidad, las acciones y los responsables. ¿Dónde pasa la mayor parte de su tiempo?",
    },
    {
        "key": "p07", "num": 7, "title": "Dirigir en el Gemba",
        "points": [("Observa el proceso y el producto reales", "Observa"),
                   ("Habla con el operador", "Habla"),
                   ("Haz preguntas, no solo des respuestas", "Hace preguntas")],
        "example": "“¿Qué debería estar pasando? ¿Qué está pasando de verdad? ¿Qué cambió?”",
        "example_cue": "Sus tres favoritas",
        "script": "En el Gemba, no en un escritorio. Observa el proceso real y el producto real. Habla con "
                  "el operador que hace el trabajo. Compara el método real con el estándar. Y hace "
                  "preguntas que desarrollan el pensamiento, en lugar de repartir todas las respuestas. Sus "
                  "tres favoritas son simples. ¿Qué debería estar pasando? ¿Qué está pasando de verdad? ¿Y "
                  "qué cambió? ¿Cuál preguntarías primero?",
    },
    {
        "key": "p08", "num": 8, "title": "Trabajo estándar del líder",
        "points": [("Revisiones por frecuencia", "enlista sus revisiones"),
                   ("Secuencia, tiempo de ciclo, puntos de calidad", "Revisa"),
                   ("El SOP más reciente en cada estación", "Y el SOP más reciente")],
        "example": "La lista de Sunita: inicio de turno, cada hora, cada cambio de modelo, fin de turno.",
        "example_cue": "Su lista corre",
        "script": "Un Hancho también necesita trabajo estándar. El trabajo estándar del líder enlista sus "
                  "revisiones, según qué tan seguido pasan. Revisa la secuencia de trabajo, el tiempo de "
                  "ciclo contra el TAKT, y los puntos de calidad. Revisa que las herramientas y los "
                  "fixtures estén bien. Y el SOP más reciente debe estar en cada estación, y entenderse. Su "
                  "lista corre al inicio del turno, cada hora, en cada cambio de modelo, y al final. ¿Qué "
                  "incluiría la tuya?",
    },
    {
        "key": "p09", "num": 9, "title": "Gestión visual",
        "points": [("Plan contra real, cada hora", "El plan contra lo real"),
                   ("Calidad, paros, acciones abiertas", "El rendimiento a la primera"),
                   ("Ver, reaccionar, registrar, dar seguimiento", "Cada número en rojo")],
        "example": "De 10 a 11 a.m.: plan 120 TV, real 98. Rojo.",
        "example_cue": "A las once en punto",
        "script": "Haz que la línea se lea de un vistazo. El plan contra lo real, cada hora. El rendimiento "
                  "a la primera, los defectos principales, las razones de paro, y las acciones abiertas con "
                  "responsables. Pero un tablero no es decoración. Cada número en rojo debe provocar una "
                  "respuesta. Velo, reacciona, regístralo, y dale seguimiento. A las once en punto, el "
                  "tablero de Sunita se puso en rojo. Plan, ciento veinte TV. Real, noventa y ocho. ¿Qué "
                  "debe hacer primero?",
    },
    {
        "key": "p10", "num": 10, "title": "Respuesta a anormalidades",
        "points": [("Detecta, contén, llama", "Detecta la brecha"),
                   ("Corrige y confirma", "Corrige el proceso"),
                   ("Previene y comparte", "Luego previénelo")],
        "example": "Nivel 1: el equipo lo corrige. Nivel 2: pide apoyo. Nivel 3: escala a la gerencia.",
        "example_cue": "Hay tres niveles",
        "script": "Sigue una respuesta clara. Detecta la brecha, contenla para proteger al cliente, y llama "
                  "al apoyo correcto. Corrige el proceso, y confirma que la producción vuelve a ser buena. "
                  "Luego previénelo, y comparte lo que aprendiste. Hay tres niveles. Nivel uno, el equipo "
                  "lo corrige. Nivel dos, llama a calidad, ingeniería o mantenimiento. Nivel tres, riesgo "
                  "de seguridad o para el cliente, escala ya. ¿Qué nivel era el de Sunita?",
    },
    {
        "key": "p11", "num": 11, "title": "La hora roja de Sunita",
        "points": [("Producción: 98 contra 120 por hora", "La producción había bajado"),
                   ("Rendimiento a la primera: de 98.5% a 95.8%", "El rendimiento a la primera"),
                   ("Trabajo amontonado antes de la prueba", "Y el trabajo se amontonaba")],
        "example": "Empezó justo después del cambio de modelo de las 10 en punto.",
        "example_cue": "Todo empezó",
        "script": "Esto es lo que vio. La producción había bajado a noventa y ocho TV por hora, contra un "
                  "plan de ciento veinte. El rendimiento a la primera había caído casi tres puntos. Y el "
                  "trabajo se amontonaba frente a la estación de prueba. Tres números, todos moviéndose "
                  "hacia el lado equivocado. Todo empezó justo después del cambio de modelo de las diez. "
                  "¿Irías primero a la estación de prueba?",
    },
    {
        "key": "p12", "num": 12, "title": "Contener, luego ir a ver",
        "points": [("Retén las TV sospechosas", "retuvo"),
                   ("Encuentra la estación cuello de botella", "encontró el cuello de botella"),
                   ("Compara el método con el estándar", "comparó el método")],
        "example": "Estación 6: en el modelo nuevo, el cable del panel tomaba otra ruta, y los operadores lo "
                   "doblaban a mano.",
        "example_cue": "En la estación seis",
        "script": "Todavía no. Primero, retuvo cada TV sospechosa desde las diez. Cliente protegido. Luego "
                  "recorrió la línea, y encontró el cuello de botella antes de la prueba. Comparó el método "
                  "con el estándar, en cada estación. En la estación seis, el cable del panel del modelo "
                  "nuevo tomaba otra ruta. El fixture todavía guiaba la ruta vieja. Así que los operadores "
                  "doblaban el cable a mano, y algunos no quedaban asentados. ¿Era de nivel uno?",
    },
    {
        "key": "p13", "num": 13, "title": "Llamar, corregir, confirmar",
        "points": [("Nivel 2: llamar a ingeniería", "Llamó a ingeniería"),
                   ("Corregir el fixture, actualizar el SOP", "ajustó la guía del cable"),
                   ("Confirmar durante varios ciclos", "lo confirmó")],
        "example": "Para la 1 p.m.: 120 TV por hora, rendimiento a la primera de 98.6%.",
        "example_cue": "Para la una",
        "script": "Era de nivel dos. Llamó a ingeniería, con hechos, fotos y las unidades con falla. "
                  "Ingeniería ajustó la guía del cable para el modelo nuevo, y el SOP se actualizó. Sunita "
                  "lo confirmó durante varios ciclos, no solo con una TV buena. Para la una, la línea "
                  "volvió a ciento veinte por hora. El rendimiento a la primera era de noventa y ocho punto "
                  "seis. ¿Quién se aseguró de que cada turno lo supiera?",
    },
    {
        "key": "p14", "num": 14, "title": "Desarrollar a las personas",
        "points": [("Explicar, mostrar, practicar, verificar", "Explica, demuestra"),
                   ("Certifica las habilidades críticas", "Certifica las habilidades críticas"),
                   ("Entrena en varios puestos para cubrir", "Entrena en varios puestos")],
        "example": "Sunita entrenó a dos operadores en la nueva ruta del cable antes del turno de noche.",
        "example_cue": "Sunita entrenó",
        "script": "Un Hancho desarrolla capacidad, no dependencia. Usa un ritmo simple de entrenamiento. "
                  "Explica, demuestra, déjalos practicar, y luego verifica. Certifica las habilidades "
                  "críticas antes de que alguien trabaje solo. Entrena en varios puestos, para que una "
                  "ausencia no pare la línea. Y enseña a resolver problemas, no solo el trabajo. Sunita "
                  "entrenó a dos operadores en la nueva ruta del cable, antes de que empezara el turno de "
                  "noche. ¿Tu línea podría correr sin ti?",
    },
    {
        "key": "p15", "num": 15, "title": "Medirlo, y luego empezar",
        "points": [("KPI cada hora, cada día, cada semana", "Revisa la producción"),
                   ("Audita para entrenar, no para culpar", "Audita para entrenar"),
                   ("Un plan de 30 días", "Este es un plan de treinta días")],
        "example": "Semana 1 puestos · semana 2 tablero por hora · semana 3 habilidades · semana 4 auditoría "
                   "y revisión.",
        "example_cue": "Este es un plan de treinta días",
        "script": "Mide los resultados y la disciplina. Revisa la producción y los paros cada hora, la "
                  "calidad cada día, y las habilidades y el Kaizen cada semana. Un número en verde sin "
                  "disciplina no va a durar. Audita para entrenar a tu equipo, no para atrapar a la gente. "
                  "Este es un plan de treinta días. Semana uno, define los puestos y el trabajo estándar "
                  "del líder. Semana dos, arranca el tablero por hora. Semana tres, habilidades y "
                  "entrenamiento. Semana cuatro, auditoría y revisión. ¿Qué semana empezarás?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Líder de equipo", "sub": "班長", "icon": "person", "with": 0},
        {"label": "Un sistema", "icon": "gear", "with": 1},
        {"label": "En el Gemba", "icon": "walk", "tone": "good", "with": 2}]},
    "p02": {"type": "steps", "items": [
        {"label": "¿Estándar?", "with": 0}, {"label": "¿Real?", "with": 0},
        {"label": "¿Brecha y causa?", "with": 1}, {"label": "Actuar y prevenir", "with": 2}]},
    "p03": {"type": "versus", "items": [
        {"label": "Líder lejano", "sub": "Brecha encontrada a la mañana siguiente", "icon": "clock", "tone": "bad", "with": 0},
        {"label": "Hancho en la línea", "sub": "Brecha encontrada en esta hora", "icon": "person", "tone": "good", "with": 1}]},
    "p04": {"type": "icons", "items": [
        {"label": "Seguridad", "icon": "shield", "with": 0},
        {"label": "Calidad", "icon": "check", "with": 0},
        {"label": "Entrega", "icon": "calendar", "with": 1},
        {"label": "Costo", "icon": "scale", "with": 1},
        {"label": "Personas", "icon": "person", "with": 2},
        {"label": "Proceso", "icon": "clipboard", "with": 2}]},
    "p05": {"type": "flow", "items": [
        {"label": "Preparación", "sub": "Personas, material, herramientas", "icon": "clipboard", "with": 0},
        {"label": "Junta", "sub": "Meta, alertas, aprendizaje", "icon": "person", "with": 1},
        {"label": "Revisiones de arranque", "sub": "Primera pieza", "icon": "check", "tone": "good", "with": 2}]},
    "p06": {"type": "timeline", "items": [
        {"label": "Plan contra real", "sub": "Cada hora", "icon": "clock", "with": 0},
        {"label": "Reaccionar, entrenar", "sub": "Todo el turno", "icon": "hand", "with": 1},
        {"label": "Entrega de turno", "sub": "Fin de turno", "icon": "clipboard", "tone": "good", "with": 3}]},
    "p07": {"type": "icons", "items": [
        {"label": "Observar", "icon": "search", "with": 0},
        {"label": "Hablar", "icon": "person", "with": 1},
        {"label": "Preguntar, no ordenar", "icon": "key", "tone": "good", "with": 2}]},
    "p08": {"type": "doc", "items": [
        {"label": "Inicio de turno: preparación", "icon": "calendar", "with": "example"},
        {"label": "Cada hora: plan contra real", "icon": "clock", "with": "example"},
        {"label": "Cambio de modelo: primera pieza", "icon": "check", "with": "example"},
        {"label": "Fin de turno: entrega", "icon": "clipboard", "with": "example"}]},
    "p09": {"type": "bars", "label": "", "note": "10–11 a.m.: plan contra real", "with": "example", "items": [
        {"label": "Plan", "value": 120, "tone": "good", "with": "example"},
        {"label": "Real", "value": 98, "tone": "bad", "with": "example"}]},
    "p10": {"type": "ladder", "top": "NIVEL 3", "bottom": "NIVEL 1", "items": [
        {"label": "Riesgo de seguridad o para el cliente: escala ya", "icon": "warning", "tone": "bad", "with": "example"},
        {"label": "Llama a las áreas de apoyo", "icon": "person", "with": "example"},
        {"label": "El equipo restablece el estándar", "icon": "hand", "tone": "good", "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "98 contra 120 por hora", "icon": "chartDown", "tone": "bad", "with": 0},
        {"label": "FPY 98.5% → 95.8%", "icon": "test", "tone": "bad", "with": 1},
        {"label": "WIP antes de la prueba", "icon": "stack", "tone": "bad", "with": 2}]},
    "p12": {"type": "flow", "items": [
        {"label": "Retener las TV sospechosas", "icon": "lock", "with": 0},
        {"label": "Encontrar el cuello de botella", "icon": "search", "with": 1},
        {"label": "Estación 6: cambió la ruta del cable", "icon": "wrench", "tone": "bad", "with": "example"}]},
    "p13": {"type": "compare", "before": {"label": "11 a.m.", "value": 98}, "after": {"label": "1 p.m.", "value": 120},
            "unit": "TV por hora", "note": "Rendimiento a la primera de vuelta en 98.6%", "with": "example"},
    "p14": {"type": "steps", "items": [
        {"label": "Explicar", "with": 0}, {"label": "Demostrar", "with": 0},
        {"label": "Practicar", "with": 0}, {"label": "Verificar", "with": 1}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Puestos, trabajo estándar del líder", "sub": "Semana 1", "icon": "clipboard", "with": 2},
        {"label": "Tablero por hora", "sub": "Semana 2", "icon": "chartUp", "with": 2},
        {"label": "Habilidades, entrenamiento", "sub": "Semana 3", "icon": "person", "with": 2},
        {"label": "Auditoría, revisión", "sub": "Semana 4", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "El trabajo de un Hancho es principalmente…",
        "options": ["Llenar el reporte del turno al final del día",
                    "Dirigir en el Gemba: mantener el estándar, reaccionar a las brechas, desarrollar a las "
                    "personas",
                    "Hacer en persona la estación más difícil, cada turno"],
        "correct": 1,
        "explanation": "Un Hancho dirige donde se crea el valor: protege el estándar, responde rápido a las "
                       "anormalidades y desarrolla la capacidad del equipo. Los reportes y cubrir estaciones no "
                       "son el centro del puesto.",
        "q_script": "Prueba rápida. ¿Cuál es el trabajo principal de un Hancho? Tómate unos segundos.",
        "a_script": "Es el segundo. Dirigir en el Gemba. Mantener el estándar, reaccionar a las brechas, y "
                    "desarrollar a tu gente.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "El tablero por hora se pone en rojo y las unidades sospechosas pueden tener un riesgo de "
                    "seguridad. ¿Qué nivel de respuesta?",
        "options": ["Nivel 1: el equipo lo corrige en silencio",
                    "Nivel 2: llamar a mantenimiento cuando esté libre",
                    "Nivel 3: contener y escalar a la gerencia de inmediato"],
        "correct": 2,
        "explanation": "El riesgo de seguridad o para el cliente es de nivel 3: contén las unidades y escala de "
                       "inmediato. No esperes a ver si el equipo puede con ello.",
        "q_script": "Una más, y esta es un escenario. El tablero por hora se pone en rojo, y las unidades "
                    "sospechosas pueden tener un riesgo de seguridad. ¿Qué nivel de respuesta es? Piénsalo.",
        "a_script": "Es nivel tres. Contén las unidades, y escala a la gerencia de inmediato. El riesgo de "
                    "seguridad nunca espera.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
