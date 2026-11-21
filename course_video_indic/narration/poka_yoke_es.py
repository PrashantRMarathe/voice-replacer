"""poka_yoke in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh poka_yoke_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "pk_es"
NAME = "poka_yoke_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Shigeo Shingo": "Shiguéo Shingo",
    "Poka Yokes": "Poka Yoke",
    "Poka Yoke": "Poka Yoke",
    "Pareto": "Pareto",
    "QRQC": "cu erre cu ce",
    "FMEA": "efe eme e a",
    "NVR": "ene ve erre",
    "MES": "eme e ese",
    "SOP": "ese o pe",
    "PPM": "pe pe eme",
    "SMT": "ese eme te",
    "BOM": "be o eme",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Dieciocho grabadoras de video salieron sin un tornillo. La operadora era hábil y "
    "cuidadosa. Simplemente era humana. ¿Te suena familiar? En esta lección aprenderás Poka "
    "Yoke, o a prueba de errores. Verás cómo diseñar un proceso donde la acción incorrecta "
    "sea imposible, o se detecte al instante. Seguiremos a Divya, ingeniera de procesos en "
    "una línea de ensamble de NVR, mientras saca la memoria de la calidad."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Los errores son predecibles, así que elimínalos desde el "
    "diseño. Prefiere prevenir a detectar, y detectar a advertir. Y pon a prueba cada "
    "dispositivo con muestras malas, para saber que sigue funcionando. Esta es tu acción para "
    "esta semana. Busca en tu línea un chequeo que dependa de la memoria, y haz un boceto de "
    "un Poka Yoke para él. Excelente trabajo al completar esta lección. Ahora aprenderás "
    "QRQC, control de calidad de respuesta rápida."
)

# Each page: title, 2-5 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es Poka Yoke",
        "points": [("En japonés: a prueba de errores", "Poka Yoke es un término japonés"),
                   ("No dependas de la memoria", "No dependas de"),
                   ("Acción incorrecta imposible, o visible al instante", "Diseña el proceso")],
        "example": "Divya cambió una etiqueta de 'revisa la orientación' por un conector con guía. Una "
                   "etiqueta advierte. Una guía previene.",
        "example_cue": "La línea de Divya",
        "script": "Esta es la idea central. Poka Yoke es un término japonés que significa a prueba de "
                  "errores. No dependas de que alguien recuerde hacer lo correcto. Diseña el proceso para "
                  "que la acción incorrecta no pueda ocurrir, o se vea al instante. La línea de Divya tenía "
                  "una etiqueta que decía: revisa la orientación del conector. Ella la cambió por un "
                  "conector con guía que solo entra de una forma. Una etiqueta advierte. Una guía previene. "
                  "¿Y de dónde vino esta idea?",
    },
    {
        "key": "p02", "num": 2, "title": "Error contra defecto",
        "points": [("Del Sistema de Producción Toyota", "Poka Yoke nació"),
                   ("Error: la acción incorrecta", "El error es la acción incorrecta"),
                   ("Defecto: el producto malo que resulta", "El defecto es el producto malo"),
                   ("Detén el error antes de que sea defecto", "Detienes el error")],
        "example": "La inspección al final de la línea encuentra problemas cuando la mano de obra y las "
                   "piezas ya se gastaron.",
        "example_cue": "La inspección al final de la línea",
        "script": "Poka Yoke nació en el Sistema de Producción Toyota, con el ingeniero Shigeo Shingo. Su "
                  "idea clave fue simple. Un error y un defecto son distintos. El error es la acción "
                  "incorrecta, como invertir un conector. El defecto es el producto malo que resulta. "
                  "Detienes el error antes de que se vuelva defecto. La inspección al final de la línea "
                  "encuentra problemas cuando ya gastaste la mano de obra y las piezas. ¿Por qué esperar "
                  "tanto?",
    },
    {
        "key": "p03", "num": 3, "title": "La jerarquía de controles",
        "points": [("1 Eliminar: pines de ubicación asimétricos", "Lo mejor, eliminar"),
                   ("2 Prevenir: interbloqueo con código de barras", "Después, prevenir"),
                   ("3 Detectar y detener: sensor de tornillo faltante", "Luego, detectar y detener"),
                   ("4 Advertir: una alarma", "Más débil aún"),
                   ("5 Inspeccionar después — lo más débil", "Lo más débil, inspeccionar después")],
        "example": "Elige los controles por qué tan bien detienen errores — no por qué tan fáciles son de "
                   "instalar.",
        "example_cue": "Elige los controles",
        "script": "No todos los controles son iguales. Este es el orden de fuerza. Lo mejor, eliminar la "
                  "posibilidad de error, con pines de ubicación asimétricos. Después, prevenir la acción "
                  "incorrecta, como un interbloqueo con código de barras. Luego, detectar y detener, como "
                  "un sensor que nota un tornillo faltante. Más débil aún, una alarma de advertencia. Lo "
                  "más débil, inspeccionar después. Elige los controles por qué tan bien detienen errores, "
                  "no por qué tan fáciles son de instalar. ¿En qué nivel están tus chequeos hoy?",
    },
    {
        "key": "p04", "num": 4, "title": "Reglas de ingeniería",
        "points": [("Una señal positiva de aprobado, no 'sin alarma'", "Primero, busca"),
                   ("A prueba de fallas si se pierde energía o sensor", "Segundo, el control debe"),
                   ("Bypass: raro, registrado, con tiempo límite", "Tercero, haz que cualquier bypass"),
                   ("Pruébalo con condiciones incorrectas", "Cuarto, nunca digas")],
        "example": "Divya desconectó el cable del sensor durante una prueba. El fixture siguió bloqueado.",
        "example_cue": "Divya desconectó el cable",
        "script": "Sigue cuatro reglas de ingeniería. Primero, busca una señal positiva de aprobado, no "
                  "solo la ausencia de alarma. Segundo, el control debe fallar de forma segura. Si se "
                  "pierde la energía o un sensor, se detiene. Tercero, haz que cualquier bypass sea raro, "
                  "registrado y con tiempo límite. Cuarto, nunca digas que funciona hasta probarlo con "
                  "condiciones incorrectas. Divya desconectó el cable del sensor durante una prueba. El "
                  "fixture siguió bloqueado. ¿Y qué tipos de Poka Yoke existen?",
    },
    {
        "key": "p05", "num": 5, "title": "Tres métodos",
        "points": [("Contacto: forma, tamaño, posición", "El método de contacto"),
                   ("Valor fijo: la cantidad correcta", "El método de valor fijo"),
                   ("Paso de movimiento: la secuencia correcta", "El método de paso de movimiento")],
        "example": "Problema de orientación → contacto. Pieza faltante → valor fijo. Escanear, programar, "
                   "probar, etiquetar en orden → paso de movimiento.",
        "example_cue": "Tienes un problema de orientación",
        "script": "Hay tres métodos clásicos. El método de contacto usa forma, tamaño o posición para "
                  "distinguir lo correcto de lo incorrecto. Un nido asimétrico es un ejemplo. El método de "
                  "valor fijo revisa la cantidad, como un contador que exige los seis tornillos. El método "
                  "de paso de movimiento revisa la secuencia. Escanear, programar, probar y luego "
                  "etiquetar, en ese orden. Cada uno puede prevenir o detectar. ¿Tienes un problema de "
                  "orientación? Usa contacto. ¿Falta una pieza? Usa valor fijo.",
    },
    {
        "key": "p06", "num": 6, "title": "El error humano es predecible",
        "points": [("Los errores humanos son predecibles", "Los errores humanos son predecibles"),
                   ("Omitir, pieza equivocada, invertida, fuera de orden", "Las personas omiten pasos"),
                   ("Pregunta qué lo hizo posible, no quién", "Así que pregunta qué")],
        "example": "Firmware equivocado → nombres de receta parecidos → modelo elegido a mano → escaneo del "
                   "MES no vinculado al programador.",
        "example_cue": "Divya rastreó",
        "script": "Los errores humanos son predecibles, así que trátalos como riesgos del sistema. Las "
                  "personas omiten pasos, toman la pieza equivocada, invierten cosas o hacen pasos fuera de "
                  "orden. Ingresan un ajuste incorrecto, o confunden etiquetas. Así que pregunta qué hizo "
                  "posible el error, no quién lo cometió. Divya rastreó un firmware equivocado hasta "
                  "recetas con nombres parecidos. El modelo se elegía a mano. El escaneo del MES no estaba "
                  "vinculado al programador. ¿Ya ves la solución?",
    },
    {
        "key": "p07", "num": 7, "title": "Un método de diseño en 8 pasos",
        "points": [("Definir, observar, medir, hallar la causa", "Define el defecto"),
                   ("Elegir la idea robusta más simple", "Elige la idea"),
                   ("Prototipo y prueba con piezas malas", "Construye un prototipo"),
                   ("Actualizar el SOP, capacitar, monitorear", "Luego actualiza el SOP")],
        "example": "Acuerda el éxito antes de instalar: piezas malas rechazadas, piezas buenas aprobadas, el "
                   "ritmo se mantiene.",
        "example_cue": "Antes de instalar",
        "script": "Usa un equipo multifuncional, y trabaja en ocho pasos. Define el defecto. Observa la "
                  "operación real, y encuentra dónde ocurre el error. Mide la línea base, y encuentra la "
                  "causa. Elige la idea robusta más simple. Construye un prototipo, y ponlo a prueba con "
                  "piezas buenas y malas. Luego actualiza el SOP, capacita, y sigue monitoreando. Antes de "
                  "instalar algo, acuerden cómo se ve el éxito. Piezas malas rechazadas, piezas buenas "
                  "aprobadas, y tu ritmo se mantiene.",
    },
    {
        "key": "p08", "num": 8, "title": "Aplicaciones en ensamble",
        "points": [("Señal de torque vinculada a la orden de trabajo", "Vinculó la señal de torque"),
                   ("El fixture solo libera si cada tornillo está bien", "El fixture solo libera"),
                   ("Conectores con guía, sensor de empaque", "También agregó conectores")],
        "example": "Tornillos faltantes: 18 en 10,000 → 1 en 10,000, cerca de 94% menos.",
        "example_cue": "Los tornillos faltantes bajaron",
        "script": "Ahora vamos a la línea de ensamble de Divya. Los tornillos faltantes eran el problema "
                  "mayor. Vinculó la señal de torque del atornillador a la orden de trabajo. El fixture "
                  "solo libera cuando cada tornillo tiene un buen resultado. Una charola magnética no podía "
                  "comprobar eso. Los tornillos faltantes bajaron de dieciocho en diez mil a uno. Eso es "
                  "cerca de noventa y cuatro por ciento menos. También agregó conectores con guía, y un "
                  "sensor de empaque antes de cerrar. ¿Y las tarjetas de adentro?",
    },
    {
        "key": "p09", "num": 9, "title": "Aplicaciones en SMT y prueba",
        "points": [("Cada carrete del alimentador escaneado contra el BOM", "Así que escanea cada carrete"),
                   ("Versión del programa revisada antes de arrancar", "Revisa la versión del programa"),
                   ("Serie vinculada a modelo, firmware y registro de aprobado", "En la prueba, vincula"),
                   ("Una caída de red nunca debe 'aprobar'", "Y asegúrate de que una caída de red")],
        "example": "El probador de Divya no puede imprimir una etiqueta sin un registro de aprobado para esa "
                   "serie.",
        "example_cue": "El probador de Divya",
        "script": "En la línea de tarjetas, un ajuste incorrecto puede crear miles de defectos rápido. Así "
                  "que escanea cada carrete del alimentador contra la lista de materiales. Revisa la "
                  "versión del programa antes de que arranque la máquina. En la prueba, vincula cada número "
                  "de serie con su modelo, firmware y registro de aprobado. El probador de Divya no puede "
                  "imprimir una etiqueta sin ese registro. Y asegúrate de que una caída de red nunca cree "
                  "un falso aprobado. ¿Ya probaste el tuyo así?",
    },
    {
        "key": "p10", "num": 10, "title": "Empaque y embarque",
        "points": [("Escaneo de serie + etiqueta de caja coinciden", "Así que escanea la serie"),
                   ("Accesorios contados antes de cerrar", "cuenta los accesorios"),
                   ("La revisión de peso tiene puntos ciegos", "La revisión de peso ayuda"),
                   ("Los códigos de barras se pueden burlar", "un código de barras no es")],
        "example": "Un adaptador equivocado pesaba lo mismo que el correcto — una charola de kit con forma "
                   "lo detectó.",
        "example_cue": "Divya encontró un adaptador",
        "script": "Un producto perfecto todavía puede volverse una queja en el empaque. Así que escanea la "
                  "serie, compara la etiqueta de la caja, y cuenta los accesorios antes de cerrar la caja. "
                  "La revisión de peso ayuda, pero tiene puntos ciegos. Divya encontró un adaptador "
                  "equivocado que pesaba lo mismo que el correcto. Una charola de kit con forma lo detectó. "
                  "Y recuerda, un código de barras no es a prueba de errores por sí solo. Las etiquetas "
                  "duplicadas y las anulaciones manuales pueden burlarlo. ¿Entonces cada solución debe ser "
                  "cara?",
    },
    {
        "key": "p11", "num": 11, "title": "Bajo costo y seguro",
        "points": [("Simple: pines, guías, interruptores, charolas", "Pines, guías, interruptores"),
                   ("Nunca crear un punto de atrapamiento", "Un dispositivo nunca debe"),
                   ("Los sensores de calidad no son sistemas de seguridad", "un sensor de calidad común"),
                   ("Planea limpieza y calibración", "Planea también su limpieza")],
        "example": "El mejor dispositivo de Divya costó ₹1,200: dos pines que evitan que el panel trasero se "
                   "ponga al revés.",
        "example_cue": "El mejor dispositivo de Divya",
        "script": "Para nada. Muchos de los mejores Poka Yokes son simples. Pines, guías, interruptores de "
                  "límite, charolas de conteo y calibradores pasa, no pasa. El mejor dispositivo de Divya "
                  "costó mil doscientas rupias. Dos pines que evitan que el panel trasero se ponga al "
                  "revés. Pero la seguridad va primero. Un dispositivo nunca debe crear un punto de "
                  "atrapamiento. Y un sensor de calidad común no es un sistema de seguridad. Planea también "
                  "su limpieza y calibración. ¿Y cómo haces que perdure?",
    },
    {
        "key": "p12", "num": 12, "title": "FMEA, plan de control y auditorías",
        "points": [("FMEA: vincular al modo de falla", "En el FMEA"),
                   ("Plan de control: método y reacción", "En el plan de control"),
                   ("Trabajo estandarizado: señal de aprobado, quién reinicia", "En el trabajo estandarizado"),
                   ("Audita con una muestra mala conocida", "Dale una muestra mala conocida")],
        "example": "Divya le da a cada dispositivo una muestra mala conocida, en cada turno.",
        "example_cue": "Divya lo hace en cada turno",
        "script": "Integra cada dispositivo a tu sistema de calidad. En el FMEA, vincúlalo al modo de falla "
                  "que controla. En el plan de control, escribe el método y la reacción. En el trabajo "
                  "estandarizado, muestra cómo se ve un aprobado, y quién puede reiniciar el dispositivo. "
                  "Luego, audítalo. No solo revises que el dispositivo exista. Dale una muestra mala "
                  "conocida, y confirma que la rechaza. Divya lo hace en cada turno. ¿Cómo mides el "
                  "beneficio?",
    },
    {
        "key": "p13", "num": 13, "title": "KPI y ahorros",
        "points": [("Bajan los PPM de defectos y los escapes", "Los PPM de defectos"),
                   ("Sube el rendimiento a la primera", "El rendimiento a la primera debe subir"),
                   ("Vigila los falsos rechazos", "Y vigila los falsos rechazos")],
        "example": "60,000 unidades/mes, defectos de 0.8% a 0.2% ≈ ₹65,000 ahorrados al mes, menos el costo "
                   "de operación.",
        "example_cue": "La línea de Divya produce",
        "script": "Mide el resultado, y la salud de tu dispositivo. Los PPM de defectos y los escapes al "
                  "cliente deben bajar. El rendimiento a la primera debe subir. Y vigila los falsos "
                  "rechazos. Un sensor que rechaza unidades buenas invita a la gente a hacerle bypass. La "
                  "línea de Divya produce sesenta mil unidades al mes. Bajar los defectos de casi uno por "
                  "ciento a una cuarta parte ahorra cerca de sesenta y cinco mil rupias al mes. Luego resta "
                  "tu costo de operación.",
    },
    {
        "key": "p14", "num": 14, "title": "Plan de 90 días",
        "points": [("Semanas 1–2: principales modos de falla + línea base", "En las primeras dos semanas"),
                   ("Semanas 3–4: opciones de diseño, acordar la lógica", "En las dos semanas siguientes"),
                   ("Mes 2: piloto en una estación", "En el segundo mes"),
                   ("Mes 3: documentar, capacitar, copiar", "En el último mes")],
        "example": "Prueba cada condición incorrecta que conozcas durante el piloto.",
        "example_cue": "prueba cada condición incorrecta",
        "script": "Este es un plan simple de noventa días. En las primeras dos semanas, elige tus "
                  "principales modos de falla con el Pareto y el FMEA, y fija una línea base. En las dos "
                  "semanas siguientes, diseña opciones y acuerda la lógica. En el segundo mes, haz un "
                  "piloto en una estación, y prueba cada condición incorrecta que conozcas. En el último "
                  "mes, actualiza los documentos, capacita a la gente, y luego cópialo a otras líneas. "
                  "¿Quién es responsable de cada parte?",
    },
    {
        "key": "p15", "num": 15, "title": "Lista de liberación",
        "points": [("Modo de falla claro, con línea base", "Está claro el modo de falla"),
                   ("Seguridad y ergonomía revisadas", "Se revisaron la seguridad"),
                   ("Muestras malas probadas en cada modelo", "Se probó con muestras malas"),
                   ("Pérdida de energía, sin red, bypass resueltos", "Maneja la pérdida de energía")],
        "example": "Producción es dueña de la estación. Ingeniería la diseña. Calidad la pone a prueba.",
        "example_cue": "Producción es dueña",
        "script": "Producción es dueña de la estación. Ingeniería la diseña, y Calidad la pone a prueba. "
                  "Antes de liberar cualquier dispositivo, usa una lista final. ¿Está claro el modo de "
                  "falla, con una línea base? ¿Se revisaron la seguridad y la ergonomía? ¿Se probó con "
                  "muestras malas en cada modelo? ¿Maneja la pérdida de energía, el modo sin red y el "
                  "bypass? El mejor Poka Yoke hace natural la acción correcta, e imposible la incorrecta.",
    },
]

# The picture beside each page's boxes (same layouts and icons as English, Spanish
# labels). Items appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "versus", "items": [
        {"label": "Una etiqueta advierte", "sub": "'Revisa la orientación'", "icon": "sticker", "with": "example"},
        {"label": "Una guía previene", "sub": "Entra de una sola forma", "icon": "key", "with": "example"}]},
    "p02": {"type": "flow", "stop": {"after": 0, "label": "DETENER AQUÍ", "with": 3}, "items": [
        {"label": "Error", "sub": "La acción incorrecta", "icon": "hand", "tone": "bad", "with": 1},
        {"label": "Defecto", "sub": "El producto malo", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Detectado al final de la línea", "sub": "Mano de obra y piezas ya gastadas", "icon": "search", "tone": "bad", "with": "example"}]},
    "p03": {"type": "ladder", "items": [
        {"label": "Eliminar", "icon": "pin"}, {"label": "Prevenir", "icon": "barcode"},
        {"label": "Detectar y detener", "icon": "sensor"}, {"label": "Advertir", "icon": "warning"},
        {"label": "Inspeccionar después", "icon": "search"}]},
    "p04": {"type": "icons", "items": [
        {"label": "Aprobado positivo", "icon": "check"}, {"label": "A prueba de fallas", "icon": "power"},
        {"label": "Bypass registrado", "icon": "lock"}, {"label": "Probar casos incorrectos", "icon": "test"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Contacto", "sub": "Forma, tamaño, posición", "icon": "shape"},
        {"label": "Valor fijo", "sub": "La cantidad correcta", "icon": "count"},
        {"label": "Paso de movimiento", "sub": "El orden correcto", "icon": "sequence"}]},
    "p06": {"type": "flow", "items": [
        {"label": "Nombres de receta parecidos", "icon": "sticker", "tone": "bad", "with": 2},
        {"label": "Modelo elegido a mano", "icon": "hand", "tone": "bad", "with": 2},
        {"label": "Firmware equivocado", "icon": "chip", "tone": "bad", "with": 2},
        {"label": "Solución: vincular el escaneo del MES", "sub": "al programador", "icon": "barcode", "tone": "good", "with": "example"}]},
    "p07": {"type": "steps", "items": [
        {"label": "Definir", "with": 0}, {"label": "Observar", "with": 0},
        {"label": "Medir", "with": 0}, {"label": "Hallar la causa", "with": 0},
        {"label": "Elegir una idea", "with": 1}, {"label": "Prototipo", "with": 2},
        {"label": "Ponerlo a prueba", "with": 2}, {"label": "Estandarizar", "with": 3}]},
    "p08": {"type": "assembly", "label": "Línea NVR de Divya: el fixture cuenta cada tornillo",
            "then": {"type": "compare", "before": {"label": "Antes", "value": 18}, "after": {"label": "Después", "value": 1},
                     "unit": "tornillos faltantes por cada 10,000 unidades", "note": "cerca de 94% menos"}},
    "p09": {"type": "flow", "stop": {"after": 2, "label": "SIN APROBADO, SIN ETIQUETA", "with": "example"}, "items": [
        {"label": "Carrete escaneado contra el BOM", "icon": "barcode", "with": 0},
        {"label": "Versión del programa revisada", "icon": "chip", "with": 1},
        {"label": "Registro de aprobado por serie", "icon": "test", "with": 2},
        {"label": "Se imprime la etiqueta", "icon": "label", "tone": "good", "with": "example"}]},
    "p10": {"type": "versus", "items": [
        {"label": "Revisión de peso", "sub": "Adaptador equivocado, mismo peso", "icon": "scale", "with": "example"},
        {"label": "Charola de kit con forma", "sub": "El adaptador equivocado no entra", "icon": "tray", "with": "example"}]},
    "p11": {"type": "stat", "value": 1200, "prefix": "₹", "icon": "pin", "label": "Dos pines de ubicación",
            "unit": "Ya no hay paneles traseros puestos al revés"},
    "p12": {"type": "flow", "items": [
        {"label": "FMEA", "sub": "El modo de falla", "icon": "clipboard"},
        {"label": "Plan de control", "sub": "Método y reacción", "icon": "shield"},
        {"label": "Trabajo estandarizado", "sub": "Señal de aprobado, quién reinicia", "icon": "person"},
        {"label": "Auditoría", "sub": "Una muestra mala conocida", "icon": "test", "tone": "good"}]},
    "p13": {"type": "compare", "before": {"label": "Antes", "value": 0.8}, "after": {"label": "Después", "value": 0.2},
            "suffix": "%", "decimals": 1, "unit": "tasa de defectos, 60,000 unidades al mes", "note": "≈ ₹65,000 ahorrados al mes"},
    "p14": {"type": "timeline", "items": [
        {"label": "Modos de falla + línea base", "sub": "W1–2", "span": 2, "icon": "search"},
        {"label": "Opciones de diseño, acordar la lógica", "sub": "W3–4", "span": 2, "icon": "gear"},
        {"label": "Piloto en una estación", "sub": "Mes 2", "span": 4, "icon": "test"},
        {"label": "Documentar, capacitar, copiar", "sub": "Mes 3", "span": 4, "icon": "clipboard"}]},
    "p15": {"type": "icons", "items": [
        {"label": "Producción", "sub": "Dueña de la estación", "icon": "person", "with": "example"},
        {"label": "Ingeniería", "sub": "La diseña", "icon": "gear", "with": "example"},
        {"label": "Calidad", "sub": "La pone a prueba", "icon": "shield", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un fixture no se libera hasta contar los seis tornillos. ¿Qué método de Poka Yoke es "
                    "este?",
        "options": ["Método de contacto", "Método de valor fijo", "Método de paso de movimiento"],
        "correct": 1,
        "explanation": "Confirma la cantidad correcta, así que es el método de valor fijo. Contacto revisa forma "
                       "o posición; paso de movimiento revisa la secuencia.",
        "q_script": "Prueba rápida. Un fixture no se libera hasta contar los seis tornillos. ¿Qué método de "
                    "Poka Yoke es ese? Tómate unos segundos.",
        "a_script": "Es el método de valor fijo. Confirma la cantidad correcta. Contacto revisa la forma, y "
                    "paso de movimiento revisa la secuencia.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un nuevo sensor de empaque rechaza tantas unidades buenas que los operadores empiezan a "
                    "hacerle bypass. ¿Qué debe hacer el equipo PRIMERO?",
        "options": ["Quitar el sensor", "Sancionar a los operadores",
                    "Controlar el bypass y corregir los falsos rechazos con muestras verificadas",
                    "Agregar un letrero recordatorio"],
        "correct": 2,
        "explanation": "Los falsos rechazos invitan al bypass. Bloquea el bypass, luego mejora la posición, la "
                       "iluminación o los umbrales con muestras buenas y malas conocidas, y da seguimiento a la "
                       "tasa de falsos rechazos.",
        "q_script": "Una más, y esta es un escenario. Un nuevo sensor de empaque rechaza tantas unidades "
                    "buenas que los operadores empiezan a hacerle bypass. ¿Qué debe hacer primero el equipo? "
                    "Piénsalo.",
        "a_script": "Controla el bypass, y luego corrige los falsos rechazos. Mejora el ajuste del sensor, "
                    "con muestras buenas y malas conocidas. Los falsos rechazos invitan a la gente a hacerle "
                    "bypass a un dispositivo.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
