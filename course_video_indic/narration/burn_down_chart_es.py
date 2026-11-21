"""burn_down_chart in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh burn_down_chart_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "bd_es"
NAME = "burn_down_chart_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Cycle Time Study": "sáikol táim stódi",
    "Burn Down Chart": "bern dáun chart",
    "Kaizen": "Káizen",
    "RF": "erre efe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "El mes pasado, el camión se fue con ochenta routers de menos. Nadie lo vio venir, hasta "
    "el viernes en la tarde. ¿Te suena familiar? En esta lección aprenderás el Burn Down "
    "Chart. Verás cómo seguir el trabajo que falta. Notarás un retraso el día dos, no el día "
    "cinco, y te recuperarás a tiempo. Seguiremos a Sneha, supervisora de producción en una "
    "línea de routers Wi-Fi, mientras se asegura de que no vuelva a pasar."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Dibuja primero la línea ideal, y nunca la vuelvas a dibujar "
    "para verte mejor. Cuenta solo el trabajo que de verdad está completo y bueno. Y cuando "
    "la línea suba por encima de la ideal, actúa ese mismo día, con un responsable. Esta es "
    "tu acción para esta semana. Elige un trabajo con fecha límite, y dibuja su gráfica de "
    "trabajo pendiente antes del turno de mañana. Excelente trabajo al completar esta "
    "lección. Ahora aprenderás el Cycle Time Study."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué muestra la gráfica",
        "points": [("Trabajo pendiente contra tiempo disponible", "cuánto trabajo falta"),
                   ("Arriba: trabajo pendiente. A lo ancho: tiempo", "El eje vertical"),
                   ("La línea baja hacia cero", "la línea debe bajar")],
        "example": "La gráfica de Sneha: un pizarrón junto a la línea, visible para cada turno.",
        "example_cue": "Sneha dibuja la suya",
        "script": "Esta es la idea. Una gráfica de trabajo pendiente muestra cuánto trabajo falta, contra "
                  "el tiempo que tienes. El eje vertical es el trabajo pendiente. El eje horizontal es el "
                  "tiempo. Conforme tu equipo termina trabajo, la línea debe bajar hacia cero. Eso es todo. "
                  "Simple, pero poderoso. Sneha dibuja la suya en un pizarrón junto a la línea, para que "
                  "cada turno la vea. ¿Y por qué a Lean le gusta tanto una gráfica tan simple?",
    },
    {
        "key": "p02", "num": 2, "title": "Por qué Lean la usa",
        "points": [("Una meta se vuelve un camino visible", "convierte una meta en un camino"),
                   ("Ve una brecha mientras es pequeña", "Ves una brecha"),
                   ("Enfócate en la restricción", "enfocar a tu gente")],
        "example": "El mes pasado: solo una fecha límite. La brecha apareció el viernes en la tarde.",
        "example_cue": "El mes pasado, Sneha",
        "script": "Porque convierte una meta en un camino que puedes ver. Una fecha límite sola no te dice "
                  "nada, hasta que no la cumples. Esta gráfica te muestra cada día si vas bien. Ves una "
                  "brecha mientras todavía es pequeña. Y puedes enfocar a tu gente en la única restricción "
                  "que impide terminar. El mes pasado, Sneha solo tenía una fecha límite. Encontró la "
                  "brecha el viernes. ¿Cuánto valdrían para ti dos días extra?",
    },
    {
        "key": "p03", "num": 3, "title": "Para qué sirve",
        "points": [("Trabajo pendiente visible para todos", "hace visible el trabajo pendiente"),
                   ("Avance real contra el ritmo necesario", "Compara el avance real"),
                   ("Detecta retrasos a tiempo", "Detecta los retrasos a tiempo"),
                   ("Recuperación respaldada por hechos", "respalda tus acciones de recuperación")],
        "example": "La meta: cada unidad planeada llega a cero en la fecha límite.",
        "example_cue": "La meta es simple",
        "script": "¿Y qué hace de verdad esta gráfica por ti? Hace visible el trabajo pendiente para todo "
                  "el equipo, no solo para quien planea. Compara el avance real con el ritmo que necesitas. "
                  "Detecta los retrasos a tiempo, cuando recuperarse todavía es barato. Y respalda tus "
                  "acciones de recuperación con hechos, no con sensaciones. La meta es simple. Cada unidad "
                  "planeada llega a cero en la fecha límite. Veamos qué hay en la gráfica.",
    },
    {
        "key": "p04", "num": 4, "title": "Los cinco elementos",
        "points": [("Ejes: trabajo pendiente, tiempo", "El eje vertical"),
                   ("Línea ideal: el ritmo que necesitas", "La línea ideal"),
                   ("Línea real: lo que de verdad pasó", "La línea real"),
                   ("Brecha: real menos ideal", "la brecha es")],
        "example": "Sneha sigue los routers que faltan por terminar, día con día.",
        "example_cue": "Sneha sigue los routers",
        "script": "La gráfica tiene cinco partes. El eje vertical es el trabajo pendiente, en unidades, "
                  "defectos, acciones u horas. El eje horizontal es el tiempo, en turnos, días o semanas. "
                  "La línea ideal es el ritmo que necesitas. La línea real es lo que de verdad pasó. Y la "
                  "brecha es la distancia entre las dos. Sneha sigue los routers que faltan por terminar, "
                  "día con día. ¿Qué unidad contarías en tu línea?",
    },
    {
        "key": "p05", "num": 5, "title": "El reto de Sneha",
        "points": [("1,000 routers en trabajo en proceso", "Mil routers"),
                   ("5 días hábiles para el camión", "El camión sale"),
                   ("Pendiente = planeado − terminado", "El trabajo pendiente es igual")],
        "example": "Día 0: nada terminado, quedan 1,000 routers.",
        "example_cue": "En el día cero",
        "script": "Este es el reto de Sneha este mes. Mil routers están atorados en trabajo en proceso. "
                  "Todavía necesitan prueba final y empaque, y solo cuentan las unidades buenas. El camión "
                  "sale en cinco días hábiles. La cuenta empieza simple. El trabajo pendiente es igual al "
                  "trabajo total planeado, menos lo que ya terminaste. En el día cero, no hay nada hecho, "
                  "así que quedan los mil. ¿Adivinas qué ritmo necesita cada día?",
    },
    {
        "key": "p06", "num": 6, "title": "El ritmo ideal",
        "points": [("Ritmo = trabajo total ÷ periodos", "trabajo total dividido"),
                   ("1,000 ÷ 5 = 200 al día", "Doscientos al día"),
                   ("Dibújala primero, nunca la redibujes", "Dibújala antes")],
        "example": "Línea ideal: 1,000 → 800 → 600 → 400 → 200 → 0",
        "example_cue": "Así que su línea ideal",
        "script": "El ritmo ideal es el trabajo total dividido entre los periodos que tienes. Para Sneha, "
                  "son mil routers en cinco días. Doscientos al día. Así que su línea ideal baja a cero en "
                  "cinco pasos iguales. Esa línea recta es su plan. Dibújala antes de empezar el trabajo, y "
                  "nunca la redibujes para verte mejor. Si mueves el plan, escondes la brecha. ¿Y qué pasó "
                  "después de dos días?",
    },
    {
        "key": "p07", "num": 7, "title": "Día dos: encontrar la brecha",
        "points": [("Terminados: 320", "Su equipo ha terminado"),
                   ("Pendientes: 680. Ideal: 600", "Así que quedan seiscientos ochenta"),
                   ("Brecha: 80 atrás del plan", "La brecha es"),
                   ("Tres días para recuperarse, sin tocar la calidad", "Tiene tres días")],
        "example": "Detectado el martes, no el viernes.",
        "example_cue": "lo sabe el martes",
        "script": "Al final del día dos, Sneha actualiza su gráfica. Su equipo ha terminado trescientos "
                  "veinte routers. Así que quedan seiscientos ochenta. Pero su línea ideal dice que "
                  "deberían quedar seiscientos. La brecha es de ochenta routers atrás del plan. ¿Es un "
                  "desastre? No, pero es una señal. Tiene tres días para recuperarlos, sin recortar nada de "
                  "calidad. Y lo sabe el martes, no el viernes.",
    },
    {
        "key": "p08", "num": 8, "title": "Leer las líneas",
        "points": [("Arriba de la ideal: atrasado. Busca la restricción", "línea real está arriba"),
                   ("Abajo de la ideal: adelantado. Confirma la calidad", "Si está abajo"),
                   ("Ir adelante con unidades malas no es ir adelante", "Ir adelante con unidades malas")],
        "example": "La línea de Sneha está arriba de la ideal. ¿Qué impide que los routers se terminen?",
        "example_cue": "La línea de Sneha estaba arriba",
        "script": "¿Y cómo lees las líneas? Si la línea real está arriba de la ideal, queda más trabajo del "
                  "planeado. Busca la restricción, y asigna una acción de recuperación. Si está abajo, vas "
                  "adelantado. Muy bien, pero confirma la calidad, y sostén el ritmo. Ir adelante con "
                  "unidades malas no es ir adelante. La línea de Sneha estaba arriba. Así que su pregunta "
                  "era simple. ¿Qué impide que los routers se terminen? ¿Qué revisarías primero?",
    },
    {
        "key": "p09", "num": 9, "title": "Líneas planas y llegar a cero",
        "points": [("Línea plana: nada se cerró", "Una línea plana significa"),
                   ("Revisa paro, responsable, datos", "Así que revisa si hay un paro"),
                   ("En cero: verifica, luego cierra", "cuando la línea llega a cero")],
        "example": "Miércoles: la línea de Sneha se quedó plana un turno completo.",
        "example_cue": "El miércoles",
        "script": "Otros dos patrones importan. Una línea plana significa que nada se cerró. O el trabajo "
                  "se detuvo, o nadie actualizó la gráfica. A veces las dos cosas. Así que revisa si hay un "
                  "paro, revisa al responsable, y revisa los datos. ¿Y cuando la línea llega a cero? No "
                  "solo celebres. Verifica que cada unidad cumpla los criterios de aceptación, y luego "
                  "ciérrala formalmente. El miércoles, la línea de Sneha se quedó plana un turno completo. "
                  "¿Adivinas por qué?",
    },
    {
        "key": "p10", "num": 10, "title": "La revisión diaria",
        "points": [("Actualiza y compara", "Actualiza, registrando"),
                   ("Explica la causa principal", "Explica la causa principal"),
                   ("Actúa: un responsable y una hora límite", "Actúa, con un responsable"),
                   ("Confirma en la siguiente actualización", "Luego confirma")],
        "example": "Sneha hace la revisión en 10 minutos, al inicio de cada turno.",
        "example_cue": "Sneha la hace",
        "script": "Antes de saberlo, este es el hábito que lo detecta. Una gráfica solo ayuda si la revisas "
                  "igual cada día. Actualiza, registrando lo terminado y recalculando lo que falta. Compara "
                  "lo real con lo ideal. Explica la causa principal de cualquier brecha mala. Actúa, con un "
                  "responsable y una hora límite. Luego confirma, en la siguiente actualización, que la "
                  "línea vuelve a bajar. Sneha la hace en diez minutos, al inicio de cada turno. ¿Podrías "
                  "tú?",
    },
    {
        "key": "p11", "num": 11, "title": "La recuperación de Sneha",
        "points": [("Restricción: un probador RF parado", "Una estación de prueba RF"),
                   ("Segundo probador, personal prioritario", "Un técnico puso"),
                   ("Un solo responsable actualiza la gráfica", "Nombró a un responsable")],
        "example": "Viernes: cero routers pendientes, unas horas antes del camión.",
        "example_cue": "Para el viernes",
        "script": "Esto es lo que significaba la línea plana del miércoles. Una estación de prueba RF "
                  "estaba parada por calibración. Los routers se amontonaron frente a ella. Y nadie "
                  "actualizó la gráfica, porque no se nombró a nadie. Sneha arregló las dos cosas. Un "
                  "técnico puso en marcha un segundo probador, y la prueba recibió personal prioritario. "
                  "Nombró a un responsable para actualizar la gráfica a una hora fija. Para el viernes, la "
                  "línea tocó cero, unas horas antes del camión. ¿Dónde más podrías usar esto?",
    },
    {
        "key": "p12", "num": 12, "title": "Dónde usarla",
        "points": [("Un inicio claro, un final claro, una fecha límite", "siempre que el trabajo tenga"),
                   ("Producción: trabajo en proceso, recuperación", "Vacía el trabajo en proceso"),
                   ("Calidad: defectos críticos a cero", "Cierra cada defecto crítico"),
                   ("Acciones de mantenimiento y de Kaizen", "Termina las acciones de mantenimiento")],
        "example": "El equipo de calidad de Sneha ahora baja a cero los defectos abiertos antes del "
                   "embarque.",
        "example_cue": "El equipo de calidad de Sneha",
        "script": "Esta gráfica no es solo para producción. Úsala siempre que el trabajo tenga una cantidad "
                  "inicial clara, un final claro y una fecha límite. Vacía el trabajo en proceso antes de "
                  "un cambio de modelo. Recupera un faltante antes del corte de embarque. Cierra cada "
                  "defecto crítico antes del embarque. Termina las acciones de mantenimiento abiertas, o "
                  "las tareas de Kaizen, antes de una revisión. El equipo de calidad de Sneha ahora también "
                  "baja los defectos abiertos. ¿Qué tiene fecha límite en tu piso esta semana?",
    },
    {
        "key": "p13", "num": 13, "title": "Datos honestos",
        "points": [("Una unidad, una cantidad inicial congelada", "Usa una sola unidad"),
                   ("Define “completo” antes de empezar", "Define exactamente cuándo"),
                   ("Cuenta solo la producción buena", "cuenta solo la producción")],
        "example": "Routers esperando reprueba: no cuentan como completos.",
        "example_cue": "El jueves",
        "script": "Una gráfica es tan honesta como sus datos. Usa una sola unidad de medida de principio a "
                  "fin. Congela la cantidad inicial, a menos que se apruebe un cambio de alcance. Define "
                  "exactamente cuándo algo cuenta como completo. Y cuenta solo la producción que cumple "
                  "calidad. El jueves, el equipo de Sneha quería contar los routers que esperaban reprueba. "
                  "Ella dijo que no. Lo hecho a medias no está hecho, y una unidad que falló tampoco. ¿Tú "
                  "los habrías contado?",
    },
    {
        "key": "p14", "num": 14, "title": "Errores comunes",
        "points": [("Cambiar la cantidad inicial", "Cambiar la cantidad inicial"),
                   ("Actualizaciones tardías o irregulares", "Las actualizaciones tardías"),
                   ("Contar unidades parciales o rechazadas", "Contar trabajo parcial"),
                   ("Una gráfica sin acciones", "Una gráfica sin acciones")],
        "example": "Sneha anota los cambios de alcance aprobados en un recuadro aparte junto a su gráfica.",
        "example_cue": "Sneha anota los cambios",
        "script": "Cuidado con algunos errores comunes. Cambiar la cantidad inicial esconde la brecha "
                  "original. Las actualizaciones tardías hacen que reacciones cuando el retraso ya creció. "
                  "Contar trabajo parcial, o unidades rechazadas, hace que el avance se vea mejor de lo que "
                  "es. Y una gráfica sin acciones es solo un reporte. Sneha anota los cambios de alcance "
                  "aprobados en un recuadro aparte junto a su gráfica. La brecha original sigue visible. "
                  "¿Qué error has visto antes?",
    },
    {
        "key": "p15", "num": 15, "title": "Fortalezas, límites y lista de revisión",
        "points": [("Simple, rápida, una alerta temprana", "Esta gráfica es simple"),
                   ("No encuentra la causa raíz por sí sola", "no explica"),
                   ("Define, confirma, calcula, nombra un responsable", "esta es tu lista de revisión"),
                   ("Actualiza, actúa, cierra solo en cero", "Luego actualiza")],
        "example": "Sneha pega esta lista junto a cada gráfica nueva.",
        "example_cue": "Sneha pega esta lista",
        "script": "¿Y cuál es el veredicto? Esta gráfica es simple, rápida de leer, y te avisa antes de la "
                  "fecha límite. Pero no explica la causa raíz por sí sola. Y depende de actualizaciones "
                  "honestas y a tiempo. Así que esta es tu lista de revisión. Define el trabajo, y qué "
                  "significa completo. Confirma la cantidad inicial y la fecha. Calcula el ritmo ideal, y "
                  "nombra un responsable. Luego actualiza, actúa, y cierra solo en cero. Sneha pega esta "
                  "lista junto a cada gráfica nueva.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Trabajo pendiente", "icon": "stack", "with": 0},
        {"label": "Tiempo disponible", "icon": "clock", "with": 1},
        {"label": "Baja a cero", "icon": "chartDown", "tone": "good", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Solo una fecha límite", "sub": "Brecha encontrada el viernes", "icon": "calendar", "tone": "bad", "with": "example"},
        {"label": "Una gráfica de trabajo pendiente", "sub": "Brecha vista mientras es pequeña", "icon": "chartDown", "tone": "good", "with": 1}]},
    "p03": {"type": "icons", "items": [
        {"label": "Visible para todos", "icon": "search", "with": 0},
        {"label": "Real contra ritmo", "icon": "scale", "with": 1},
        {"label": "Alerta temprana", "icon": "warning", "with": 2},
        {"label": "Hechos, no sensaciones", "icon": "clipboard", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Trabajo pendiente", "sub": "Eje vertical", "icon": "stack", "with": 0},
        {"label": "Tiempo", "sub": "Eje horizontal", "icon": "calendar", "with": 0},
        {"label": "Línea ideal", "icon": "chartDown", "with": 1},
        {"label": "Línea real", "icon": "pin", "with": 2},
        {"label": "Brecha", "icon": "scale", "tone": "bad", "with": 3}]},
    "p05": {"type": "stat", "value": 1000, "icon": "box", "label": "routers en trabajo en proceso",
            "unit": "5 días hábiles para el camión", "with": 0},
    "p06": {"type": "bars", "label": "", "note": "Línea ideal: 200 routers menos cada día", "with": "example", "items": [
        {"label": "Día 0", "value": 1000, "with": "example"},
        {"label": "Día 1", "value": 800, "with": "example"},
        {"label": "Día 2", "value": 600, "with": "example"},
        {"label": "Día 3", "value": 400, "with": "example"},
        {"label": "Día 4", "value": 200, "with": "example"},
        {"label": "Día 5", "value": 0, "tone": "good", "with": "example"}]},
    "p07": {"type": "bars", "label": "", "note": "Routers pendientes, final del día 2: 80 atrás del plan", "items": [
        {"label": "Ideal", "value": 600, "tone": "good", "with": 1},
        {"label": "Real", "value": 680, "tone": "bad", "with": 1}]},
    "p08": {"type": "versus", "items": [
        {"label": "Arriba de la ideal", "sub": "Atrasado: busca la restricción", "icon": "chartUp", "tone": "bad", "with": 0},
        {"label": "Abajo de la ideal", "sub": "Adelantado: confirma la calidad", "icon": "chartDown", "tone": "good", "with": 1}]},
    "p09": {"type": "flow", "items": [
        {"label": "Línea plana", "sub": "Nada se cerró", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "¿Paro? ¿Responsable? ¿Datos?", "icon": "search", "with": 1},
        {"label": "En cero: verifica, cierra", "icon": "check", "tone": "good", "with": 2}]},
    "p10": {"type": "steps", "items": [
        {"label": "Actualiza", "with": 0}, {"label": "Compara", "with": 0},
        {"label": "Explica", "with": 1}, {"label": "Actúa", "with": 2},
        {"label": "Confirma", "with": 3}]},
    "p11": {"type": "flow", "items": [
        {"label": "Probador RF parado", "icon": "test", "tone": "bad", "with": 0},
        {"label": "Segundo probador en marcha", "icon": "wrench", "with": 1},
        {"label": "Un responsable de la gráfica", "icon": "person", "with": 2}],
        "then": {"type": "stat", "value": 0, "icon": "check", "label": "routers pendientes el viernes",
                 "unit": "unas horas antes del camión", "with": "example"}},
    "p12": {"type": "icons", "items": [
        {"label": "Trabajo en proceso", "icon": "box", "with": 1},
        {"label": "Recuperar faltantes", "icon": "chartUp", "with": 1},
        {"label": "Defectos críticos", "icon": "warning", "with": 2},
        {"label": "Mantenimiento, Kaizen", "icon": "wrench", "with": 3}]},
    "p13": {"type": "icons", "items": [
        {"label": "Una unidad, inicio congelado", "icon": "lock", "with": 0},
        {"label": "“Completo” definido", "icon": "clipboard", "with": 1},
        {"label": "Solo producción buena", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Esperando reprueba", "sub": "No completo", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Aprobado y empacado", "sub": "Cuenta", "icon": "check", "tone": "good", "with": "example"}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Cantidad inicial movida", "icon": "stack", "tone": "bad", "with": 0},
        {"label": "Actualizaciones tardías", "icon": "clock", "tone": "bad", "with": 1},
        {"label": "Parcial o rechazado", "icon": "trash", "tone": "bad", "with": 2},
        {"label": "Sin acciones", "icon": "cross", "tone": "bad", "with": 3}]},
    "p15": {"type": "doc", "items": [
        {"label": "Define el trabajo y “completo”", "icon": "clipboard", "with": 2},
        {"label": "Confirma la cantidad inicial y la fecha", "icon": "calendar", "with": 2},
        {"label": "Ritmo ideal, un responsable", "icon": "person", "with": 2},
        {"label": "Actualiza, actúa, cierra solo en cero", "icon": "check", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Hay que sacar 800 unidades en 4 días. Después del día 2, hay 340 hechas. ¿Dónde está el "
                    "equipo?",
        "options": ["60 unidades adelante del plan", "60 unidades atrás del plan", "Exactamente en el plan"],
        "correct": 1,
        "explanation": "Pendiente ideal en el día 2 = 800 − 2 × 200 = 400. Pendiente real = 800 − 340 = 460. 460 "
                       "− 400 = 60 atrás del plan.",
        "q_script": "Prueba rápida. Hay que sacar ochocientas unidades en cuatro días. Después del día dos, "
                    "hay trescientas cuarenta hechas. ¿Dónde está el equipo? Tómate unos segundos.",
        "a_script": "Van sesenta unidades atrás. Deberían quedar cuatrocientas, pero todavía quedan "
                    "cuatrocientas sesenta. La línea real está arriba de la ideal.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Una gráfica de defectos pendientes lleva dos días plana. ¿Qué debe revisar primero el "
                    "equipo?",
        "options": ["Nada: una línea plana significa que todo está estable",
                    "Si el trabajo se detuvo, quién es el responsable, y si los datos se actualizaron",
                    "Redibujar la línea ideal para que coincida con la realidad"],
        "correct": 1,
        "explanation": "Una línea plana significa que nada se cerró. Revisa si hay un paro, el responsable y los "
                       "datos. Redibujar la línea ideal solo esconde la brecha.",
        "q_script": "Una más, y esta es un escenario. Una gráfica de defectos pendientes lleva dos días "
                    "plana. ¿Qué debe revisar primero el equipo? Piénsalo.",
        "a_script": "Revisa si el trabajo se detuvo, quién es el responsable, y si alguien actualizó los "
                    "datos. Redibujar la línea ideal solo escondería la brecha.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
