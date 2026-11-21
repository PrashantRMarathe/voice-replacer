"""yamazumi in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh yamazumi_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "yz_es"
NAME = "yamazumi_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Zero Defects": "sírou dífects",
    "Yamazumi": "Yamazumi",
    "Heijunka": "Jeiyunka",
    "Gemba": "Guemba",
    "TAKT": "takt",
    "ECRS": "e ce erre ese",
    "SMED": "esméd",
    "ESD": "e ese de",
    "SOP": "ese o pe",
    "A": "a",
    "B": "be",
    "C": "ce",
    "D": "de",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Cada tarde, la celda de decodificadores de Meera se atrasa. Tres operadores esperan, "
    "mientras uno está enterrado en tornillos. Nadie es flojo. El trabajo simplemente está "
    "apilado de forma dispareja. En esta lección aprenderás Yamazumi, una gráfica simple que "
    "muestra exactamente dónde se amontona el trabajo. Y verás cómo Meera rebalancea su línea "
    "con datos reales."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Mide el trabajo real, no el mejor caso. Apílalo contra el "
    "TAKT para ver dónde se amontona. Y rebalancea con cuidado, nunca a costa de la seguridad "
    "o la calidad. Tu acción esta semana: mide una estación de tu línea, y dibuja su barra "
    "contra el TAKT. Excelente trabajo al completar esta lección. Ahora aprenderás Zero "
    "Defects, la última lección del curso."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es Yamazumi",
        "points": [("Una gráfica de barras apiladas del trabajo por estación", "Es una gráfica de barras apiladas"),
                   ("En japonés: 'apilarse'", "La palabra japonesa significa"),
                   ("Cada barra: las tareas de un operador", "Cada barra apila"),
                   ("Arriba de la línea del TAKT = no puede seguir el paso", "Cualquier barra arriba")],
        "example": "La celda de decodificadores de Meera: cuatro operadores, cuatro barras apiladas, una "
                   "línea del TAKT.",
        "example_cue": "Esta es la celda de Meera",
        "script": "¿Y qué es Yamazumi? Es una gráfica de barras apiladas del trabajo en cada estación. La "
                  "palabra japonesa significa apilarse. Cada barra apila las tareas de un operador, en "
                  "segundos. Una línea horizontal marca el tiempo TAKT, el ritmo que necesita tu cliente. "
                  "Cualquier barra arriba de esa línea no puede seguir el paso. Convierte tus estudios de "
                  "tiempos en una conversación de balanceo. Esta es la celda de Meera, con cuatro "
                  "operadores. ¿Ya ves el problema?",
    },
    {
        "key": "p02", "num": 2, "title": "Propósito y beneficios",
        "points": [("Desbalance, esperas, sobrecarga de un vistazo", "Ves el desbalance"),
                   ("Una base objetiva para el personal", "Te da una base objetiva"),
                   ("Muestra dónde ayuda el entrenamiento cruzado", "También muestra dónde"),
                   ("Nunca reemplaza las revisiones de ingeniería", "Pero Yamazumi nunca reemplaza")],
        "example": "Un operador espera mientras otro pelea con un trabajo largo de atornillado — mover una "
                   "tarea pequeña podría suavizar el flujo.",
        "example_cue": "En la celda de Meera",
        "script": "¿Para qué molestarse? Porque la gráfica hace visibles los problemas. Ves el desbalance, "
                  "las esperas y la sobrecarga de un vistazo. Te da una base objetiva para el personal, no "
                  "una corazonada. También muestra dónde ayudaría el entrenamiento cruzado. En la celda de "
                  "Meera, un operador espera mientras otro pelea con un trabajo largo de atornillado. Mover "
                  "una tarea pequeña podría suavizar el flujo. Pero Yamazumi nunca reemplaza las revisiones "
                  "de ingeniería. Primero, necesitas tres tiempos clave.",
    },
    {
        "key": "p03", "num": 3, "title": "TAKT, ciclo y contenido de trabajo",
        "points": [("TAKT: tiempo neto ÷ unidades buenas necesarias", "Es tu tiempo neto disponible"),
                   ("Tiempo de ciclo: cada cuánto sale una unidad", "El tiempo de ciclo es"),
                   ("Contenido de trabajo: la suma de las tareas manuales", "El contenido de trabajo es"),
                   ("Mantén aparte el tiempo de máquina", "Mantén aparte el tiempo de máquina")],
        "example": "420 minutos netos ÷ 840 unidades = TAKT de 30 segundos. La estación B necesita 35.",
        "example_cue": "Meera tiene cuatrocientos",
        "script": "Primero, el tiempo TAKT. Es tu tiempo neto disponible dividido entre las unidades buenas "
                  "que necesita el cliente. El tiempo de ciclo es cada cuánto sale de verdad una unidad de "
                  "una estación. El contenido de trabajo es la suma de las tareas manuales en una unidad. "
                  "Mantén aparte el tiempo de máquina. Meera tiene cuatrocientos veinte minutos netos. La "
                  "demanda es de ochocientas cuarenta unidades. Es un TAKT de treinta segundos. Su estación "
                  "B necesita treinta y cinco. ¿Puede seguir el paso sola?",
    },
    {
        "key": "p04", "num": 4, "title": "Estructura de la gráfica",
        "points": [("Una barra por operador o estación", "Dibujas una barra vertical"),
                   ("Segundos en el lado, línea del TAKT a lo ancho", "El eje vertical"),
                   ("Cada bloque = una tarea, en orden", "Cada bloque de color"),
                   ("Los colores muestran tipos de tarea, no calificaciones", "Los colores muestran tipos de tarea")],
        "example": "La estación A apila 22 segundos; la estación B llega a 35, muy arriba de la línea.",
        "example_cue": "En la gráfica de Meera",
        "script": "Ahora, armemos la gráfica. Dibujas una barra vertical por operador o estación. El eje "
                  "vertical muestra segundos. Una línea horizontal marca el TAKT. Cada bloque de color es "
                  "una tarea, apilada en el orden del trabajo estándar. Los colores muestran tipos de "
                  "tarea, nunca calificaciones de desempeño. Etiqueta cada barra con su muestra y su turno. "
                  "En la gráfica de Meera, la estación A apila veintidós segundos. La estación B llega a "
                  "treinta y cinco, muy arriba de la línea. ¿Y de dónde salen estos números?",
    },
    {
        "key": "p05", "num": 5, "title": "Un estudio de tiempos confiable",
        "points": [("Define dónde empieza y termina cada tarea", "Define dónde empieza"),
                   ("Muchos ciclos, en varios turnos", "Observa muchos ciclos"),
                   ("Registra caminatas, paros, cambios de modelo", "Registra las caminatas"),
                   ("Separa el tiempo de máquina del manual", "Separa el tiempo de máquina")],
        "example": "La carga de firmware corre mientras el operador atornilla, así que Meera mide cada "
                   "elemento por separado.",
        "example_cue": "En la celda de Meera",
        "script": "Salen de la observación real en el Gemba. Tu gráfica es tan buena como sus datos. Define "
                  "dónde empieza y termina cada tarea. Observa muchos ciclos, en varios turnos, no solo el "
                  "más rápido. Registra las caminatas, los paros menores y los cambios de modelo también. "
                  "Separa el tiempo de máquina del manejo manual. En la celda de Meera, la carga de "
                  "firmware corre mientras el operador atornilla. Así que ella mide cada elemento por "
                  "separado. ¿Qué tipos de trabajo vas a encontrar?",
    },
    {
        "key": "p06", "num": 6, "title": "Clasificar el trabajo",
        "points": [("Agrega valor: lo que quiere el cliente", "El trabajo que agrega valor cambia"),
                   ("Necesario sin valor agregado: revisiones, trazabilidad", "El trabajo necesario sin valor agregado"),
                   ("Desperdicio: buscar, caminar, esperar", "El desperdicio es buscar"),
                   ("ECRS — pero conserva las revisiones de calidad y seguridad", "Cuestiona cada paso")],
        "example": "El operador de Meera camina 5 segundos por tornillos. Los contenedores en el punto de "
                   "uso eliminan ese desperdicio.",
        "example_cue": "El operador de Meera camina",
        "script": "Vas a encontrar tres tipos de trabajo. El trabajo que agrega valor cambia el producto "
                  "como lo quiere el cliente. El trabajo necesario sin valor agregado cubre las revisiones "
                  "obligatorias y la trazabilidad. El desperdicio es buscar, caminar y esperar. Cuestiona "
                  "cada paso con ECRS: eliminar, combinar, reordenar, simplificar. Pero nunca quites una "
                  "revisión obligatoria de calidad o seguridad. El operador de Meera camina cinco segundos "
                  "por tornillos. Los contenedores en el punto de uso eliminan ese desperdicio. Ahora "
                  "puedes mapear el estado actual.",
    },
    {
        "key": "p07", "num": 7, "title": "Armar el estado actual",
        "points": [("Demanda aprobada → TAKT", "Empieza con la demanda aprobada"),
                   ("Una barra por estación, línea del TAKT trazada", "Arma una barra por estación"),
                   ("Compara la gráfica con la realidad", "Luego recorre el piso"),
                   ("Una barra corta ≠ capacidad libre", "una barra corta no prueba")],
        "example": "TAKT de 30 s: A = 22, B = 35, C = 27, D = 20. B va 5 segundos arriba — la primera "
                   "prioridad.",
        "example_cue": "Este es el estado actual de Meera",
        "script": "Empieza con la demanda aprobada, y calcula el TAKT. Arma una barra por estación, apila "
                  "cada tarea, y traza la línea del TAKT. Luego recorre el piso y compara la gráfica con la "
                  "realidad. Este es el estado actual de Meera. La estación A corre veintidós segundos, y "
                  "la B corre treinta y cinco. La C corre veintisiete, y la D corre veinte. La estación B "
                  "va cinco segundos arriba del TAKT. Esa es su primera prioridad. Y recuerda, una barra "
                  "corta no prueba que tengas capacidad libre.",
    },
    {
        "key": "p08", "num": 8, "title": "Balancear la línea",
        "points": [("Mueve tareas o mejora los métodos", "Balancear significa mover"),
                   ("No barras perfectamente iguales", "La meta no son barras perfectamente iguales"),
                   ("Respeta acomodo, secuencia, habilidades, revisiones", "Debes respetar el acomodo"),
                   ("Prueba ECRS antes de agregar gente", "Prueba ECRS")],
        "example": "Una tarea de etiquetado de 5 segundos pasa de B a D: B = 30, D = 25. Luego piloto y "
                   "volver a medir.",
        "example_cue": "Meera encuentra una tarea de cinco segundos",
        "script": "Balancear significa mover tareas factibles, o mejorar métodos, para que cada estación "
                  "pueda sostener el ritmo. La meta no son barras perfectamente iguales. Debes respetar el "
                  "acomodo, la secuencia de tareas, los fixtures, las habilidades y las revisiones de "
                  "calidad. Prueba ECRS antes de agregar gente. Meera encuentra una tarea de cinco segundos "
                  "de etiquetado que no depende del resto del trabajo de B. La pasa a la estación D. B baja "
                  "a treinta, y D sube a veinticinco. Luego hace un piloto y vuelve a medir.",
    },
    {
        "key": "p09", "num": 9, "title": "Personal y eficiencia",
        "points": [("Trabajo manual ÷ TAKT, redondea hacia arriba", "Suma el trabajo manual"),
                   ("Eficiencia de balance: trabajo contra capacidad", "La eficiencia de balance compara"),
                   ("Un piso de planeación, no una promesa", "Tómalo como un piso de planeación"),
                   ("Comprueba la producción antes de recortar gente", "Nunca recortes operadores")],
        "example": "104 segundos de trabajo con un TAKT de 30 segundos = 4 operadores; eficiencia de unos "
                   "87%.",
        "example_cue": "La celda de Meera tiene ciento",
        "script": "¿Cuánta gente necesitas de verdad? Suma el trabajo manual, divide entre el TAKT, y "
                  "redondea hacia arriba. La celda de Meera tiene ciento cuatro segundos de trabajo. Con un "
                  "TAKT de treinta segundos, son cuatro operadores. La eficiencia de balance compara el "
                  "trabajo asignado con la capacidad del personal. La suya es de unos ochenta y siete por "
                  "ciento. Tómalo como un piso de planeación, no como una promesa. Nunca recortes "
                  "operadores antes de comprobar la producción buena, con seguridad y de forma consistente.",
    },
    {
        "key": "p10", "num": 10, "title": "Cuellos de botella y máquinas",
        "points": [("No toda barra larga es un cuello de botella del operador", "No toda barra larga"),
                   ("Las máquinas compartidas necesitan su propia revisión", "Las máquinas pueden correr"),
                   ("Separa manual, automático, carga, espera", "Separa el tiempo manual"),
                   ("Ajusta por tiempo en marcha, cambios, rendimiento", "Luego ajusta por el tiempo en marcha")],
        "example": "Dos probadores de audio: 160 unidades/hora en papel — unas 140 buenas en la realidad.",
        "example_cue": "Mira los dos probadores",
        "script": "Este es un error común. No toda barra larga es un cuello de botella del operador. Las "
                  "máquinas pueden correr mientras la gente trabaja, así que el equipo compartido necesita "
                  "su propia revisión de capacidad. Separa el tiempo manual, el ciclo automático, la carga "
                  "y la espera. Luego ajusta por el tiempo en marcha, los cambios de modelo y el "
                  "rendimiento a la primera. Mira los dos probadores de la línea de audio en pantalla. En "
                  "papel, manejan ciento sesenta unidades por hora. En la realidad, son unas ciento "
                  "cuarenta buenas. ¿Lo habrías planeado así?",
    },
    {
        "key": "p11", "num": 11, "title": "Líneas de modelos mezclados",
        "points": [("Una sola gráfica puede esconder problemas", "Entonces una sola gráfica puede esconder"),
                   ("Barras por modelo, el peor caso", "Así que usa barras por modelo"),
                   ("Personal flexible y calificado", "Planea personal flexible y calificado"),
                   ("Heijunka y SMED suavizan la mezcla", "Y usa el Heijunka")],
        "example": "Promedia 27 s en la mezcla, pero 42 s en el modelo de audio — un lote largo amontona "
                   "trabajo rápido.",
        "example_cue": "Una estación podría promediar",
        "script": "¿Y si tu línea arma varios modelos? Entonces una sola gráfica puede esconder problemas. "
                  "Una estación podría promediar veintisiete segundos en la mezcla. Pero en el modelo de "
                  "audio, necesita cuarenta y dos. Corre un lote largo de ese modelo, y el trabajo se "
                  "amontona rápido. Así que usa barras por modelo, y revisa el peor caso. Planea personal "
                  "flexible y calificado. Y usa el Heijunka y el SMED para suavizar la mezcla. ¿Y cómo "
                  "sabes que un nuevo balance de verdad funcionó?",
    },
    {
        "key": "p12", "num": 12, "title": "KPI y verificación",
        "points": [("Una gráfica balanceada es una hipótesis", "Una gráfica balanceada es solo"),
                   ("Adelantados: cumplimiento del trabajo estándar", "Vigila las medidas adelantadas"),
                   ("Atrasados: producción buena, defectos, UPPH", "Vigila las atrasadas"),
                   ("Revisa la ergonomía con los operadores", "revisa la ergonomía")],
        "example": "El cumplimiento del plan cuenta las unidades buenas contra el plan; el rendimiento a la "
                   "primera cuenta las unidades que pasan a la primera.",
        "example_cue": "El cumplimiento del plan cuenta",
        "script": "Una gráfica balanceada es solo una hipótesis. La compruebas con resultados. Vigila las "
                  "medidas adelantadas, como el cumplimiento del trabajo estándar. Vigila las atrasadas, "
                  "como la producción buena, los defectos y las unidades por hora-persona. Mantén "
                  "consistentes tus definiciones. En pantalla, dos medidas se parecen pero significan cosas "
                  "distintas. El cumplimiento del plan cuenta las unidades buenas contra el plan. El "
                  "rendimiento a la primera cuenta las unidades que pasan a la primera. Y después de "
                  "cualquier cambio, revisa la ergonomía con tus operadores.",
    },
    {
        "key": "p13", "num": 13, "title": "Caso: celda de decodificadores",
        "points": [("Antes: B limitaba la producción cerca de 103/hora", "Antes, la estación B limitaba"),
                   ("Después: B baja a 30 segundos", "Después del piloto"),
                   ("Unas 116 buenas/hora contra 120 teóricas", "La producción subió"),
                   ("Terminado solo después de dos semanas estables", "Solo lo dio por terminado")],
        "example": "Quedar abajo de 120 es normal: el tiempo en marcha y el rendimiento siempre cuestan "
                   "algo.",
        "example_cue": "Y eso es normal",
        "script": "Veamos cómo resultó el cambio de Meera. Antes, la estación B limitaba la celda cerca de "
                  "ciento tres unidades por hora. Después del piloto, la estación B bajó a treinta "
                  "segundos. La producción subió a unas ciento dieciséis unidades buenas por hora. Es menos "
                  "que las ciento veinte teóricas. Y eso es normal, porque el tiempo en marcha y el "
                  "rendimiento siempre cuestan algo. Solo lo dio por terminado después de dos semanas "
                  "estables. ¿Qué revisarías después?",
    },
    {
        "key": "p14", "num": 14, "title": "Sí y no",
        "points": [("Mide el trabajo real, mantén los datos al día", "Mide el trabajo real"),
                   ("Involucra a operadores, Calidad, Ingeniería", "Involucra a los operadores"),
                   ("Protege seguridad, ESD, pruebas, trazabilidad", "Protege la seguridad, el ESD"),
                   ("Sin tiempos del mejor caso, sin recortar personal", "No uses tiempos de ciclo del mejor caso")],
        "example": "Quitar una revisión de código de barras parece ahorrar 6 segundos. No es un balance — es "
                   "un riesgo de trazabilidad.",
        "example_cue": "Quitar una revisión de código de barras",
        "script": "Unas reglas firmes. Mide el trabajo real, y mantén tus datos al día. Involucra a los "
                  "operadores, a Calidad y a Ingeniería. Protege la seguridad, el ESD, las pruebas y la "
                  "trazabilidad. No uses tiempos de ciclo del mejor caso. Y no conviertas Yamazumi en una "
                  "herramienta para recortar personal, o la gente deja de compartir datos reales. Aquí hay "
                  "una trampa. Quitar una revisión de código de barras parece ahorrar seis segundos. No es "
                  "un balance. Es un riesgo de trazabilidad. ¿Tu equipo lo notaría?",
    },
    {
        "key": "p15", "num": 15, "title": "Ruta de 90 días",
        "points": [("Días 1–30: línea piloto, estudios de tiempos, base", "En los primeros treinta días"),
                   ("Días 31–60: ECRS, rebalancear, calificar", "En los siguientes treinta"),
                   ("Días 61–90: verificar, actualizar los SOP, extender", "En los últimos treinta"),
                   ("Mantén las gráficas al día", "Luego mantén tus gráficas al día")],
        "example": "Una gráfica desactualizada es peor que no tener gráfica.",
        "example_cue": "Una gráfica desactualizada",
        "script": "¿Listo para empezar? Este es un plan de noventa días. En los primeros treinta días, "
                  "elige una línea piloto, reúne la demanda y los estudios de tiempos, y arma las gráficas "
                  "base. En los siguientes treinta, haz talleres de ECRS, rebalancea y califica a los "
                  "operadores. En los últimos treinta, verifica el rendimiento y la producción, actualiza "
                  "los SOP, y extiende a líneas parecidas. Luego mantén tus gráficas al día cada vez que "
                  "cambien la demanda, la mezcla o el personal. Una gráfica desactualizada es peor que no "
                  "tener gráfica.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson). Station bars use the
# current state from p07 (TAKT 30 s).
CURRENT = [("A", 22, None), ("B", 35, "bad"), ("C", 27, None), ("D", 20, None)]


def takt_bars(stations, note, unit, with_="example"):
    return {"type": "bars", "label": "TAKT", "value": 30, "suffix": " s", "note": note, "unit": unit,
            "with": with_, "items": [{"label": f"estación {s}", "value": v, "tone": t, "with": with_}
                                     for s, v, t in stations]}


VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Barras apiladas", "icon": "stack", "with": 0},
        {"label": "'Apilarse'", "icon": "box", "with": 1},
        {"label": "Las tareas de un operador", "icon": "person", "with": 2},
        {"label": "Arriba del TAKT: no sigue el paso", "icon": "warning", "tone": "bad", "with": 3}],
        "then": takt_bars(CURRENT, "B no puede seguir el paso", "La celda de Meera: segundos de trabajo en cada estación")},
    "p02": {"type": "icons", "items": [
        {"label": "Desbalance de un vistazo", "icon": "search", "with": 0},
        {"label": "Personal basado en hechos", "icon": "person", "with": 1},
        {"label": "Dónde entrenar en varios puestos", "icon": "sequence", "with": 2},
        {"label": "Las revisiones de ingeniería siguen siendo necesarias", "icon": "wrench", "tone": "bad", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Trabajo largo de atornillado", "sub": "Sobrecarga", "icon": "screw", "with": "example"},
            {"label": "Quita una tarea pequeña", "sub": "Flujo suave", "icon": "sequence", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Tiempo neto ÷ unidades buenas", "icon": "clock", "with": 0},
        {"label": "Tiempo de ciclo", "sub": "Cada cuánto sale una", "icon": "sequence", "with": 1},
        {"label": "Contenido de trabajo", "sub": "Suma de las tareas manuales", "icon": "hand", "with": 2},
        {"label": "Tiempo de máquina", "sub": "Aparte", "icon": "gear", "with": 3}],
        "then": {"type": "stat", "value": 30, "suffix": " s", "icon": "clock", "label": "Tiempo TAKT",
                 "unit": "420 minutos netos ÷ 840 unidades", "with": "example"}},
    "p04": takt_bars([("A", 22, None), ("B", 35, "bad")], "B está arriba de la línea",
                     "Una barra por estación, línea del TAKT horizontal", with_=0),
    "p05": {"type": "flow", "items": [
        {"label": "Define inicio y fin", "icon": "pin", "with": 0},
        {"label": "Muchos ciclos, cada turno", "icon": "clock", "with": 1},
        {"label": "Caminatas, paros, cambios de modelo", "icon": "walk", "with": 2},
        {"label": "Máquina, aparte de lo manual", "icon": "gear", "tone": "good", "with": 3}]},
    "p06": {"type": "icons", "items": [
        {"label": "Agrega valor", "icon": "check", "tone": "good", "with": 0},
        {"label": "Necesario: revisiones, trazabilidad", "icon": "shield", "with": 1},
        {"label": "Desperdicio: buscar, caminar, esperar", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "ECRS, conserva las revisiones", "icon": "wrench", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "5 s de caminata por tornillos", "sub": "Desperdicio", "icon": "walk", "with": "example"},
            {"label": "Contenedores en el punto de uso", "sub": "Caminata eliminada", "icon": "tray", "with": "example"}]}},
    "p07": takt_bars(CURRENT, "B va 5 s arriba: primera prioridad", "El estado actual de Meera"),
    "p08": {"type": "icons", "items": [
        {"label": "Mueve trabajo, mejora el método", "icon": "sequence", "with": 0},
        {"label": "No exactamente iguales", "icon": "scale", "with": 1},
        {"label": "Acomodo, secuencia, habilidad, revisiones", "icon": "clipboard", "with": 2},
        {"label": "ECRS antes que más gente", "icon": "person", "with": 3}],
        "then": takt_bars([("A", 22, None), ("B", 30, "good"), ("C", 27, None), ("D", 25, None)],
                          "Etiquetado de 5 s B → D", "Después del cambio: piloto, y volver a medir")},
    "p09": {"type": "stat", "value": 4, "suffix": " operadores", "icon": "person", "label": "104 s de trabajo ÷ TAKT de 30 s, redondeado hacia arriba",
            "unit": "Eficiencia de balance de unos 87%", "with": "example"},
    "p10": {"type": "icons", "items": [
        {"label": "Barra larga ≠ problema del operador", "icon": "person", "with": 0},
        {"label": "Máquinas compartidas", "icon": "gear", "with": 1},
        {"label": "Manual · automático · carga · espera", "icon": "clock", "with": 2},
        {"label": "Tiempo en marcha, cambios, rendimiento", "icon": "chartDown", "with": 3}],
        "then": {"type": "compare", "before": {"label": "En papel", "value": 160}, "after": {"label": "Reales, buenas", "value": 140},
                 "unit": "unidades por hora, dos probadores de audio", "note": "Planea con el número real", "with": "example"}},
    "p11": {"type": "bars", "label": "TAKT", "value": 30, "suffix": " s", "note": "El promedio lo esconde",
            "unit": "Una estación, segundos por unidad", "with": "example", "items": [
        {"label": "Promedio de la mezcla", "value": 27, "with": "example"},
        {"label": "Modelo de audio", "value": 42, "tone": "bad", "with": "example"}]},
    "p12": {"type": "icons", "items": [
        {"label": "Una hipótesis por comprobar", "icon": "test", "with": 0},
        {"label": "Adelantado: trabajo estándar", "icon": "clipboard", "with": 1},
        {"label": "Atrasado: producción, defectos, UPPH", "icon": "chartUp", "with": 2},
        {"label": "Ergonomía con los operadores", "icon": "person", "with": 3}]},
    "p13": {"type": "compare", "before": {"label": "Antes", "value": 103}, "after": {"label": "Después", "value": 116},
            "unit": "unidades buenas por hora (teoría: 120)", "note": "Terminado tras dos semanas estables", "with": 2},
    "p14": {"type": "icons", "items": [
        {"label": "Trabajo real, datos al día", "icon": "clock", "tone": "good", "with": 0},
        {"label": "Operadores, Calidad, Ingeniería", "icon": "person", "tone": "good", "with": 1},
        {"label": "Seguridad, ESD, pruebas, trazabilidad", "icon": "shield", "tone": "good", "with": 2},
        {"label": "Mejor caso, recortar gente", "icon": "cross", "tone": "bad", "with": 3}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Línea piloto, estudios de tiempos, base", "sub": "Días 1–30", "icon": "clock", "with": 0},
        {"label": "ECRS, rebalanceo, calificación", "sub": "31–60", "icon": "sequence", "with": 1},
        {"label": "Verificar, actualizar el SOP, extender", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "La estación 4 corre 33 s contra un TAKT de 30 segundos; la estación 1 corre 22 s. ¿Qué "
                    "debes probar primero?",
        "options": ["Pedirle al operador de la estación 4 que trabaje más rápido",
                    "Pasar una tarea factible de la estación 4 a la estación 1, o mejorar su método, y luego "
                    "hacer un piloto y volver a medir",
                    "Quitar una revisión de calidad en la estación 4",
                    "Cambiar el TAKT a 33 segundos"],
        "correct": 1,
        "explanation": "Balancear mueve trabajo factible o mejora el método. Presionar a la gente, quitar "
                       "revisiones o redefinir el TAKT esconde el problema en lugar de corregirlo.",
        "q_script": "Prueba rápida, y es un escenario. La estación cuatro corre treinta y tres segundos "
                    "contra un TAKT de treinta segundos. La estación uno corre veintidós. ¿Qué debes probar "
                    "primero? Tómate unos segundos.",
        "a_script": "Busca una tarea factible para pasar de la estación cuatro a la estación uno, o mejora su "
                    "método. Luego haz un piloto y vuelve a medir. Presionar a la gente o quitar revisiones "
                    "no es balancear.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "420 minutos netos atienden una demanda de 840 unidades buenas. ¿Cuál es el tiempo TAKT?",
        "options": ["20 segundos por unidad",
                    "30 segundos por unidad",
                    "2 segundos por unidad",
                    "60 segundos por unidad"],
        "correct": 1,
        "explanation": "TAKT = tiempo neto ÷ demanda = 420 × 60 ÷ 840 = 30 segundos por unidad.",
        "q_script": "Una más. Tu línea tiene cuatrocientos veinte minutos netos. La demanda es de ochocientas "
                    "cuarenta unidades buenas. ¿Cuál es tu tiempo TAKT? Piénsalo.",
        "a_script": "Son treinta segundos por unidad. Convierte los minutos a segundos, y luego divide entre "
                    "la demanda.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
