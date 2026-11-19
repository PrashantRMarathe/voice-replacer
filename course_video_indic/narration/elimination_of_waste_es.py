"""elimination_of_waste in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh elimination_of_waste_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ew_es"
NAME = "elimination_of_waste_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Elimination of Waste": "eliminéishon of uéist",
    "TIMWOODS": "tim uúds",
    "Pareto": "Pareto",
    "Gemba": "Guemba",
    "Muda": "Muda",
    "ECRS": "e ce erre ese",
    "FMEA": "efe eme e a",
    "SOP": "ese o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Cada mes, mil quinientas barras de sonido regresaban a retrabajo. Corregir cada una "
    "costaba cuarenta y dos rupias. Nadie lo había sumado nunca. ¿Te suena familiar? En esta "
    "lección aprenderás Elimination of Waste. Verás cómo detectar el trabajo que tu cliente "
    "no pagaría, eliminar su causa, y comprobar la ganancia. Seguiremos a Deepak, gerente de "
    "producción en una línea de barras de sonido."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. El desperdicio es todo lo que tu cliente no pagaría, pero "
    "nunca tus revisiones de seguridad o calidad. Encuéntralo con hechos en el Gemba, no con "
    "opiniones. Y elimina la causa, luego comprueba la ganancia y sostenla. Esta es tu acción "
    "para esta semana. Recorre tu línea durante treinta minutos, y anota tres desperdicios "
    "como hechos. Excelente trabajo al completar esta lección. Ahora aprenderás FMEA, el "
    "análisis de modos de falla y sus efectos."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es de verdad el desperdicio",
        "points": [("Usa recursos, no agrega valor al cliente", "El desperdicio es cualquier actividad"),
                   ("No es un recorte de costos de una vez", "No es un recorte"),
                   ("Elimina la causa, evita que regrese", "eliminas su causa raíz")],
        "example": "La línea de Deepak: 1,500 barras de sonido retrabajadas cada mes.",
        "example_cue": "En la línea de Deepak",
        "script": "Empecemos con una definición. El desperdicio es cualquier actividad que usa tiempo, "
                  "espacio, material o esfuerzo, pero no agrega valor para tu cliente. Eliminarlo no es un "
                  "recorte de costos de una sola vez. Encuentras el desperdicio, eliminas su causa raíz, y "
                  "evitas que regrese. En la línea de Deepak, mil quinientas barras de sonido se "
                  "retrabajaban cada mes. ¿Y cómo decides qué es valor, y qué es desperdicio?",
    },
    {
        "key": "p02", "num": 2, "title": "La prueba del valor",
        "points": [("Cambia el producto", "Cambia el producto"),
                   ("El cliente pagaría por ello", "El cliente pagaría"),
                   ("Hecho bien, a la primera", "Se hace bien"),
                   ("Si no: necesario, o puro desperdicio", "Todo lo demás")],
        "example": "Colocar la bocina: valor. Volver a colocarla después de un zumbido: puro desperdicio.",
        "example_cue": "Colocar la bocina",
        "script": "Usa una prueba simple del valor. Una actividad agrega valor solo cuando se cumplen tres "
                  "cosas. Cambia el producto. El cliente pagaría por ese cambio. Y se hace bien, a la "
                  "primera. Todo lo demás es necesario, como una revisión legal, o puro desperdicio. "
                  "Colocar la bocina es valor. Volver a colocarla después de un zumbido es puro "
                  "desperdicio. ¿Cuánto de tu día pasa esa prueba?",
    },
    {
        "key": "p03", "num": 3, "title": "Por qué importa",
        "points": [("Flujo más rápido, menor tiempo de entrega", "El trabajo fluye más rápido"),
                   ("Menos defectos y menos retrabajo", "Menos defectos"),
                   ("Capacidad liberada, sin gastar más", "Liberas personas"),
                   ("Ideas de quienes hacen el trabajo", "tu gente puede")],
        "example": "La meta de Deepak: liberar capacidad para un modelo nuevo, sin agregar un turno.",
        "example_cue": "Deepak necesitaba",
        "script": "¿Para qué molestarse? Porque el desperdicio esconde tu capacidad. Elimínalo, y el "
                  "trabajo fluye más rápido, así que el tiempo de entrega baja. Menos defectos significa "
                  "menos retrabajo y menos devoluciones. Liberas personas, máquinas, espacio y dinero, sin "
                  "nueva inversión. Y tu gente puede usar sus ideas. Deepak necesitaba espacio para un "
                  "modelo nuevo de barra de sonido, sin agregar un turno. ¿De dónde saldría tu capacidad "
                  "libre?",
    },
    {
        "key": "p04", "num": 4, "title": "Tres reglas de protección",
        "points": [("Las revisiones de seguridad y calidad no son desperdicio", "Nunca llames desperdicio"),
                   ("No le pases el desperdicio a otro", "No le pases el desperdicio"),
                   ("Las personas nunca son el desperdicio", "las personas nunca son")],
        "example": "La prueba final de audio se queda. Protege al cliente.",
        "example_cue": "En la línea de Deepak",
        "script": "Antes de empezar a recortar, tres reglas de protección. Nunca llames desperdicio a una "
                  "revisión de seguridad o de calidad, a menos que una revisión de riesgos lo apruebe. No "
                  "le pases el desperdicio a otro turno, a un proveedor o a tu cliente. Moverlo no es "
                  "eliminarlo. Y las personas nunca son el desperdicio. La habilidad sin usar sí lo es. En "
                  "la línea de Deepak, la prueba final de audio se queda. Protege a cada cliente. ¿Y qué "
                  "desperdicios buscas?",
    },
    {
        "key": "p05", "num": 5, "title": "Los ocho desperdicios",
        "points": [("Transporte, inventario, movimiento, espera", "Transporte, inventario"),
                   ("Sobreproducción, sobreproceso", "sobreproducción"),
                   ("Defectos, habilidades sin usar", "defectos y habilidades sin usar")],
        "example": "Recuérdalos como TIMWOODS.",
        "example_cue": "Recuérdalos como TIMWOODS",
        "script": "Lean agrupa el desperdicio en ocho tipos. Los volverás a ver en la lección de Muda. "
                  "Transporte, inventario, movimiento y espera. Luego sobreproducción, y sobreproceso, que "
                  "significa hacer más de lo que el cliente necesita. Por último, defectos y habilidades "
                  "sin usar. Recuérdalos como TIMWOODS. Cada uno se esconde en algún lugar de cada línea, "
                  "incluida la tuya. La verdadera habilidad no es nombrarlos. Es verlos en tu propia línea. "
                  "¿Y cómo los buscas?",
    },
    {
        "key": "p06", "num": 6, "title": "El recorrido de desperdicios",
        "points": [("Ve al Gemba durante el trabajo normal", "Ve al Gemba"),
                   ("Anota hechos, nunca culpes", "Anota hechos"),
                   ("Dónde, qué, cuánto tiempo, qué tan seguido", "Anota dónde pasó")],
        "example": "Hecho: “Cuatro operadores esperaron 12 minutos por rejillas faltantes.” Opinión: "
                   "“Almacén siempre llega tarde.”",
        "example_cue": "Compara estas dos",
        "script": "Haz un recorrido de desperdicios. Ve al Gemba durante la producción normal, no durante "
                  "una visita. Anota hechos, y nunca culpes a una persona. Anota dónde pasó, qué producto, "
                  "cuánto tiempo y qué tan seguido. Observa a las personas, las piezas y el papeleo. "
                  "Compara estas dos. Cuatro operadores esperaron doce minutos por rejillas faltantes. O, "
                  "almacén siempre llega tarde. Solo la primera te dice dónde buscar, y qué tan grande es. "
                  "¿Cuál puedes corregir de verdad?",
    },
    {
        "key": "p07", "num": 7, "title": "Lo que encontró Deepak",
        "points": [("Esperar kits que llegan tarde", "Los operadores esperaban"),
                   ("Estirarse y caminar por herramientas", "se estiraban y caminaban"),
                   ("Un escaneo de código de barras duplicado", "el mismo código de barras"),
                   ("Retrabajo: barras de sonido con zumbido", "el más grande")],
        "example": "El retrabajo fue el más grande: 1,500 barras de sonido con zumbido al mes.",
        "example_cue": "el más grande",
        "script": "En una hora, el equipo de Deepak llenó una página. Los operadores esperaban kits que "
                  "llegaban tarde. Se estiraban y caminaban por desarmadores en cada ciclo. Empaque "
                  "escaneaba el mismo código de barras dos veces, en dos sistemas distintos. Pero el más "
                  "grande era el retrabajo. Mil quinientas barras de sonido al mes fallaban la prueba de "
                  "zumbido, y regresaban al banco de reparación. ¿Cómo mides cuánto tiempo es de verdad "
                  "valor?",
    },
    {
        "key": "p08", "num": 8, "title": "Medir el flujo",
        "points": [("Eficiencia de flujo = tiempo de valor ÷ tiempo de entrega", "La eficiencia de flujo es"),
                   ("18 min de valor en 240 min", "dieciocho minutos"),
                   ("Solo 7.5% del tiempo agrega valor", "siete y medio")],
        "example": "Una barra de sonido pasa 4 horas en la planta. Solo 18 minutos la cambian.",
        "example_cue": "Una barra de sonido pasa",
        "script": "Ponle un número. La eficiencia de flujo es el tiempo que agrega valor, dividido entre el "
                  "tiempo de entrega total. Una barra de sonido pasa cuatro horas dentro de la planta de "
                  "Deepak. Solo dieciocho minutos de eso la cambian de verdad. Es una eficiencia de flujo "
                  "de siete y medio por ciento. Todo lo demás es esperar, mover, revisar o corregir. No te "
                  "asustes. Es normal al inicio. ¿Pero qué desperdicio atacas primero?",
    },
    {
        "key": "p09", "num": 9, "title": "Encontrar la causa raíz",
        "points": [("Pareto: elige la pérdida más grande", "Usa un Pareto"),
                   ("Pregunta por qué, con evidencia", "Luego pregunta por qué"),
                   ("Corrige la causa, no el síntoma", "Corrige la causa")],
        "example": "Causa raíz: el cable de la bocina no tenía una ruta fija, así que tocaba el cono.",
        "example_cue": "El cable no tenía",
        "script": "Usa un Pareto, y elige primero la pérdida más grande. Para Deepak, era el retrabajo. "
                  "Luego pregunta por qué, con evidencia. ¿Por qué zumbaban las barras de sonido? Un cable "
                  "de la bocina tocaba el cono. ¿Por qué? El cable no tenía una ruta fija, así que cada "
                  "operador lo ponía distinto. Esa es una causa de proceso, no una persona descuidada. "
                  "Corrige la causa, no el síntoma. ¿Y qué contramedida elegirías?",
    },
    {
        "key": "p10", "num": 10, "title": "Contramedidas: ECRS",
        "points": [("Elimina lo innecesario", "Elimina lo que"),
                   ("Combina tareas o revisiones", "Combina tareas"),
                   ("Reordena la secuencia o el acomodo", "Reordena"),
                   ("Simplifica lo que queda", "Simplifica")],
        "example": "Un clip para guiar el cable, carritos de kits en la línea, un escaneo en lugar de dos.",
        "example_cue": "El equipo de Deepak eligió",
        "script": "Piensa en ECRS. Elimina lo que no se necesita. Combina tareas o revisiones que van "
                  "juntas. Reordena la secuencia o el acomodo. Simplifica lo que queda, y hazlo visual. El "
                  "equipo de Deepak eligió tres cambios. Un pequeño clip que guía el cable de la bocina por "
                  "un solo camino. Carritos de kits entregados en la línea cada hora. Y un escaneo en "
                  "empaque en lugar de dos. ¿Qué letra de ECRS corresponde a cada uno?",
    },
    {
        "key": "p11", "num": 11, "title": "El costo de los defectos",
        "points": [("Internos: desecho, retrabajo, reprueba", "Las fallas internas"),
                   ("Externos: devoluciones, garantía, fletes", "Las fallas externas"),
                   ("Cada reparación esconde más desperdicio", "cada reparación")],
        "example": "Retrabajo: ₹42 por barra de sonido, 1,500 al mes.",
        "example_cue": "Cada retrabajo",
        "script": "Los defectos son el desperdicio más caro. Las fallas internas significan desecho, "
                  "retrabajo, reprueba y líneas detenidas. Las fallas externas significan devoluciones, "
                  "reclamos de garantía y fletes urgentes. Y cada reparación esconde más desperdicio, como "
                  "manejo, espera y papeleo. Una barra de sonido con zumbido se abría, se le cambiaba la "
                  "ruta del cable, se volvía a probar y se registraba otra vez. Cada retrabajo en la línea "
                  "de Deepak costaba cuarenta y dos rupias. Con mil quinientas al mes, se sumaba rápido. ¿Y "
                  "funcionó el clip?",
    },
    {
        "key": "p12", "num": 12, "title": "Los resultados",
        "points": [("Retrabajo: de 1,500 a 300 al mes", "El retrabajo bajó"),
                   ("Rendimiento a la primera hasta 99%", "El rendimiento a la primera"),
                   ("Estirarse por herramientas: de 22 s a 13 s", "estirarse por herramientas")],
        "example": "Misma gente, mismo turno. Espacio para el modelo nuevo.",
        "example_cue": "Misma gente",
        "script": "Sí funcionó, después de una prueba de cuatro semanas. El retrabajo bajó de mil "
                  "quinientas a trescientas barras de sonido al mes. El rendimiento a la primera subió a "
                  "noventa y nueve por ciento. Con carritos de kits y herramientas a la mano, estirarse por "
                  "herramientas bajó de veintidós a trece segundos por ciclo. Misma gente, mismo turno, y "
                  "ahora hay espacio para el modelo nuevo. ¿Pero cuánto valía en dinero?",
    },
    {
        "key": "p13", "num": 13, "title": "Comprobar el dinero",
        "points": [("Ahorro = costo evitado − costo de la solución", "El ahorro es"),
                   ("Separa el ahorro duro de la capacidad", "Separa el ahorro duro"),
                   ("Finanzas confirma los números", "Finanzas debe confirmar")],
        "example": "1,200 retrabajos menos × ₹42 × 12 meses ≈ ₹6 lakh. Menos ₹1.2 lakh de la solución: ≈ "
                   "₹4.8 lakh netos.",
        "example_cue": "Mil doscientos retrabajos menos",
        "script": "El ahorro es el costo que evitas, menos lo que costó la solución. Mil doscientos "
                  "retrabajos menos al mes, a cuarenta y dos rupias, durante un año. Son unas seiscientas "
                  "mil rupias. Los clips, los carritos y el cambio de sistema costaron unas ciento veinte "
                  "mil. Así que el beneficio neto del primer año es de unas cuatrocientas ochenta mil "
                  "rupias. Separa el ahorro duro de la capacidad liberada. Y Finanzas debe confirmar los "
                  "números. ¿Cómo haces que se quede?",
    },
    {
        "key": "p14", "num": 14, "title": "Hacer que se quede",
        "points": [("Actualiza el SOP, el acomodo, el entrenamiento", "Actualiza el SOP"),
                   ("Tablero diario: meta, real, brecha, acción", "Un tablero diario"),
                   ("Audita a los 7, 30 y 90 días", "Audita a los siete")],
        "example": "La auditoría de Deepak en el día 30: un turno había dejado de usar el clip. Se corrigió "
                   "el mismo día.",
        "example_cue": "En el día treinta",
        "script": "Haz que la nueva forma sea la forma normal. Actualiza el SOP, el acomodo y el "
                  "entrenamiento. Un tablero diario muestra la meta, lo real, la brecha y la acción, con un "
                  "responsable. Audita a los siete, treinta y noventa días, porque la desviación es "
                  "silenciosa. En el día treinta, un turno había dejado de usar el clip. El equipo de "
                  "Deepak lo encontró, y lo corrigió el mismo día. ¿Tu auditoría lo habría detectado?",
    },
    {
        "key": "p15", "num": 15, "title": "Tu plan de 30 días",
        "points": [("Días 1–7: elige un producto, recorre, mapea", "En la primera semana"),
                   ("Días 8–18: Pareto, causa raíz, piloto", "En los siguientes once días"),
                   ("Días 19–30: mide, estandariza, audita", "En los últimos doce días")],
        "example": "Luego compártelo: otras líneas copian lo que funcionó, después de revisar que encaja.",
        "example_cue": "Luego compártelo",
        "script": "Este es un plan de treinta días que puedes empezar ya. En la primera semana, elige una "
                  "familia de productos, recorre el Gemba, y mapea el flujo. En los siguientes once días, "
                  "usa un Pareto, encuentra la causa raíz, y haz un piloto pequeño. En los últimos doce "
                  "días, mide el resultado, actualiza el estándar, y audítalo. Luego compártelo, para que "
                  "otras líneas copien lo que funcionó. ¿Qué producto vas a recorrer primero?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Sin valor para el cliente", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "No son recortes de una vez", "icon": "calendar", "with": 1},
        {"label": "Elimina la causa", "icon": "key", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 1500, "icon": "wave", "label": "barras de sonido retrabajadas cada mes",
                 "unit": "La línea de Deepak", "with": "example"}},
    "p02": {"type": "steps", "items": [
        {"label": "Cambia el producto", "with": 0},
        {"label": "El cliente pagaría", "with": 1},
        {"label": "Bien a la primera", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Volver a colocar tras un zumbido", "sub": "Puro desperdicio", "icon": "wrench", "tone": "bad", "with": "example"},
            {"label": "Colocar la bocina", "sub": "Valor", "icon": "wave", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Flujo más rápido", "icon": "chartDown", "with": 0},
        {"label": "Menos defectos", "icon": "check", "with": 1},
        {"label": "Capacidad liberada", "icon": "box", "with": 2},
        {"label": "Ideas de la gente", "icon": "person", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Conserva las revisiones de seguridad y calidad", "icon": "shield", "tone": "good", "with": 0},
        {"label": "No pases el desperdicio", "icon": "sequence", "with": 1},
        {"label": "Las personas no son desperdicio", "icon": "person", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Transporte", "icon": "sequence", "with": 0},
        {"label": "Inventario", "icon": "stack", "with": 0},
        {"label": "Movimiento", "icon": "walk", "with": 0},
        {"label": "Espera", "icon": "clock", "with": 0},
        {"label": "Sobreproducción", "icon": "box", "with": 1},
        {"label": "Sobreproceso", "icon": "gear", "with": 1},
        {"label": "Defectos", "icon": "cross", "with": 2},
        {"label": "Habilidades sin usar", "icon": "person", "with": 2}]},
    "p06": {"type": "flow", "items": [
        {"label": "Producción normal", "icon": "walk", "with": 0},
        {"label": "Hechos, sin culpa", "icon": "clipboard", "with": 1},
        {"label": "Dónde · cuánto tiempo · qué tan seguido", "icon": "clock", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "“Almacén siempre llega tarde”", "sub": "Opinión", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "“4 esperaron 12 min por rejillas”", "sub": "Hecho", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Kits tardíos", "icon": "clock", "tone": "bad", "with": 0},
        {"label": "Estirarse por herramientas", "icon": "walk", "tone": "bad", "with": 1},
        {"label": "Doble escaneo", "icon": "barcode", "tone": "bad", "with": 2},
        {"label": "Barras de sonido con zumbido", "icon": "wave", "tone": "bad", "with": 3}]},
    "p08": {"type": "compare", "before": {"label": "Tiempo de entrega", "value": 240}, "after": {"label": "Agrega valor", "value": 18},
            "unit": "minutos por barra de sonido", "note": "Eficiencia de flujo 7.5%", "with": 1},
    "p09": {"type": "steps", "items": [
        {"label": "Las barras de sonido zumban", "with": 1},
        {"label": "El cable toca el cono", "with": 1},
        {"label": "El cable no tiene ruta fija", "with": "example"}]},
    "p10": {"type": "steps", "items": [
        {"label": "Eliminar", "with": 0}, {"label": "Combinar", "with": 1},
        {"label": "Reordenar", "with": 2}, {"label": "Simplificar", "with": 3}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Clip para guiar el cable", "icon": "shape", "tone": "good", "with": "example"},
            {"label": "Carritos de kits cada hora", "icon": "box", "with": "example"},
            {"label": "Un escaneo, no dos", "icon": "barcode", "with": "example"}]}},
    "p11": {"type": "icons", "items": [
        {"label": "Internos", "sub": "Desecho, retrabajo, reprueba", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "Externos", "sub": "Devoluciones, garantía", "icon": "box", "tone": "bad", "with": 1},
        {"label": "Ocultos", "sub": "Manejo, espera, papeleo", "icon": "clock", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 42, "prefix": "₹", "icon": "wrench", "label": "por retrabajo",
                 "unit": "1,500 retrabajos al mes", "with": "example"}},
    "p12": {"type": "compare", "before": {"label": "Antes", "value": 1500}, "after": {"label": "Después", "value": 300},
            "unit": "barras de sonido retrabajadas al mes", "note": "FPY 99% · alcance de herramientas 22 s → 13 s", "with": 0},
    "p13": {"type": "stat", "value": 4.8, "decimals": 1, "prefix": "₹", "suffix": " lakh", "icon": "chartUp",
            "label": "beneficio neto, primer año", "unit": "₹6 lakh evitados − ₹1.2 lakh de la solución", "with": "example"},
    "p14": {"type": "timeline", "items": [
        {"label": "Estándar actualizado", "sub": "Día 0", "icon": "clipboard", "with": 0},
        {"label": "Auditoría", "sub": "Día 7", "icon": "search", "with": 2},
        {"label": "Desviación detectada", "sub": "Día 30", "icon": "warning", "with": "example"},
        {"label": "Auditoría", "sub": "Día 90", "icon": "check", "tone": "good", "with": 2}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Recorrer y mapear", "sub": "Días 1–7", "icon": "walk", "with": 0},
        {"label": "Causa y piloto", "sub": "Días 8–18", "icon": "search", "with": 1},
        {"label": "Comprobar y sostener", "sub": "Días 19–30", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un producto pasa 300 minutos en la planta, pero solo 30 minutos lo cambian. ¿Cuál es la "
                    "eficiencia de flujo?",
        "options": ["10%", "30%", "90%"],
        "correct": 0,
        "explanation": "Eficiencia de flujo = tiempo que agrega valor ÷ tiempo de entrega total = 30 ÷ 300 = "
                       "10%. El otro 90% es esperar, mover, revisar o corregir.",
        "q_script": "Prueba rápida. Un producto pasa trescientos minutos en la planta. Solo treinta minutos "
                    "lo cambian de verdad. ¿Cuál es la eficiencia de flujo? Tómate unos segundos.",
        "a_script": "Es diez por ciento. Divide el tiempo que agrega valor entre el tiempo de entrega total. "
                    "El resto es esperar, mover, revisar o corregir.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Para bajar el tiempo de ciclo, un equipo propone quitar la prueba final de audio. ¿Qué "
                    "debe pasar?",
        "options": ["Quitarla: las pruebas no cambian el producto",
                    "Conservarla a menos que una revisión de riesgos lo apruebe, y reducir los defectos que "
                    "atrapa",
                    "Pasar la prueba a las instalaciones del cliente"],
        "correct": 1,
        "explanation": "Las revisiones de calidad obligatorias no son desperdicio para quitar por capricho. "
                       "Conserva la prueba a menos que una revisión de riesgos apruebe un cambio, y ataca los "
                       "defectos detrás de ella. Pasarla al cliente solo mueve el desperdicio.",
        "q_script": "Una más, y esta es un escenario. Para bajar el tiempo de ciclo, un equipo quiere quitar "
                    "la prueba final de audio. ¿Qué debe pasar? Piénsalo.",
        "a_script": "Conserva la prueba, a menos que una revisión de riesgos apruebe un cambio. Luego ataca "
                    "los defectos que atrapa. Pasarla al cliente solo mueve el desperdicio.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
