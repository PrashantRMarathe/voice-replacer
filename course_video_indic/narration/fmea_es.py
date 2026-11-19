"""fmea in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh fmea_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "fm_es"
NAME = "fmea_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Gemba": "Guemba",
    "FMEA": "efe eme e a",
    "RPN": "erre pe ene",
    "SOP": "ese o pe",
    "5G": "cinco ge",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Seis unidades de radio para exteriores regresaron del campo, llenas de agua. En dos, "
    "faltaba el empaque. En cuatro, estaba torcido. Todas habían pasado la inspección final. "
    "¿Te suena familiar? En esta lección aprenderás FMEA, el análisis de modos de falla y sus "
    "efectos. Verás cómo encontrar riesgos antes de que lleguen a un cliente, y atacar "
    "primero los más grandes. Seguiremos a Asha, ingeniera de calidad en una planta de "
    "telecomunicaciones."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Construye una cadena clara, del efecto al modo de falla y a "
    "una causa que puedas controlar. Califica con evidencia, y nunca dejes que el número "
    "reemplace al criterio. Y prefiere la prevención, luego comprueba que funciona antes de "
    "volver a calificar. Esta es tu acción para esta semana. Elige un paso crítico, y escribe "
    "su cadena de falla con tu equipo. Excelente trabajo al completar esta lección. Ahora "
    "aprenderás Gemba, el lugar real."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es el FMEA",
        "points": [("¿Cómo podría fallar, y por qué?", "Pregunta cómo"),
                   ("¿Cuál sería el efecto?", "cuál sería el efecto"),
                   ("Actúa antes de que llegue al cliente", "Luego actúas")],
        "example": "El objetivo de Asha: el empaque de la carcasa de una celda pequeña 5G para exteriores.",
        "example_cue": "El objetivo de Asha",
        "script": "El FMEA es un método de equipo para pensar antes de que la falla ocurra. Pregunta cómo "
                  "podría fallar un producto o un proceso, y por qué. Pregunta cuál sería el efecto, y qué "
                  "controles tienes hoy. Luego actúas, antes de que la falla llegue a tu cliente. Eso es "
                  "calidad integrada, no inspección. El objetivo de Asha era el empaque de la carcasa de "
                  "una celda pequeña 5G para exteriores. ¿Y qué palabras necesitas?",
    },
    {
        "key": "p02", "num": 2, "title": "Las palabras clave",
        "points": [("Modo de falla: cómo falla", "Un modo de falla"),
                   ("Efecto: lo que sufre el cliente", "El efecto"),
                   ("Causa: por qué podría pasar", "La causa"),
                   ("Control y acción", "Un control")],
        "example": "Modo: empaque torcido. Efecto: agua adentro. Causa: no se revisa el asentado.",
        "example_cue": "Para Asha",
        "script": "Aprende cinco palabras. Un modo de falla es cómo falla el requisito. El efecto es lo que "
                  "le pasa al siguiente proceso, o al cliente. La causa es por qué podría pasar. Un control "
                  "previene la causa, o detecta la falla. Y una acción reduce el riesgo. Para Asha, el modo "
                  "era un empaque torcido. El efecto era agua adentro. ¿Adivinas la causa?",
    },
    {
        "key": "p03", "num": 3, "title": "Tipos de FMEA",
        "points": [("FMEA de sistema y de diseño", "Los de sistema y de diseño"),
                   ("FMEA de proceso: pasos de manufactura", "Un FMEA de proceso"),
                   ("Límites claros de inicio y fin", "Fija límites claros")],
        "example": "El alcance de Asha: de tomar el empaque a la carcasa sellada y probada.",
        "example_cue": "El alcance de Asha",
        "script": "Hay varios tipos. Los de sistema y de diseño, o FMEA de sistema y FMEA de diseño, "
                  "revisan el producto y cómo trabajan juntas sus partes. El de maquinaria revisa el "
                  "equipo. Un FMEA de proceso revisa tus pasos de manufactura, y es el que usan la mayoría "
                  "de los equipos Lean. Fija límites claros, para que el trabajo sea manejable. El alcance "
                  "de Asha iba de tomar el empaque, a una carcasa sellada y probada. ¿Cuándo debes hacer "
                  "uno?",
    },
    {
        "key": "p04", "num": 4, "title": "Cuándo empezar o actualizar",
        "points": [("Producto o proceso nuevo", "un producto nuevo"),
                   ("Cualquier cambio: material, herramental, acomodo", "cualquier cambio"),
                   ("Después de una queja o una fuga", "después de una queja")],
        "example": "Asha actualizó el suyo el mismo día que regresaron los seis radios mojados.",
        "example_cue": "Asha actualizó",
        "script": "Empieza uno para un producto nuevo o un proceso nuevo. Actualízalo después de cualquier "
                  "cambio. Eso incluye material, equipo, software, herramental, acomodo o método. Y "
                  "actualízalo después de una queja, o cuando sepas que un control no funciona. Un FMEA de "
                  "hace dos años describe una fábrica que ya no existe. Asha actualizó el suyo el día que "
                  "regresaron los radios mojados. ¿Quién lo construye?",
    },
    {
        "key": "p05", "num": 5, "title": "El equipo y la información",
        "points": [("Un equipo de varias áreas", "Trae a producción"),
                   ("Operadores con experiencia", "Incluye operadores con experiencia"),
                   ("Diagrama de flujo, datos, instrucciones de trabajo", "Trae también la información"),
                   ("Visita el Gemba antes de calificar", "ve al Gemba")],
        "example": "En el Gemba, Asha vio dos tamaños de empaque compartiendo un mismo contenedor.",
        "example_cue": "En el Gemba",
        "script": "Trae a producción, ingeniería, calidad, mantenimiento y pruebas. Incluye operadores con "
                  "experiencia que conocen el trabajo real. Trae también la información. Un flujo del "
                  "proceso, datos de defectos, instrucciones de trabajo y lecciones aprendidas. Luego ve al "
                  "Gemba antes de calificar nada. Compara el método escrito con lo que de verdad pasa. En "
                  "el Gemba, Asha vio dos tamaños de empaque compartiendo un mismo contenedor. ¿Qué "
                  "anotarías tú?",
    },
    {
        "key": "p06", "num": 6, "title": "Los siete pasos",
        "points": [("Planear, estructura, función", "Planea el alcance"),
                   ("Análisis de fallas", "analiza las fallas"),
                   ("Análisis de riesgos", "califica el riesgo"),
                   ("Optimizar y documentar", "toma acción")],
        "example": "El equipo de Asha: un requisito y una cadena de falla a la vez.",
        "example_cue": "El equipo de Asha",
        "script": "El método tiene siete pasos. Planea el alcance, mapea la estructura, y escribe lo que "
                  "cada paso debe lograr. Luego analiza las fallas, y califica el riesgo. Por último, toma "
                  "acción, y documenta lo que cambió. Una regla simple mantiene cuerdas las juntas. El "
                  "equipo de Asha trabajó un requisito y una cadena de falla a la vez. ¿Y cómo se ve un "
                  "buen requisito?",
    },
    {
        "key": "p07", "num": 7, "title": "Escribir funciones claras",
        "points": [("Un verbo de acción más un requisito", "un verbo, más"),
                   ("Medible, no vago", "medible")],
        "example": "Débil: “Poner empaque.” Fuerte: “Colocar el empaque correcto completo en la ranura, sin "
                   "torcer ni dañar.”",
        "example_cue": "Compara estas",
        "script": "Escribe cada función como un verbo, más un requisito que puedas revisar. Hazla medible, "
                  "no vaga. Ensamblar correctamente no le dice nada a nadie. Compara estas. Poner empaque. "
                  "O, colocar el empaque correcto completo en la ranura, sin torcer ni dañar. La segunda te "
                  "dice exactamente cómo puede fallar. Faltante, de tamaño equivocado, mal asentado, o "
                  "torcido. ¿Puedes reescribir así uno de tus propios pasos?",
    },
    {
        "key": "p08", "num": 8, "title": "La cadena de falla",
        "points": [("Efecto: entrada de agua, falla en campo", "El efecto es"),
                   ("Modo: empaque faltante o torcido", "El modo de falla es"),
                   ("Causa: algo que puedas controlar", "La causa debe")],
        "example": "Causa: dos tamaños de empaque en un contenedor, y nadie revisa que esté asentado.",
        "example_cue": "Las causas de Asha eran",
        "script": "Ahora une la cadena. El efecto es la entrada de agua, y un radio que falla en un poste. "
                  "El modo de falla es un empaque faltante, o torcido. La causa debe ser algo que de verdad "
                  "puedas controlar. Nunca escribas descuido ni error humano. Las causas de Asha eran "
                  "específicas. Dos tamaños de empaque compartían un contenedor. Y nada revisaba que el "
                  "empaque estuviera asentado. Ahora puedes diseñar una solución. ¿Pero qué riesgo va "
                  "primero?",
    },
    {
        "key": "p09", "num": 9, "title": "Severidad, ocurrencia, detección",
        "points": [("Severidad: qué tan malo es el efecto", "La severidad califica"),
                   ("Ocurrencia: qué tan seguido pasa la causa", "La ocurrencia califica"),
                   ("Detección: qué tan probable es atraparlo", "La detección califica"),
                   ("Cada calificación necesita evidencia", "Respalda cada calificación")],
        "example": "Riesgo del empaque: severidad 8, ocurrencia 5, detección 6.",
        "example_cue": "El equipo de Asha calificó",
        "script": "Calificas tres cosas, normalmente del uno al diez. La severidad califica qué tan malo es "
                  "el efecto. La ocurrencia califica qué tan seguido pasa la causa, con la prevención de "
                  "hoy. La detección califica qué tan probable es que lo atrapes antes de que se escape. "
                  "Aquí, diez significa que probablemente no lo atraparás. Respalda cada calificación con "
                  "datos, no con sensaciones. El equipo de Asha calificó el empaque con ocho, cinco y seis. "
                  "¿Cuánto da eso?",
    },
    {
        "key": "p10", "num": 10, "title": "Número de prioridad de riesgo",
        "points": [("RPN = severidad × ocurrencia × detección", "El número de prioridad de riesgo"),
                   ("8 × 5 × 6 = 240", "Son doscientos"),
                   ("Una guía, no un veredicto", "Pero tómalo")],
        "example": "RPN del empaque: 240, el más alto de la hoja de Asha.",
        "example_cue": "Fue el número más alto",
        "script": "El número de prioridad de riesgo multiplica las tres calificaciones. Para el empaque, "
                  "ocho por cinco por seis. Son doscientos cuarenta. Fue el número más alto de la hoja de "
                  "Asha. Pero tómalo como una guía, no como un veredicto. Calificaciones distintas pueden "
                  "dar el mismo RPN. Y los equipos pueden caer en la tentación de mover las calificaciones "
                  "para pasar un límite. ¿Y qué más debes mirar?",
    },
    {
        "key": "p11", "num": 11, "title": "La severidad va primero",
        "points": [("Una severidad alta necesita acción de todos modos", "una severidad alta"),
                   ("Prioridad de acción alta, media, baja", "Muchos equipos ahora usan"),
                   ("Pregunta: ¿qué es débil, la prevención o la detección?", "Y pregunta siempre")],
        "example": "Un riesgo de seguridad con RPN de 90 puede importar más que uno cosmético de 200.",
        "example_cue": "Un riesgo de seguridad",
        "script": "Mira primero la severidad. Una severidad alta necesita acción, aunque su RPN se vea "
                  "moderado. Muchos equipos ahora usan la prioridad de acción, calificada como alta, media "
                  "o baja. Alta significa actuar, o explicar formalmente por qué no puedes. Y pregunta "
                  "siempre qué control es débil, la prevención o la detección. Un riesgo de seguridad que "
                  "califica noventa puede importar más que uno cosmético que califica doscientos. ¿Estás de "
                  "acuerdo?",
    },
    {
        "key": "p12", "num": 12, "title": "Prevención contra detección",
        "points": [("Prevención: evitar que ocurra la causa", "Los controles de prevención"),
                   ("Detección: atraparlo antes de liberar", "Los controles de detección"),
                   ("Lo automático le gana al criterio humano", "lo automático le gana")],
        "example": "El único control de Asha: una revisión visual final. Detección, y débil.",
        "example_cue": "El único control de Asha",
        "script": "Conoce qué tipo de control tienes. Los controles de prevención evitan que ocurra la "
                  "causa, como una pieza con guía o un bloqueo de receta. Los controles de detección "
                  "atrapan la falla antes de liberar, como un sensor o una prueba. Pregunta si cada uno "
                  "revisa todas las unidades, y si se puede brincar. Y lo automático le gana al criterio "
                  "humano, casi siempre. El único control de Asha era una revisión visual final. Detección, "
                  "y débil. ¿Qué agregarías?",
    },
    {
        "key": "p13", "num": 13, "title": "Elegir acciones fuertes",
        "points": [("Eliminar la causa", "Primero, elimina"),
                   ("Prevenirla: bloqueo, guía, interbloqueo", "Después, previene"),
                   ("Mejorar la detección", "Luego mejora la detección"),
                   ("Entrenamiento y listas al final", "El entrenamiento y las listas")],
        "example": "Las acciones de Asha: un empaque por charola con guía, un fixture para la ranura, un "
                   "sensor de presencia y una prueba de fugas.",
        "example_cue": "Asha eligió",
        "script": "Algunas acciones son más fuertes que otras. Primero, elimina la causa por diseño, si "
                  "puedes. Después, previene, con un bloqueo, una guía o un interbloqueo. Luego reduce la "
                  "variación. Luego mejora la detección con una revisión automática. El entrenamiento y las "
                  "listas van al final, cuando no hay nada más fuerte. Asha eligió una charola con guía "
                  "para un solo tamaño de empaque, un fixture para la ranura, un sensor de presencia, y una "
                  "prueba de fugas. ¿Funcionó?",
    },
    {
        "key": "p14", "num": 14, "title": "Verificar, luego recalificar",
        "points": [("Compruébalo en condiciones reales", "Comprueba que funciona"),
                   ("La severidad se queda en 8: mismo efecto", "La severidad se quedó"),
                   ("Ocurrencia 5 → 2, detección 6 → 2", "La ocurrencia bajó"),
                   ("RPN 240 → 32", "El RPN bajó")],
        "example": "Primero la prueba: el sensor atrapó cada muestra mala en una prueba de 500 unidades.",
        "example_cue": "La prueba de Asha",
        "script": "Nunca vuelvas a calificar solo porque compraste un sensor. Primero comprueba que "
                  "funciona en condiciones reales. La prueba de Asha vino de una corrida de quinientas "
                  "unidades. El sensor atrapó cada muestra mala. La severidad se quedó en ocho, porque el "
                  "agua adentro sigue siendo igual de mala. La ocurrencia bajó a dos, y la detección bajó a "
                  "dos. El RPN bajó de doscientos cuarenta a treinta y dos. ¿Ya terminó el trabajo?",
    },
    {
        "key": "p15", "num": 15, "title": "Mantenerlo vivo",
        "points": [("Actualiza el plan de control, el SOP, el entrenamiento", "Actualiza el plan de control, el SOP"),
                   ("Revisa los riesgos altos cada semana", "Revisa los riesgos altos abiertos"),
                   ("Copia las lecciones a productos parecidos", "Copia lo que aprendiste")],
        "example": "El equipo de Asha copió la charola con guía a otras dos unidades para exteriores.",
        "example_cue": "El equipo de Asha copió",
        "script": "No del todo. Un FMEA es un documento vivo, no un formato para archivar. Actualiza el "
                  "plan de control, el SOP, el entrenamiento y las auditorías. Revisa los riesgos altos "
                  "abiertos cada semana, y toda la hoja después de cualquier queja. Copia lo que aprendiste "
                  "a productos parecidos. El equipo de Asha copió la charola con guía a otras dos unidades "
                  "para exteriores. Y ningún radio mojado ha regresado desde entonces. ¿Dónde empezarás el "
                  "tuyo?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "¿Cómo podría fallar?", "icon": "search", "with": 0},
        {"label": "¿Cuál es el efecto?", "icon": "warning", "with": 1},
        {"label": "Actúa primero", "icon": "shield", "tone": "good", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Modo de falla", "sub": "Cómo falla", "icon": "cross", "with": 0},
        {"label": "Efecto", "sub": "Lo que causa", "icon": "warning", "with": 1},
        {"label": "Causa", "sub": "Por qué pasa", "icon": "search", "with": 2},
        {"label": "Control, acción", "sub": "Lo que lo detiene", "icon": "shield", "tone": "good", "with": 3}]},
    "p03": {"type": "icons", "items": [
        {"label": "Sistema", "icon": "stack", "with": 0},
        {"label": "Diseño", "icon": "shape", "with": 0},
        {"label": "Proceso", "icon": "sequence", "tone": "good", "with": 1},
        {"label": "Límites", "icon": "pin", "with": 2}]},
    "p04": {"type": "icons", "items": [
        {"label": "Producto o proceso nuevo", "icon": "box", "with": 0},
        {"label": "Cualquier cambio", "icon": "gear", "with": 1},
        {"label": "Queja o fuga", "icon": "warning", "tone": "bad", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "De varias áreas", "icon": "person", "with": 0},
        {"label": "Operadores", "icon": "hand", "with": 1},
        {"label": "Datos y flujo", "icon": "clipboard", "with": 2},
        {"label": "Primero el Gemba", "icon": "walk", "tone": "good", "with": 3}]},
    "p06": {"type": "steps", "items": [
        {"label": "Planear", "with": 0}, {"label": "Estructura", "with": 0},
        {"label": "Función", "with": 0}, {"label": "Falla", "with": 1},
        {"label": "Riesgo", "with": 2}, {"label": "Optimizar", "with": 3},
        {"label": "Documentar", "with": 3}]},
    "p07": {"type": "versus", "items": [
        {"label": "“Poner empaque”", "sub": "Vago", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "“Empaque correcto, bien asentado, sin torcer”", "sub": "Medible", "icon": "check", "tone": "good", "with": "example"}]},
    "p08": {"type": "flow", "items": [
        {"label": "Efecto", "sub": "Entrada de agua", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Modo de falla", "sub": "Faltante o torcido", "icon": "cross", "tone": "bad", "with": 1},
        {"label": "Causa", "sub": "Contenedor mezclado, sin revisión de asentado", "icon": "search", "with": "example"}]},
    "p09": {"type": "bars", "label": "", "note": "Severidad · Ocurrencia · Detección, del 1 al 10", "with": "example", "items": [
        {"label": "Sev.", "value": 8, "tone": "bad", "with": "example"},
        {"label": "Ocu.", "value": 5, "with": "example"},
        {"label": "Det.", "value": 6, "with": "example"}]},
    "p10": {"type": "stat", "value": 240, "icon": "warning", "label": "RPN del empaque",
            "unit": "8 × 5 × 6", "with": 1},
    "p11": {"type": "ladder", "top": "ALTA", "bottom": "BAJA", "items": [
        {"label": "Actúa, o justifica por qué no", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Revisa y mejora", "icon": "search", "with": 1},
        {"label": "Mantén y vigila", "icon": "check", "tone": "good", "with": 1}]},
    "p12": {"type": "versus", "items": [
        {"label": "Detección", "sub": "Revisión visual final", "icon": "search", "with": 1},
        {"label": "Prevención", "sub": "Evita la causa", "icon": "key", "tone": "good", "with": 0}]},
    "p13": {"type": "ladder", "top": "LO MÁS FUERTE", "bottom": "LO MÁS DÉBIL", "items": [
        {"label": "Eliminar por diseño", "icon": "shape", "with": 0},
        {"label": "Prevenir: guía, bloqueo", "icon": "key", "with": 1},
        {"label": "Detectar en automático", "icon": "sensor", "with": 2},
        {"label": "Entrenar, lista", "icon": "clipboard", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Antes", "value": 240}, "after": {"label": "Después", "value": 32},
            "unit": "RPN del empaque", "note": "Ocurrencia 5 → 2 · Detección 6 → 2", "with": 3},
    "p15": {"type": "flow", "items": [
        {"label": "Plan de control, SOP", "icon": "clipboard", "with": 0},
        {"label": "Revisión semanal de riesgos", "icon": "calendar", "with": 1},
        {"label": "Copiar a unidades parecidas", "icon": "sequence", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "¿Cuál es una causa útil para un FMEA?",
        "options": ["Descuido del operador",
                    "Dos tamaños de empaque comparten un contenedor en la estación",
                    "Entra agua al radio"],
        "correct": 1,
        "explanation": "Una causa útil es una condición específica que puedes controlar. El descuido es culpa, y "
                       "el agua adentro es el efecto.",
        "q_script": "Prueba rápida. ¿Cuál de estas es una causa útil, para un FMEA? Tómate unos segundos.",
        "a_script": "Es la segunda. Es una condición específica que puedes controlar. El descuido es solo "
                    "culpa, y el agua adentro es el efecto.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Después de agregar un sensor y una prueba de fugas, el equipo quiere bajar la severidad "
                    "de 8 a 4. ¿Es correcto?",
        "options": ["Sí: el riesgo ahora es menor",
                    "No: la severidad cambia solo si cambia el efecto",
                    "Sí, si el RPN se queda abajo de 100"],
        "correct": 1,
        "explanation": "La severidad califica el efecto. El agua dentro de un radio es igual de mala que antes. "
                       "Los controles nuevos bajan la ocurrencia y la detección, no la severidad.",
        "q_script": "Una más, y esta es un escenario. Después de agregar un sensor y una prueba de fugas, el "
                    "equipo quiere bajar la severidad de ocho a cuatro. ¿Es correcto? Piénsalo.",
        "a_script": "No. La severidad califica el efecto, y el agua adentro es igual de mala que antes. Los "
                    "controles nuevos bajan la ocurrencia y la detección.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
