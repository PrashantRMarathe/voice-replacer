"""kaizen in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh kaizen_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "kz_es"
NAME = "kaizen_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Low Cost Automation": "lóu cost otoméishon",
    "Kaizen": "Káizen",
    "Gemba": "Guemba",
    "Check": "chek",
    "Plan": "plan",
    "PDCA": "pe de ce a",
    "SDCA": "ese de ce a",
    "ECRS": "e ce erre ese",
    "TAKT": "takt",
    "SOP": "ese o pe",
    "Act": "akt",
    "Do": "du",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Cada monitor en la línea de Suresh se volteaba dos veces. Boca abajo, y luego boca "
    "arriba otra vez. Nadie preguntaba por qué. Siempre se había hecho así. ¿Te suena "
    "familiar? En esta lección aprenderás Kaizen, la mejora continua. Verás cómo los cambios "
    "pequeños y probados, hechos por las personas que hacen el trabajo, suman grandes "
    "resultados. Seguiremos a Suresh, líder de línea en ensamble de monitores."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. El Kaizen es un hábito diario, no un evento de una vez. "
    "Prueba en pequeño, mide con honestidad, y revisa que nada más empeoró. Y estandariza "
    "cada ganancia, para que sea el punto de partida de la siguiente. Esta es tu acción para "
    "esta semana. Pregúntale a un operador qué hace difícil su trabajo, y prueba una solución "
    "pequeña. Excelente trabajo al completar esta lección. Ahora aprenderás Low Cost "
    "Automation."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué significa Kaizen",
        "points": [("Cambio para mejorar", "cambio para mejorar"),
                   ("Muchos cambios pequeños y disciplinados", "muchos cambios pequeños"),
                   ("Hechos por las personas más cercanas al trabajo", "Los hacen las personas")],
        "example": "La línea de Suresh: dos volteos de cada monitor, cada unidad, cada turno.",
        "example_cue": "En la línea de Suresh",
        "script": "Kaizen es una palabra japonesa que significa cambio para mejorar. En una fábrica, "
                  "significa mejora continua a través de muchos cambios pequeños. Los hacen las personas "
                  "más cercanas al trabajo, todos los días. No un gran proyecto, una vez al año. En la "
                  "línea de Suresh, cada monitor se volteaba dos veces, en cada turno. Son miles de "
                  "levantamientos pesados a la semana. ¿Y qué hace que una mejora sea un Kaizen?",
    },
    {
        "key": "p02", "num": 2, "title": "Qué lo hace Kaizen",
        "points": [("Continuo y impulsado por las personas", "Es continuo"),
                   ("Empieza en el Gemba", "Empieza en el Gemba"),
                   ("Primero bajo costo, respaldado por datos", "Prueba primero ideas"),
                   ("Termina en un estándar nuevo", "Y termina")],
        "example": "Cada estándar mejorado es la base del siguiente Kaizen.",
        "example_cue": "Luego el ciclo",
        "script": "Algunas cosas lo distinguen. Es continuo, y lo impulsan las personas, no solo los "
                  "ingenieros. Empieza en el Gemba, con lo que de verdad ves. Prueba primero ideas de bajo "
                  "costo, y revisa los resultados con datos. Y termina en un estándar nuevo, el mejor "
                  "método que conoces hoy. Luego el ciclo vuelve a empezar, desde esa nueva base. ¿Qué "
                  "mentalidad necesita eso?",
    },
    {
        "key": "p03", "num": 3, "title": "La mentalidad Kaizen",
        "points": [("Todo proceso puede mejorar", "Todo proceso puede"),
                   ("Los problemas son para aprender, no para culpar", "Los problemas son"),
                   ("Creatividad antes que capital", "la creatividad antes que el capital")],
        "example": "“Siempre lo hemos volteado” es justo la frase que el Kaizen cuestiona.",
        "example_cue": "Siempre lo hemos",
        "script": "Empieza con una creencia. Todo proceso puede mejorar, incluso uno bueno. Los problemas "
                  "son oportunidades para aprender, no razones para culpar a alguien. Ve a ver antes de "
                  "decidir. Y usa la creatividad antes que el capital. Una marca de cinta muchas veces le "
                  "gana a una máquina nueva. Siempre lo hemos hecho así es justo la frase que el Kaizen "
                  "cuestiona. ¿Cuándo la oíste por última vez en tu línea?",
    },
    {
        "key": "p04", "num": 4, "title": "Tipos de Kaizen",
        "points": [("Kaizen diario: de minutos a días", "El Kaizen diario"),
                   ("Kaizen puntual: una pérdida específica", "El Kaizen puntual"),
                   ("Evento Kaizen: de tres a cinco días", "Un evento Kaizen"),
                   ("Kaizen de sistema: el flujo de punta a punta", "El Kaizen de sistema")],
        "example": "El doble volteo: un Kaizen puntual, del propio equipo de Suresh.",
        "example_cue": "El doble volteo",
        "script": "El Kaizen viene en distintos tamaños. El Kaizen diario es pequeño y local, como acercar "
                  "una herramienta. El Kaizen puntual ataca una pérdida específica, en horas o días. Un "
                  "evento Kaizen reúne a un equipo de varias áreas durante tres a cinco días. El Kaizen de "
                  "sistema corrige el flujo entre departamentos, durante semanas. El doble volteo fue un "
                  "Kaizen puntual, del propio equipo de Suresh. ¿Qué tamaño le queda a tu mayor dolor?",
    },
    {
        "key": "p05", "num": 5, "title": "El Kaizen corre con PDCA",
        "points": [("Plan: observa, define, encuentra la causa", "Plan significa"),
                   ("Do: una prueba pequeña y segura", "Do significa"),
                   ("Check: compara con la base", "Check significa"),
                   ("Act: estandariza, o aprende y repite", "Act significa")],
        "example": "El SDCA sostiene el estándar. El PDCA lo mejora.",
        "example_cue": "Su gemelo",
        "script": "Cada Kaizen sigue el PDCA. Plan significa observar, definir la brecha, y encontrar la "
                  "causa. Do significa una prueba pequeña y segura. Check significa comparar el resultado "
                  "con tu base y tu meta. Act significa estandarizarlo, o aprender e intentar otra vez. Su "
                  "gemelo es el SDCA, que mantiene firme el estándar. Los equipos fuertes alternan entre "
                  "los dos. Sin el PDCA, una idea es solo un cambio sin probar. ¿Por dónde empiezas?",
    },
    {
        "key": "p06", "num": 6, "title": "Velo en el Gemba",
        "points": [("Observa el trabajo como de verdad es", "Observa el trabajo"),
                   ("Cuenta caminatas, estiramientos, volteos", "Cuenta las caminatas"),
                   ("Pregunta qué hace difícil el trabajo", "Pregúntales a los operadores")],
        "example": "Voltear boca abajo para poner la base, boca arriba para probar. Dos levantamientos de un "
                   "monitor de 6 kg.",
        "example_cue": "El equipo de Suresh lo vio",
        "script": "En el Gemba, claro. Observa el trabajo como de verdad es, no como dice el SOP. Cuenta "
                  "las caminatas, los estiramientos, las búsquedas y los levantamientos. Pregúntales a los "
                  "operadores qué hace difícil su trabajo. El equipo de Suresh lo vio de inmediato. Cada "
                  "monitor iba boca abajo para poner la base, y luego boca arriba otra vez para la prueba. "
                  "Dos levantamientos de un monitor de seis kilos, cada vez. ¿Qué anotarías?",
    },
    {
        "key": "p07", "num": 7, "title": "Definir el problema",
        "points": [("El síntoma, luego los hechos", "Empieza con el síntoma"),
                   ("Mide la pérdida", "Mide la pérdida"),
                   ("Una meta con fecha límite", "Fija una meta")],
        "example": "Ciclo de 38 s contra un TAKT de 35 s. 2 volteos por unidad. 15 rayones de panel por cada "
                   "1,000.",
        "example_cue": "Los hechos de Suresh",
        "script": "Empieza con el síntoma. La línea no cumplía su meta por hora. Luego reúne los hechos. "
                  "Mide la pérdida, y separa los hechos de las opiniones. Los hechos de Suresh eran claros. "
                  "El tiempo de ciclo era de treinta y ocho segundos, contra un TAKT de treinta y cinco. "
                  "Cada volteo arriesgaba un rayón, y quince paneles de cada mil salían rayados. Fija una "
                  "meta con fecha límite, y deja fuera la solución. ¿Qué meta te pondrías?",
    },
    {
        "key": "p08", "num": 8, "title": "Generar ideas",
        "points": [("Primero pregunta a los operadores", "Pregúntales primero a los operadores"),
                   ("Usa ECRS", "Usa ECRS"),
                   ("Mira otras líneas", "Mira otras líneas")],
        "example": "Leela, una operadora: “¿Por qué no poner la base mientras el monitor sigue en su "
                   "charola?”",
        "example_cue": "Leela, una operadora",
        "script": "Ahora genera ideas, y muchas. Pregúntales primero a los operadores. ¿Qué hace difícil "
                  "este trabajo? ¿Qué quitaría un paso? Usa ECRS, eliminar, combinar, reordenar y "
                  "simplificar. Mira otras líneas, y también otras industrias. Leela, una operadora del "
                  "turno de noche, tuvo la mejor idea. ¿Por qué no poner la base mientras el monitor sigue "
                  "boca abajo, en su charola? ¿Por qué nadie le había preguntado antes?",
    },
    {
        "key": "p09", "num": 9, "title": "Elegir la idea",
        "points": [("La seguridad y la calidad son filtros", "La seguridad y la calidad"),
                   ("Califica impacto, facilidad, costo, rapidez", "Luego califica"),
                   ("Debe corregir una causa comprobada", "Y la idea debe")],
        "example": "La idea de Leela: alta en impacto, facilidad y costo. Ganó.",
        "example_cue": "La idea de Leela",
        "script": "Elige con una tabla de puntos simple. La seguridad y la calidad son filtros. Si una idea "
                  "falla, queda fuera, sin importar su puntaje. Luego califica el impacto, la facilidad, el "
                  "costo y la rapidez, con pesos acordados. Y la idea debe atacar una causa que "
                  "comprobaste. Debe ser tan simple que todos puedan seguirla. La idea de Leela calificó "
                  "alto en impacto, facilidad y costo. Ganó fácilmente. ¿Cómo debes probarla?",
    },
    {
        "key": "p10", "num": 10, "title": "Pruébala en pequeño",
        "points": [("Una hipótesis y un alcance", "Escribe una hipótesis"),
                   ("Las mismas medidas que la base", "Mídela igual"),
                   ("Observa a las personas, no solo los números", "Observa a los operadores")],
        "example": "Una estación, un turno: pasos en nueva secuencia y una almohadilla de espuma en la "
                   "charola. Costo: casi nada.",
        "example_cue": "La prueba de Suresh",
        "script": "Primero en pequeño y seguro. Escribe una hipótesis. Si ponemos la base en la charola, "
                  "los dos volteos desaparecen. Fija el alcance, una estación y un turno. Mídela igual que "
                  "mediste la base. Observa a los operadores, no solo los números. La prueba de Suresh "
                  "corrió en una estación, durante un turno. Usó una nueva secuencia del trabajo y una "
                  "almohadilla de espuma en la charola. Casi no costó nada. ¿Qué pasó?",
    },
    {
        "key": "p11", "num": 11, "title": "Revisar los resultados",
        "points": [("Tiempo de ciclo: de 38 s a 33 s", "El tiempo de ciclo bajó"),
                   ("Volteos por unidad: de 2 a 0", "Los dos volteos"),
                   ("Rayones: de 15 a 3 por cada 1,000", "Los rayones bajaron"),
                   ("Nada más empeoró", "nada más empeoró")],
        "example": "Regla del equilibrio: la meta mejora, y la seguridad, la calidad y la entrega no sufren.",
        "example_cue": "Esa es la regla del equilibrio",
        "script": "El tiempo de ciclo bajó a treinta y tres segundos, ya dentro del TAKT. Los dos volteos "
                  "desaparecieron. Los rayones bajaron de quince a tres por cada mil. Y el equipo revisó "
                  "que nada más empeoró. Los resultados de prueba, la seguridad y la siguiente estación se "
                  "mantuvieron. Los operadores dijeron que su espalda notó la diferencia antes de la "
                  "comida. Esa es la regla del equilibrio. Mejorar un número mientras dañas otro no es "
                  "Kaizen. ¿Pero cómo sabes que va a durar?",
    },
    {
        "key": "p12", "num": 12, "title": "Medir con honestidad",
        "points": [("Mismas definiciones, antes y después", "Usa las mismas definiciones"),
                   ("Cuenta la producción buena, no la bruta", "Cuenta la producción buena"),
                   ("Revisa otra vez a los 30, 60, 90 días", "revisa otra vez")],
        "example": "Día 30: sigue en 33 s. Día 90: sigue en 33 s, y 3 rayones por cada 1,000.",
        "example_cue": "Suresh revisó",
        "script": "Mídelo con honestidad. Usa las mismas definiciones antes y después. Cuenta la producción "
                  "buena, no la producción bruta. Muestra el cambio real, no solo un porcentaje. Y revisa "
                  "que otra cosa, como una mezcla de modelos más fácil, no lo haya causado. Luego revisa "
                  "otra vez a los treinta, sesenta y noventa días. Suresh revisó en el día treinta, y otra "
                  "vez en el noventa. Seguía en treinta y tres segundos. ¿Qué lo deja fijo?",
    },
    {
        "key": "p13", "num": 13, "title": "Estandarizar la ganancia",
        "points": [("Actualiza el SOP y el trabajo estándar", "Actualiza el SOP"),
                   ("Entrena a todos, quita la forma vieja", "Entrena a cada operador"),
                   ("Nombra un responsable y audítalo", "Nombra un responsable")],
        "example": "Las instrucciones viejas del volteo se quitaron de cada estación esa misma semana.",
        "example_cue": "Suresh quitó",
        "script": "Un Kaizen no termina hasta que es el estándar. Actualiza el SOP y el trabajo estándar. "
                  "Entrena a cada operador, y confirma que lo entienden. Quita el método viejo, para que "
                  "nadie regrese a él. Nombra un responsable, y audítalo. Suresh quitó las instrucciones "
                  "viejas del volteo de cada estación, esa misma semana. El método nuevo se volvió la base. "
                  "Y la base es donde empieza el siguiente Kaizen. ¿Cómo mantienes las ideas llegando?",
    },
    {
        "key": "p14", "num": 14, "title": "Hacerlo un hábito",
        "points": [("Un tablero de ideas visible", "Un tablero de ideas visible"),
                   ("Respuesta rápida a cada idea", "Responde cada idea"),
                   ("Reconoce a las personas", "Reconoce")],
        "example": "El equipo de Suresh: 40 ideas en 3 meses, 27 probadas, 19 estandarizadas.",
        "example_cue": "En tres meses",
        "script": "Haz del Kaizen un hábito diario. Un tablero de ideas visible ayuda a que la gente vea "
                  "que sus ideas importan. Responde cada idea en menos de una semana, aunque la respuesta "
                  "sea no. Reconoce a las personas, no solo los ahorros. Y revisa cada semana las ideas en "
                  "curso. En tres meses, el equipo de Suresh registró cuarenta ideas. Probaron veintisiete, "
                  "y estandarizaron diecinueve. ¿Qué pasaría en tu línea?",
    },
    {
        "key": "p15", "num": 15, "title": "Empieza mañana",
        "points": [("Elige un dolor que se repite", "Elige un dolor que se repite"),
                   ("Observa diez ciclos, habla con el equipo", "Observa diez ciclos"),
                   ("Prueba la solución segura más pequeña", "prueba la solución segura más pequeña")],
        "example": "Kaizen = mejoras pequeñas × repetición disciplinada × sentido de dueño.",
        "example_cue": "Mejoras pequeñas",
        "script": "Así puedes empezar mañana. Elige un dolor que se repite en tu línea. Observa diez "
                  "ciclos, y mide la pérdida. Habla con las personas que hacen el trabajo, y fija una meta "
                  "medible. Luego prueba la solución segura más pequeña que puedas. Si funciona, "
                  "estandarízala. Mejoras pequeñas, repetidas con disciplina, por personas que se sienten "
                  "dueñas de ellas. Así las líneas comunes se vuelven grandes. ¿A quién le vas a preguntar "
                  "primero?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Cambio para mejorar", "icon": "chartUp", "with": 0},
        {"label": "Pasos pequeños", "icon": "sequence", "with": 1},
        {"label": "Por el equipo", "icon": "person", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 2, "icon": "weight", "label": "volteos de cada monitor",
                 "unit": "cada unidad, cada turno", "with": "example"}},
    "p02": {"type": "icons", "items": [
        {"label": "Continuo", "icon": "sequence", "with": 0},
        {"label": "Basado en el Gemba", "icon": "walk", "with": 1},
        {"label": "Bajo costo, datos", "icon": "scale", "with": 2},
        {"label": "Estándar nuevo", "icon": "clipboard", "tone": "good", "with": 3}]},
    "p03": {"type": "versus", "items": [
        {"label": "“Siempre lo hemos hecho así”", "sub": "Aceptar la pérdida", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "“Todo proceso puede mejorar”", "sub": "Kaizen", "icon": "check", "tone": "good", "with": 0}]},
    "p04": {"type": "ladder", "top": "LO MÁS GRANDE", "bottom": "LO MÁS PEQUEÑO", "items": [
        {"label": "Kaizen de sistema", "sub": "Semanas", "icon": "stack", "with": 3},
        {"label": "Evento Kaizen", "sub": "3–5 días", "icon": "calendar", "with": 2},
        {"label": "Kaizen puntual", "sub": "De horas a días", "icon": "pin", "with": 1},
        {"label": "Kaizen diario", "sub": "Minutos", "icon": "hand", "with": 0}]},
    "p05": {"type": "flow", "items": [
        {"label": "Plan", "icon": "clipboard", "with": 0},
        {"label": "Do", "icon": "wrench", "with": 1},
        {"label": "Check", "icon": "search", "with": 2},
        {"label": "Act", "icon": "check", "tone": "good", "with": 3}]},
    "p06": {"type": "flow", "items": [
        {"label": "Boca abajo: poner la base", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Boca arriba: probar", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Dos levantamientos de 6 kg", "icon": "warning", "tone": "bad", "with": "example"}]},
    "p07": {"type": "bars", "label": "TAKT", "value": 35, "suffix": " s", "with": "example", "items": [
        {"label": "Tiempo de ciclo", "value": 38, "tone": "bad", "with": "example"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Preguntar a los operadores", "icon": "person", "with": 0},
        {"label": "ECRS", "icon": "key", "with": 1},
        {"label": "Otras líneas", "icon": "search", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Voltear dos veces", "sub": "Hoy", "icon": "weight", "tone": "bad", "with": "example"},
            {"label": "Poner la base en la charola", "sub": "La idea de Leela", "icon": "check", "tone": "good", "with": "example"}]}},
    "p09": {"type": "icons", "with": "example", "items": [
        {"label": "Brazo robótico", "sub": "Puntaje 2.4", "icon": "gear", "with": "example"},
        {"label": "Ayuda para levantar", "sub": "Puntaje 3.6", "icon": "weight", "with": "example"},
        {"label": "La idea de Leela", "sub": "Puntaje 4.7 de 5", "icon": "check", "tone": "good", "with": "example"}]},
    "p10": {"type": "doc", "items": [
        {"label": "Hipótesis: los dos volteos desaparecen", "icon": "key", "with": 0},
        {"label": "Alcance: una estación, un turno", "icon": "pin", "with": 0},
        {"label": "Mismas medidas que la base", "icon": "scale", "with": 1},
        {"label": "Almohadilla de espuma + nueva secuencia", "icon": "shape", "with": "example"}]},
    "p11": {"type": "compare", "before": {"label": "Antes", "value": 15}, "after": {"label": "Prueba", "value": 3},
            "unit": "rayones de panel por cada 1,000 monitores", "note": "Ciclo 38 s → 33 s · volteos 2 → 0", "with": 2},
    "p12": {"type": "timeline", "items": [
        {"label": "Base", "sub": "Antes", "icon": "clipboard", "with": 0},
        {"label": "Sigue en 33 s", "sub": "Día 30", "icon": "check", "with": "example"},
        {"label": "Sigue en 33 s", "sub": "Día 90", "icon": "check", "tone": "good", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Actualizar el SOP", "icon": "clipboard", "with": 0},
        {"label": "Entrenar, quitar la forma vieja", "icon": "person", "with": 1},
        {"label": "Responsable y auditoría", "icon": "search", "tone": "good", "with": 2}]},
    "p14": {"type": "bars", "label": "", "note": "El equipo de Suresh, primeros tres meses", "with": "example", "items": [
        {"label": "Ideas", "value": 40, "with": "example"},
        {"label": "Probadas", "value": 27, "with": "example"},
        {"label": "Estandarizadas", "value": 19, "tone": "good", "with": "example"}]},
    "p15": {"type": "steps", "items": [
        {"label": "Un dolor que se repite", "with": 0},
        {"label": "Diez ciclos, hablar con el equipo", "with": 1},
        {"label": "La solución segura más pequeña", "with": 2},
        {"label": "Estandarizar", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "¿Cuál es el mejor planteamiento de problema para un Kaizen?",
        "options": ["“Necesitamos un brazo robótico en la línea de monitores”",
                    "“El tiempo de ciclo es de 38 s contra un TAKT de 35 s, con 2 volteos por unidad; llegar "
                    "a 35 s en 4 semanas”",
                    "“Los operadores son muy lentos”"],
        "correct": 1,
        "explanation": "Un buen planteamiento tiene la brecha medida, la pérdida observada y una meta con fecha "
                       "límite, sin nombrar una solución ni culpar a las personas.",
        "q_script": "Prueba rápida. ¿Cuál de estos es el mejor planteamiento de problema para un Kaizen? "
                    "Tómate unos segundos.",
        "a_script": "Es el segundo. Tiene la brecha medida, la pérdida observada, y una meta con fecha "
                    "límite. Los otros son una solución y una culpa.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Una prueba baja el tiempo de ciclo 4 segundos, pero los operadores reportan tensión en "
                    "el hombro. ¿Y ahora qué?",
        "options": ["Estandarizarlo: la meta mejoró",
                    "Tratarlo como todavía no exitoso: adaptar el método y volver a probar",
                    "Rotar a los operadores cada hora y conservarlo"],
        "correct": 1,
        "explanation": "La regla del equilibrio: un Kaizen solo tiene éxito si la seguridad, la calidad y las "
                       "personas no sufren. La tensión significa que el método necesita cambiar antes de "
                       "volverse el estándar.",
        "q_script": "Una más, y esta es un escenario. Una prueba baja el tiempo de ciclo cuatro segundos. "
                    "Pero los operadores reportan tensión en el hombro. ¿Qué debe hacer el equipo? Piénsalo.",
        "a_script": "Todavía no es un éxito. Adapta el método y vuelve a probar. Un Kaizen solo cuenta cuando "
                    "la seguridad y las personas no pagan por la ganancia.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
