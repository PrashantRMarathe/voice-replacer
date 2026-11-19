"""x_matrix in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh x_matrix_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "xm_es"
NAME = "x_matrix_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Hoshin Kanri": "Joshin Kanri",
    "X-Matrix": "équis mátrix",
    "Yamazumi": "Yamazumi",
    "Kaizen": "Káizen",
    "RACI": "rasi",
    "KPI": "ka pe i",
    "BOM": "be o eme",
    "SMED": "esméd",
    "IT": "i te",
    "Plan": "plan",
    "Check": "chek",
    "Act": "akt",
    "Do": "du",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Cuarenta proyectos de mejora. Todos los equipos ocupados. Aun así, la entrega seguía "
    "fallando, trimestre tras trimestre. ¿Te suena familiar? En esta lección aprenderás la "
    "X-Matrix, el corazón de una hoja del Hoshin Kanri. Verás cómo ligar unas pocas metas "
    "grandes a los proyectos y a los números que las comprueban. Seguiremos a Arjun, jefe de "
    "operaciones en una planta de electrónica, mientras convierte un portafolio ocupado en "
    "uno enfocado."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Elige unas pocas prioridades reales, no una lista de "
    "deseos. Liga cada meta a un proyecto, un KPI y un solo responsable. Y revisa con "
    "honestidad, porque los números deben moverse, no solo la gráfica. Esta es tu acción para "
    "esta semana. Escribe un objetivo para tu área como un resultado, no como una actividad. "
    "Excelente trabajo al completar esta lección. Ahora aprenderás Yamazumi, para balancear "
    "el trabajo en tu línea."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "X-Matrix y Hoshin Kanri",
        "points": [("Toda tu estrategia en una hoja", "pone toda tu estrategia"),
                   ("Objetivos → metas → proyectos → indicadores → responsables", "Liga los objetivos de largo plazo"),
                   ("Una lista corta de acciones reales", "Su trabajo es convertir"),
                   ("No es una gráfica para la pared", "No es una gráfica de colores")],
        "example": "Arjun quiere entregas confiables y menos defectos. ¿Puede rastrear esa meta hasta el "
                   "trabajo en el piso?",
        "example_cue": "Arjun quiere entregas confiables",
        "script": "Esta es la idea central. La X-Matrix pone toda tu estrategia en una hoja. Liga los "
                  "objetivos de largo plazo, las metas de este año, los proyectos de mejora, los "
                  "indicadores medibles, y los responsables detrás de ellos. Su trabajo es convertir la "
                  "estrategia en una lista corta de acciones reales. No es una gráfica de colores para "
                  "colgar en la pared. Arjun quiere entregas confiables y menos defectos. ¿Puede rastrear "
                  "esa meta hasta el trabajo en el piso? Primero, ¿de dónde viene el método?",
    },
    {
        "key": "p02", "num": 2, "title": "Origen y alineación",
        "points": [("Hoshin Kanri: gestión de la dirección", "Más o menos, significa"),
                   ("Alinea la dirección con el trabajo diario", "Alinea hacia dónde"),
                   ("Limita las prioridades a lo que puedes darle recursos", "Así que limita tus prioridades"),
                   ("En dos sentidos, no de arriba hacia abajo", "Y mantén la conversación")],
        "example": "La planta de Arjun corría decenas de Kaizen locales — solo unos pocos de verdad ayudaban "
                   "a la entrega al cliente.",
        "example_cue": "Su planta corría decenas",
        "script": "El Hoshin Kanri es un enfoque japonés. Más o menos, significa gestión de la dirección. "
                  "Alinea hacia dónde vas con lo que de verdad haces cada día. La X-Matrix es simplemente "
                  "la imagen de esa alineación. Esta es la trampa que encontró Arjun. Su planta corría "
                  "decenas de Kaizen locales. Solo unos pocos de verdad ayudaban a la entrega al cliente. "
                  "Así que limita tus prioridades a lo que puedes darle recursos. Y mantén la conversación "
                  "en dos sentidos, no de arriba hacia abajo. Ahora, ¿qué va en la hoja?",
    },
    {
        "key": "p03", "num": 3, "title": "Cuatro cuadrantes clave",
        "points": [("Objetivos de avance: 3–5 años", "Primero, los objetivos de avance"),
                   ("Objetivos anuales: este año", "Segundo, los objetivos anuales"),
                   ("Proyectos de mejora", "Tercero, los proyectos de mejora"),
                   ("KPI y metas: la prueba", "Cuarto, los KPI y las metas")],
        "example": "La cadena de Arjun va de una calidad de clase mundial hasta una meta de rendimiento.",
        "example_cue": "La cadena de Arjun va",
        "script": "Una X-Matrix típica tiene cuatro partes ligadas. Primero, los objetivos de avance, a "
                  "tres o cinco años. Segundo, los objetivos anuales, el avance que necesitas este año. "
                  "Tercero, los proyectos de mejora, el trabajo que cambia el desempeño. Cuarto, los KPI y "
                  "las metas, la prueba de que funciona. Los responsables van al lado, en una tabla de "
                  "responsabilidades. Los formatos varían según la plantilla, así que agrega siempre una "
                  "leyenda. La cadena de Arjun va de una calidad de clase mundial hasta una meta de "
                  "rendimiento. Empecemos por arriba.",
    },
    {
        "key": "p04", "num": 4, "title": "Objetivos de avance",
        "points": [("Unos pocos resultados grandes: de 3 a 5", "Elige de tres a cinco"),
                   ("Resultado, horizonte, la base de hoy", "Escribe el resultado"),
                   ("Revisa metas que choquen", "Y revisa metas")],
        "example": "El resultado de Arjun: bajar las devoluciones de clientes dos tercios, mientras crece la "
                   "producción.",
        "example_cue": "Arjun escribió un resultado claro",
        "script": "Los objetivos de avance nombran unos pocos resultados grandes, más allá de la mejora "
                  "normal del día a día. Elige de tres a cinco, no una lista de deseos. Escribe el "
                  "resultado, el horizonte de tiempo, y la base de hoy. Y revisa metas que choquen entre "
                  "sí, como la velocidad contra la seguridad. Arjun escribió un resultado claro. Bajar las "
                  "devoluciones de clientes dos tercios, mientras crece la producción. Nota que es un "
                  "resultado, no una actividad. Lo puedes medir. ¿Y cómo lo divides en este año?",
    },
    {
        "key": "p05", "num": 5, "title": "Objetivos anuales",
        "points": [("Resultados medibles para este año", "Los objetivos anuales convierten"),
                   ("Base, meta, periodo, fuente de datos", "Define la base"),
                   ("Catchball: prueben juntos si es factible", "Luego usa el catchball")],
        "example": "Año uno: una parte de la baja de devoluciones, acordada tras estudiar las fallas en "
                   "campo.",
        "example_cue": "Para el año uno",
        "script": "Los objetivos anuales convierten esa dirección en resultados que puedes medir este año. "
                  "No solo repartas porcentajes redondos. Define la base, la meta, el periodo y la fuente "
                  "de datos. Mantén corta la lista. Luego usa el catchball. Es el ir y venir donde los "
                  "equipos prueban si una meta de verdad es factible. Para el año uno, Arjun busca una "
                  "parte de la baja, no toda. Sus equipos la acordaron después de estudiar las fallas en "
                  "campo. ¿Y qué proyectos te van a llevar ahí?",
    },
    {
        "key": "p06", "num": 6, "title": "Proyectos de mejora",
        "points": [("Problema, alcance, responsable, hitos, revisión", "Uno bueno tiene"),
                   ("Más inspección casi nunca = un gran avance", "Agregar más inspección"),
                   ("Elige con evidencia: impacto contra esfuerzo", "Elige los proyectos con evidencia")],
        "example": "Un interbloqueo de código de barras contra el BOM bloquea componentes equivocados — el "
                   "éxito se declara solo cuando las pruebas y los datos de defectos coinciden.",
        "example_cue": "En la línea de teléfonos de Arjun",
        "script": "Los proyectos son los cambios que mueven tus metas anuales. Uno bueno tiene un "
                  "planteamiento del problema, un alcance, un responsable, hitos, y una forma de verificar "
                  "resultados. Aquí hay un error común. Agregar más inspección casi nunca da un gran "
                  "avance. Elige los proyectos con evidencia, y compara el impacto contra el esfuerzo, el "
                  "costo y el riesgo. En la línea de teléfonos de Arjun, un interbloqueo de código de "
                  "barras contra el BOM bloquea componentes equivocados. Pero él solo declara el éxito "
                  "cuando las pruebas y los datos de defectos coinciden. ¿Cómo sabrás que funciona?",
    },
    {
        "key": "p07", "num": 7, "title": "KPI adelantados y atrasados",
        "points": [("Atrasados: resultados ya obtenidos", "Los indicadores atrasados miden"),
                   ("Adelantados: condiciones que los predicen", "Los indicadores adelantados miden"),
                   ("Define el denominador y la fuente de datos", "Define el denominador de cada uno"),
                   ("No premies números redefinidos", "Y nunca premies")],
        "example": "En la línea de Arjun, el 98% de las unidades pasa a la primera.",
        "example_cue": "En la línea de Arjun",
        "script": "Ese es el trabajo de los KPI. Los indicadores atrasados miden resultados que ya "
                  "obtuviste, como el rendimiento a la primera, las devoluciones y la entrega a tiempo. Los "
                  "indicadores adelantados miden las condiciones que los predicen, como auditorías, "
                  "revisiones de ajuste y entrenamiento. Necesitas los dos. Define el denominador de cada "
                  "uno y su fuente de datos. Y nunca premies un número que solo mejoró porque alguien "
                  "cambió su definición. En la línea de Arjun, el noventa y ocho por ciento de las unidades "
                  "pasa a la primera. ¿Pero qué tan fuerte mueve cada proyecto cada número?",
    },
    {
        "key": "p08", "num": 8, "title": "Fuerza de la relación",
        "points": [("Los símbolos muestran la fuerza del vínculo", "La matriz usa símbolos"),
                   ("Acuerden primero la leyenda", "acuerden primero su leyenda"),
                   ("Califica el vínculo, no la importancia", "Califica el vínculo"),
                   ("Busca huecos y promesas de más", "Luego busca huecos")],
        "example": "El interbloqueo del fixture de Arjun reduce mucho las piezas equivocadas — y casi no "
                   "toca el consumo de energía.",
        "example_cue": "El interbloqueo del fixture de Arjun",
        "script": "La matriz usa símbolos para mostrar qué tan fuerte se ligan dos cosas. Muchas veces un "
                  "círculo lleno significa fuerte, y un círculo vacío significa moderado. Ninguna "
                  "convención es universal, así que acuerden primero su leyenda. Califica el vínculo, no "
                  "qué tan importante se siente la cosa. Luego busca huecos. ¿Hay una meta anual sin ningún "
                  "proyecto detrás? ¿Hay un proyecto que dice ayudar en todo? El interbloqueo del fixture "
                  "de Arjun reduce mucho las piezas equivocadas. Casi no toca el consumo de energía. ¿Y "
                  "quién se asegura de que pase?",
    },
    {
        "key": "p09", "num": 9, "title": "Responsables y catchball",
        "points": [("Un solo responsable para cada uno", "Dale a cada objetivo"),
                   ("Nombra los equipos de apoyo", "Nombra también los equipos de apoyo"),
                   ("RACI: responsable, quien rinde cuentas, consultado, informado", "Quién es responsable"),
                   ("El responsable necesita presupuesto y autoridad", "Asegúrate de que tu responsable")],
        "example": "Automatización de prueba de decodificadores: Ingeniería, Producción, Calidad e IT ayudan "
                   "— un líder de proyecto sigue rindiendo cuentas.",
        "example_cue": "En la automatización de prueba",
        "script": "Las metas fallan cuando la responsabilidad es confusa. Dale a cada objetivo y a cada "
                  "proyecto un solo responsable que rinda cuentas. Nombra también los equipos de apoyo. Esa "
                  "es la idea detrás de RACI. ¿Quién es responsable, quién rinde cuentas, a quién se "
                  "consulta, y a quién se informa? Asegúrate de que tu responsable tenga el presupuesto y "
                  "la autoridad para quitar barreras. En la automatización de prueba de decodificadores de "
                  "Arjun, Ingeniería, Producción, Calidad e IT ayudan. Pero un líder de proyecto sigue "
                  "rindiendo cuentas. Si se atora, sabes a quién preguntar.",
    },
    {
        "key": "p10", "num": 10, "title": "Taller de construcción",
        "points": [("Primero reúne evidencia", "Antes del taller"),
                   ("Alcance, base, objetivos, resultados", "Acuerden el alcance"),
                   ("Proyectos de alto impacto, cada uno con un KPI", "Elige proyectos de alto impacto"),
                   ("Califica vínculos, asigna responsables, fija revisiones", "Por último, califica los vínculos")],
        "example": "En el taller de Arjun, tres departamentos ligaron proyectos a una meta de entrega.",
        "example_cue": "En el taller de Arjun",
        "script": "Construye la matriz desde la estrategia hasta el trabajo real. Antes del taller, reúne "
                  "evidencia sobre clientes, desempeño, capacidad y costo. Luego avanza paso a paso. "
                  "Acuerden el alcance y la base. Elijan unos pocos objetivos de avance. Definan los "
                  "resultados de este año. Elige proyectos de alto impacto, y dale a cada uno un KPI. Por "
                  "último, califica los vínculos, asigna responsables, y fija un ritmo de revisión. En el "
                  "taller de Arjun, tres departamentos ligaron proyectos a una meta de entrega. ¿Cómo se ve "
                  "tu matriz terminada?",
    },
    {
        "key": "p11", "num": 11, "title": "Ejemplo resuelto",
        "points": [("Entrega de 90% → 98%", "la entrega a tiempo pasa"),
                   ("Rendimiento a la primera → 99%", "El rendimiento a la primera sube"),
                   ("Cambio de modelo de 50 → 20 minutos", "El cambio de modelo baja"),
                   ("Planeación, Calidad, Ingeniería son dueñas de uno cada una", "Planeación es dueña de la entrega")],
        "example": "Proyectos: un tablero de preparación, un interbloqueo de código de barras y un piloto de "
                   "SMED.",
        "example_cue": "Los proyectos son",
        "script": "Esta es la matriz terminada de Arjun. Los números son supuestos de entrenamiento. Sus "
                  "grandes avances son entrega confiable, prevención de defectos, y capacidad flexible. "
                  "Este año, la entrega a tiempo pasa del noventa al noventa y ocho por ciento. El "
                  "rendimiento a la primera sube a noventa y nueve. El cambio de modelo baja de cincuenta "
                  "minutos a veinte. Los proyectos son un tablero de preparación, un interbloqueo de código "
                  "de barras, y un piloto de SMED. Planeación es dueña de la entrega, Calidad del "
                  "rendimiento, e Ingeniería del cambio de modelo. ¿Ves cada línea de vista?",
    },
    {
        "key": "p12", "num": 12, "title": "Ritmo de revisión — PDCA",
        "points": [("Una herramienta viva: Plan, Do, Check, Act", "Plan, Do, Check"),
                   ("Diario / semanal: excepciones, hitos", "Cada día y cada semana"),
                   ("Mensual: tendencias de KPI y riesgos", "Cada mes, revisa"),
                   ("Trimestral: ¿sigue apoyando la estrategia?", "Cada trimestre, pregunta")],
        "example": "El rendimiento se estancó aun después del entrenamiento — así que Arjun revisó si el "
                   "control del proceso de verdad cambió.",
        "example_cue": "El rendimiento se estancó",
        "script": "La X-Matrix es una herramienta viva, no un póster. Revísala con Plan, Do, Check, Act. "
                  "Compara los resultados con las metas, encuentra las causas de las brechas, y adapta. "
                  "Cada día y cada semana, sigue las excepciones y los hitos. Cada mes, revisa las "
                  "tendencias de KPI y los riesgos. Cada trimestre, pregunta si cada proyecto sigue "
                  "apoyando la estrategia. Esto es lo que aprendió Arjun. El rendimiento se estancó aun "
                  "después de terminar el entrenamiento. Así que revisó si el control del proceso de verdad "
                  "había cambiado. ¿Qué trampas debes evitar?",
    },
    {
        "key": "p13", "num": 13, "title": "Sí y no",
        "points": [("Unos pocos resultados medibles, responsables claros", "Así que sí mantén unos pocos"),
                   ("Revisa los vínculos causales y los recursos", "Sí revisa los vínculos causales"),
                   ("No todo 'fuertemente ligado'", "no marques cada proyecto"),
                   ("Proyecto terminado ≠ beneficio entregado", "No tomes un proyecto terminado")],
        "example": "Un proyecto se marcó como completo, pero las quejas siguieron igual.",
        "example_cue": "Uno de los proyectos de Arjun",
        "script": "Una matriz se vuelve papeleo muerto muy rápido. Demasiadas metas, palabras vagas y "
                  "vínculos sin revisar lo logran. Así que sí mantén unos pocos resultados medibles con "
                  "responsables claros. Sí revisa los vínculos causales y los recursos detrás de ellos. "
                  "Pero no marques cada proyecto como fuertemente ligado a cada KPI. No tomes un proyecto "
                  "terminado como un beneficio entregado. Y nunca reescribas una base en silencio. Uno de "
                  "los proyectos de Arjun se marcó como completo, pero las quejas siguieron igual. ¿Cómo "
                  "comprobarías el valor real?",
    },
    {
        "key": "p14", "num": 14, "title": "Cuentas de costo y beneficio",
        "points": [("Entrega a tiempo = a tiempo ÷ total por entregar", "La entrega a tiempo es"),
                   ("Baja relativa = baja ÷ tasa anterior", "Una reducción relativa es"),
                   ("Recuperación = inversión ÷ ahorro mensual", "La recuperación es")],
        "example": "Defectos de 2% → 1.2% suena poco — es una baja relativa de 40%. El interbloqueo se paga "
                   "en 6 meses.",
        "example_cue": "Que los defectos bajen del dos",
        "script": "Los beneficios necesitan fórmulas consistentes, o nadie va a confiar en ellos. La "
                  "entrega a tiempo es los embarques a tiempo entre el total por entregar. Una reducción "
                  "relativa es la baja dividida entre la tasa anterior. La recuperación es la inversión "
                  "dividida entre el ahorro mensual verificado. Aquí hay una trampa que vas a encontrar. "
                  "Que los defectos bajen del dos por ciento al uno punto dos suena poco. En realidad es "
                  "una baja relativa del cuarenta por ciento. Y el interbloqueo de Arjun se paga en seis "
                  "meses. ¿Y cómo empiezas mañana?",
    },
    {
        "key": "p15", "num": 15, "title": "Ruta de 90 días",
        "points": [("Días 1–30: bases, borrador de la matriz", "En los primeros treinta días"),
                   ("Días 31–60: catchball, proyectos, responsables", "En los siguientes treinta"),
                   ("Días 61–90: revisar vínculos, revisión, auditoría", "En los últimos treinta")],
        "example": "¿Qué resultado? ¿Qué meta? ¿Qué proyecto? ¿Qué KPI? ¿Quién es dueño del resultado?",
        "example_cue": "Qué resultado importa",
        "script": "Empieza con un piloto, y forma el hábito de revisión antes de extenderlo a todos lados. "
                  "En los primeros treinta días, reúne las bases y haz el borrador de la matriz. En los "
                  "siguientes treinta, haz el catchball, aprueba proyectos, y asigna responsables. En los "
                  "últimos treinta, revisa los vínculos, revisa las brechas, y audita el resultado. Luego "
                  "hazte tus cinco preguntas. ¿Qué resultado importa? ¿Qué meta lo apoya? ¿Qué proyecto "
                  "cambia el proceso? ¿Qué KPI lo comprueba? ¿Y quién es dueño del resultado?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Objetivos de largo plazo", "icon": "chartUp", "with": 1},
        {"label": "Metas de este año", "icon": "calendar", "with": 1},
        {"label": "Proyectos de mejora", "icon": "wrench", "with": 1},
        {"label": "Indicadores y responsables", "icon": "person", "tone": "good", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Gestión de la dirección", "icon": "sequence", "with": 0},
        {"label": "La estrategia se une al trabajo diario", "icon": "calendar", "with": 1}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Decenas de Kaizen locales", "sub": "Pocos ayudaron a la entrega", "icon": "stack", "with": "example"},
            {"label": "Unas pocas prioridades con recursos", "sub": "En dos sentidos, no de arriba hacia abajo", "icon": "key", "with": 2}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Avance", "sub": "3–5 años", "icon": "chartUp", "with": 0},
        {"label": "Anual", "sub": "Este año", "icon": "calendar", "with": 1},
        {"label": "Proyectos", "sub": "El trabajo", "icon": "wrench", "with": 2},
        {"label": "KPI y metas", "sub": "La prueba", "icon": "check", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "De 3 a 5 resultados grandes", "icon": "key", "with": 0},
        {"label": "Resultado, horizonte, base", "icon": "clipboard", "with": 1},
        {"label": "Metas que chocan", "sub": "Velocidad contra seguridad", "icon": "scale", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 2, "suffix": "/3", "icon": "chartDown", "label": "menos devoluciones de clientes",
                 "unit": "Mientras crece la producción: un resultado, no una actividad", "with": "example"}},
    "p05": {"type": "doc", "items": [
        {"label": "Objetivo anual · Año 1", "icon": "label", "with": 0},
        {"label": "Base · meta · periodo", "icon": "clipboard", "with": 1},
        {"label": "Fuente de datos nombrada", "icon": "search", "with": 1},
        {"label": "Catchball: ¿es factible?", "icon": "sequence", "with": 2},
        {"label": "Acordado con las fallas en campo", "icon": "check", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Problema, alcance, responsable", "icon": "clipboard", "with": 0},
        {"label": "Más inspección", "sub": "Casi nunca un gran avance", "icon": "search", "tone": "bad", "with": 1},
        {"label": "Impacto contra esfuerzo", "icon": "scale", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Escanea el código de barras de la pieza", "icon": "barcode", "with": "example"},
            {"label": "Compáralo contra el BOM", "icon": "clipboard", "with": "example"},
            {"label": "¿Pieza equivocada? Bloqueada", "icon": "lock", "tone": "good", "with": "example"}]}},
    "p07": {"type": "versus", "items": [
        {"label": "Atrasados", "sub": "Rendimiento, devoluciones, entrega", "icon": "chartUp", "with": 0},
        {"label": "Adelantados", "sub": "Auditorías, ajustes, entrenamiento", "icon": "search", "with": 1}],
        "then": {"type": "stat", "value": 98, "suffix": "%", "icon": "check", "label": "pasan a la primera",
                 "unit": "Rendimiento a la primera en la línea de Arjun", "with": "example"}},
    "p08": {"type": "matrix", "prefix": "check", "cols": ["Piezas equivocadas", "Rendimiento", "Energía"],
            "note": "Califica el vínculo, no la importancia", "items": [
        {"label": "Interbloqueo", "cells": [3, 3, None], "with": "example"},
        {"label": "Piloto de SMED", "cells": [None, None, 3], "with": "example"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Responsable", "icon": "wrench", "with": 2},
        {"label": "Rinde cuentas", "sub": "Un solo responsable", "icon": "person", "tone": "good", "with": 0},
        {"label": "Consultado", "icon": "search", "with": 2},
        {"label": "Informado", "icon": "clipboard", "with": 2}]},
    "p10": {"type": "steps", "items": [
        {"label": "Evidencia", "with": 0}, {"label": "Alcance, base", "with": 1},
        {"label": "Objetivos", "with": 1}, {"label": "Proyectos + KPI", "with": 2},
        {"label": "Vínculos, responsables", "with": 3}, {"label": "Ritmo de revisión", "with": 3}]},
    "p11": {"type": "compare", "before": {"label": "Hoy", "value": 90}, "after": {"label": "Este año", "value": 98},
            "suffix": "%", "unit": "entrega a tiempo", "note": "Planeación es dueña", "with": 0,
            "then": {"type": "icons", "with": "example", "items": [
                {"label": "Tablero de preparación", "sub": "Entrega", "icon": "chartUp", "with": "example"},
                {"label": "Interbloqueo de código de barras", "sub": "Rendimiento a 99%", "icon": "barcode", "with": "example"},
                {"label": "Piloto de SMED", "sub": "Cambio de modelo 50 → 20 min", "icon": "clock", "with": "example"}]}},
    "p12": {"type": "timeline", "items": [
        {"label": "Excepciones, hitos", "sub": "Diario / semanal", "icon": "calendar", "with": 1},
        {"label": "Tendencias de KPI, riesgos", "sub": "Mensual", "icon": "chartUp", "with": 2},
        {"label": "¿Sigue en la estrategia?", "sub": "Trimestral", "icon": "search", "with": 3}]},
    "p13": {"type": "icons", "items": [
        {"label": "Pocos resultados, responsables claros", "icon": "person", "tone": "good", "with": 0},
        {"label": "Revisar vínculos + recursos", "icon": "check", "tone": "good", "with": 1},
        {"label": "Todo 'fuerte'", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Terminado ≠ entregado", "icon": "warning", "tone": "bad", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Antes", "value": 2}, "after": {"label": "Después", "value": 1.2},
            "decimals": 1, "suffix": "%", "unit": "tasa de defectos", "note": "Una baja relativa de 40% · recuperación en 6 meses", "with": "example"},
    "p15": {"type": "timeline", "items": [
        {"label": "Bases, borrador de la matriz", "sub": "Días 1–30", "icon": "clipboard", "with": 0},
        {"label": "Catchball, proyectos, responsables", "sub": "31–60", "icon": "person", "with": 1},
        {"label": "Revisar vínculos, revisión, auditoría", "sub": "61–90", "icon": "search", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "¿Cuál de estos va en la dimensión de KPI / metas, y no en los objetivos de avance?",
        "options": ["Ser de clase mundial en calidad del producto", "Subir el rendimiento a la primera a 99% este año", "Encantar a cada cliente"],
        "correct": 1,
        "explanation": "Una meta es medible, con un número y una fecha. Los otros son objetivos de dirección, no "
                       "medidas.",
        "q_script": "Prueba rápida. ¿Cuál de estos va en los KPI y las metas, en lugar de los objetivos de "
                    "avance? Tómate unos segundos.",
        "a_script": "Subir el rendimiento a la primera al noventa y nueve por ciento este año. Una meta lleva "
                    "un número y una fecha. Los otros dos son direcciones, no medidas.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "La meta anual de entrega a tiempo de una planta no tiene ningún proyecto ligado. ¿Qué "
                    "debe hacer PRIMERO el equipo?",
        "options": ["Marcar un vínculo fuerte con el proyecto más cercano", "Encontrar o lanzar un proyecto que pueda mover la entrega — o replantear la meta",
                    "Dejarlo; el KPI mejorará solo"],
        "correct": 1,
        "explanation": "Una meta sin proyecto de apoyo es un hueco. Ciérralo con trabajo real, o revisa la meta; "
                       "nunca llenes la casilla con un vínculo que no tenga mecanismo.",
        "q_script": "Una más, y esta es un escenario. La meta anual de entrega de una planta no tiene ningún "
                    "proyecto ligado. ¿Qué debe hacer primero el equipo? Piénsalo.",
        "a_script": "Encuentra o lanza un proyecto que de verdad pueda mover la entrega, o replantea la meta. "
                    "Dibujar un vínculo sin un mecanismo real solo esconde el hueco.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
