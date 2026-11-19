"""cycle_time_study in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh cycle_time_study_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ct_es"
NAME = "cycle_time_study_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Cycle Time Study": "sáikol táim stódi",
    "Design Thinking": "disáin tínkin",
    "Gemba": "Guemba",
    "TAKT": "takt",
    "ECRS": "e ce erre ese",
    "UPH": "u pe hache",
    "FPY": "efe pe ye",
    "SOP": "ese o pe",
    "ESD": "e ese de",
    "A": "a",
    "C": "ce",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "El reporte decía que cada estación era más rápida que veinticuatro segundos. Aun así, la "
    "línea de monitores no cumplía su meta por hora, turno tras turno. ¿Entonces los números "
    "de quién estaban mal? ¿Te suena familiar? En esta lección aprenderás el Cycle Time "
    "Study. Verás cómo tomar bien el tiempo de una estación, encontrar el cuello de botella "
    "real, y corregirlo sin apurar a la gente. Seguiremos a Imran, ingeniero de procesos en "
    "una línea de ensamble de monitores."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Define primero el límite, o tus números no se podrán "
    "comparar. Mira la dispersión, no solo el promedio. Y corrige el método en el cuello de "
    "botella, nunca saltándote revisiones de calidad. Esta es tu acción para esta semana. "
    "Toma el tiempo de diez ciclos en una estación, y compara el más largo con el TAKT. "
    "Excelente trabajo al completar esta lección. Ahora aprenderás Design Thinking."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es el tiempo de ciclo",
        "points": [("Tiempo entre unidades terminadas", "el tiempo entre"),
                   ("En un límite definido", "en un límite que tú defines"),
                   ("Bajo condiciones declaradas", "bajo condiciones que declaras")],
        "example": "El reporte decía que la estación C tardaba 21 segundos. El cronómetro de Imran decía 28.",
        "example_cue": "El reporte decía",
        "script": "Empecemos con una definición clara. El tiempo de ciclo es el tiempo entre una unidad "
                  "terminada y la siguiente. Se mide en un límite que tú defines, bajo condiciones que "
                  "declaras. Suena simple, ¿verdad? Esta es la razón por la que no lo es. El reporte decía "
                  "que la estación de prueba de pantalla tardaba veintiún segundos. Imran se paró ahí con "
                  "un cronómetro, y midió veintiocho. Los dos números eran honestos. ¿Cómo pueden ser "
                  "ciertos los dos?",
    },
    {
        "key": "p02", "num": 2, "title": "Los límites importan",
        "points": [("Tiempo manual: trabajo con las manos", "El tiempo manual es"),
                   ("Tiempo de máquina: prueba, dosificado, curado", "El tiempo de máquina es"),
                   ("Ciclo de estación: el intervalo real de repetición", "El ciclo de estación"),
                   ("Mismo límite, o no hay comparación", "Si dos equipos")],
        "example": "Los 21 segundos venían de tiempos estándar viejos. Los 28 segundos eran el intervalo "
                   "real de unidad a unidad.",
        "example_cue": "El reporte usaba",
        "script": "Porque midieron cosas distintas. El tiempo manual es el trabajo con las manos, como "
                  "atornillar y conectar. El tiempo de máquina es automático, como una prueba o un curado. "
                  "El ciclo de estación es el intervalo real de repetición, con cualquier traslape. No "
                  "puedes simplemente sumarlos. El reporte usaba tiempos estándar viejos, sin reintentos ni "
                  "esperas. Imran midió de un monitor terminado al siguiente. Si dos equipos usan límites "
                  "distintos, sus números no se pueden comparar. ¿Y qué número le importa a tu cliente?",
    },
    {
        "key": "p03", "num": 3, "title": "Tiempo de ciclo contra TAKT, tiempo de entrega, UPH",
        "points": [("Tiempo de ciclo: cada cuánto terminas uno", "El tiempo de ciclo pregunta"),
                   ("TAKT: el ritmo que pide la demanda", "El TAKT pregunta"),
                   ("Tiempo de entrega: de la orden al final, con esperas", "El tiempo de entrega es"),
                   ("UPH: unidades buenas por hora", "El UPH cuenta")],
        "example": "La línea de Imran: TAKT de 24 segundos, así que necesita 150 monitores por hora.",
        "example_cue": "En la línea de Imran",
        "script": "Cuatro medidas suenan parecido, pero responden preguntas distintas. El tiempo de ciclo "
                  "pregunta, ¿cada cuánto terminas uno? El TAKT pregunta, ¿qué ritmo pide la demanda? El "
                  "tiempo de entrega es todo el recorrido, de la orden al final, incluyendo esperas. Puede "
                  "ser de días, aunque tu ciclo sea de segundos. El UPH cuenta unidades buenas por hora. En "
                  "la línea de Imran, el TAKT es de veinticuatro segundos. Son ciento cincuenta monitores "
                  "por hora. ¿Cuáles de estas sigues tú?",
    },
    {
        "key": "p04", "num": 4, "title": "Comparar con el TAKT",
        "points": [("Arriba del TAKT: falta capacidad", "Si el tiempo de ciclo está arriba"),
                   ("Igual al TAKT: sin margen", "Si es igual"),
                   ("Abajo del TAKT: hay margen, no sobreproduzcas", "Si está abajo")],
        "example": "La estación C con 28 segundos está 4 segundos arriba de un TAKT de 24 segundos.",
        "example_cue": "La estación de prueba de pantalla de Imran",
        "script": "Ahora compara tu ciclo con el TAKT. Si el tiempo de ciclo está arriba del TAKT, esa "
                  "estación no puede seguir el paso. Te falta capacidad. Si es igual, no tienes espacio "
                  "para ningún tropiezo o paro. Si está abajo, tienes margen. Pero no lo uses para "
                  "sobreproducir. La estación de prueba de pantalla de Imran estaba en veintiocho segundos. "
                  "Son cuatro segundos arriba del TAKT, en cada ciclo. ¿Y cómo haces un estudio en el que "
                  "puedas confiar?",
    },
    {
        "key": "p05", "num": 5, "title": "Preparar el estudio",
        "points": [("Un propósito y una estación claros", "Elige la estación"),
                   ("Anota las condiciones", "Anota las condiciones"),
                   ("Solo ciclos normales, retrasos registrados", "Separa el arranque"),
                   ("Explícaselo al operador", "Y dile al operador")],
        "example": "La meta de Imran: medir el intervalo de repetición de la estación C para revisar su "
                   "capacidad contra el TAKT.",
        "example_cue": "La meta de Imran era",
        "script": "Un buen estudio empieza con un propósito. Elige la estación, tal vez un posible cuello "
                  "de botella, o una que varía mucho. Anota las condiciones. Eso es el modelo, el operador, "
                  "el turno y las herramientas. Separa el arranque, el cambio de modelo y el retrabajo de "
                  "los ciclos normales. Y dile al operador por qué estás ahí. Estudias el proceso, no lo "
                  "juzgas a él. La meta de Imran era una frase. Revisar la estación C contra el TAKT. "
                  "¿Listo para dividir el trabajo?",
    },
    {
        "key": "p06", "num": 6, "title": "Dividir los elementos",
        "points": [("Divide el trabajo en elementos visibles", "Divide el trabajo"),
                   ("Inicio y final claros para cada uno", "Cada elemento necesita"),
                   ("La espera se registra aparte", "Registra la espera aparte"),
                   ("Nunca recortes revisiones de calidad o seguridad", "Nunca quites")],
        "example": "Estación C: cargar 4 s, escanear etiqueta 3 s, prueba de pantalla 13 s, etiqueta de "
                   "serie 4 s, descargar 3 s, espera 1 s.",
        "example_cue": "Imran dividió la estación C",
        "script": "Divide el trabajo en elementos pequeños que de verdad puedas ver. Cada elemento necesita "
                  "un inicio y un final claros, para no contar nada dos veces. Registra la espera aparte "
                  "del tiempo de trabajo. Luego clasifica cada paso como que agrega valor, necesario, o "
                  "puro desperdicio. Nunca quites una revisión obligatoria de calidad o seguridad. Imran "
                  "dividió la estación C en seis partes. Cargar, escanear la etiqueta, la prueba de "
                  "pantalla, la etiqueta de serie, descargar, y un poco de espera. ¿Dónde mirarías primero?",
    },
    {
        "key": "p07", "num": 7, "title": "La hoja del cronómetro",
        "points": [("Mide ciclos repetidos, no uno", "Mide muchos ciclos"),
                   ("Promedio: 28 s. Rango: de 26 a 32 s", "El promedio fue"),
                   ("Registra cada ciclo anormal", "Registra cada ciclo anormal")],
        "example": "El ciclo más largo: 32 segundos, cuando el escaneo de la etiqueta falló dos veces.",
        "example_cue": "El ciclo más largo",
        "script": "Nunca confíes en un solo ciclo que se ve bien. Mide muchos ciclos seguidos. Imran midió "
                  "diez. El promedio fue de veintiocho segundos. Pero la dispersión iba desde veintiséis "
                  "hasta treinta y dos. Registra cada ciclo anormal, con su razón, no solo el número. El "
                  "ciclo más largo fue cuando el escaneo de la etiqueta falló dos veces. Un promedio solo "
                  "lo habría escondido. ¿Qué esconde tu ciclo más largo?",
    },
    {
        "key": "p08", "num": 8, "title": "Calcular la capacidad",
        "points": [("Producción por hora = 3,600 ÷ tiempo de ciclo", "La producción por hora es"),
                   ("Estación C: unos 129 por hora", "Con veintiocho segundos"),
                   ("Estaciones necesarias = contenido de trabajo ÷ TAKT", "Para saber cuántas")],
        "example": "La demanda pide 150 por hora. La estación C hace unos 129. Esa es la brecha.",
        "example_cue": "La demanda pide",
        "script": "Ahora convierte el tiempo en capacidad. La producción por hora es los segundos de una "
                  "hora, divididos entre tu tiempo de ciclo. Con veintiocho segundos, la estación C hace "
                  "unos ciento veintinueve monitores por hora. La demanda pide ciento cincuenta. Esa es la "
                  "brecha, en números claros. Para saber cuántas estaciones necesitas, divide el contenido "
                  "total de trabajo entre el TAKT, y redondea hacia arriba. Declara cada supuesto. ¿Tu plan "
                  "usa tiempo neto, después de descansos?",
    },
    {
        "key": "p09", "num": 9, "title": "La variación importa",
        "points": [("Los promedios esconden ciclos largos", "los promedios esconden"),
                   ("Grafica los ciclos en orden de tiempo", "Grafica tus ciclos"),
                   ("Nunca borres ciclos largos para verte bien", "Nunca borres"),
                   ("Reporta la dispersión y el % arriba del TAKT", "Reporta el tiempo típico")],
        "example": "Estación C: 3 de 10 ciclos duraron 30 segundos o más.",
        "example_cue": "En la estación C",
        "script": "Aquí hay una trampa. Dos estaciones pueden tener el mismo promedio, y comportarse muy "
                  "distinto. Los promedios esconden los ciclos largos que forman filas. Así que grafica tus "
                  "ciclos en orden de tiempo. Sepáralos por modelo y turno antes de juntarlos. Nunca borres "
                  "ciclos largos solo para mejorar el promedio. Mejor investígalos. Reporta el tiempo "
                  "típico, la dispersión, y qué tan seguido pasas del TAKT. En la estación C, tres de cada "
                  "diez ciclos duraron treinta segundos o más. ¿Te suena familiar?",
    },
    {
        "key": "p10", "num": 10, "title": "Encontrar el cuello de botella",
        "points": [("La estación más lenta marca el ritmo", "La estación más lenta"),
                   ("Busca filas antes, tiempo muerto después", "Busca una fila"),
                   ("Corrige primero la restricción", "Corrige primero la restricción")],
        "example": "Estaciones A 19 s, B 22 s, C 28 s, D 21 s. La estación C limita la línea.",
        "example_cue": "Imran midió las cuatro",
        "script": "¿Y qué estación limita de verdad tu línea? La estación más lenta casi siempre marca el "
                  "ritmo. Busca una fila que se forma frente a ella, y gente esperando después. Imran midió "
                  "las cuatro estaciones. Base y cubierta, colocación de tarjeta, prueba de pantalla y "
                  "empaque. Solo la prueba de pantalla estaba arriba del TAKT. Corrige primero la "
                  "restricción. Acelerar cualquier otra estación solo amontona más trabajo en proceso. ¿Y "
                  "por qué era lenta la estación C?",
    },
    {
        "key": "p11", "num": 11, "title": "¿Por qué es lenta?",
        "points": [("Ve a ver: la estación real", "Imran fue al Gemba"),
                   ("¿Método, diseño, máquina o espera?", "Una estación lenta puede ser"),
                   ("Revisa reintentos, alarmas y horas", "Revisó")],
        "example": "Reintentos en el escaneo de etiquetas, y una etiqueta de serie puesta en la misma "
                   "estación de prueba.",
        "example_cue": "Encontró dos cosas",
        "script": "Imran fue al Gemba, y observó la estación real. Una estación lenta puede ser un problema "
                  "de método, un problema de diseño, una máquina lenta, o simplemente espera. Cada uno "
                  "necesita una solución distinta. Revisó los reintentos de escaneo, los códigos de alarma "
                  "y las horas de prueba. Encontró dos cosas. Las etiquetas quedaban chuecas, así que el "
                  "escáner fallaba seguido. Y el operador también pegaba la etiqueta de serie, ahí mismo, "
                  "dentro del ciclo. ¿Qué intentarías tú?",
    },
    {
        "key": "p12", "num": 12, "title": "Mejorar el método",
        "points": [("Eliminar, combinar, reordenar, simplificar", "Piensa en ECRS"),
                   ("Primero soluciones simples y baratas", "Luego busca"),
                   ("Nunca te saltes pruebas para ahorrar tiempo", "Pero nunca recortes un ciclo")],
        "example": "Una guía de etiquetas endereza cada etiqueta. El escáner lee a la primera.",
        "example_cue": "Imran agregó",
        "script": "Corrige el método antes de pedirle a alguien que vaya más rápido. Piensa en ECRS. "
                  "Eliminar, combinar, reordenar y simplificar. Luego busca soluciones simples y baratas, "
                  "como guías, alimentadores y revisiones de código de barras. Pero nunca recortes un ciclo "
                  "saltándote una prueba, una revisión de torque o el control ESD. Eso no es mejora. Imran "
                  "agregó una pequeña guía de etiquetas. Ahora cada etiqueta queda derecha, y el escáner la "
                  "lee a la primera. ¿Y la etiqueta de serie?",
    },
    {
        "key": "p13", "num": 13, "title": "Rebalancear la línea",
        "points": [("Pasa trabajo a estaciones con tiempo libre", "Pasa trabajo a"),
                   ("Conserva secuencia, habilidades y revisiones", "Revisa la secuencia"),
                   ("Sin nuevas caminatas ni riesgo ergonómico", "Y asegúrate")],
        "example": "Etiqueta de serie pasada a la estación A: A 23 s, C 23 s. Ahora cada estación está abajo "
                   "del TAKT.",
        "example_cue": "Imran pasó la etiqueta de serie",
        "script": "Luego, rebalancea la línea. Pasa trabajo a estaciones con tiempo libre, pero solo si es "
                  "seguro. Revisa la secuencia, las herramientas, las habilidades y las revisiones en la "
                  "nueva estación. Y asegúrate de no agregar caminatas, esfuerzo o riesgo de defectos. "
                  "Imran pasó la etiqueta de serie a la estación A. La estación A quedó en veintitrés "
                  "segundos. La estación C bajó a veintitrés. Ahora cada estación está abajo del TAKT. ¿Es "
                  "el final de la historia?",
    },
    {
        "key": "p14", "num": 14, "title": "Compruébalo y luego estandariza",
        "points": [("Prueba en varios turnos y modelos", "Haz la prueba"),
                   ("Compara dispersión, FPY y producción", "Compara la dispersión"),
                   ("Actualiza el trabajo estándar y entrena", "actualiza el trabajo estándar"),
                   ("Escala rápido cualquier desviación", "Fija un disparador")],
        "example": "Disparador: 3 ciclos seguidos arriba del TAKT significan que el líder de equipo revisa "
                   "la estación.",
        "example_cue": "El disparador de Imran",
        "script": "Todavía no. Una mañana rápida no prueba nada. Haz la prueba en varios turnos y modelos. "
                  "Compara la dispersión, el rendimiento a la primera y la producción, no solo el promedio. "
                  "Si la calidad se mantiene, actualiza el trabajo estándar y entrena a cada turno. Fija un "
                  "disparador, para detectar rápido cualquier desviación. El disparador de Imran era "
                  "simple. Tres ciclos seguidos arriba del TAKT, y el líder de equipo revisa la estación. "
                  "¿Quién revisaría la tuya?",
    },
    {
        "key": "p15", "num": 15, "title": "Tu plan de 30 días",
        "points": [("Semana 1: define y mide la base", "En la semana uno"),
                   ("Semana 2: encuentra el cuello de botella", "En la semana dos"),
                   ("Semana 3: prueba una contramedida", "En la semana tres"),
                   ("Semana 4: verifica, estandariza, entrena", "En la semana cuatro")],
        "example": "La línea de Imran ahora hace 150 monitores por hora, con el mismo rendimiento a la "
                   "primera.",
        "example_cue": "La línea de Imran ahora",
        "script": "Ahora te toca a ti. Este es un plan simple de treinta días. En la semana uno, define el "
                  "límite de una estación, y mide al menos diez ciclos. En la semana dos, encuentra el "
                  "cuello de botella y sus causas. En la semana tres, prueba una contramedida. En la semana "
                  "cuatro, verifícala, actualiza el SOP, y entrena. La línea de Imran ahora hace sus ciento "
                  "cincuenta por hora, y el rendimiento a la primera no se movió. ¿A qué estación le "
                  "tomarás el tiempo primero?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "De unidad a unidad", "icon": "sequence", "with": 0},
        {"label": "Límite definido", "icon": "pin", "with": 1},
        {"label": "Condiciones declaradas", "icon": "clipboard", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "21 s", "sub": "El reporte", "icon": "clipboard", "with": "example"},
            {"label": "28 s", "sub": "El cronómetro de Imran", "icon": "clock", "with": "example"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Manual", "sub": "Trabajo con las manos", "icon": "hand", "with": 0},
        {"label": "Máquina", "sub": "Prueba, dosificado, curado", "icon": "gear", "with": 1},
        {"label": "Ciclo de estación", "sub": "Intervalo real de repetición", "icon": "clock", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Tiempos estándar viejos", "sub": "21 segundos", "icon": "clipboard", "with": "example"},
            {"label": "De unidad a unidad", "sub": "28 segundos", "icon": "sequence", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Tiempo de ciclo", "sub": "Cada cuánto terminas", "icon": "clock", "with": 0},
        {"label": "TAKT", "sub": "Ritmo que pide la demanda", "icon": "wave", "with": 1},
        {"label": "Tiempo de entrega", "sub": "De la orden al final", "icon": "calendar", "with": 2},
        {"label": "UPH", "sub": "Unidades buenas por hora", "icon": "count", "with": 3}],
        "then": {"type": "stat", "value": 150, "icon": "count", "label": "monitores por hora necesarios",
                 "unit": "TAKT de 24 segundos", "with": "example"}},
    "p04": {"type": "ladder", "top": "FALTA CAPACIDAD", "bottom": "MARGEN", "items": [
        {"label": "Arriba del TAKT", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Igual al TAKT", "icon": "scale", "with": 1},
        {"label": "Abajo del TAKT", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
            {"label": "Estación C", "value": 28, "tone": "bad", "with": "example"}]}},
    "p05": {"type": "flow", "items": [
        {"label": "Propósito y estación", "icon": "pin", "with": 0},
        {"label": "Condiciones", "icon": "clipboard", "with": 1},
        {"label": "Solo ciclos normales", "icon": "clock", "with": 2},
        {"label": "Explicar al operador", "icon": "person", "tone": "good", "with": 3}]},
    "p06": {"type": "bars", "label": "", "note": "Elementos de la estación C: 28 s en total", "with": "example", "items": [
        {"label": "Cargar", "value": 4, "with": "example"},
        {"label": "Escanear", "value": 3, "with": "example"},
        {"label": "Prueba", "value": 13, "with": "example"},
        {"label": "Etiqueta de serie", "value": 4, "with": "example"},
        {"label": "Descargar", "value": 3, "with": "example"},
        {"label": "Espera", "value": 1, "tone": "bad", "with": "example"}]},
    "p07": {"type": "bars", "label": "", "note": "Diez ciclos medidos en la estación C (segundos)", "items": [
        {"label": "Más rápido", "value": 26, "tone": "good", "with": 1},
        {"label": "Promedio", "value": 28, "with": 1},
        {"label": "Más lento", "value": 32, "tone": "bad", "with": "example"}]},
    "p08": {"type": "compare", "before": {"label": "Estación C", "value": 129}, "after": {"label": "Demanda", "value": 150},
            "unit": "monitores por hora", "note": "3,600 ÷ 28 ≈ 129", "with": 1},
    "p09": {"type": "icons", "items": [
        {"label": "Los promedios esconden", "icon": "search", "tone": "bad", "with": 0},
        {"label": "Orden de tiempo", "icon": "chartUp", "with": 1},
        {"label": "Conserva los ciclos largos", "icon": "lock", "with": 2},
        {"label": "Dispersión, % arriba del TAKT", "icon": "scale", "with": 3}],
        "then": {"type": "stat", "value": 3, "suffix": " / 10", "icon": "clock", "label": "ciclos de 30 segundos o más",
                 "unit": "estación C", "with": "example"}},
    "p10": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
        {"label": "A", "value": 19, "with": "example"},
        {"label": "B", "value": 22, "with": "example"},
        {"label": "C", "value": 28, "tone": "bad", "with": "example"},
        {"label": "D", "value": 21, "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Método", "icon": "clipboard", "with": 1},
        {"label": "Diseño", "icon": "shape", "with": 1},
        {"label": "Máquina", "icon": "gear", "with": 1},
        {"label": "Espera", "icon": "clock", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Etiquetas chuecas", "icon": "label", "tone": "bad", "with": "example"},
            {"label": "Reintentos de escaneo", "icon": "barcode", "tone": "bad", "with": "example"},
            {"label": "Etiqueta de serie dentro del ciclo", "icon": "sticker", "tone": "bad", "with": "example"}]}},
    "p12": {"type": "steps", "items": [
        {"label": "Eliminar", "with": 0}, {"label": "Combinar", "with": 0},
        {"label": "Reordenar", "with": 0}, {"label": "Simplificar", "with": 0}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Antes", "sub": "Etiquetas chuecas, reintentos de escaneo", "icon": "barcode", "tone": "bad", "with": "example"},
            {"label": "Guía de etiquetas", "sub": "Lee a la primera", "icon": "check", "tone": "good", "with": "example"}]}},
    "p13": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
        {"label": "A", "value": 23, "with": "example"},
        {"label": "B", "value": 22, "with": "example"},
        {"label": "C", "value": 23, "tone": "good", "with": "example"},
        {"label": "D", "value": 21, "with": "example"}]},
    "p14": {"type": "flow", "items": [
        {"label": "Prueba: turnos, modelos", "icon": "calendar", "with": 0},
        {"label": "Dispersión, FPY, producción", "icon": "chartUp", "with": 1},
        {"label": "Trabajo estándar, entrenamiento", "icon": "clipboard", "with": 2},
        {"label": "Disparador: 3 arriba del TAKT", "icon": "warning", "tone": "good", "with": "example"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Definir y medir la base", "sub": "Semana 1", "icon": "clock", "with": 0},
        {"label": "Cuello de botella", "sub": "Semana 2", "icon": "search", "with": 1},
        {"label": "Prueba", "sub": "Semana 3", "icon": "wrench", "with": 2},
        {"label": "Estandarizar", "sub": "Semana 4", "icon": "check", "tone": "good", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "El tiempo de ciclo de una estación es de 30 segundos. ¿Cuál es su producción teórica por "
                    "hora?",
        "options": ["90 unidades", "120 unidades", "180 unidades"],
        "correct": 1,
        "explanation": "Producción por hora = 3,600 ÷ tiempo de ciclo = 3,600 ÷ 30 = 120 unidades por hora, "
                       "antes de cualquier pérdida.",
        "q_script": "Prueba rápida. El tiempo de ciclo de una estación es de treinta segundos. ¿Cuál es su "
                    "producción teórica por hora? Tómate unos segundos.",
        "a_script": "Son ciento veinte. Divide los segundos de una hora entre el tiempo de ciclo, y recuerda, "
                    "eso es antes de cualquier pérdida.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Después de un cambio, el tiempo de ciclo de una estación baja de 28 a 22 segundos, pero "
                    "el rendimiento a la primera cae. ¿Y ahora qué?",
        "options": ["Estandarizarlo: la estación es más rápida",
                    "Detener el cambio y averiguar por qué bajó la calidad",
                    "Agregar un inspector final para atrapar los defectos"],
        "correct": 1,
        "explanation": "Un ciclo más rápido que hace más defectos no es una mejora. Detén el cambio, averigua "
                       "por qué bajó el rendimiento, y estandariza solo cuando la calidad se mantenga.",
        "q_script": "Una más, y esta es un escenario. Después de un cambio, una estación es seis segundos más "
                    "rápida. Pero el rendimiento a la primera cae. ¿Qué debe hacer el equipo? Piénsalo.",
        "a_script": "Detén el cambio, y averigua por qué bajó la calidad. Un ciclo más rápido que hace más "
                    "defectos no es ninguna mejora.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
