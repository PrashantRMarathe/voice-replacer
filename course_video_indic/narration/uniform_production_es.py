"""uniform_production in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh uniform_production_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "up_es"
NAME = "uniform_production_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Heijunka": "Jeiyunka",
    "Kanban": "Kanban",
    "Mura": "Mura",
    "Muri": "Muri",
    "Muda": "Muda",
    "TAKT": "takt",
    "EPEI": "e pe e i",
    "SMED": "esméd",
    "WIP": "doble u i pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Lunes, tres mil teléfonos. Martes, casi nada. Para el miércoles, el banco de prueba se "
    "ahoga y la cuenta de horas extra sube. ¿Te suena familiar? En esta lección aprenderás la "
    "producción uniforme. Verás cómo nivelar el volumen y la mezcla, para que tu línea corra "
    "a un ritmo estable que de verdad pueda sostener. Seguiremos a Kavya, planeadora de "
    "producción en una planta de electrónica, mientras calma un programa muy disparejo."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Nivela el volumen y la mezcla, para seguir la demanda real. "
    "Revisa los cuellos de botella y los cambios de modelo antes de confiar en un patrón. Y "
    "haz visible el plan, con reglas claras para cuando las cosas cambien. Esta es tu acción "
    "para esta semana. Busca un producto que armas en un lote grande, y dibuja un patrón más "
    "pequeño que se repita. Excelente trabajo al completar esta lección. Ahora vas a mapear "
    "todo tu flujo de valor."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué significa la producción uniforme",
        "points": [("Nivelar — Heijunka", "La producción uniforme significa nivelar"),
                   ("Suavizar el volumen y la mezcla", "Suavizas el volumen"),
                   ("Un patrón de liberación estable", "Los pedidos irregulares se vuelven"),
                   ("Seguir la demanda real, no cantidades iguales", "Pero nivelar no significa")],
        "example": "La planta de Kavya hace teléfonos, decodificadores y equipos de audio — en secuencias "
                   "pequeñas que se repiten, no todos los teléfonos primero.",
        "example_cue": "La planta de Kavya hace",
        "script": "Esta es la idea central. La producción uniforme significa nivelar. Lean lo llama "
                  "Heijunka. Suavizas el volumen y la mezcla de lo que armas, durante un periodo fijo. Los "
                  "pedidos irregulares se vuelven un patrón de liberación estable que tu línea de verdad "
                  "puede cumplir. Pero nivelar no significa hacer cantidades iguales de todo. Significa "
                  "ajustar la mezcla y el ritmo a la demanda real. La planta de Kavya hace teléfonos, "
                  "decodificadores y equipos de audio. En lugar de todos los teléfonos primero, planea "
                  "secuencias pequeñas que se repiten. ¿Por qué importa eso?",
    },
    {
        "key": "p02", "num": 2, "title": "Por qué importa nivelar",
        "points": [("La demanda nunca llega pareja", "La demanda casi nunca llega"),
                   ("Perseguir picos: horas extra, inventario, calidad inestable", "Si persigues cada pico"),
                   ("Nivelar suaviza dentro de una ventana de planeación", "Nivelar suaviza tus liberaciones"),
                   ("Todavía necesitas algo de colchón", "todavía necesitarás algo de colchón")],
        "example": "Un pedido grande de teléfonos llegó el lunes. Kavya lo repartió en la semana, como lo "
                   "permitía la fecha de entrega.",
        "example_cue": "La semana pasada, un pedido grande de teléfonos",
        "script": "La demanda casi nunca llega pareja. Si persigues cada pico, tienes horas extra, montones "
                  "de producto terminado, proveedores presionados, y una calidad inestable. Nivelar suaviza "
                  "tus liberaciones dentro de una ventana de planeación acordada. No borra las variaciones "
                  "de la demanda, y todavía necesitarás algo de colchón. La semana pasada, un pedido grande "
                  "de teléfonos llegó el lunes. Kavya no lo armó todo ese día. Lo repartió en la semana, "
                  "porque la fecha de entrega lo permitía. ¿Y qué sale mal exactamente cuando el trabajo es "
                  "disparejo?",
    },
    {
        "key": "p03", "num": 3, "title": "Mura, Muri y Muda",
        "points": [("Mura: disparidad", "Mura es disparidad"),
                   ("Muri: sobrecarga", "Muri es sobrecarga"),
                   ("Muda: desperdicio", "Muda es desperdicio")],
        "example": "El probador maneja ~2,000 unidades al día; ensamble liberó más de 3,000 para prueba en "
                   "un día — se formó una fila.",
        "example_cue": "El probador funcional de Kavya",
        "script": "Lean nombra tres problemas conectados. Mura es disparidad. Muri es sobrecarga. Muda es "
                  "desperdicio. Así se conectan. Las liberaciones disparejas crean picos. Los picos "
                  "sobrecargan a tus personas y máquinas. Y la sobrecarga genera defectos, esperas e "
                  "inventario extra. El probador funcional de Kavya maneja unas dos mil unidades al día. El "
                  "mes pasado, ensamble liberó más de tres mil para prueba en un solo día. Ensamble cumplió "
                  "su plan, pero se formó una fila en prueba. ¿Puedes ver esa cadena en tu propia línea?",
    },
    {
        "key": "p04", "num": 4, "title": "Nivelar el volumen",
        "points": [("Reparte la producción en un horizonte", "Nivelar el volumen reparte"),
                   ("Demanda neta = demanda + inventario final − inventario", "Primero, calcula la demanda neta"),
                   ("Divide entre los días de producción", "Luego divide entre los días de producción"),
                   ("Revisa materiales, rendimiento, tiempo en marcha, personal", "Revisa los materiales")],
        "example": "30,000 unidades de necesidad neta en 5 días = 6,000 unidades buenas al día, parejas.",
        "example_cue": "La necesidad neta de Kavya",
        "script": "Empieza con el volumen. Nivelar el volumen reparte tu producción planeada en un "
                  "horizonte razonable. Primero, calcula la demanda neta. Es la demanda del cliente, más el "
                  "inventario con el que quieres terminar, menos el inventario útil que tienes. Luego "
                  "divide entre los días de producción disponibles. La necesidad neta de Kavya esta semana "
                  "es de treinta mil unidades, en cinco días. Son seis mil unidades buenas al día, parejas. "
                  "¿Pero tu línea de verdad puede sostener eso? Revisa los materiales, el rendimiento, el "
                  "tiempo en marcha y el personal primero.",
    },
    {
        "key": "p05", "num": 5, "title": "Nivelar la mezcla",
        "points": [("Patrones pequeños que se repiten y siguen la demanda", "Nivelar la mezcla repite"),
                   ("La proporción sale de la demanda", "Es una proporción de tres, dos, uno"),
                   ("Revisa cambios de modelo, fixtures, piezas", "Debes revisar los cambios de modelo")],
        "example": "3,000 teléfonos, 2,000 decodificadores, 1,000 de audio → 3 : 2 : 1 → "
                   "Teléfono–Decodificador–Teléfono–Audio–Decodificador–Teléfono.",
        "example_cue": "Kavya necesita tres mil",
        "script": "Ahora la mezcla. Nivelar la mezcla repite tus productos en patrones pequeños que siguen "
                  "la demanda, en lugar de un gran lote de cada uno. Kavya necesita tres mil teléfonos, dos "
                  "mil decodificadores, y mil equipos de audio. Es una proporción de tres, dos, uno. Así "
                  "que un patrón de seis unidades podría ser teléfono, decodificador, teléfono, audio, "
                  "decodificador, teléfono. Pero aquí está el detalle. Un patrón bonito en papel no siempre "
                  "se puede armar. Debes revisar los cambios de modelo, los fixtures y las piezas primero. "
                  "¿Y qué tan rápido debe correr el patrón?",
    },
    {
        "key": "p06", "num": 6, "title": "Tiempo TAKT y pitch",
        "points": [("TAKT: el ritmo que pide el cliente", "El TAKT es el ritmo"),
                   ("Tiempo neto ÷ unidades buenas requeridas", "Divide tu tiempo neto disponible"),
                   ("Pitch: el tiempo para liberar un lote", "El pitch es el tiempo"),
                   ("TAKT promedio ≠ que cada modelo siga el paso", "Un TAKT promedio no")],
        "example": "Una unidad cada 4.2 segundos → un pitch de 100 unidades de 7 minutos.",
        "example_cue": "El turno de Kavya necesita",
        "script": "Ahí entra el TAKT. El TAKT es el ritmo que pide tu cliente. Divide tu tiempo neto "
                  "disponible entre las unidades buenas requeridas. Nivelar luego fija el orden práctico de "
                  "las liberaciones a ese ritmo. El pitch es el tiempo para liberar un lote, muchas veces "
                  "de cien unidades. El turno de Kavya necesita una unidad cada cuatro punto dos segundos. "
                  "Así que un pitch de cien unidades son siete minutos. Pero cuidado. Un TAKT promedio no "
                  "prueba que cada modelo pueda seguir el paso. ¿Cómo le muestras el plan al piso?",
    },
    {
        "key": "p07", "num": 7, "title": "La caja de nivelación",
        "points": [("Un programa visual", "Es un programa visual"),
                   ("Horarios a lo ancho, productos hacia abajo", "Los horarios van"),
                   ("Tarjetas: qué liberar, cuántos", "Las tarjetas en cada horario"),
                   ("Faltantes y horarios perdidos visibles", "Los horarios perdidos")],
        "example": "Cada 30 minutos el tablero de Kavya libera el siguiente lote; los kits se preparan en "
                   "ese orden.",
        "example_cue": "Cada treinta minutos",
        "script": "Con una caja de nivelación. Es un programa visual. Los horarios van a lo ancho en las "
                  "columnas, y los productos van hacia abajo en las filas. Las tarjetas en cada horario "
                  "muestran qué liberar, y cuántos. Cada treinta minutos, el tablero de Kavya libera el "
                  "siguiente lote. Los kits se preparan en ese orden, no por comodidad. Los horarios "
                  "perdidos y los faltantes se ven de un vistazo. Esta es una prueba rápida para tu línea. "
                  "¿Un operador puede ver la siguiente liberación, y a quién llamar, sin preguntarle a "
                  "nadie?",
    },
    {
        "key": "p08", "num": 8, "title": "EPEI y cambio de modelo",
        "points": [("Patrones pequeños = más cambios de modelo", "Los patrones pequeños significan"),
                   ("EPEI: cada pieza en cada intervalo", "El EPEI mide"),
                   ("SMED: preparar fuera del tiempo detenido", "Por eso importa el SMED")],
        "example": "6 cambios al día: de 20 a 8 minutos = 72 minutos recuperados cada día.",
        "example_cue": "Los seis cambios diarios de Kavya",
        "script": "Los patrones pequeños significan más cambios de modelo. El EPEI mide qué tan seguido "
                  "haces cada pieza. Significa cada pieza en cada intervalo. Kavya arma cada familia una "
                  "vez al día, así que su EPEI es de un día. Armar cada una dos veces por turno responde "
                  "más rápido, pero duplica los cambios de modelo. Por eso importa el SMED. Pasas el "
                  "trabajo de preparación fuera del tiempo detenido. Los seis cambios diarios de Kavya "
                  "bajaron de veinte minutos a ocho. Son setenta y dos minutos recuperados cada día. ¿Dónde "
                  "pierde tiempo tu línea?",
    },
    {
        "key": "p09", "num": 9, "title": "Cuellos de botella y modelos mezclados",
        "points": [("Nivelar no le gana a un límite de capacidad", "Nivelar no puede superar"),
                   ("Carga las estaciones con la mezcla real", "Debes cargar cada estación"),
                   ("No bloquees el modelo más lento", "Y si programa")],
        "example": "40% de las unidades necesitan una prueba de 12 segundos = unas 340 pruebas/hora contra "
                   "~300 de un probador. Agrega un segundo probador.",
        "example_cue": "El cuarenta por ciento de las unidades",
        "script": "Esta es una verdad dura. Nivelar no puede superar un límite real de capacidad. Debes "
                  "cargar cada estación con la mezcla real, no con el promedio. Kavya revisó su área de "
                  "prueba. El cuarenta por ciento de las unidades necesita una prueba de doce segundos. Son "
                  "unas trescientas cuarenta pruebas por hora. Un probador da unas trescientas, incluso "
                  "antes de las pérdidas. Así que necesita un segundo probador, sin importar la secuencia. "
                  "Y si programa el modelo más lento en un solo bloque largo, el probador se ahoga. "
                  "¿Conoces tu modelo más lento?",
    },
    {
        "key": "p10", "num": 10, "title": "Control de Kanban y WIP",
        "points": [("Kanban: qué surtir, cuándo", "Las señales Kanban le dicen"),
                   ("Contenedores estándar, carriles de primero en entrar, primero en salir", "Los contenedores estándar"),
                   ("Los límites de WIP detienen la sobreproducción", "Los límites de WIP detienen"),
                   ("Kits al ritmo del pitch y la mezcla", "Ajusta tu ritmo de kits")],
        "example": "Faltaba un kit de decodificador — el equipo lo registró y siguió la regla aprobada de "
                   "reprogramación.",
        "example_cue": "El martes pasado",
        "script": "Un programa nivelado necesita materiales estables. Las señales Kanban le dicen al "
                  "almacén qué surtir, y cuándo. Los contenedores estándar y los carriles de primero en "
                  "entrar, primero en salir evitan que la línea se quede sin material. Los límites de WIP "
                  "detienen la sobreproducción de los procesos anteriores. Ajusta tu ritmo de kits al pitch "
                  "y a la mezcla. El martes pasado, faltaba un kit de decodificador. El equipo de Kavya no "
                  "cambió una pieza en silencio. Lo registraron, y siguieron la regla aprobada de "
                  "reprogramación. ¿Qué haría tu equipo?",
    },
    {
        "key": "p11", "num": 11, "title": "Manejar los cambios de demanda",
        "points": [("Una ventana cercana congelada", "Así que necesitas un horizonte de planeación"),
                   ("Reprogramar en el piso causa caos", "Reprogramar constantemente"),
                   ("Decide quién aprueba los cambios", "Decide quién puede aprobar")],
        "example": "Se pidieron 500 equipos de audio antes: Kavya revisó fechas, inventario, piezas y "
                   "capacidad de prueba primero.",
        "example_cue": "Una mañana, un cliente",
        "script": "La demanda va a seguir cambiando. Así que necesitas un horizonte de planeación, y una "
                  "ventana cercana congelada o muy controlada. Reprogramar constantemente en el piso causa "
                  "caos. Decide quién puede aprobar un cambio de secuencia, y por qué. Una mañana, un "
                  "cliente pidió quinientos equipos de audio antes. Kavya no solo los metió en la fila. "
                  "Revisó las fechas de entrega, el producto terminado, los componentes y la capacidad de "
                  "prueba primero. Luego cambió los siguientes horarios de liberación. ¿Quién aprueba los "
                  "cambios en tu línea?",
    },
    {
        "key": "p12", "num": 12, "title": "KPI de nivelación",
        "points": [("Sigue la producción y la estabilidad juntas", "Sigue la producción y la estabilidad"),
                   ("Cumplimiento del programa", "El cumplimiento del programa compara"),
                   ("Días de WIP", "Los días de WIP muestran"),
                   ("Más FPY, paros, horas extra", "Agrega el rendimiento a la primera")],
        "example": "95% de las unidades programadas terminadas. 12,000 unidades de WIP = 2 días de "
                   "producción.",
        "example_cue": "La línea de Kavya terminó",
        "script": "¿Cómo sabes que nivelar funciona? Sigue la producción y la estabilidad juntas. El "
                  "cumplimiento del programa compara lo que terminaste con lo que planeaste. La línea de "
                  "Kavya terminó el noventa y cinco por ciento de sus unidades programadas. Los días de WIP "
                  "muestran cuánto espera el trabajo. Sus doce mil unidades de WIP son dos días de "
                  "producción. Agrega el rendimiento a la primera, los paros y las horas extra. Si no, "
                  "podrías mejorar el cumplimiento y dañar la calidad en silencio. ¿Qué números revisa tu "
                  "equipo cada día?",
    },
    {
        "key": "p13", "num": 13, "title": "Caso práctico: línea compartida",
        "points": [("Mezcla 3 : 2 : 1, TAKT de 4.2 s", "La mezcla es tres"),
                   ("Patrón de 60 unidades: 30 · 20 · 10", "Prueba un patrón de sesenta"),
                   ("Revisa ruta, herramental, límites de prueba", "Pero primero revisa"),
                   ("Cambios de modelo más rápidos, sin atajos", "Aceleró los cambios de modelo")],
        "example": "Un patrón cada cuatro minutos en teoría — pero sus ajustes eran muy lentos para ese "
                   "ritmo.",
        "example_cue": "En teoría, es un patrón",
        "script": "Juntemos todo en la línea compartida de Kavya. La mezcla es tres a dos a uno. El TAKT "
                  "promedio es de cuatro punto dos segundos. Prueba un patrón de sesenta unidades. Treinta "
                  "teléfonos, veinte decodificadores, y diez equipos de audio. En teoría, es un patrón cada "
                  "cuatro minutos más o menos. Pero primero revisa la ruta, el herramental compartido, y "
                  "los límites de prueba de cada producto. Sus ajustes resultaron muy lentos para ese "
                  "ritmo. ¿Y qué hizo? Aceleró los cambios de modelo, en lugar de forzar atajos inseguros. "
                  "¿Tú lo harías?",
    },
    {
        "key": "p14", "num": 14, "title": "Errores comunes",
        "points": [("Nivelar con el tiempo bruto", "Nivelar con el tiempo bruto"),
                   ("Cantidades iguales para una mezcla desigual", "Forzar cantidades iguales"),
                   ("Más producción de la que la línea puede hacer", "Programar más producción buena"),
                   ("Saltarse las revisiones de primera pieza para alcanzar", "nunca te saltes las revisiones de primera pieza")],
        "example": "Probadores de firmware parados mientras el tablero pedía decodificadores: más WIP solo "
                   "mueve el cuello de botella. Escala.",
        "example_cue": "Un día, el tablero de Kavya",
        "script": "Un plan puede verse nivelado en papel mientras el piso sigue en caos. Cuidado con estos "
                  "errores. Nivelar con el tiempo bruto, e ignorar los descansos y las pérdidas. Forzar "
                  "cantidades iguales cuando la mezcla de tu cliente no es igual. Programar más producción "
                  "buena de la que tu línea de verdad puede hacer. Un día, el tablero de Kavya pedía "
                  "decodificadores, pero los probadores de firmware estaban parados. Liberar más trabajo "
                  "solo movería el cuello de botella. Así que escaló y actualizó el plan. Y nunca te saltes "
                  "las revisiones de primera pieza para alcanzar.",
    },
    {
        "key": "p15", "num": 15, "title": "Ruta de 90 días",
        "points": [("Una familia, un horizonte", "Empieza en pequeño"),
                   ("Días 1–30: demanda, mezcla, TAKT, ajustes", "En los primeros treinta días"),
                   ("Días 31–60: tablero piloto, kits, cambios de modelo", "En los siguientes treinta"),
                   ("Días 61–90: verificar, estandarizar, extender", "En los últimos treinta")],
        "example": "Planeación fija las liberaciones, Producción arma, Ingeniería revisa la capacidad, "
                   "Calidad protege los controles, Materiales tiene los kits listos.",
        "example_cue": "Planeación fija las liberaciones",
        "script": "Empieza en pequeño, con una familia de productos y un horizonte de planeación. En los "
                  "primeros treinta días, mapea la demanda, la mezcla, el TAKT, los cuellos de botella y "
                  "los ajustes. En los siguientes treinta, haz un piloto de tu tablero de nivelación, tu "
                  "ritmo de kits, y cambios de modelo más rápidos. En los últimos treinta, verifica el "
                  "rendimiento, el cumplimiento y la entrega. Luego estandariza y extiende. Dale a cada "
                  "quien un papel claro. Planeación fija las liberaciones, Producción arma, e Ingeniería "
                  "revisa la capacidad. Calidad protege los controles, y Materiales tiene los kits listos. "
                  "¿Quién sería el dueño de tu piloto?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "versus", "items": [
        {"label": "Todos los teléfonos primero", "sub": "Luego decodificadores, luego audio", "icon": "stack", "with": 1},
        {"label": "Secuencias pequeñas que se repiten", "sub": "Ajustadas a la demanda real", "icon": "sequence", "with": "example"}]},
    "p02": {"type": "icons", "items": [
        {"label": "La demanda es dispareja", "icon": "wave"}, {"label": "Perseguir picos", "sub": "Horas extra, inventario", "icon": "clock", "tone": "bad"},
        {"label": "Nivela las liberaciones", "icon": "sequence"}, {"label": "Algo de colchón", "icon": "box"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Armarlo todo el lunes", "sub": "Horas extra, prueba apurada", "icon": "stack"},
            {"label": "Repartido en la semana", "sub": "La fecha de entrega lo permitía", "icon": "calendar"}]}},
    "p03": {"type": "flow", "items": [
        {"label": "Mura", "sub": "Las liberaciones disparejas crean picos", "icon": "wave", "tone": "bad", "with": 0},
        {"label": "Muri", "sub": "Los picos sobrecargan personas y máquinas", "icon": "weight", "tone": "bad", "with": 1},
        {"label": "Muda", "sub": "Defectos, esperas, inventario", "icon": "trash", "tone": "bad", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "Se forma una fila en prueba", "unit": "unidades en un día", "with": "example", "items": [
            {"label": "El probador puede", "value": 2000, "tone": "good", "with": "example"},
            {"label": "Liberadas", "value": 3200, "tone": "bad", "with": "example"}]}},
    "p04": {"type": "icons", "items": [
        {"label": "Un horizonte razonable", "icon": "calendar"}, {"label": "Demanda neta", "icon": "count"},
        {"label": "÷ días de producción", "icon": "sequence"}, {"label": "Revisa que se pueda sostener", "icon": "search"}],
        "then": {"type": "stat", "value": 6000, "icon": "chartUp", "label": "unidades buenas al día, todos los días",
                 "unit": "30,000 unidades de necesidad neta ÷ 5 días", "with": "example"}},
    "p05": {"type": "steps", "items": [
        {"label": "Teléfono", "sub": "P", "with": "example"}, {"label": "Decodificador", "sub": "B", "with": "example"},
        {"label": "Teléfono", "sub": "P", "with": "example"}, {"label": "Audio", "sub": "A", "with": "example"},
        {"label": "Decodificador", "sub": "B", "with": "example"}, {"label": "Teléfono", "sub": "P", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "El ritmo del cliente", "icon": "clock", "with": 0},
        {"label": "Tiempo neto ÷ unidades buenas", "icon": "count", "with": 1},
        {"label": "Pitch", "sub": "Tiempo para liberar un lote", "icon": "box", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Una unidad cada 4.2 s", "icon": "clock", "with": "example"},
            {"label": "× un lote de 100 unidades", "icon": "box", "with": "example"},
            {"label": "= un pitch de 7 minutos", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "doc", "items": [
        {"label": "Caja de nivelación · línea compartida", "icon": "calendar", "with": 0},
        {"label": "08:00  Teléfono · Decodificador · Teléfono", "icon": "sequence", "with": 1},
        {"label": "08:30  Audio · Decodificador · Teléfono", "icon": "sequence", "with": 1},
        {"label": "09:00  Siguiente lote: kits listos", "icon": "box", "with": 2},
        {"label": "¿Horario perdido? Se ve de inmediato", "icon": "warning", "with": 3}]},
    "p08": {"type": "icons", "items": [
        {"label": "Más cambios de modelo", "icon": "sequence", "with": 0},
        {"label": "EPEI", "sub": "Cada pieza en cada intervalo", "icon": "calendar", "with": 1},
        {"label": "SMED", "sub": "Preparar fuera del tiempo detenido", "icon": "wrench", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Antes", "value": 20}, "after": {"label": "Después del SMED", "value": 8},
                 "suffix": " min", "unit": "por cambio de modelo, seis al día", "note": "72 minutos recuperados cada día", "with": "example"}},
    "p09": {"type": "bars", "label": "Un probador", "value": 300, "note": "no alcanza ni antes de las pérdidas: agrega un segundo probador", "unit": "pruebas por hora (40% de las unidades necesitan una prueba de 12 s)", "items": [
        {"label": "Pruebas necesarias", "value": 343, "tone": "bad", "with": "example"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Señales Kanban", "icon": "label"}, {"label": "Carriles FIFO", "icon": "sequence"},
        {"label": "Límites de WIP", "icon": "stack"}, {"label": "Kits al ritmo del pitch", "icon": "tray"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Una ventana congelada", "icon": "lock", "with": 0},
        {"label": "Reprogramar en el piso", "sub": "Causa caos", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Quién aprueba", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "500 de audio pedidos antes", "icon": "box", "with": "example"},
            {"label": "Revisa fechas, inventario, piezas, prueba", "icon": "search", "with": "example"},
            {"label": "Luego cambia los siguientes horarios", "icon": "sequence", "tone": "good", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Producción + estabilidad", "icon": "chartUp"}, {"label": "Cumplimiento del programa", "icon": "check"},
        {"label": "Días de WIP", "icon": "clock"}, {"label": "FPY, paros, horas extra", "icon": "shield"}],
        "then": {"type": "stat", "value": 95, "suffix": "%", "icon": "check", "label": "de las unidades programadas terminadas",
                 "unit": "12,000 unidades de WIP = 2 días de producción", "with": "example"}},
    "p13": {"type": "stat", "value": 4.2, "decimals": 1, "suffix": " s", "icon": "clock", "label": "TAKT promedio, mezcla 3 : 2 : 1",
            "unit": "teléfonos : decodificadores : audio", "with": 0,
            "then": {"type": "bars", "label": "", "note": "Un patrón cada 4 minutos aprox.", "unit": "unidades en un patrón de 60 unidades", "with": 1, "items": [
                {"label": "Teléfonos", "value": 30, "with": 1}, {"label": "Decodificadores", "value": 20, "with": 1},
                {"label": "Audio", "value": 10, "with": 1}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Tiempo bruto", "icon": "clock", "tone": "bad"}, {"label": "Cantidades iguales", "icon": "scale", "tone": "bad"},
        {"label": "Planear de más", "icon": "stack", "tone": "bad"}, {"label": "Saltarse la primera pieza", "icon": "warning", "tone": "bad"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Demanda, mezcla, TAKT, ajustes", "sub": "Días 1–30", "icon": "clipboard", "with": 1},
        {"label": "Tablero piloto, kits, cambios de modelo", "sub": "31–60", "icon": "calendar", "with": 2},
        {"label": "Verificar, estandarizar, extender", "sub": "61–90", "icon": "chartUp", "with": 3}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Planeación", "icon": "calendar", "with": "example"}, {"label": "Producción", "icon": "wrench", "with": "example"},
            {"label": "Ingeniería", "icon": "gear", "with": "example"}, {"label": "Calidad", "icon": "shield", "with": "example"},
            {"label": "Materiales", "icon": "box", "with": "example"}]}},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p06",
        "question": "Kavya necesita 3,000 teléfonos, 2,000 decodificadores y 1,000 equipos de audio. ¿Qué "
                    "secuencia tiene la mezcla nivelada?",
        "options": ["Todos los teléfonos, luego todos los decodificadores, luego todo el audio", "Teléfono–Decodificador–Teléfono–Audio–Decodificador–Teléfono, repetido",
                    "Uno de cada producto, por turnos"],
        "correct": 1,
        "explanation": "El patrón que se repite sigue la proporción de demanda 3 : 2 : 1. Los lotes grandes "
                       "crean picos; las cantidades iguales ignoran la mezcla real.",
        "q_script": "Prueba rápida. Kavya necesita tres mil teléfonos, dos mil decodificadores, y mil equipos "
                    "de audio. ¿Qué secuencia tiene la mezcla nivelada? Tómate unos segundos.",
        "a_script": "El patrón que se repite. Teléfono, decodificador, teléfono, audio, decodificador, "
                    "teléfono. Sigue la demanda. Las cantidades iguales ignoran la mezcla real.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un cliente de repente quiere 500 equipos de audio antes. ¿Qué debe hacer PRIMERO Kavya?",
        "options": ["Meterlos en el siguiente horario", "Revisar fechas, inventario, piezas y capacidad de prueba, y luego cambiar los horarios",
                    "Negarse — el programa está congelado", "Agregar horas extra y armarlos todos hoy"],
        "correct": 1,
        "explanation": "Primero revisa el impacto, y luego cambia los siguientes horarios de liberación con las "
                       "reglas acordadas. Meterlos a ciegas en la fila, o negarse de entrada, causan problemas.",
        "q_script": "Una más, y esta es un escenario. Un cliente de repente quiere quinientos equipos de "
                    "audio antes. ¿Qué debe hacer primero Kavya? Piénsalo.",
        "a_script": "Primero revisa el impacto. Fechas de entrega, producto terminado, componentes, y "
                    "capacidad de prueba. Luego cambia los siguientes horarios de liberación, con las reglas "
                    "acordadas. Meterlos a ciegas en la fila, o negarse de entrada, causan problemas.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
