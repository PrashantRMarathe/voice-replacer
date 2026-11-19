"""a3_problem_solving in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh a3_problem_solving_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "a3_es"
NAME = "a3_problem_solving_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Burn Down Chart": "bern dáun chart",
    "Five Whys": "fáiv juáis",
    "Ishikawa": "Ishikawa",
    "Genbutsu": "Guenbutsu",
    "Genjitsu": "Guenyitsu",
    "Pareto": "Pareto",
    "Gemba": "Guemba",
    "PDCA": "pe de ce a",
    "MES": "eme e ese",
    "SOP": "ese o pe",
    "A3": "a tres",
    "3G": "tres ge",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Quinientos setenta y seis servidores fallaron su primera prueba de arranque en cuatro "
    "semanas. ¿La primera solución propuesta? Poner dos inspectores más. ¿Te suena familiar? "
    "En esta lección aprenderás la solución de problemas con A3. Verás cómo contar toda la "
    "historia de un problema en una sola hoja, desde la brecha real hasta una solución "
    "comprobada. Seguiremos a Karthik, ingeniero de pruebas en una línea de ensamble de "
    "servidores, mientras escribe su primer A3."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Empieza con una brecha medible, nunca con una causa ni una "
    "solución. Ve a ver, y prueba cada causa con evidencia. Y estandariza solo lo que tu "
    "piloto de verdad comprobó. Esta es tu acción para esta semana. Elige un problema que se "
    "repite, y escribe su planteamiento en una hoja A3. Excelente trabajo al completar esta "
    "lección. Ahora aprenderás el Burn Down Chart, para seguir el trabajo contra el tiempo."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es un A3",
        "points": [("Su nombre viene del papel tamaño A3", "Un A3 se llama así"),
                   ("Toda la historia del problema en una hoja", "Cuenta toda la historia"),
                   ("Definir, buscar causas, probar, sostener", "Defines el problema"),
                   ("Visual, y hecho en equipo", "Es visual")],
        "example": "El reporte de Karthik decía “los operadores son descuidados”. Su gerente le devolvió una "
                   "hoja A3 en blanco.",
        "example_cue": "Su reporte decía",
        "script": "Un A3 se llama así por un tamaño de papel. Cuenta toda la historia de un problema en una "
                  "sola hoja. Defines el problema, encuentras sus causas reales, pruebas soluciones y "
                  "mantienes los resultados. Es visual, y lo construyes en equipo. Así conoció Karthik su "
                  "primer A3. Su reporte decía que los operadores son descuidados. Su gerente se lo "
                  "devolvió, con una hoja A3 en blanco. ¿Entonces qué cuenta de verdad como problema?",
    },
    {
        "key": "p02", "num": 2, "title": "Los problemas son brechas",
        "points": [("Un problema es una brecha medible", "Un problema es una brecha"),
                   ("No saltes de la queja a la solución", "El A3 evita que saltes"),
                   ("Una brecha se puede medir e investigar", "Puedes medir una brecha")],
        "example": "“Los operadores son descuidados” es culpar. “Las fallas de arranque subieron a 4.8%” es "
                   "una brecha.",
        "example_cue": "Compara dos frases",
        "script": "Esta es la idea clave. Un problema es una brecha, entre lo que está pasando y el "
                  "estándar que necesitas. El A3 evita que saltes de una queja directo a una solución. "
                  "Compara dos frases. Los operadores son descuidados es culpar. Las fallas de arranque "
                  "subieron a cuatro punto ocho por ciento. Eso es una brecha. Puedes medir una brecha. "
                  "También puedes investigarla. ¿Qué tipo de frase escuchas más en tu piso?",
    },
    {
        "key": "p03", "num": 3, "title": "Dónde encaja el A3: PDCA",
        "points": [("Problemas que siguen regresando", "Úsalo para problemas"),
                   ("Problemas que los equipos resuelven juntos", "Brilla cuando"),
                   ("Basado en Plan · Do · Check · Act", "sigue el PDCA")],
        "example": "Las fallas de arranque de Karthik: repetidas, costosas y de varias áreas.",
        "example_cue": "Las fallas de arranque de Karthik",
        "script": "¿Dónde encaja el A3? Úsalo para problemas que siguen regresando. Defectos repetidos, "
                  "paros, faltantes y producción perdida son buenos candidatos. Brilla cuando Producción, "
                  "Calidad e Ingeniería deben resolver algo juntos. Y en el fondo, sigue el PDCA. Planeas, "
                  "y luego haces un piloto pequeño. Revisas los resultados contra la meta. Después actúas, "
                  "estandarizando o replanteando. Las fallas de arranque de Karthik encajan perfecto. ¿Y "
                  "qué va en tu hoja?",
    },
    {
        "key": "p04", "num": 4, "title": "Anatomía de un A3",
        "points": [("Izquierda: antecedentes, situación actual, meta", "El lado izquierdo"),
                   ("Análisis de causa raíz: por qué existe la brecha", "El análisis de causa raíz explica"),
                   ("Derecha: contramedidas, plan, seguimiento", "El lado derecho"),
                   ("Cada panel responde una pregunta", "Cada panel responde")],
        "example": "La hoja de Karthik: siete paneles, una página, de izquierda a derecha.",
        "example_cue": "La hoja de Karthik tiene",
        "script": "Imagina la hoja. El lado izquierdo cuenta la historia hasta ahora. Los antecedentes "
                  "dicen por qué importa ahora. La situación actual muestra lo que de verdad pasa. La meta "
                  "dice qué resultado, y para cuándo. El análisis de causa raíz explica por qué existe la "
                  "brecha. El lado derecho pasa a la acción, con contramedidas, un plan y seguimiento. Cada "
                  "panel responde una pregunta. La hoja de Karthik tiene siete paneles, leídos de izquierda "
                  "a derecha. ¿Podrías nombrar la pregunta detrás de cada uno?",
    },
    {
        "key": "p05", "num": 5, "title": "El planteamiento del problema",
        "points": [("Nombra la brecha, nunca una causa", "nombra la brecha"),
                   ("Línea · producto · periodo · medida", "Nombra la línea"),
                   ("Un denominador claro, mismas definiciones", "Usa un denominador claro"),
                   ("Sin culpa, sin solución", "No hay culpa")],
        "example": "Línea 2, el mes pasado: 4.8% de 12,000 servidores falló la primera prueba de arranque, "
                   "contra una referencia de 1.5%.",
        "example_cue": "Esta es la versión de Karthik",
        "script": "Ahora, el panel más difícil de hacer bien. Un buen planteamiento nombra la brecha, pero "
                  "nunca afirma una causa. Nombra la línea, el producto, el periodo y la medida. Usa un "
                  "denominador claro y las mismas definiciones. Esta es la versión de Karthik. Durante el "
                  "último mes en la Línea Dos, las fallas en la primera prueba de arranque promediaron "
                  "cuatro punto ocho por ciento. La referencia era uno punto cinco, sobre doce mil "
                  "servidores. ¿Notas lo que falta? No hay culpa, ni solución.",
    },
    {
        "key": "p06", "num": 6, "title": "Ir a ver: las 3G",
        "points": [("Gemba: el lugar real", "Gemba es el lugar real"),
                   ("Genbutsu: las cosas reales", "Genbutsu significa"),
                   ("Genjitsu: los hechos reales", "Genjitsu significa")],
        "example": "7 de 10 servidores con falla en el banco: un módulo de memoria un poco levantado.",
        "example_cue": "Karthik puso diez",
        "script": "Antes de abrir una hoja de cálculo, ve a ver. Lean lo llama las 3G. Gemba es el lugar "
                  "real, así que te paras en la estación de prueba. Genbutsu significa las cosas reales, "
                  "como servidores con falla, fixtures y registros de prueba. Genjitsu significa los hechos "
                  "reales, que revisas tú mismo. Karthik puso diez servidores con falla en el banco. En "
                  "siete de ellos, un módulo de memoria estaba un poco levantado. ¿Algún reporte le habría "
                  "mostrado eso?",
    },
    {
        "key": "p07", "num": 7, "title": "Datos en los que puedes confiar",
        "points": [("Una definición clara", "empiezan con una definición clara"),
                   ("Cuenta unidades únicas: las repruebas no pueden ocultar fallas", "¿Por qué únicos?"),
                   ("Revisa horas, números de serie, calibración", "¿Las horas están bien"),
                   ("El registro de línea coincide con el MES", "¿El registro de la línea")],
        "example": "Tasa de falla a la primera = servidores únicos que fallan su primera prueba válida ÷ "
                   "servidores únicos probados.",
        "example_cue": "La tasa de falla a la primera es",
        "script": "Los buenos datos empiezan con una definición clara. La regla de Karthik era simple. La "
                  "tasa de falla a la primera es los servidores únicos que fallan su primera prueba válida, "
                  "divididos entre los servidores únicos probados. ¿Por qué únicos? Porque las repruebas "
                  "pueden ocultar fallas, o contar un servidor dos veces. Luego revisa los datos mismos. "
                  "¿Las horas están bien, y cada número de serie es único? ¿El probador está calibrado? ¿El "
                  "registro de la línea coincide con el MES? Solo entonces puedes confiar en tu gráfica.",
    },
    {
        "key": "p08", "num": 8, "title": "Ver la brecha",
        "points": [("Tendencia semanal: sube cada semana", "tendencia semanal subió"),
                   ("Unas 400 fallas de más", "Son casi cuatrocientas"),
                   ("Pareto: ordena las fallas por modo", "Luego una gráfica de Pareto")],
        "example": "Memoria no detectada: 288 de 576 fallas, la mitad del total.",
        "example_cue": "Memoria no detectada",
        "script": "¿Y qué mostró la gráfica? La tendencia semanal subió cada semana sin falta. Para la "
                  "semana cuatro, llegó a cinco y medio por ciento. Con la tasa de referencia, esperarías "
                  "unas ciento ochenta fallas. Él tenía quinientas setenta y seis. Son casi cuatrocientas "
                  "de más. Luego una gráfica de Pareto las separó por modo de falla. Memoria no detectada "
                  "era la mitad. La brecha está clara, pero no prueba una causa. ¿Por dónde empezarías?",
    },
    {
        "key": "p09", "num": 9, "title": "Meta y alcance",
        "points": [("Meta: 2% o menos en 6 semanas", "La de Karthik era clara"),
                   ("Límites de control: tiempo de prueba, repruebas, fugas", "Agrega también límites"),
                   ("Alcance: qué entra, qué no", "Luego fija el alcance")],
        "example": "Fuera del alcance: aflojar los límites de prueba para verse mejor.",
        "example_cue": "Aflojar los límites de prueba",
        "script": "Ahora, fija una meta que de verdad puedas probar. La de Karthik era clara. Bajar las "
                  "fallas en la primera prueba de arranque de la Línea Dos a dos por ciento o menos, en "
                  "seis semanas. Agrega también límites, como el tiempo de prueba, la tasa de repruebas y "
                  "los defectos que se escapan. Aseguran que no ganes haciendo trampa. Luego fija el "
                  "alcance. Las fallas de memoria de la Línea Dos entran. Aflojar los límites de prueba "
                  "queda fuera. ¿Ves por qué importa?",
    },
    {
        "key": "p10", "num": 10, "title": "Explorar causas: Ishikawa",
        "points": [("Primero piensa en grande", "piensa en grande"),
                   ("Seis M: personas, máquina, método…", "Ordena las posibles causas"),
                   ("Cada rama es una suposición hasta comprobarla", "Cada rama es solo")],
        "example": "¿Está entrenada la inserción? ¿Cambió el chasis? ¿El cierre varía por lote?",
        "example_cue": "El equipo de Karthik preguntó",
        "script": "Ahora, ¿por qué existe la brecha? Primero, piensa en grande con un diagrama de Ishikawa. "
                  "Ordena las posibles causas en seis M. Personas, máquina, método, material, medición y "
                  "medio ambiente. El equipo de Karthik preguntó en cada una. ¿Está entrenado el método de "
                  "inserción? ¿Cambió el chasis? ¿El cierre del módulo varía por lote? Pero ten cuidado. "
                  "Cada rama es solo una suposición hasta que la compruebas. ¿Y cómo reduces las opciones?",
    },
    {
        "key": "p11", "num": 11, "title": "Causa raíz: Five Whys",
        "points": [("Pregunta por qué, paso a paso", "profundiza con los Five Whys"),
                   ("Termina en una causa de proceso que puedas corregir", "Esa es una causa de proceso"),
                   ("Una cadena no es prueba: compruébala", "Pero una cadena")],
        "example": "Causa raíz: las instrucciones de trabajo no se revisaron cuando cambió el chasis.",
        "example_cue": "Las instrucciones de trabajo no se revisaron",
        "script": "Luego profundiza con los Five Whys. ¿Por qué fallaron la prueba de arranque? Un módulo "
                  "de memoria no estaba bien asentado. ¿Por qué? El seguro cerró antes de que el módulo "
                  "bajara del todo. ¿Por qué? El chasis nuevo dejaba menos espacio para presionar derecho. "
                  "¿Por qué no se cambió el método? Las instrucciones de trabajo no se revisaron cuando "
                  "cambió el chasis. Esa es una causa de proceso que puedes corregir. Pero una cadena no es "
                  "prueba. Karthik presionó módulos en ángulo, y la falla apareció cada vez.",
    },
    {
        "key": "p12", "num": 12, "title": "Contramedidas y contención",
        "points": [("Rompe la causa comprobada", "rompan la causa"),
                   ("Evalúa: efecto, riesgo, costo, sostenibilidad", "Evalúa cada una"),
                   ("Contén ahora, corrige para siempre", "Mientras tanto, contén")],
        "example": "Guía de inserción · revisión del seguro · revisión de instrucciones en cada cambio de "
                   "chasis",
        "example_cue": "El equipo de Karthik eligió tres",
        "script": "Ahora elige contramedidas que rompan la causa. El equipo de Karthik eligió tres. Una "
                  "guía de inserción que mantiene el módulo derecho. Una revisión del seguro antes de que "
                  "el servidor salga de la estación. Y una revisión de las instrucciones de trabajo en cada "
                  "cambio de chasis. Evalúa cada una por su efecto, riesgo, costo y qué tan fácil es "
                  "sostenerla. Mientras tanto, contén. Los servidores sospechosos se retuvieron y se "
                  "revisaron otra vez. La contención protege a tu cliente, pero no es la solución.",
    },
    {
        "key": "p13", "num": 13, "title": "Plan y responsables",
        "points": [("Un responsable, una fecha, evidencia", "tu plan nombra un responsable"),
                   ("Semanas 1–2: confirmar la causa, piloto", "Ingeniería de pruebas confirma"),
                   ("Semanas 3–4: actualizar el SOP, entrenar a cada turno", "Mantenimiento y producción"),
                   ("Semanas 5–6: verificar los resultados", "Calidad verifica")],
        "example": "¿Atorado? Escala con el bloqueo exacto y la decisión que necesitas.",
        "example_cue": "¿Atorado?",
        "script": "Una acción sin responsable casi nunca pasa. Por eso tu plan nombra un responsable, una "
                  "fecha y la evidencia de cada acción. Ingeniería de pruebas confirma la causa en la "
                  "semana uno. Ingeniería de procesos prueba la guía de inserción en la semana dos. "
                  "Mantenimiento y producción actualizan el SOP y entrenan a cada turno para la semana "
                  "cuatro. Calidad verifica los resultados en las semanas cinco y seis. ¿Atorado? Escala "
                  "con el bloqueo exacto. ¿Y cómo sabes que funcionó?",
    },
    {
        "key": "p14", "num": 14, "title": "Piloto y revisión",
        "points": [("La misma mezcla de productos que la base", "con la misma mezcla de productos"),
                   ("De 4.8% a 1.6%: meta cumplida", "Las fallas bajaron"),
                   ("También revisó los límites", "revisó también los límites"),
                   ("¿No se cumplió? Revisa la causa, no la meta", "Si no hubiera")],
        "example": "Piloto: 48 fallas en 3,000 servidores = 1.6%.",
        "example_cue": "Karthik lo corrió",
        "script": "Un piloto es un experimento, no un anuncio. Karthik lo corrió con tres mil servidores, "
                  "con la misma mezcla de productos que la base. Las fallas bajaron a uno punto seis por "
                  "ciento. Meta cumplida. Pero revisó también los límites. El tiempo de prueba se mantuvo "
                  "estable, y ningún otro modo de falla creció. ¿Se sostuvo en cada turno? Sí. Si no "
                  "hubiera sido así, revisarías la causa, nunca cambiarías la meta en silencio.",
    },
    {
        "key": "p15", "num": 15, "title": "Sostener y tu A3 de 30 días",
        "points": [("Actualiza el SOP, la lista de revisión, el entrenamiento", "Actualiza el SOP"),
                   ("Revisión al inicio del turno; repaso a los 30/60/90 días", "Agrega una revisión del seguro"),
                   ("Cópialo solo a líneas que de verdad coincidan", "Cópialo a otras líneas"),
                   ("Tu propio A3 en 30 días", "Ahora te toca a ti")],
        "example": "Días 1–5: un problema real, la base en el Gemba. Día 20: causas y piloto. Día 30: "
                   "presenta tu A3.",
        "example_cue": "En los primeros cinco días",
        "script": "Por último, haz que la nueva forma sea la forma normal. Actualiza el SOP, la lista de "
                  "revisión y el entrenamiento. Agrega una revisión del seguro al inicio de cada turno, y "
                  "revisa la tendencia a los treinta, sesenta y noventa días. Cópialo a otras líneas solo "
                  "después de comprobar que de verdad coinciden. Ahora te toca a ti. En los primeros cinco "
                  "días, elige un problema real y revisa su base en el Gemba. Para el día veinte, verifica "
                  "las causas y corre un piloto. Para el día treinta, presenta tu A3.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Papel tamaño A3", "icon": "label", "with": 0},
        {"label": "La historia en una hoja", "icon": "clipboard", "with": 1},
        {"label": "Causas, pruebas, resultados", "icon": "search", "with": 2},
        {"label": "Hecho en equipo", "icon": "person", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "“Los operadores son descuidados”", "sub": "El primer reporte de Karthik", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Una hoja A3 en blanco", "sub": "La respuesta de su gerente", "icon": "clipboard", "tone": "good", "with": "example"}]}},
    "p02": {"type": "versus", "items": [
        {"label": "Culpa", "sub": "“Los operadores son descuidados”", "icon": "person", "tone": "bad", "with": "example"},
        {"label": "Brecha", "sub": "Fallas de arranque hasta 4.8%", "icon": "chartUp", "tone": "good", "with": "example"}]},
    "p03": {"type": "icons", "items": [
        {"label": "Defectos repetidos", "icon": "warning", "with": 0},
        {"label": "Paros, faltantes", "icon": "clock", "with": 0},
        {"label": "De varias áreas", "icon": "person", "with": 1}],
        "then": {"type": "flow", "with": 2, "items": [
            {"label": "Plan", "icon": "clipboard", "with": 2},
            {"label": "Do", "sub": "Piloto pequeño", "icon": "wrench", "with": 2},
            {"label": "Check", "sub": "Contra la meta", "icon": "search", "with": 2},
            {"label": "Act", "sub": "Estandarizar", "icon": "check", "tone": "good", "with": 2}]}},
    "p04": {"type": "doc", "items": [
        {"label": "Antecedentes · por qué ahora", "icon": "label", "with": 0},
        {"label": "Situación actual · meta", "icon": "chartUp", "with": 0},
        {"label": "Causa raíz · por qué la brecha", "icon": "search", "with": 1},
        {"label": "Contramedidas · plan", "icon": "wrench", "with": 2},
        {"label": "Seguimiento · ¿funcionó?", "icon": "check", "with": 2}]},
    "p05": {"type": "versus", "items": [
        {"label": "Débil", "sub": "“La calidad está mal en todos lados”", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Preciso", "sub": "Línea 2 · el mes pasado · 4.8% contra 1.5%", "icon": "check", "tone": "good", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Gemba", "sub": "Lugar real", "icon": "walk", "with": 0},
        {"label": "Genbutsu", "sub": "Cosas reales", "icon": "chip", "with": 1},
        {"label": "Genjitsu", "sub": "Hechos reales", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 7, "suffix": " / 10", "icon": "chip", "label": "servidores con falla en el banco",
                 "unit": "un módulo de memoria un poco levantado", "with": "example"}},
    "p07": {"type": "flow", "items": [
        {"label": "Definición clara", "icon": "clipboard", "with": 0},
        {"label": "Servidores únicos", "icon": "count", "with": 1},
        {"label": "Horas, números de serie", "icon": "barcode", "with": 2},
        {"label": "El registro coincide con el MES", "icon": "check", "tone": "good", "with": 3}]},
    "p08": {"type": "bars", "label": "", "note": "Fallas en la primera prueba de arranque por cada 1,000 servidores, por semana", "items": [
        {"label": "W1", "value": 41, "with": 0},
        {"label": "W2", "value": 46, "with": 0},
        {"label": "W3", "value": 50, "with": 0},
        {"label": "W4", "value": 55, "tone": "bad", "with": 0}],
        "then": {"type": "bars", "label": "", "note": "Modos de falla: 576 fallas a la primera", "with": 2, "items": [
            {"label": "Memoria", "value": 288, "tone": "bad", "with": 2},
            {"label": "Ventilador", "value": 144, "with": 2},
            {"label": "Red", "value": 86, "with": 2},
            {"label": "Otro", "value": 58, "with": 2}]}},
    "p09": {"type": "icons", "items": [
        {"label": "Meta", "sub": "≤ 2% en 6 semanas", "icon": "pin", "tone": "good", "with": 0},
        {"label": "Límites", "sub": "Tiempo de prueba, repruebas, fugas", "icon": "shield", "with": 1}],
        "then": {"type": "versus", "with": 2, "items": [
            {"label": "Fuera del alcance", "sub": "Aflojar los límites de prueba", "icon": "cross", "tone": "bad", "with": 2},
            {"label": "Dentro del alcance", "sub": "Fallas de memoria, Línea 2", "icon": "check", "tone": "good", "with": 2}]}},
    "p10": {"type": "icons", "items": [
        {"label": "Personas", "icon": "person", "with": 1},
        {"label": "Máquina", "icon": "gear", "with": 1},
        {"label": "Método", "icon": "clipboard", "with": 1},
        {"label": "Material", "icon": "box", "with": 1},
        {"label": "Medición", "icon": "scale", "with": 1},
        {"label": "Medio ambiente", "icon": "wave", "with": 1}]},
    "p11": {"type": "steps", "items": [
        {"label": "Módulo mal asentado", "with": 0},
        {"label": "El seguro cerró muy pronto", "with": 0},
        {"label": "Menos espacio en el chasis nuevo", "with": 0},
        {"label": "Instrucciones sin revisar", "with": "example"}],
        "then": {"type": "stat", "value": 100, "suffix": "%", "icon": "test", "label": "falla reproducida",
                 "unit": "presionando módulos en ángulo", "with": 2}},
    "p12": {"type": "flow", "items": [
        {"label": "Guía de inserción", "icon": "shape", "with": "example"},
        {"label": "Revisión del seguro", "icon": "sensor", "with": "example"},
        {"label": "Revisión en cada cambio de chasis", "icon": "clipboard", "tone": "good", "with": "example"}],
        "then": {"type": "flow", "with": 2, "items": [
            {"label": "Contención", "sub": "Protege al cliente ahora", "icon": "lock", "with": 2},
            {"label": "Contramedida", "sub": "Elimina la causa para siempre", "icon": "key", "tone": "good", "with": 2}]}},
    "p13": {"type": "timeline", "items": [
        {"label": "Confirmar causa, piloto", "sub": "Semanas 1–2", "icon": "test", "with": 1},
        {"label": "Actualizar el SOP, entrenar", "sub": "Semanas 3–4", "icon": "clipboard", "with": 2},
        {"label": "Verificar resultados", "sub": "Semanas 5–6", "icon": "check", "tone": "good", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Base", "value": 4.8}, "after": {"label": "Piloto", "value": 1.6},
            "decimals": 1, "suffix": "%", "unit": "servidores que fallan la primera prueba de arranque",
            "note": "Meta ≤ 2%: cumplida", "with": 1},
    "p15": {"type": "timeline", "items": [
        {"label": "Un problema real, la base", "sub": "Días 1–5", "icon": "walk", "with": "example"},
        {"label": "Causas y piloto", "sub": "Para el día 20", "icon": "search", "with": "example"},
        {"label": "Presenta tu A3", "sub": "Día 30", "icon": "clipboard", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "¿Cuál es el mejor planteamiento de problema para un A3?",
        "options": ["Los operadores son descuidados al poner la memoria",
                    "Las fallas en la primera prueba de arranque de la Línea 2 promediaron 4.8% contra 1.5% "
                    "en 4 semanas",
                    "Necesitamos dos inspectores más en prueba"],
        "correct": 1,
        "explanation": "Nombra la línea, el periodo y la medida, con una referencia, y no afirma ninguna causa. "
                       "Las otras son una culpa y una solución.",
        "q_script": "Prueba rápida. ¿Cuál de estos es el mejor planteamiento de problema para un A3? Tómate "
                    "unos segundos.",
        "a_script": "Es el segundo. Nombra la línea, el periodo y la medida, y no afirma una causa. Los otros "
                    "son una culpa y una solución.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "El piloto de Karthik cumple la meta, pero la tasa de repruebas se duplica. ¿Qué debe "
                    "hacer?",
        "options": ["Estandarizar de todos modos: la meta se cumplió",
                    "Investigar el límite antes de estandarizar",
                    "Subir la meta a 3% por seguridad"],
        "correct": 1,
        "explanation": "Un límite se movió, así que el cambio puede estar ocultando fallas en las repruebas en "
                       "lugar de eliminarlas. Entiéndelo antes de estandarizar.",
        "q_script": "Una más, y esta es un escenario. El piloto de Karthik cumple la meta, pero la tasa de "
                    "repruebas se duplica. ¿Qué debe hacer? Piénsalo.",
        "a_script": "Investiga antes de estandarizar. Un límite se movió, así que la solución puede estar "
                    "ocultando fallas, no eliminándolas.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
