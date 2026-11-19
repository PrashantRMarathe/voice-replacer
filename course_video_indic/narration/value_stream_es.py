"""value_stream in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh value_stream_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "vs_es"
NAME = "value_stream_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Value Stream Mapping": "váliu estrím mápin",
    "Why-Why": "juái juái",
    "Pareto": "Pareto",
    "Kanban": "Kanban",
    "Kaizen": "Káizen",
    "Gemba": "Guemba",
    "TAKT": "takt",
    "WIP": "doble u i pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Un decodificador tarda quince minutos en armarse y probarse. Aun así, tarda casi cuatro "
    "días en llegar al cliente. ¿A dónde se va todo ese tiempo? En esta lección aprenderás "
    "Value Stream Mapping. Verás cómo dibujar el flujo real de material e información. Luego "
    "encontrarás las esperas, y diseñarás un mejor estado futuro. Seguiremos a Rahul, "
    "ingeniero de mejora, mientras mapea la línea de decodificadores de su planta."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Mapea el flujo real, del material y de la información. La "
    "mayor parte de tu tiempo de entrega se esconde en las esperas, no en el trabajo. Y "
    "diseña un estado futuro que puedas comprobar, antes de recortar inventario. Esta es tu "
    "acción para esta semana. Recorre una familia de productos hacia atrás desde embarques, y "
    "cuenta cada montón que pases. Excelente trabajo al completar esta lección. Ahora "
    "aprenderás el análisis Why-Why, para encontrar las causas reales."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué muestra un VSM",
        "points": [("Una familia de productos, del pedido a la entrega", "muestra todo el recorrido"),
                   ("El material y la información que lo mueve", "Incluye el material"),
                   ("Trabajo que agrega valor, esperas, inventario", "Muestra el trabajo que agrega valor"),
                   ("Una imagen compartida de la realidad", "Es una imagen compartida")],
        "example": "Rahul sigue un decodificador desde las tarjetas que llegan hasta embarques — con las "
                   "señales de planeación y la liberación del almacén.",
        "example_cue": "Rahul sigue un decodificador",
        "script": "Esta es la idea central. Un mapa de flujo de valor muestra todo el recorrido de una "
                  "familia de productos, del pedido del cliente a la entrega. Incluye el material, y la "
                  "información que lo mueve. Muestra el trabajo que agrega valor, las esperas, los montones "
                  "de inventario, y las señales lentas. Es una imagen compartida de la realidad, no un "
                  "diagrama de flujo decorativo. Rahul sigue un decodificador desde las tarjetas que llegan "
                  "hasta embarques. Incluye las señales de planeación y la liberación del almacén, no solo "
                  "la línea. ¿Y qué cuenta como valor para ti?",
    },
    {
        "key": "p02", "num": 2, "title": "Valor, flujo y desperdicio",
        "points": [("Valor: lo que el cliente pagaría", "El valor es lo que tu cliente"),
                   ("Necesario hoy, pero sin valor", "Algún trabajo no agrega valor"),
                   ("Puro desperdicio: esperas, transporte, retrabajo", "Luego está el puro desperdicio")],
        "example": "El decodificador de Rahul: 15 minutos de armado y prueba contra 2 días esperando la "
                   "liberación de material.",
        "example_cue": "El decodificador de Rahul pasa",
        "script": "El valor es lo que tu cliente pagaría con gusto. Cambia la forma, el ajuste o la función "
                  "del producto, bien a la primera. Algún trabajo no agrega valor pero todavía se necesita "
                  "hoy, como una inspección obligatoria. Luego está el puro desperdicio, como las esperas, "
                  "el transporte y el retrabajo. El decodificador de Rahul pasa quince minutos en armado y "
                  "prueba. Pasa dos días esperando la liberación de material. ¿Qué atacarías primero? "
                  "¿Segundos de ensamble, o días de espera?",
    },
    {
        "key": "p03", "num": 3, "title": "Familias de productos y alcance",
        "points": [("No mapees todo de una vez", "No mapees todo"),
                   ("Familia: mismos pasos y equipos", "Una familia de productos es"),
                   ("Tabla de productos × procesos", "Arma una tabla simple"),
                   ("Agrupa los productos que comparten ruta", "Luego agrupa los productos")],
        "example": "Los teléfonos y los equipos de audio comparten empaque pero se prueban muy distinto — "
                   "así que van en mapas separados.",
        "example_cue": "Rahul notó que los teléfonos",
        "script": "No mapees todo de una vez. Una familia de productos es un grupo de artículos que siguen "
                  "casi los mismos pasos y equipos. Mezclar productos que no se parecen esconde la "
                  "variación, y los promedios empiezan a mentir. Arma una tabla simple, con los productos "
                  "en un lado y los procesos arriba. Luego agrupa los productos que comparten una ruta. "
                  "Rahul notó que los teléfonos y los equipos de audio comparten empaque, pero se prueban "
                  "muy distinto. Así que van en mapas separados. ¿Qué familia mapearías primero?",
    },
    {
        "key": "p04", "num": 4, "title": "Símbolos y convenciones",
        "points": [("Íconos de fábrica: cliente y proveedor", "Los íconos de fábrica muestran"),
                   ("Cajas de proceso + cajas de datos", "Las cajas de proceso muestran"),
                   ("Triángulos: inventario esperando", "Los triángulos muestran"),
                   ("Flechas de material contra de información", "Las flechas gruesas llevan")],
        "example": "Las estrellas Kaizen marcan ideas; una línea de tiempo separa el proceso de la espera. "
                   "Agrega siempre una leyenda.",
        "example_cue": "Las estrellas Kaizen marcan",
        "script": "Los mapas de flujo de valor usan un lenguaje visual simple. Los íconos de fábrica "
                  "muestran a tu cliente y a tu proveedor. Las cajas de proceso muestran las operaciones. "
                  "Debajo van cajas de datos para el tiempo de ciclo, el cambio de modelo, el tiempo en "
                  "marcha y el rendimiento. Los triángulos muestran el inventario esperando. Las flechas "
                  "gruesas llevan el material, y las flechas delgadas llevan la información. Las estrellas "
                  "Kaizen marcan ideas de mejora. Una línea de tiempo abajo separa el proceso de la espera. "
                  "Los símbolos varían entre empresas, así que agrega siempre una leyenda. ¿Listo para "
                  "reunir datos reales?",
    },
    {
        "key": "p05", "num": 5, "title": "Recorrido por el Gemba y datos",
        "points": [("Empieza en el Gemba", "El mapeo empieza en el Gemba"),
                   ("Camina de embarques hacia el proveedor", "Camina de embarques"),
                   ("Mide tú mismo los ciclos reales", "Mide los ciclos reales"),
                   ("Cuenta el WIP en cada colchón", "Cuenta el WIP")],
        "example": "El sistema de Rahul mostraba un número para el WIP de prueba, su conteo físico otro. Los "
                   "cuadró antes de hacer cuentas.",
        "example_cue": "El sistema de Rahul mostraba",
        "script": "El mapeo empieza en el Gemba, donde de verdad pasa el trabajo. Camina de embarques hacia "
                  "el proveedor. Verás las filas reales, y si el material se jala o se empuja. Mide los "
                  "ciclos reales tú mismo, varias veces, en lugar de confiar en tiempos estándar. Cuenta el "
                  "WIP en cada colchón. El sistema de Rahul mostraba un número para el WIP de prueba. Su "
                  "conteo físico mostraba otro. Los cuadró antes de hacer cualquier cuenta. Ahora, ¿qué tan "
                  "rápido necesita tu cliente que vayas?",
    },
    {
        "key": "p06", "num": 6, "title": "Demanda del cliente y TAKT",
        "points": [("TAKT: el ritmo que necesita tu cliente", "El TAKT marca el ritmo"),
                   ("Tiempo neto ÷ unidades buenas, mismo periodo", "Divide tu tiempo neto disponible"),
                   ("Compara cada estación contra él", "Ahora compara cada estación")],
        "example": "1,200 decodificadores buenos en un turno → TAKT de 21 segundos, unos 170 por hora. Una "
                   "estación de 24 segundos no puede seguir el paso sola.",
        "example_cue": "La línea de Rahul corre",
        "script": "El TAKT marca el ritmo que necesita tu cliente. Divide tu tiempo neto disponible entre "
                  "las unidades buenas pedidas, en el mismo periodo. El tiempo neto deja fuera los "
                  "descansos y los paros planeados. La línea de Rahul corre un turno, y necesita mil "
                  "doscientos decodificadores buenos al día. Eso da un TAKT de veintiún segundos por "
                  "unidad, o unos ciento setenta por hora. Ahora compara cada estación contra él. Una "
                  "estación corre a veinticuatro segundos. ¿Qué significa eso para ti? No puede seguir el "
                  "paso, a menos que una segunda estación corra en paralelo.",
    },
    {
        "key": "p07", "num": 7, "title": "El mapa del estado actual",
        "points": [("La demanda a la derecha, el trabajo hacia el inicio", "Pon la demanda del cliente"),
                   ("Datos debajo de cada caja", "Agrega los datos"),
                   ("Dibuja el flujo de información", "Luego dibuja el flujo de información"),
                   ("Revísalo con tus operadores", "Por último, pregúntales a tus operadores")],
        "example": "Planeación liberaba lotes semanales; prueba solo podía manejar un ritmo diario — los "
                   "decodificadores se amontonaban en medio.",
        "example_cue": "El mapa de Rahul reveló",
        "script": "Ahora dibuja el estado actual. Pon la demanda del cliente a la derecha, y luego avanza "
                  "hacia el inicio por cada proceso y colchón. Agrega los datos debajo de cada caja. Luego "
                  "dibuja el flujo de información. Pronósticos, programas diarios, órdenes de trabajo y "
                  "señales Kanban. El mapa de Rahul reveló un desajuste. Planeación liberaba lotes "
                  "semanales a ensamble, pero prueba solo podía manejar un ritmo diario. Así que los "
                  "decodificadores a medio terminar se amontonaban en medio. Por último, pregúntales a tus "
                  "operadores. ¿Las flechas coinciden con un día normal?",
    },
    {
        "key": "p08", "num": 8, "title": "Tiempo de entrega e inventario",
        "points": [("Línea de tiempo: trabajo contra espera", "La línea de tiempo separa"),
                   ("Espera = colchón ÷ demanda diaria", "Para estimar la espera"),
                   ("Proporción de valor agregado: una señal, no una prueba", "Esa parte tan pequeña")],
        "example": "Tres colchones con 1,200 al día = 3.5 días de espera contra 15 minutos de proceso.",
        "example_cue": "Rahul tiene tres colchones",
        "script": "La línea de tiempo separa el tiempo de trabajo del tiempo de espera. Para estimar la "
                  "espera, divide el inventario de cada colchón entre la demanda diaria. Rahul tiene tres "
                  "colchones, y una demanda de mil doscientos al día. Juntos, guardan tres días y medio de "
                  "espera. El proceso real suma solo quince minutos. ¿Ves la brecha? Esa parte tan pequeña "
                  "es la proporción de valor agregado. Tómala como una señal, no como prueba de que toda la "
                  "espera puede desaparecer. ¿Y por qué está ahí ese inventario?",
    },
    {
        "key": "p09", "num": 9, "title": "Restricciones y causas",
        "points": [("Un mapa muestra dónde, no por qué", "Un mapa te dice"),
                   ("Filas largas, urgencias, ciclos de retrabajo", "Busca filas largas"),
                   ("Profundiza: Pareto, cinco porqués, espina de pescado", "Luego profundiza")],
        "example": "2,000 decodificadores esperando prueba: ¿pocos probadores, paros, firmware o "
                   "liberaciones en lote? Revisa antes de comprar.",
        "example_cue": "Rahul encontró dos mil",
        "script": "Un mapa te dice dónde buscar, no por qué pasa. Busca filas largas, urgencias frecuentes "
                  "y ciclos de retrabajo. Luego profundiza con gráficas de Pareto, cinco porqués o una "
                  "espina de pescado. Rahul encontró dos mil decodificadores esperando prueba. ¿Eran muy "
                  "pocos probadores? ¿Paros? ¿Un firmware inestable? ¿O liberaciones en lotes grandes? Cada "
                  "una necesita una solución distinta. Así que revisó los datos antes de que alguien "
                  "comprara un probador nuevo. ¿Qué revisarías primero?",
    },
    {
        "key": "p10", "num": 10, "title": "Estado futuro: flujo y jalar",
        "points": [("Flujo continuo al TAKT o por debajo", "Usa flujo continuo"),
                   ("Carriles de primero en entrar, primero en salir con tope", "usa un carril de primero en entrar, primero en salir"),
                   ("Supermercado con señales de jalar", "usa un supermercado"),
                   ("Un solo proceso marcapasos", "Luego elige un marcapasos")],
        "example": "El diseño de Rahul: ensamble y empaque comparten un carril con tope; las tarjetas se "
                   "jalan de un supermercado.",
        "example_cue": "En el diseño de Rahul",
        "script": "Ahora diseña el estado futuro. Debe ser mejor, y también realista. Usa flujo continuo "
                  "donde los pasos puedan correr al TAKT o por debajo. Donde no puedan, usa un carril de "
                  "primero en entrar, primero en salir con un tope firme. Donde el flujo no se pueda "
                  "conectar, usa un supermercado con señales de jalar. Luego elige un marcapasos, el único "
                  "proceso que programas. En el diseño de Rahul, ensamble y empaque comparten un carril con "
                  "tope. Las tarjetas se jalan de un supermercado. ¿Dónde podría fluir tu línea?",
    },
    {
        "key": "p11", "num": 11, "title": "Pitch, Kanban y surtido",
        "points": [("Pitch = TAKT × cantidad del empaque", "El pitch es el ritmo"),
                   ("Tamaño del Kanban: tiempo de entrega y demanda", "Los tamaños del Kanban dependen"),
                   ("Comprueba el surtido antes de recortar inventario", "Comprueba que el surtido funciona")],
        "example": "Empaques de 20 → un pitch de 7 minutos. Un kit dura 6 minutos pero un surtido tarda 12: "
                   "más kits, o un surtido más rápido.",
        "example_cue": "Los empaques de Rahul llevan",
        "script": "Nivelar hace predecibles las señales de jalar. El pitch es el ritmo para mover un "
                  "empaque estándar. Es el TAKT por la cantidad del empaque. Los empaques de Rahul llevan "
                  "veinte decodificadores, así que su pitch es de siete minutos. Los tamaños del Kanban "
                  "dependen del tiempo de entrega del surtido y de la demanda. Un kit dura seis minutos, "
                  "pero un surtido tarda doce. Así que necesita más kits, o un surtido más rápido. Esta es "
                  "la regla para ti. Comprueba que el surtido funciona antes de recortar inventario. ¿Listo "
                  "para el caso completo?",
    },
    {
        "key": "p12", "num": 12, "title": "Caso práctico resuelto",
        "points": [("1,200 decodificadores al día; 4,200 esperando", "La demanda es de mil doscientos"),
                   ("3.5 días de fila", "Son tres días y medio"),
                   ("Estado futuro: colchones a la mitad", "Su estado futuro reduce a la mitad"),
                   ("Valida primero capacidad, material, calidad", "¿La capacidad de prueba")],
        "example": "El tiempo en fila baja a menos de dos días — una reducción de 50%. Pero todavía no lo "
                   "cambia.",
        "example_cue": "El tiempo en fila baja",
        "script": "Este es el caso de Rahul, con números de entrenamiento. La demanda es de mil doscientos "
                  "decodificadores al día. Hoy, cuatro mil doscientas unidades esperan en tres colchones. "
                  "Son tres días y medio de fila. Su estado futuro reduce a la mitad cada colchón, a dos "
                  "mil cien unidades. El tiempo en fila baja a menos de dos días. Es una reducción del "
                  "cincuenta por ciento. Pero todavía no lo cambia. ¿La capacidad de prueba, la entrega de "
                  "material y los controles de calidad aguantan con menos colchón? ¿Cómo lo revisarías?",
    },
    {
        "key": "p13", "num": 13, "title": "KPI y beneficios reales",
        "points": [("Mide todo el flujo", "Mide todo el flujo"),
                   ("Tiempo de entrega, WIP, entrega, FPY", "Sigue el tiempo de entrega, el WIP"),
                   ("Base, luego verifica durante semanas", "Fija una base"),
                   ("Cuidado con el inventario que solo se movió", "Cuidado con el inventario")],
        "example": "Menos WIP libera unos ₹31 lakh de inventario — dinero liberado una vez, no ganancia cada "
                   "año.",
        "example_cue": "El menor WIP de Rahul",
        "script": "Mide todo el flujo, no solo la velocidad de las estaciones. Sigue el tiempo de entrega, "
                  "el WIP, la entrega a tiempo y el rendimiento a la primera. Fija una base, y luego "
                  "verifica durante varias semanas representativas. Cuidado con el inventario que "
                  "simplemente se movió a otro lado. Aquí hay una trampa de dinero. El menor WIP de Rahul "
                  "libera unos tres millones cien mil rupias de inventario. Es dinero liberado una sola "
                  "vez. No son tres millones cien mil de ganancia cada año. ¿Tu equipo de finanzas notaría "
                  "la diferencia? Repórtalo con honestidad.",
    },
    {
        "key": "p14", "num": 14, "title": "Gobierno y 90 días",
        "points": [("Cada área tiene un papel", "Mejorar el flujo de valor necesita"),
                   ("Días 1–30: elegir la familia, mapear el actual", "En los primeros treinta días"),
                   ("Días 31–60: diseñar el futuro, piloto de jalar", "En los siguientes treinta"),
                   ("Días 61–90: estabilizar, auditar, crecer", "En los últimos treinta")],
        "example": "Rahul corrigió el cuello de botella de prueba antes de recortar su colchón — si no, la "
                   "línea se queda sin material.",
        "example_cue": "Rahul corrigió el cuello de botella de prueba",
        "script": "Mejorar el flujo de valor necesita a todas las áreas. Planeación es dueña de la lógica "
                  "del programa. Producción es dueña del flujo, Calidad de los controles, y Materiales del "
                  "surtido. La gerencia quita las barreras. En los primeros treinta días, elige la familia "
                  "y mapea el estado actual. En los siguientes treinta, diseña el estado futuro y haz un "
                  "piloto de jalar. En los últimos treinta, estabiliza, audita y crece. Rahul corrigió el "
                  "cuello de botella de prueba antes de recortar su colchón. Si no, la línea se queda sin "
                  "material. ¿Cuál sería tu primer piloto?",
    },
    {
        "key": "p15", "num": 15, "title": "Sí, no y plantilla",
        "points": [("Actualízalo cuando cambie la demanda o la ruta", "Actualízalo cuando"),
                   ("Mapea el flujo real, con los operadores", "Así que sí mapea el flujo real"),
                   ("Tiempo de ciclo ≠ tiempo de entrega", "no confundas el tiempo de ciclo"),
                   ("Revisa la capacidad antes de quitar colchones", "no quites colchones")],
        "example": "Un mapa con solo cajas de proceso no es un mapa de flujo de valor. Es solo un diagrama "
                   "de flujo.",
        "example_cue": "Un mapa con solo cajas de proceso",
        "script": "Un buen mapa es una herramienta viva para decidir. Actualízalo cuando cambien la "
                  "demanda, la ruta o las restricciones principales. Así que sí mapea el flujo real, con "
                  "unidades consistentes, e involucra a tus operadores. Sí muestra las rutas de retrabajo y "
                  "las señales de planeación. Pero no confundas el tiempo de ciclo con el tiempo de "
                  "entrega. No llames ahorro anual a un dinero liberado una vez. Y no quites colchones "
                  "antes de revisar la capacidad y el surtido. Un mapa con solo cajas de proceso no es un "
                  "mapa de flujo de valor. Es solo un diagrama de flujo.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Una familia de productos", "icon": "box"}, {"label": "Material + información", "icon": "sequence"},
        {"label": "Trabajo contra espera", "icon": "clock"}, {"label": "Una imagen compartida", "icon": "person"}]},
    "p02": {"type": "versus", "items": [
        {"label": "2 días esperando", "sub": "la liberación de material", "icon": "clock", "with": "example"},
        {"label": "15 minutos de trabajo real", "sub": "armado y probado", "icon": "wrench", "with": "example"}]},
    "p03": {"type": "matrix", "prefix": "check", "cols": ["Ensamble", "Prueba de teléfono", "Prueba de audio", "Empaque"],
            "note": "Mismo empaque, prueba distinta: mapas separados", "items": [
        {"label": "Teléfonos", "cells": [3, 3, None, 3], "with": 2},
        {"label": "Audio", "cells": [3, None, 3, 3], "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Cliente, proveedor", "icon": "box"}, {"label": "Cajas de proceso + de datos", "icon": "clipboard"},
        {"label": "Triángulos: inventario", "icon": "stack"}, {"label": "Material contra información", "icon": "sequence"}]},
    "p05": {"type": "flow", "items": [
        {"label": "Ve al Gemba", "icon": "walk"},
        {"label": "Camina hacia atrás desde embarques", "icon": "sequence"},
        {"label": "Mide ciclos reales", "icon": "clock"},
        {"label": "Cuenta cada colchón", "sub": "Cuadra con el sistema", "icon": "count", "tone": "good"}]},
    "p06": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "El ritmo del cliente", "icon": "clock", "with": 0},
        {"label": "Tiempo neto ÷ unidades buenas", "icon": "count", "with": 1},
        {"label": "Compara cada estación", "icon": "scale", "with": 2}],
        "then": {"type": "bars", "label": "TAKT", "value": 21, "suffix": " s", "note": "no puede seguir el paso sola",
                 "unit": "1,200 decodificadores buenos por turno ≈ 170 por hora", "with": "example", "items": [
            {"label": "Una estación", "value": 24, "tone": "bad", "with": "example"}]}},
    "p07": {"type": "flow", "items": [
        {"label": "Planeación: lotes semanales", "icon": "calendar", "with": "example"},
        {"label": "Los decodificadores se amontonan", "sub": "A medio terminar, esperando", "icon": "stack", "tone": "bad", "with": "example"},
        {"label": "Prueba: un ritmo diario", "icon": "test", "with": "example"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Trabajo contra espera", "icon": "clock", "with": 0},
        {"label": "Colchón ÷ demanda diaria", "icon": "count", "with": 1},
        {"label": "Proporción de valor agregado", "sub": "Una señal, no una prueba", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 3.5, "decimals": 1, "suffix": " días", "icon": "clock", "label": "de espera",
                 "unit": "contra solo 15 minutos de proceso", "with": "example"}},
    "p09": {"type": "flow", "items": [
        {"label": "Un mapa muestra dónde, no por qué", "icon": "search", "with": 0},
        {"label": "Filas, urgencias, retrabajo", "icon": "stack", "with": 1},
        {"label": "Pareto, cinco porqués, espina de pescado", "icon": "gear", "with": 2}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "¿Pocos probadores?", "icon": "test", "with": "example"},
            {"label": "¿Paros?", "icon": "clock", "with": "example"},
            {"label": "¿Firmware?", "icon": "chip", "with": "example"},
            {"label": "¿Liberaciones en lote?", "icon": "stack", "with": "example"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "Tarjetas jaladas de un supermercado", "icon": "tray"},
        {"label": "Ensamble", "icon": "wrench"},
        {"label": "Un carril FIFO con tope", "icon": "sequence"},
        {"label": "Empaque: el marcapasos", "icon": "box", "tone": "good"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Pitch = TAKT × empaque", "icon": "count", "with": 0},
        {"label": "Tamaño del Kanban", "icon": "label", "with": 1},
        {"label": "Comprueba el surtido", "icon": "check", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Empaques de 20: un pitch de 7 minutos", "icon": "box", "with": "example"},
            {"label": "Un kit dura 6 min; un surtido tarda 12", "icon": "clock", "tone": "bad", "with": "example"},
            {"label": "Más kits, o un surtido más rápido", "icon": "check", "tone": "good", "with": "example"}]}},
    "p12": {"type": "stat", "value": 3.5, "decimals": 1, "suffix": " días", "icon": "clock", "label": "de fila hoy",
            "unit": "4,200 unidades esperando ÷ 1,200 al día", "with": 1,
            "then": {"type": "compare", "before": {"label": "Hoy", "value": 4200}, "after": {"label": "Estado futuro", "value": 2100},
                     "unit": "unidades esperando en tres colchones", "note": "Tiempo en fila reducido a la mitad (planeado)", "with": 2}},
    "p13": {"type": "icons", "items": [
        {"label": "Todo el flujo", "icon": "sequence"}, {"label": "Tiempo de entrega, WIP, entrega, FPY", "icon": "chartUp"},
        {"label": "Base, luego semanas", "icon": "calendar"}, {"label": "Inventario que solo se movió", "icon": "stack", "tone": "bad"}],
        "then": {"type": "stat", "value": 31, "prefix": "₹", "suffix": " lakh", "icon": "box", "label": "de inventario liberado",
                 "unit": "Dinero liberado una vez: no ganancia cada año", "with": "example"}},
    "p14": {"type": "timeline", "items": [
        {"label": "Elegir la familia, mapear el actual", "sub": "Días 1–30", "icon": "search", "with": 1},
        {"label": "Diseñar el futuro, piloto de jalar", "sub": "31–60", "icon": "sequence", "with": 2},
        {"label": "Estabilizar, auditar, crecer", "sub": "61–90", "icon": "chartUp", "with": 3}]},
    "p15": {"type": "icons", "items": [
        {"label": "Actualizar cuando algo cambie", "icon": "sequence", "tone": "good"},
        {"label": "Flujo real, con los operadores", "icon": "person", "tone": "good"},
        {"label": "Ciclo ≠ tiempo de entrega", "icon": "cross", "tone": "bad"},
        {"label": "Capacidad antes de recortar colchones", "icon": "warning", "tone": "bad"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un colchón tiene 2,400 unidades y la demanda es de 1,200 al día. ¿Cuántos días de "
                    "inventario son?",
        "options": ["Medio día", "2 días", "1,200 días"],
        "correct": 1,
        "explanation": "Días de inventario = unidades esperando ÷ demanda diaria = 2,400 ÷ 1,200 = 2 días.",
        "q_script": "Prueba rápida. Un colchón tiene dos mil cuatrocientas unidades, y la demanda es de mil "
                    "doscientas al día. ¿Cuántos días de inventario son? Tómate unos segundos.",
        "a_script": "Dos días. Divide las unidades que esperan entre la demanda diaria. El colchón guarda "
                    "exactamente dos días de producción.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Rahul encuentra 2,000 decodificadores esperando prueba. ¿Qué debe hacer PRIMERO el "
                    "equipo?",
        "options": ["Comprar otro probador de inmediato", "Confirmar la causa: capacidad, paros, firmware o liberación en lote",
                    "Recortar el colchón a la mitad para forzar el flujo"],
        "correct": 1,
        "explanation": "Un mapa muestra dónde buscar, no por qué. Confirma primero el mecanismo; comprar un "
                       "probador o recortar el colchón a ciegas puede no corregir nada, o dejar la línea sin "
                       "material.",
        "q_script": "Una más, y esta es un escenario. Rahul encuentra dos mil decodificadores esperando "
                    "prueba. ¿Qué debe hacer primero el equipo? Piénsalo.",
        "a_script": "Confirma primero la causa. Puede ser capacidad, paros, firmware, o liberaciones en lotes "
                    "grandes. Comprar un probador o recortar el colchón a ciegas puede no corregir nada, o "
                    "dejar la línea sin material.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
