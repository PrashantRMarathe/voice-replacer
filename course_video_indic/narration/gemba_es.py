"""gemba in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh gemba_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "gb_es"
NAME = "gemba_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Genbutsu": "Guenbutsu",
    "Genjitsu": "Guenyitsu",
    "Hancho": "Jancho",
    "Gemba": "Guemba",
    "PPE": "pe pe e",
    "ESD": "e ese de",
    "3G": "tres ge",
    "G": "ge",
    "A": "a",
    "B": "be",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "El tablero decía que el turno B era descuidado. El doble de audífonos fallaba la prueba "
    "de audio que en el turno A. El plan era simple. Volver a entrenar al turno B. Nadie "
    "había visto un solo audífono con falla. ¿Te suena familiar? En esta lección aprenderás "
    "Gemba, y las 3G detrás de él. Verás cómo ir al lugar real, examinar la cosa real, y "
    "revisar los hechos reales. Seguiremos a Manoj, supervisor de producción en una línea de "
    "audífonos inalámbricos."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Ve al lugar real, y observa ciclos reales antes de decidir. "
    "Toma la cosa real en la mano, y compárala con una buena. Y revisa los hechos reales, con "
    "conteos, tiempos y un denominador. Esta es tu acción para esta semana. Toma un problema "
    "que se repite, y haz una visita 3G de treinta minutos. Excelente trabajo al completar "
    "esta lección. Ahora aprenderás Hancho, el liderazgo en el piso de producción."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ir a ver",
        "points": [("Gemba: el lugar real", "Gemba significa"),
                   ("Genbutsu: la cosa real", "Genbutsu significa"),
                   ("Genjitsu: los hechos reales", "Genjitsu significa")],
        "example": "La regla de Manoj: ninguna decisión sobre el turno B hasta tener en la mano un audífono "
                   "con falla.",
        "example_cue": "Manoj puso una regla",
        "script": "Lean tiene un hábito simple. Ve a ver, antes de decidir. Viene en tres palabras "
                  "japonesas, que muchos llaman las 3G. Gemba significa el lugar real, donde pasa el "
                  "trabajo. Genbutsu significa la cosa real, como la pieza con falla. Genjitsu significa "
                  "los hechos reales. Manoj puso una regla. Ninguna decisión sobre el turno B, hasta tener "
                  "en la mano un audífono con falla. ¿Por qué importa eso?",
    },
    {
        "key": "p02", "num": 2, "title": "Por qué los reportes no bastan",
        "points": [("Los tableros muestran síntomas", "Los tableros muestran"),
                   ("Los reportes esconden el contexto", "Los reportes esconden"),
                   ("Los hechos detienen la culpa", "Y los hechos detienen")],
        "example": "El tablero mostraba las fallas del turno B. No mostraba por qué.",
        "example_cue": "El tablero de Manoj",
        "script": "Porque los reportes solo cuentan parte de la historia. Los tableros muestran síntomas, "
                  "no causas. Los reportes esconden la secuencia, los atajos y el contexto. Una pieza, un "
                  "fixture o una estación muchas veces muestran evidencia que ninguna hoja de cálculo "
                  "puede. Y los hechos detienen la culpa, y el dinero gastado en la solución equivocada. El "
                  "tablero de Manoj mostraba que el turno B fallaba más. No podía mostrar por qué. ¿Y por "
                  "dónde empiezas?",
    },
    {
        "key": "p03", "num": 3, "title": "Las 3G en una vista",
        "points": [("¿Dónde pasó?", "Gemba pregunta"),
                   ("¿Qué se afectó exactamente?", "Genbutsu pregunta"),
                   ("¿Qué ocurrió de verdad?", "Genjitsu pregunta")],
        "example": "Línea 2 · prueba de audio · audífono izquierdo · 22 de 1,100 en el turno B",
        "example_cue": "Para Manoj",
        "script": "Piensa en cada G como una pregunta. Gemba pregunta, ¿dónde pasó? La línea, la estación, "
                  "el paso. Genbutsu pregunta, ¿qué se afectó exactamente? La unidad, la pieza, la "
                  "herramienta. Genjitsu pregunta, ¿qué ocurrió de verdad? Tiempos, conteos y mediciones. "
                  "Para Manoj, era la línea dos, la prueba de audio, y el audífono izquierdo. Veintidós "
                  "fallas de mil cien, en el turno B. Así que vamos al lugar.",
    },
    {
        "key": "p04", "num": 4, "title": "Gemba: el lugar real",
        "points": [("Ten una pregunta clara", "Empieza con una pregunta clara"),
                   ("Avisa al dueño del área, usa el PPE", "Avisa al dueño del área"),
                   ("Observa varios ciclos completos", "Observa varios"),
                   ("Compara con el estándar", "Compara lo que ves")],
        "example": "La pregunta de Manoj: ¿qué es distinto en la prueba de audio del turno B?",
        "example_cue": "La pregunta de Manoj",
        "script": "Empieza con una pregunta clara, y un proceso objetivo. Avisa al dueño del área que vas a "
                  "ir, y sigue las reglas de PPE y ESD. Observa varios ciclos completos, sin interferir. "
                  "Compara lo que ves con el trabajo estándar aprobado. Luego haz preguntas neutrales, y "
                  "anota cualquier brecha con su hora y lugar. La pregunta de Manoj era corta. ¿Qué es "
                  "distinto en la prueba de audio del turno B? ¿Cómo debes comportarte ahí?",
    },
    {
        "key": "p05", "num": 5, "title": "Modales en el Gemba",
        "points": [("No es una inspección sorpresa", "no es una inspección sorpresa"),
                   ("Escucha antes de sugerir", "Escucha antes"),
                   ("Nunca juzgues por un solo ciclo", "nunca juzgues")],
        "example": "Manoj se quedó una hora completa del turno B, y preguntó: “¿Qué hace difícil este "
                   "trabajo?”",
        "example_cue": "Manoj se quedó una hora completa en el turno B",
        "script": "Una visita al Gemba no es una inspección sorpresa, ni una búsqueda de a quién culpar. "
                  "Escucha antes de sugerir nada. No interrumpas el trabajo crítico. Y nunca juzgues por un "
                  "solo ciclo, porque un ciclo te puede engañar. Manoj se quedó una hora completa en el "
                  "turno B. Hizo una pregunta. ¿Qué te hace difícil este trabajo? Las respuestas lo "
                  "sorprendieron. ¿Pero qué debes tomar en la mano?",
    },
    {
        "key": "p06", "num": 6, "title": "Genbutsu: la cosa real",
        "points": [("La unidad con falla, la pieza, la herramienta", "Eso significa la unidad con falla"),
                   ("Anota modelo, lote, hora, estación", "Anota el modelo"),
                   ("Compara lo malo con lo bueno", "Compara una unidad mala")],
        "example": "Audífonos izquierdos con falla: soldadura opaca y granulosa en el cable de la bocina. "
                   "Los buenos: brillante y lisa.",
        "example_cue": "Manoj comparó",
        "script": "Toma la cosa real en la mano. Eso significa la unidad con falla, el componente, el "
                  "fixture o la herramienta. Anota el modelo, el lote, la hora y la estación antes de "
                  "tocarla. Inspecciónala sin cambiar la evidencia. Compara una unidad mala con una buena, "
                  "lado a lado, bajo la misma luz. Manoj comparó audífonos izquierdos con falla con unos "
                  "buenos. Las uniones de soldadura con falla se veían opacas y granulosas. ¿Qué podría "
                  "causar eso?",
    },
    {
        "key": "p07", "num": 7, "title": "La seguridad va primero",
        "points": [("Nunca brinques un interbloqueo", "Nunca brinques"),
                   ("Bloqueo antes de abrir un equipo", "Bloquea primero"),
                   ("Manejo ESD para electrónica", "maneja la electrónica")],
        "example": "Manoj le pidió al técnico enfriar y bloquear el cautín antes de revisarlo.",
        "example_cue": "Manoj le pidió",
        "script": "Una regla le gana a la curiosidad. Nunca brinques un interbloqueo, ni abras un equipo "
                  "energizado, solo para ver la cosa real. Bloquea primero, y deja que lo haga una persona "
                  "calificada. Maneja la electrónica con protección ESD, o crearás defectos nuevos mientras "
                  "investigas. Manoj le pidió al técnico enfriar y bloquear la estación de soldadura antes "
                  "de revisarla. La evidencia segura es buena evidencia. ¿Y los hechos?",
    },
    {
        "key": "p08", "num": 8, "title": "Genjitsu: los hechos reales",
        "points": [("Hechos, no opiniones", "Cambia las opiniones"),
                   ("Conteos con un denominador", "Usa conteos"),
                   ("Una señal no es una prueba", "es una señal")],
        "example": "Turno B: 22 de 1,100 (2.0%). Turno A: 9 de 1,050 (0.9%).",
        "example_cue": "El turno B tuvo",
        "script": "Cambia las opiniones por hechos. La prueba es lenta es una opinión. La mediana del "
                  "tiempo de prueba subió de cuarenta y seis a sesenta y un segundos es un hecho. Usa "
                  "conteos con un denominador, y horas en las que puedas confiar. El turno B tuvo veintidós "
                  "fallas de mil cien. El turno A tuvo nueve de unas mil. Esa diferencia es una señal para "
                  "investigar. ¿Pero prueba que el turno B la causó?",
    },
    {
        "key": "p09", "num": 9, "title": "Una investigación conectada",
        "points": [("Primero define y contén", "Define el problema"),
                   ("Lugar, cosa, hechos, juntos", "ve al lugar"),
                   ("Prueba las causas antes de corregir", "Luego prueba")],
        "example": "Manoj retuvo los audífonos sospechosos del turno B antes que nada.",
        "example_cue": "Manoj retuvo",
        "script": "No. Así que usa las 3G como una sola investigación conectada, no como tres casillas para "
                  "marcar. Define el problema en números, y protege primero a tu cliente. Luego ve al "
                  "lugar, inspecciona la cosa, y reúne los hechos, juntos. Luego prueba las posibles "
                  "causas, antes de cambiar nada de forma permanente. Manoj retuvo primero todos los "
                  "audífonos sospechosos del turno B. Luego regresó a la estación. ¿Qué le mostró el lugar?",
    },
    {
        "key": "p10", "num": 10, "title": "Lo que mostró el lugar",
        "points": [("Misma gente, mismo método", "seguía el mismo método"),
                   ("Una punta de cautín distinta", "la punta del cautín"),
                   ("Cambiada el lunes en la noche", "cambiado el lunes")],
        "example": "El cautín del turno B tenía una punta más chica del almacén de refacciones. No la "
                   "estándar.",
        "example_cue": "Había salido",
        "script": "Al principio, nada se veía mal. El turno B seguía el mismo método que el turno A, paso a "
                  "paso. Luego Manoj miró de cerca la punta del cautín. Era más chica que la de la estación "
                  "del turno A. La habían cambiado el lunes en la noche. Había salido del almacén de "
                  "refacciones, y no era la punta estándar. ¿Una punta más chica podría hacer una unión más "
                  "débil? ¿Cómo lo averiguarías?",
    },
    {
        "key": "p11", "num": 11, "title": "Lo que mostraron los hechos",
        "points": [("Fallas por estación y hora", "Manoj mapeó"),
                   ("Empezaron justo después del cambio de punta", "empezaron el turno"),
                   ("Una prueba controlada lo confirmó", "Luego una prueba controlada")],
        "example": "Prueba: punta estándar 1 falla de 300. Punta más chica: 7 de 300.",
        "example_cue": "Con la punta estándar",
        "script": "Manoj mapeó cada falla por estación, hora y lote. Empezaron el turno después del cambio "
                  "de punta, y solo en esa estación. Luego una prueba controlada, aprobada por ingeniería, "
                  "probó las dos puntas. Con la punta estándar, falló un audífono de trescientos. Con la "
                  "punta más chica, fallaron siete. La punta más chica no podía meter suficiente calor en "
                  "la unión. ¿Entonces el turno B era descuidado?",
    },
    {
        "key": "p12", "num": 12, "title": "Las 3G alimentan la causa raíz",
        "points": [("Cada porqué respaldado por evidencia", "Cada porqué"),
                   ("Nunca termines en “error del operador”", "Nunca termines"),
                   ("Pregunta qué hizo posible el error", "Pregunta qué condición")],
        "example": "Causa raíz: el almacén de refacciones tenía la punta equivocada, y el estándar no la "
                   "nombraba.",
        "example_cue": "El último porqué de Manoj",
        "script": "No. Las 3G les dan evidencia real a tus herramientas de causa raíz. Con los cinco "
                  "porqués, cada porqué debe estar respaldado por algo que viste o mediste. Nunca termines "
                  "en error del operador, o más entrenamiento. Pregunta qué condición del proceso hizo "
                  "posible el error. El último porqué de Manoj era claro. El almacén de refacciones tenía "
                  "la punta equivocada, y el estándar no nombraba el tipo de punta. ¿Y qué cambió?",
    },
    {
        "key": "p13", "num": 13, "title": "Corregir y verificar",
        "points": [("La punta correcta, nombrada en el estándar", "nombraba el tipo de punta"),
                   ("Revisión de la punta al inicio de cada turno", "una revisión de la punta"),
                   ("Verificado durante cinco turnos", "verificó el resultado")],
        "example": "Turno B: de 20 a 8 por cada 1,000, igual que el turno A.",
        "example_cue": "Las fallas del turno B",
        "script": "La solución fue simple. El estándar ahora nombraba el tipo de punta, y el almacén de "
                  "refacciones solo tenía la correcta. Una revisión de la punta se sumó a la rutina de "
                  "inicio de turno. Luego verificó el resultado durante cinco turnos completos, no en una "
                  "buena hora. Las fallas del turno B bajaron de veinte por cada mil a ocho, igual que el "
                  "turno A. Y el turno B nunca necesitó volver a entrenarse. ¿Cómo podrías hacer de esto un "
                  "hábito diario?",
    },
    {
        "key": "p14", "num": 14, "title": "El recorrido de 30 minutos por el Gemba",
        "points": [("Primero propósito y seguridad", "revisa la seguridad"),
                   ("Observa, luego revisa la cosa y los datos", "observa el proceso"),
                   ("Acuerda la contención y un responsable", "acuerda la contención")],
        "example": "La pregunta de Manoj en cada parada: “¿Cuál es el estándar, y qué está pasando de "
                   "verdad?”",
        "example_cue": "La pregunta favorita de Manoj",
        "script": "Hazlo trabajo estándar. En un recorrido de treinta minutos, primero revisa la seguridad, "
                  "la brecha y tu propósito. Luego observa el proceso en el punto de trabajo durante diez "
                  "minutos. Inspecciona la pieza afectada, y revisa los datos clave. Pregúntale al equipo "
                  "por las causas, acuerda la contención, y nombra un responsable con fecha. La pregunta "
                  "favorita de Manoj es simple. ¿Cuál es el estándar, y qué está pasando de verdad? ¿Qué "
                  "preguntarías tú?",
    },
    {
        "key": "p15", "num": 15, "title": "Errores que evitar",
        "points": [("Dirigir desde el tablero", "Dirigir solo"),
                   ("Tomar una muestra como la verdad", "Tomar una sola muestra"),
                   ("Cerrar después de entrenar", "Cerrar un problema")],
        "example": "Manoj ahora pasa los primeros 30 minutos de cada turno en el Gemba.",
        "example_cue": "Manoj ahora pasa",
        "script": "Cuidado con algunos errores comunes. Dirigir solo desde el tablero. Confiar en "
                  "entrevistas, sin tomar la pieza en la mano. Tomar una sola muestra como la verdad. "
                  "Cambiar ajustes durante la investigación, y destruir la evidencia. Cerrar un problema "
                  "después de entrenar, sin revisar que se detuvo. Manoj ahora pasa los primeros treinta "
                  "minutos de cada turno en el Gemba. ¿Podrías hacer lo mismo?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Gemba", "sub": "Lugar real", "icon": "walk", "with": 0},
        {"label": "Genbutsu", "sub": "Cosa real", "icon": "wave", "with": 1},
        {"label": "Genjitsu", "sub": "Hechos reales", "icon": "search", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Tablero", "sub": "Muestra síntomas", "icon": "chartUp", "with": 0},
        {"label": "El lugar real", "sub": "Muestra causas", "icon": "walk", "tone": "good", "with": 2}]},
    "p03": {"type": "flow", "items": [
        {"label": "¿Dónde?", "sub": "Línea 2, prueba de audio", "icon": "pin", "with": 0},
        {"label": "¿Qué?", "sub": "Audífono izquierdo", "icon": "wave", "with": 1},
        {"label": "¿Qué ocurrió?", "sub": "22 de 1,100", "icon": "count", "with": 2}]},
    "p04": {"type": "steps", "items": [
        {"label": "Pregunta clara", "with": 0}, {"label": "Dueño, PPE, ESD", "with": 1},
        {"label": "Observa ciclos completos", "with": 2}, {"label": "Compara con el estándar", "with": 3}]},
    "p05": {"type": "versus", "items": [
        {"label": "Inspección sorpresa", "sub": "Buscar culpables", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Visita respetuosa", "sub": "“¿Qué hace esto difícil?”", "icon": "person", "tone": "good", "with": "example"}]},
    "p06": {"type": "versus", "items": [
        {"label": "Audífono con falla", "sub": "Unión opaca y granulosa", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "Audífono bueno", "sub": "Unión brillante y lisa", "icon": "check", "tone": "good", "with": "example"}]},
    "p07": {"type": "icons", "items": [
        {"label": "Ningún interbloqueo brincado", "icon": "lock", "with": 0},
        {"label": "Primero el bloqueo", "icon": "key", "with": 1},
        {"label": "Protección ESD", "icon": "shield", "tone": "good", "with": 2}]},
    "p08": {"type": "bars", "label": "", "note": "Fallas por cada 1,000 audífonos: una señal, no una prueba", "with": "example", "items": [
        {"label": "Turno A", "value": 9, "with": "example"},
        {"label": "Turno B", "value": 20, "tone": "bad", "with": "example"}]},
    "p09": {"type": "steps", "items": [
        {"label": "Definir y contener", "with": 0},
        {"label": "Lugar", "with": 1}, {"label": "Cosa", "with": 1}, {"label": "Hechos", "with": 1},
        {"label": "Probar causas", "with": 2}]},
    "p10": {"type": "versus", "items": [
        {"label": "Punta del turno B", "sub": "Más chica, del almacén de refacciones", "icon": "wrench", "tone": "bad", "with": 1},
        {"label": "Punta estándar", "sub": "Turno A", "icon": "check", "tone": "good", "with": 1}]},
    "p11": {"type": "bars", "label": "", "note": "Prueba controlada: fallas en 300 audífonos", "with": "example", "items": [
        {"label": "Punta estándar", "value": 1, "tone": "good", "with": "example"},
        {"label": "Punta más chica", "value": 7, "tone": "bad", "with": "example"}]},
    "p12": {"type": "steps", "items": [
        {"label": "Uniones de soldadura débiles", "with": 0},
        {"label": "Punta más chica, muy poco calor", "with": 0},
        {"label": "Punta equivocada en el almacén de refacciones", "with": "example"},
        {"label": "Tipo de punta fuera del estándar", "with": "example"}]},
    "p13": {"type": "compare", "before": {"label": "Antes", "value": 20}, "after": {"label": "Después", "value": 8},
            "unit": "fallas por cada 1,000 audífonos, turno B", "note": "Igual que el turno A, verificado en 5 turnos", "with": "example"},
    "p14": {"type": "timeline", "items": [
        {"label": "Seguridad, brecha, propósito", "sub": "0–5", "icon": "shield", "with": 0, "span": 5},
        {"label": "Observar", "sub": "5–15", "icon": "walk", "with": 1, "span": 10},
        {"label": "Cosa y datos", "sub": "15–22", "icon": "search", "with": 1, "span": 7},
        {"label": "Causas, responsable", "sub": "22–30", "icon": "person", "tone": "good", "with": 2, "span": 8}]},
    "p15": {"type": "icons", "items": [
        {"label": "Solo el tablero", "icon": "chartUp", "tone": "bad", "with": 0},
        {"label": "Una sola muestra", "icon": "count", "tone": "bad", "with": 1},
        {"label": "Cerrado tras entrenar", "icon": "clipboard", "tone": "bad", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "¿Qué frase es un hecho real (Genjitsu)?",
        "options": ["“El turno B siempre es descuidado.”",
                    "“El proveedor lo causó.”",
                    "“18 de 24 fallas vinieron del lote B.”"],
        "correct": 2,
        "explanation": "Un hecho tiene conteos, un denominador y un alcance que puedes revisar. Las otras son "
                       "opiniones, y lo del proveedor todavía no está comprobado.",
        "q_script": "Prueba rápida. ¿Cuál de estas frases es un hecho real? Tómate unos segundos.",
        "a_script": "Es la última. Tiene un conteo, un denominador y un alcance que puedes revisar. Las otras "
                    "dos son solo opiniones.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "El tablero muestra un turno con el doble de defectos. El gerente quiere volver a "
                    "entrenar a ese turno. ¿Qué va primero?",
        "options": ["Entrenarlos hoy: los datos son claros",
                    "Ir a la estación, tomar las unidades con falla, y revisar los hechos",
                    "Intercambiar a los operadores de los dos turnos"],
        "correct": 1,
        "explanation": "Una diferencia entre turnos es una señal, no una prueba. Ve a ver: el lugar real, la "
                       "cosa real y los hechos reales, antes de decidir cualquier solución.",
        "q_script": "Una más, y esta es un escenario. El tablero muestra un turno con el doble de defectos. "
                    "El gerente quiere volver a entrenar a ese turno. ¿Qué debe pasar primero? Piénsalo.",
        "a_script": "Ve a ver. Visita la estación, toma las unidades con falla, y revisa los hechos. Una "
                    "diferencia entre turnos es una señal, no una prueba.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
