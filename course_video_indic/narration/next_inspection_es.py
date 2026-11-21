"""next_inspection in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh next_inspection_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ni_es"
NAME = "next_inspection_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "One Point Lesson": "uán póint léson",
    "Next Inspection": "nekst inspékshon",
    "Poka Yoke": "Poka Yoke",
    "Pareto": "Pareto",
    "Jidoka": "Yidoka",
    "Andon": "Andon",
    "FMEA": "efe eme e a",
    "CTQ": "ce te cu",
    "SOP": "ese o pe",
    "SMT": "ese eme te",
    "PCB": "pe ce be",
    "MSA": "eme ese a",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Un conector flojo, en la estación tres. Nadie lo notó. Viajó por cuatro estaciones más, "
    "la prueba final y el empaque. Luego un cliente abrió la caja. ¿Te suena familiar? En "
    "esta lección aprenderás Next Inspection. Verás cómo cada proceso puede proteger al "
    "siguiente, y atrapar los defectos donde empiezan. Seguiremos a Anita, ingeniera de "
    "calidad en una línea de cámaras de seguridad, mientras hace justo eso."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. No hagas, no pases y no aceptes un defecto. Revisa los "
    "puntos críticos en el lugar más temprano posible, y reacciona rápido. Y sigue moviendo "
    "tus controles hacia el inicio, hacia la prevención. Esta es tu acción para esta semana. "
    "Elige una entrega en tu línea, y anota lo que el siguiente proceso necesita de ella. "
    "Excelente trabajo al completar esta lección. Ahora aprenderás la One Point Lesson."
)

# One story thread: Anita's security-camera line. Assembly -> firmware -> test ->
# packing. Loose connectors and wrong labels were escaping downstream.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es Next Inspection",
        "points": [("Cada proceso protege al siguiente", "cada proceso protege"),
                   ("Confirma los puntos críticos antes de entregar", "Antes de entregar el trabajo"),
                   ("No hagas un defecto", "No hagas un defecto"),
                   ("No pases un defecto", "No pases un defecto"),
                   ("No aceptes un defecto", "No aceptes un defecto")],
        "example": "La estación de carcasa de Anita ahora revisa primero el seguro del conector.",
        "example_cue": "En la línea de Anita",
        "script": "Esta es la idea central. Next Inspection significa que cada proceso protege al "
                  "siguiente. Antes de entregar el trabajo, confirmas los puntos críticos. Y la estación "
                  "que recibe no acepta un defecto en silencio. Lo regresa de inmediato. Tres reglas lo "
                  "resumen. No hagas un defecto. No pases un defecto. No aceptes un defecto. En la línea de "
                  "Anita, la estación de carcasa ahora revisa primero el seguro del conector. ¿Y por qué "
                  "importa tanto esto?",
    },
    {
        "key": "p02", "num": 2, "title": "Por qué atraparlo temprano",
        "points": [("Los defectos cuestan más en cada paso", "Un defecto se vuelve más caro"),
                   ("Detección temprana = retroalimentación rápida", "La detección temprana también"),
                   ("Más inspección ≠ calidad", "Más inspección no")],
        "example": "Conector flojo: segundos para corregir en ensamble → abrir, reparar, volver a probar "
                   "después de la prueba → una devolución en el cliente.",
        "example_cue": "En ensamble, un conector flojo",
        "script": "Un defecto se vuelve más caro en cada paso que viaja. En ensamble, un conector flojo se "
                  "corrige en segundos. Después de la prueba, abres la carcasa, reparas y vuelves a probar. "
                  "En el cliente, es una devolución, y un golpe a tu nombre. La detección temprana también "
                  "da retroalimentación rápida. La causa sigue fresca, así que es fácil encontrarla. Pero "
                  "aquí va una advertencia. Más inspección no crea calidad. ¿Y dónde deben ir las "
                  "revisiones?",
    },
    {
        "key": "p03", "num": 3, "title": "Tres niveles de inspección",
        "points": [("En el origen: revisa primero la condición", "La inspección en el origen revisa"),
                   ("Autoinspección: revisa tu propio trabajo", "La autoinspección significa"),
                   ("Siguiente proceso: revisa antes de aceptar", "La inspección del siguiente proceso significa")],
        "example": "La línea de Anita: un sensor revisa la orientación, el ensamblador confirma el seguro, "
                   "el probador confirma el modelo.",
        "example_cue": "En la línea de Anita",
        "script": "Hay tres niveles. La inspección en el origen revisa la condición que podría crear el "
                  "defecto, antes de que pase. La autoinspección significa que revisas tu propio trabajo, "
                  "justo donde lo hiciste. La inspección del siguiente proceso significa que la estación "
                  "que recibe revisa antes de aceptar. En la línea de Anita, un sensor revisa la "
                  "orientación. El ensamblador confirma el seguro. Y el probador confirma el modelo. ¿Qué "
                  "nivel es el más fuerte? El más cercano al origen.",
    },
    {
        "key": "p04", "num": 4, "title": "El siguiente proceso es mi cliente",
        "points": [("El siguiente proceso es tu cliente", "El siguiente proceso es tu cliente"),
                   ("Producto, cantidad, calidad, etiqueta y tiempo correctos", "Necesita el producto correcto"),
                   ("Nunca pases a sabiendas una unidad anormal", "Nunca pases a sabiendas"),
                   ("Levántalo con el Andon", "Levántalo con el Andon")],
        "example": "Los ensambladores de Anita le preguntaron al equipo de firmware: ¿qué necesitan de "
                   "nosotros?",
        "example_cue": "Los ensambladores de Anita simplemente preguntaron",
        "script": "Piensa en cada entrega como una venta. El siguiente proceso es tu cliente. Necesita el "
                  "producto correcto, la cantidad y la calidad correctas, y la etiqueta y el tiempo "
                  "correctos. Así que sigue el SOP, y confirma tus puntos críticos. Nunca pases a sabiendas "
                  "una unidad anormal. Mejor levántalo con el Andon. Los ensambladores de Anita simplemente "
                  "preguntaron al equipo de firmware, ¿qué necesitan de nosotros? ¿Alguna vez le has hecho "
                  "esa pregunta a tu siguiente proceso?",
    },
    {
        "key": "p05", "num": 5, "title": "Los líderes lo hacen real",
        "points": [("Los líderes respaldan a quien para por calidad", "Los líderes deben respaldar"),
                   ("Responder rápido cuando los llaman", "Deben responder"),
                   ("Registrar defectos para aprender, nunca para culpar", "Y los defectos deben registrarse")],
        "example": "Una operadora paró la línea de Anita por un lente estrellado — su gerente le dio las "
                   "gracias frente al equipo.",
        "example_cue": "Cuando una operadora paró",
        "script": "Esto es lo que hace o rompe Next Inspection. Tus líderes. Si a la gente la presionan "
                  "para seguir corriendo a pesar de un problema, las revisiones se vuelven puro trámite. "
                  "Los líderes deben respaldar a quien para por calidad. Deben responder rápido cuando los "
                  "llaman. Y los defectos deben registrarse para aprender, nunca para culpar. Cuando una "
                  "operadora paró la línea de Anita por un lente estrellado, su gerente le dio las gracias "
                  "frente al equipo. ¿Qué pasaría en tu línea?",
    },
    {
        "key": "p06", "num": 6, "title": "Elegir qué inspeccionar",
        "points": [("Elige las revisiones por riesgo", "Así que elige por riesgo"),
                   ("CTQ del cliente: función, seguridad, ajuste", "Empieza por lo que tu cliente"),
                   ("FMEA y fugas repetidas", "Luego mira tu FMEA"),
                   ("¿Dónde puede colarse una pieza o etiqueta equivocada?", "Pregunta dónde una pieza equivocada")],
        "example": "Anita eligió cuatro: seguro del conector, versión de firmware, sello de la carcasa y "
                   "etiqueta.",
        "example_cue": "Anita eligió cuatro",
        "script": "No puedes revisar todo con el mismo cuidado. Así que elige por riesgo. Empieza por lo "
                  "que tu cliente siente, como la función, la seguridad y el ajuste. Esos son tus puntos "
                  "CTQ. Luego mira tu FMEA, y los defectos que se siguen escapando. Pregunta dónde una "
                  "pieza equivocada, un ajuste o una etiqueta podrían colarse. Anita eligió cuatro: seguro "
                  "del conector, versión de firmware, sello de la carcasa y etiqueta. Para los riesgos "
                  "altos, prefiere la prevención a una revisión visual. ¿Y cómo construyes una buena "
                  "puerta?",
    },
    {
        "key": "p07", "num": 7, "title": "Diseñar una puerta de inspección",
        "points": [("Define bueno y malo, con muestras", "Primero, define cómo se ve"),
                   ("Elige el método", "Luego elige el método"),
                   ("Fija cada cuánto revisas", "Fija cada cuánto revisas"),
                   ("Decide la reacción por adelantado", "Y decide la reacción")],
        "example": "La puerta del sello de Anita: muestras límite en el banco y un contenedor rojo para "
                   "rechazos.",
        "example_cue": "La puerta del sello de Anita",
        "script": "Una buena puerta es rápida, clara y difícil de brincar. Primero, define cómo se ve lo "
                  "bueno y lo malo, con muestras límite donde puedas. Luego elige el método, un calibrador, "
                  "un sensor, un escaneo o una revisión visual. Fija cada cuánto revisas. Y decide la "
                  "reacción antes de que aparezca un defecto. La puerta del sello de Anita tiene muestras "
                  "en el banco, y un contenedor rojo para rechazos. ¿Y qué pasa cuando la puerta encuentra "
                  "algo?",
    },
    {
        "key": "p08", "num": 8, "title": "El plan de reacción",
        "points": [("Detén o avisa con el Andon", "Detén o avisa con el Andon"),
                   ("Identifica defecto, modelo, número de serie", "Identifica el defecto"),
                   ("Contén hasta la última unidad buena", "Contén cada unidad"),
                   ("Corrige, verifica, previene", "Corrige el proceso")],
        "example": "Firmware equivocado en la prueba: se retuvo cada unidad desde la última revisión buena.",
        "example_cue": "Cuando el probador de Anita encontró",
        "script": "Reaccionas, rápido y en orden. Detén o avisa con el Andon. Identifica el defecto, el "
                  "modelo y el número de serie. Contén cada unidad hasta la última buena conocida. Corrige "
                  "el proceso, y verifica la primera unidad buena antes de volver a arrancar. Luego "
                  "encuentra la causa raíz, y evita que regrese. Cuando el probador de Anita encontró "
                  "firmware equivocado, se retuvo cada unidad desde la última revisión buena. Un plan vago "
                  "significa retrasos e inventario mezclado.",
    },
    {
        "key": "p09", "num": 9, "title": "Herramientas Lean que ayudan",
        "points": [("El Poka Yoke detiene la pieza o el paso equivocado", "El Poka Yoke evita"),
                   ("Jidoka y Andon detienen y piden ayuda", "Jidoka y Andon"),
                   ("El trabajo estándar hace obvio lo bueno y lo malo", "El trabajo estándar y los estándares visuales"),
                   ("El FMEA define riesgos, las auditorías revisan controles", "Tu FMEA define")],
        "example": "Anita cambió una revisión visual de etiqueta por una comparación con escáner — ahora la "
                   "etiqueta equivocada no se puede imprimir.",
        "example_cue": "Anita cambió una revisión visual",
        "script": "Next Inspection funciona mejor con otras herramientas Lean. El Poka Yoke evita que la "
                  "pieza o el paso equivocado ocurra siquiera. Jidoka y Andon detienen la línea y piden "
                  "ayuda. El trabajo estándar y los estándares visuales hacen obvio lo bueno y lo malo. Tu "
                  "FMEA define los riesgos, y las auditorías revisan que los controles de verdad se usen. "
                  "Anita cambió una revisión visual de etiqueta por una comparación con escáner. Ahora la "
                  "etiqueta equivocada simplemente no se puede imprimir. ¿Dónde más podría funcionar eso?",
    },
    {
        "key": "p10", "num": 10, "title": "Ejemplos en electrónica",
        "points": [("SMT: inspección óptica, alimentadores verificados", "En SMT"),
                   ("Ensamble: código de barras para el PCB, contador de tornillos", "En ensamble"),
                   ("Firmware: interbloqueo de versión", "En firmware"),
                   ("Empaque: revisión de peso y escaneos", "En empaque")],
        "example": "Cada revisión va justo después del paso que protege. La inspección final es la última "
                   "red de seguridad.",
        "example_cue": "Cada revisión va justo después",
        "script": "Recorramos la línea. En SMT, la inspección óptica automática revisa las tarjetas, y se "
                  "verifican los alimentadores. En ensamble, un código de barras confirma el PCB correcto, "
                  "y un contador confirma cada tornillo. En firmware, un interbloqueo revisa la versión "
                  "antes de liberar. En empaque, una revisión de peso y escaneos atrapan un accesorio "
                  "faltante. Nota el patrón. Cada revisión va justo después del paso que protege. ¿Y la "
                  "inspección final? Es tu última red de seguridad, no tu sistema de calidad.",
    },
    {
        "key": "p11", "num": 11, "title": "Calidad en el origen",
        "points": [("El proceso anterior construye al estándar", "El proceso anterior construye al estándar"),
                   ("El proceso siguiente acepta solo lo bueno", "El proceso siguiente acepta"),
                   ("Los problemas regresan a la estación que los hizo", "Cualquier problema regresa directo"),
                   ("Cuidado con la trampa de la inspección", "cuidado con la trampa de la inspección")],
        "example": "La línea de Anita tenía un inspector después de cada estación. Ella pasó a tres a "
                   "proyectos de prevención.",
        "example_cue": "La línea de Anita antes trabajaba",
        "script": "Next Inspection apoya la calidad en el origen. El proceso anterior construye al "
                  "estándar. El proceso siguiente acepta solo lo bueno. Cualquier problema regresa directo "
                  "a la estación que lo hizo, y se corrige la causa. Ahora, cuidado con la trampa de la "
                  "inspección. Poner un inspector después de cada estación cuesta mucho, y esconde procesos "
                  "débiles. La línea de Anita antes trabajaba así. Ella pasó a tres inspectores a proyectos "
                  "de prevención. ¿Puedes confiar en las revisiones que quedan?",
    },
    {
        "key": "p12", "num": 12, "title": "¿Puedes confiar en la revisión?",
        "points": [("Las aceptaciones falsas dejan escapar defectos", "Una aceptación falsa"),
                   ("Los rechazos falsos invitan a brincar la revisión", "Un rechazo falso"),
                   ("Definiciones claras, fotos, muestras límite", "Así que define los defectos con claridad"),
                   ("Entrena a quienes revisan", "Entrena a las personas que revisan"),
                   ("Calibra los calibradores, haz un MSA", "Calibra los calibradores"),
                   ("Controla la iluminación y la distancia de vista", "Controla la iluminación")],
        "example": "Los dos inspectores de Anita no coincidían en uno de cada cinco sellos. Mejores muestras "
                   "lo corrigieron.",
        "example_cue": "Los dos inspectores de Anita",
        "script": "Una revisión solo sirve si puedes confiar en ella. Una aceptación falsa deja escapar un "
                  "defecto. Un rechazo falso crea retrabajo innecesario, y la gente empieza a brincar la "
                  "revisión. Así que define los defectos con claridad, con fotos y muestras límite. Entrena "
                  "a las personas que revisan. Calibra los calibradores, y haz un estudio de medición, "
                  "llamado MSA. Controla la iluminación y la distancia de vista. Los dos inspectores de "
                  "Anita no coincidían en uno de cada cinco sellos. Mejores muestras lo corrigieron. ¿Y "
                  "cómo mides el éxito?",
    },
    {
        "key": "p13", "num": 13, "title": "KPI de Next Inspection",
        "points": [("Rendimiento a la primera arriba", "El rendimiento a la primera debe subir"),
                   ("Tasa de fugas abajo", "La tasa de fugas debe bajar"),
                   ("Retrabajo, defectos repetidos, tiempo de respuesta", "Vigila tu tasa de retrabajo"),
                   ("Llamadas falsas registradas", "Y registra las llamadas falsas")],
        "example": "El rendimiento sube mientras el esfuerzo de inspección baja = vas ganando.",
        "example_cue": "Si el rendimiento sube",
        "script": "Sigue un conjunto equilibrado de números. El rendimiento a la primera debe subir. La "
                  "tasa de fugas debe bajar. Son los defectos encontrados después que debieron atraparse "
                  "antes. Vigila tu tasa de retrabajo y los defectos repetidos. Mide el tiempo de respuesta "
                  "de la detección, desde la señal hasta la contención. Y registra las llamadas falsas, "
                  "para saber que tus revisiones son confiables. Si el rendimiento sube mientras el "
                  "esfuerzo de inspección baja, vas ganando. ¿Listo para ver los resultados de Anita?",
    },
    {
        "key": "p14", "num": 14, "title": "Caso práctico: línea de cámaras",
        "points": [("Revisiones de entrega en 4 puntos de riesgo", "Puso revisiones de entrega"),
                   ("Plan de reacción publicado en cada puerta", "Cada puerta tuvo"),
                   ("Las revisiones de sello y etiqueta se volvieron interbloqueos", "Las revisiones de sello y etiqueta"),
                   ("Revisión semanal de fugas con el origen", "Y cada semana")],
        "example": "Después de 8 semanas: fugas de 18 a 3 por semana, retrabajo reducido a menos de la "
                   "mitad, rendimiento a la primera de 98.5%.",
        "example_cue": "Después de ocho semanas",
        "script": "Esto es lo que hizo Anita. Puso revisiones de entrega en cuatro puntos de riesgo. Cada "
                  "puerta tuvo un plan de reacción publicado. Las revisiones de sello y etiqueta se "
                  "volvieron interbloqueos. Y cada semana, revisó cada fuga con la estación que la hizo. "
                  "Después de ocho semanas, las fugas bajaron de dieciocho por semana a tres. El retrabajo "
                  "bajó a menos de la mitad. El rendimiento a la primera subió a noventa y ocho y medio por "
                  "ciento. ¿Cómo lo extenderías tú?",
    },
    {
        "key": "p15", "num": 15, "title": "Ruta y lista diaria",
        "points": [("Elige por riesgo y Pareto, mapea el flujo", "Elige un producto usando el riesgo y un Pareto"),
                   ("Diseña revisiones con planes de reacción", "Diseña las revisiones"),
                   ("Piloto en una línea, compara antes y después", "Haz un piloto en una línea"),
                   ("Estandariza el SOP, el FMEA, el entrenamiento", "Luego estandariza el SOP")],
        "example": "Preguntas diarias: ¿Los criterios están visibles? ¿Tus operadores pueden explicar el "
                   "plan de reacción?",
        "example_cue": "Cada día, haz preguntas simples",
        "script": "Extiéndelo paso a paso. Elige un producto usando el riesgo y un Pareto. Mapea el flujo, "
                  "y enlista los puntos críticos. Diseña las revisiones en el origen, propias y del "
                  "siguiente proceso, con planes de reacción. Haz un piloto en una línea, y compara antes y "
                  "después. Luego estandariza el SOP, el FMEA y el entrenamiento. Cada día, haz preguntas "
                  "simples. ¿Los criterios están visibles? ¿Tus operadores pueden explicar el plan de "
                  "reacción? Protege al siguiente proceso, cada vez.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "No hagas", "sub": "un defecto", "icon": "wrench", "with": 2},
        {"label": "No pases", "sub": "un defecto", "icon": "lock", "with": 3},
        {"label": "No aceptes", "sub": "un defecto", "icon": "shield", "with": 4}]},
    "p02": {"type": "flow", "items": [
        {"label": "En ensamble", "sub": "Segundos para corregir", "icon": "wrench", "tone": "good", "with": "example"},
        {"label": "Después de la prueba", "sub": "Abrir, reparar, volver a probar", "icon": "test", "with": "example"},
        {"label": "En el cliente", "sub": "Una devolución, y un golpe a tu nombre", "icon": "box", "tone": "bad", "with": "example"}]},
    "p03": {"type": "ladder", "top": "LO MÁS FUERTE: LO MÁS CERCA DEL ORIGEN", "bottom": "ÚLTIMA LÍNEA DE DEFENSA", "items": [
        {"label": "Origen", "icon": "sensor"}, {"label": "Propia", "icon": "hand"},
        {"label": "Siguiente proceso", "icon": "search"}]},
    "p04": {"type": "flow", "items": [
        {"label": "Tu estación", "sub": "Sigue el SOP", "icon": "wrench", "with": 0},
        {"label": "Revisa los puntos críticos", "sub": "Producto, cantidad, etiqueta, tiempo", "icon": "check", "with": 1},
        {"label": "Siguiente proceso", "sub": "Tu cliente", "icon": "person", "tone": "good", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Respalda el paro", "icon": "shield"}, {"label": "Responde rápido", "icon": "clock"},
        {"label": "Aprende, nunca culpes", "icon": "person", "tone": "good"}]},
    "p06": {"type": "icons", "items": [
        {"label": "CTQ del cliente", "sub": "Función, seguridad, ajuste", "icon": "person", "with": 1},
        {"label": "FMEA + fugas", "sub": "Lo que se sigue escapando", "icon": "clipboard", "with": 2},
        {"label": "Puntos donde se cuela", "sub": "Pieza, ajuste, etiqueta equivocados", "icon": "label", "with": 3}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Seguro del conector", "icon": "lock", "with": "example"},
            {"label": "Versión de firmware", "icon": "chip", "with": "example"},
            {"label": "Sello de la carcasa", "icon": "shield", "with": "example"},
            {"label": "Etiqueta", "icon": "label", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Muestras buenas contra malas", "icon": "shape"}, {"label": "El método", "icon": "sensor"},
        {"label": "Cada cuánto", "icon": "clock"}, {"label": "La reacción", "icon": "warning"}]},
    "p08": {"type": "flow", "items": [
        {"label": "Detener: Andon", "icon": "warning", "tone": "bad"},
        {"label": "Identificar", "sub": "Defecto, modelo, número de serie", "icon": "search"},
        {"label": "Contener", "sub": "Hasta la última unidad buena", "icon": "lock"},
        {"label": "Corregir, verificar, prevenir", "icon": "check", "tone": "good"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Poka Yoke", "icon": "key"}, {"label": "Jidoka + Andon", "icon": "warning"},
        {"label": "Trabajo estándar", "icon": "clipboard"}, {"label": "FMEA + auditorías", "icon": "shield"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Revisión visual de etiqueta", "sub": "Fácil de pasar por alto", "icon": "search"},
            {"label": "Comparación con escáner", "sub": "La etiqueta equivocada no se puede imprimir", "icon": "barcode"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "SMT", "sub": "Inspección óptica, alimentadores verificados", "icon": "chip"},
        {"label": "Ensamble", "sub": "Código de barras del PCB, contador de tornillos", "icon": "barcode"},
        {"label": "Firmware", "sub": "Interbloqueo de versión", "icon": "lock"},
        {"label": "Empaque", "sub": "Revisión de peso y escaneos", "icon": "scale"}]},
    "p11": {"type": "flow", "items": [
        {"label": "El proceso anterior construye al estándar", "icon": "wrench", "with": 0},
        {"label": "El proceso siguiente acepta solo lo bueno", "icon": "check", "with": 1},
        {"label": "Los problemas regresan al origen", "icon": "sequence", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Un inspector después de cada estación", "sub": "Costoso; esconde procesos débiles", "icon": "person"},
            {"label": "3 pasaron a prevención", "sub": "Calidad en el origen", "icon": "shield"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Aceptación falsa", "icon": "cross", "tone": "bad"}, {"label": "Rechazo falso", "icon": "warning", "tone": "bad"},
        {"label": "Definiciones claras", "icon": "clipboard"}, {"label": "Revisores entrenados", "icon": "person"},
        {"label": "Calibrar, MSA", "icon": "gear"}, {"label": "Iluminación", "icon": "sensor"}],
        "then": {"type": "stat", "value": 5, "prefix": "1 / ", "icon": "search", "label": "sellos en los que no coincidían los dos inspectores",
                 "unit": "Mejores muestras límite lo corrigieron", "with": "example"}},
    "p13": {"type": "icons", "items": [
        {"label": "Rendimiento a la primera", "sub": "Arriba", "icon": "chartUp", "tone": "good"},
        {"label": "Tasa de fugas", "sub": "Abajo", "icon": "chartDown", "tone": "good"},
        {"label": "Retrabajo, tiempo de respuesta", "icon": "clock"},
        {"label": "Llamadas falsas", "icon": "warning"}]},
    "p14": {"type": "flow", "items": [
        {"label": "Revisiones en 4 puntos de riesgo", "icon": "search", "tone": "good"},
        {"label": "Plan de reacción en cada puerta", "icon": "clipboard", "tone": "good"},
        {"label": "Interbloqueos de sello + etiqueta", "icon": "lock", "tone": "good"},
        {"label": "Revisión semanal de fugas", "icon": "calendar", "tone": "good"}],
        "then": {"type": "compare", "before": {"label": "Antes", "value": 18}, "after": {"label": "Después de 8 semanas", "value": 3},
                 "unit": "fugas por semana", "note": "Rendimiento a la primera de 98.5%", "with": "example"}},
    "p15": {"type": "steps", "items": [
        {"label": "Elegir por riesgo", "with": 0}, {"label": "Mapear el flujo", "with": 0},
        {"label": "Diseñar revisiones", "with": 1}, {"label": "Piloto en una línea", "with": 2},
        {"label": "Estandarizar", "with": 3}, {"label": "Preguntar a diario", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un sensor detiene la orientación equivocada del conector antes de colocar la pieza. ¿Qué "
                    "nivel de inspección es este?",
        "options": ["Inspección en el origen", "Autoinspección", "Inspección del siguiente proceso"],
        "correct": 0,
        "explanation": "Revisa la condición que crearía el defecto, antes de que pase. Eso es inspección en el "
                       "origen — el nivel más fuerte.",
        "q_script": "Prueba rápida. Un sensor detiene la orientación equivocada del conector antes de que la "
                    "pieza siquiera se coloque. ¿Qué nivel de inspección es ese? Tómate unos segundos.",
        "a_script": "Es inspección en el origen. Revisa la condición antes de que el defecto pueda pasar. Ese "
                    "es el nivel más fuerte.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "La prueba sigue encontrando el mismo conector flojo que viene de ensamble, así que un "
                    "gerente pone un inspector después de ensamble. ¿Cuál es la mejor jugada?",
        "options": ["Agregar un segundo inspector por seguridad", "Conservar el inspector y también corregir la causa en ensamble",
                    "Quitar todas las revisiones para ahorrar", "Pedirle a prueba que deje de reportarlo"],
        "correct": 1,
        "explanation": "Un inspector extra puede contener el riesgo por ahora, pero un defecto repetido "
                       "significa que hay que corregir el proceso en el origen — luego se puede quitar la "
                       "revisión temporal.",
        "q_script": "Una más, y esta es un escenario. La prueba sigue encontrando el mismo conector flojo que "
                    "viene de ensamble. Un gerente pone un inspector después de ensamble. ¿Cuál es la mejor "
                    "jugada? Piénsalo.",
        "a_script": "Conserva la revisión por ahora, pero corrige la causa en ensamble. Un defecto repetido "
                    "significa que el proceso necesita mejorar en el origen. Luego la revisión extra se puede "
                    "quitar.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
