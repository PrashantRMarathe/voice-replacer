"""qrqc in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh qrqc_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "qr_es"
NAME = "qrqc_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Root Cause Analysis": "rut cos análisis",
    "QRQC": "cu erre cu ce",
    "FMEA": "efe eme e a",
    "5W2H": "cinco doble u dos hache",
    "MES": "eme e ese",
    "SKU": "ese ka u",
    "SOP": "ese o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Diez de la mañana. Las cámaras empiezan a fallar la prueba de enfoque. Alguien reinicia "
    "el probador, y la línea sigue. Para el mediodía, un turno completo de cámaras "
    "sospechosas va camino al almacén. ¿Te suena familiar? En esta lección aprenderás QRQC, "
    "el control de calidad de respuesta rápida. Verás cómo reaccionar en minutos, proteger a "
    "tu cliente, y aun así encontrar la causa real. Seguiremos a Farhan, líder de calidad en "
    "una planta de cámaras."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Reacciona rápido, pero con evidencia. Primero contén, y "
    "cuadra cada unidad sospechosa. Y cierra un problema solo cuando la solución esté "
    "comprobada en producción real. Esta es tu acción para esta semana. Escribe los primeros "
    "treinta minutos de tu plan de reacción para un defecto crítico. Excelente trabajo al "
    "completar esta lección. Ahora profundizarás en el Root Cause Analysis."
)

# Each page: title, 2-5 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es QRQC",
        "points": [("Detéctalo y hazlo visible", "Lo detectas"),
                   ("Contenlo para proteger al cliente", "Lo contienes"),
                   ("Encuentra la causa con hechos, comprueba la solución", "Luego encuentras la causa"),
                   ("La rapidez nunca reemplaza a la evidencia", "La rapidez importa")],
        "example": "Línea 4: el QRQC empieza aislando la orden de trabajo — no reiniciando el probador.",
        "example_cue": "En la Línea cuatro de Farhan",
        "script": "Esta es la idea central. QRQC significa control de calidad de respuesta rápida. Es una "
                  "forma disciplinada de reaccionar a un problema. Lo detectas y lo haces visible. Lo "
                  "contienes, para proteger a tu cliente. Luego encuentras la causa con hechos, y "
                  "compruebas que la solución funciona. La rapidez importa, pero nunca reemplaza a la "
                  "evidencia. En la Línea cuatro de Farhan, el QRQC empieza aislando la orden de trabajo. "
                  "No reiniciando el probador. ¿Y qué hay detrás de este enfoque?",
    },
    {
        "key": "p02", "num": 2, "title": "Principios clave",
        "points": [("Lugar real, piezas reales", "Ve al lugar real"),
                   ("Hechos verificados, nunca culpa", "Usa hechos verificados"),
                   ("Reacciona de inmediato ante riesgo para el cliente o de seguridad", "Reacciona de inmediato"),
                   ("Contención ≠ solución permanente", "Y mantén la contención temporal")],
        "example": "La junta de Farhan empieza con la cámara con falla sobre la mesa, junto a sus registros.",
        "example_cue": "La junta de Farhan empieza",
        "script": "El QRQC nació en la calidad de los proveedores automotrices. Se apoya en algunos "
                  "principios. Ve al lugar real, y mira las piezas reales. Usa hechos verificados, nunca "
                  "opiniones ni culpas. Reacciona de inmediato ante cualquier riesgo para el cliente o de "
                  "seguridad. Y mantén la contención temporal separada de la solución permanente. La junta "
                  "de Farhan empieza con la cámara con falla sobre la mesa, junto a sus registros. ¿Qué "
                  "pondrías tú en tu mesa?",
    },
    {
        "key": "p03", "num": 3, "title": "Tres niveles de escalamiento",
        "points": [("Nivel 1: reacciona la línea o el turno", "En el nivel uno"),
                   ("Nivel 2: equipo de varias áreas", "En el nivel dos"),
                   ("Nivel 3: líderes de planta, cliente", "En el nivel tres"),
                   ("Escala de inmediato: seguridad, fuga repetida", "Escala de inmediato")],
        "example": "Tu planta fija los tiempos de escalamiento, según el riesgo.",
        "example_cue": "Tu planta fija los tiempos",
        "script": "Un buen sistema QRQC tiene tres niveles. En el nivel uno, la línea o el turno detecta el "
                  "problema, detiene o separa, y registra la evidencia. En el nivel dos, un equipo de "
                  "varias áreas investiga y actúa. En el nivel tres, los líderes de planta agregan "
                  "recursos, o hablan con el cliente. Escala de inmediato si hay un riesgo de seguridad, o "
                  "una fuga repetida. Tu planta fija los tiempos, según el riesgo. ¿Y qué pasa en los "
                  "primeros minutos?",
    },
    {
        "key": "p04", "num": 4, "title": "Los primeros 30 minutos",
        "points": [("0–5 min: detecta, ubica estación y lote, aísla", "En los primeros cinco minutos"),
                   ("Luego: avisa al líder y a Calidad, guarda muestras", "Después, avisa al líder de turno"),
                   ("Luego: encuentra el último punto bueno conocido", "Luego encuentra el último punto bueno"),
                   ("Para los 30 min: cuarentena, registro, asignación", "Para los treinta minutos")],
        "example": "Nunca vuelvas a arrancar un proceso crítico con un visto bueno de palabra.",
        "example_cue": "nunca vuelvas a arrancar un proceso crítico",
        "script": "La primera media hora marca el tono. En los primeros cinco minutos, detéctalo, ubica la "
                  "estación y el lote, y detén o aísla el flujo. Después, avisa al líder de turno y a "
                  "Calidad, y guarda muestras con falla y buenas. Luego encuentra el último punto bueno "
                  "conocido. Para los treinta minutos, pon en cuarentena el inventario sospechoso, y "
                  "registra cantidades y responsables. Y nunca vuelvas a arrancar un proceso crítico con un "
                  "visto bueno de palabra. ¿Cuál sería tu primera llamada?",
    },
    {
        "key": "p05", "num": 5, "title": "5W2H: definir el problema",
        "points": [("Qué, dónde, cuándo, quién", "Qué falló, dónde"),
                   ("Cómo se detectó, cuántos", "cómo se detectó"),
                   ("Rechazos confirmados contra población sospechosa", "Separa los rechazos confirmados")],
        "example": "Línea 4: 24 de 800 cámaras fallaron el enfoque entre las 10 y el mediodía, justo después "
                   "de un cambio de fixture de lentes.",
        "example_cue": "En la Línea cuatro, veinticuatro",
        "script": "Un planteamiento preciso evita que persigas lo equivocado. Usa el 5W2H. Qué falló, "
                  "dónde, cuándo, quién lo vio, cómo se detectó, y cuántos. Separa los rechazos confirmados "
                  "de la población sospechosa. Este es el planteamiento de Farhan. En la Línea cuatro, "
                  "veinticuatro de ochocientas cámaras fallaron el enfoque esa mañana. Empezó justo después "
                  "de un cambio de fixture de lentes. Nota cómo eso ya apunta a algún lado. ¿Pero primero, "
                  "qué pasa con las unidades sospechosas?",
    },
    {
        "key": "p06", "num": 6, "title": "Contención y cuadre",
        "points": [("Encuentra el alcance sospechoso", "Encuentra el alcance sospechoso"),
                   ("Retenlo: físicamente y en el sistema", "Retén ese inventario"),
                   ("Revisa según el riesgo", "Revísalo según el riesgo"),
                   ("Cuadra cada unidad", "Luego cuadra cada unidad")],
        "example": "2,000 cámaras sospechosas: revisadas buenas + con falla + en espera deben sumar exacto. "
                   "Ninguna unidad puede desaparecer.",
        "example_cue": "Farhan tenía dos mil",
        "script": "La contención es una barrera, no una cura. Encuentra el alcance sospechoso por número de "
                  "serie, orden de trabajo y turno. Retén ese inventario, físicamente y en el sistema. "
                  "Revísalo según el riesgo. Luego cuadra cada unidad. Farhan tenía dos mil cámaras "
                  "sospechosas. La mayoría salió buena, algunas fallaron, y el resto seguía esperando. Los "
                  "números deben sumar exacto. Ninguna unidad puede simplemente desaparecer. ¿Y dónde sigue "
                  "el equipo todo esto?",
    },
    {
        "key": "p07", "num": 7, "title": "El tablero QRQC y la junta",
        "points": [("Riesgo, contención, causa, acción, responsable, fecha", "Cada problema muestra"),
                   ("Rojo abierto · ámbar verificando · verde comprobado", "Usa rojo para abierto"),
                   ("Lleva muestras reales y gráficas de tendencia", "Lleva las muestras reales"),
                   ("Nada 'terminado' sin prueba", "cuidado con el teatro de juntas")],
        "example": "La junta de 15 minutos de Farhan: problemas nuevos, luego contención, luego acciones y "
                   "escalamientos.",
        "example_cue": "Farhan hace una junta de quince",
        "script": "El tablero QRQC es tu centro de control. Cada problema muestra su riesgo, contención, "
                  "causa, acción, responsable y fecha límite. Usa rojo para abierto, ámbar para "
                  "verificando, y verde solo para un cierre comprobado. Farhan hace una junta de quince "
                  "minutos frente al tablero en cada turno. Primero los problemas nuevos, luego la "
                  "contención, luego las acciones y los escalamientos. Lleva las muestras reales y las "
                  "gráficas de tendencia. Y cuidado con el teatro de juntas. ¿Hay algo marcado como "
                  "terminado sin prueba?",
    },
    {
        "key": "p08", "num": 8, "title": "Causa raíz con evidencia",
        "points": [("Cinco porqués = una hipótesis, no una prueba", "Una cadena de cinco porqués"),
                   ("Reproduce la falla de forma segura", "Reproduce la falla"),
                   ("Lluvia de ideas en las 6M", "Haz una lluvia de causas en"),
                   ("Pasó · se escapó · el sistema lo permitió", "Busca tres causas")],
        "example": "Una espina de pescado sola no basta: cada idea en competencia debe probarse.",
        "example_cue": "Luego prueba las ideas en competencia",
        "script": "Ahora encuentra la causa raíz, con evidencia. Una cadena de cinco porqués es una "
                  "hipótesis, no una prueba. Reproduce la falla de forma segura si puedes. Haz una lluvia "
                  "de causas en personas, máquina, método, material, medición y medio ambiente. Luego "
                  "prueba las ideas en competencia. Busca tres causas. Por qué pasó, por qué se escapó, y "
                  "qué en el sistema permitió las dos cosas. ¿Ves por qué una espina de pescado sola no "
                  "basta?",
    },
    {
        "key": "p09", "num": 9, "title": "Acción correctiva y control de cambios",
        "points": [("Corrige cómo pasó y cómo se escapó", "Ataca las dos"),
                   ("Controles de ingeniería antes que recordatorios", "Prefiere controles de ingeniería"),
                   ("Revisa tiempo de ciclo, seguridad, rechazos falsos", "Revisa el efecto"),
                   ("Actualiza el FMEA, el SOP, el entrenamiento", "Luego actualiza el FMEA")],
        "example": "Un 'revisa el fixture' de palabra se volvió un escaneo: cada fixture ligado a su receta "
                   "aprobada.",
        "example_cue": "En la línea de Farhan",
        "script": "Ahora corrige cada causa verificada. Ataca las dos, cómo pasó, y cómo se escapó. "
                  "Prefiere controles de ingeniería, como fixtures con guía e interbloqueos por escaneo, "
                  "antes que recordatorios. Revisa el efecto en el tiempo de ciclo, la seguridad y los "
                  "rechazos falsos. Luego actualiza el FMEA, el SOP y el entrenamiento. En la línea de "
                  "Farhan, una instrucción de palabra de revisar el fixture se volvió un escaneo. Ahora "
                  "cada fixture está ligado a su receta aprobada. ¿Y cuándo puedes cerrarlo?",
    },
    {
        "key": "p10", "num": 10, "title": "Criterios de cierre",
        "points": [("Instalado ≠ comprobado", "Instalar una solución"),
                   ("Reto: piezas buenas, malas y en el límite", "rétala con piezas buenas conocidas"),
                   ("En varios turnos, modelos, cambios", "Revísala en varios turnos"),
                   ("Cada unidad sospechosa decidida, luego la firma", "Asegúrate de que cada unidad sospechosa")],
        "example": "La regla de Farhan: diez días de producción sin repetición antes de que el tablero se "
                   "ponga en verde.",
        "example_cue": "Farhan espera diez",
        "script": "Esta es la trampa. Instalar una solución no es lo mismo que comprobarla. Para cerrar, "
                  "rétala con piezas buenas conocidas, malas conocidas y en el límite. Revísala en varios "
                  "turnos, modelos y cambios de modelo. Sigue la repetición y el rendimiento durante un "
                  "periodo fijo. Asegúrate de que cada unidad sospechosa tenga una decisión. Luego Calidad "
                  "y el responsable firman. Farhan espera diez días de producción sin repetición. Solo "
                  "entonces el tablero se pone en verde. ¿Cómo mides todo esto?",
    },
    {
        "key": "p11", "num": 11, "title": "KPI del QRQC",
        "points": [("Tiempo de respuesta: detección → contención", "El tiempo de respuesta va"),
                   ("% de cobertura de la contención", "La cobertura de la contención es"),
                   ("Rendimiento a la primera y tasa de defectos", "Sigue el rendimiento a la primera"),
                   ("Cierre de acciones a tiempo", "mide el cierre a tiempo")],
        "example": "95% de las unidades sospechosas encontradas = no has terminado: 5% siguen allá afuera.",
        "example_cue": "Si encontraste",
        "script": "Usa un conjunto equilibrado de medidas. El tiempo de respuesta va de la detección a la "
                  "primera contención efectiva. La cobertura de la contención es la parte de las unidades "
                  "sospechosas que ya ubicaste. Sigue el rendimiento a la primera y la tasa de defectos. Y "
                  "mide el cierre a tiempo de las acciones. Aquí va una sutil. Si encontraste el noventa y "
                  "cinco por ciento de las unidades sospechosas, no has terminado. El cinco por ciento "
                  "sigue allá afuera. ¿Listo para el caso de Farhan?",
    },
    {
        "key": "p12", "num": 12, "title": "Caso práctico: falla de enfoque",
        "points": [("24 de 800 fallan el enfoque contra < 0.5% normal", "Después del cambio de modelo"),
                   ("Retener la orden de trabajo + lo producido desde el último ajuste bueno", "Farhan retuvo la orden de trabajo"),
                   ("Comparar fixture, receta, tendencia de enfoque", "El equipo comparó"),
                   ("Probar la hipótesis de la receta", "Su hipótesis era")],
        "example": "La receta de enfoque equivocada reprodujo la falla en muestras controladas. Solo "
                   "entonces se le llamó la causa.",
        "example_cue": "Así que la probaron",
        "script": "Esta es la historia completa. Después del cambio de modelo, veinticuatro de ochocientas "
                  "cámaras fallaron el enfoque. La tasa normal era menos de medio por ciento. Farhan retuvo "
                  "la orden de trabajo, y todo lo producido desde el último ajuste bueno. El equipo comparó "
                  "los registros del fixture, las versiones de receta y las tendencias de enfoque. Su "
                  "hipótesis era la receta de enfoque equivocada. Así que la probaron en muestras "
                  "controladas, y reprodujo la falla. Solo entonces la llamaron la causa. ¿Tu equipo habría "
                  "esperado?",
    },
    {
        "key": "p13", "num": 13, "title": "Caso práctico: etiqueta que no coincide",
        "points": [("Etiqueta de la caja ≠ equipo adentro", "Una caja de grabadora de video"),
                   ("Retener la tarima, comparar cada número de serie", "El equipo retuvo la tarima"),
                   ("Rastrear escaneos y trabajos de impresión", "Luego rastrearon"),
                   ("Forzar la coincidencia serie-SKU, registrar los brincos", "Así que la solución forzó")],
        "example": "Causa raíz: la comparación del MES se apagó durante una falla de la impresora, y nadie "
                   "lo registró.",
        "example_cue": "La comparación del MES se había",
        "script": "Este es un segundo caso, de empaque. Una caja de grabadora de video mostraba el SKU "
                  "equivocado. El producto adentro funcionaba perfecto. Pero el cliente de todos modos "
                  "recibiría el artículo equivocado. El equipo retuvo la tarima, y comparó cada número de "
                  "serie con su etiqueta. Luego rastrearon los escaneos y los trabajos de impresión. La "
                  "comparación del MES se había apagado durante una falla de la impresora. Nadie lo "
                  "registró. Así que la solución forzó una coincidencia serie-SKU antes de imprimir, y "
                  "registró cada brinco. ¿Tú habrías buscado ahí?",
    },
    {
        "key": "p14", "num": 14, "title": "Implementación en 90 días",
        "points": [("Primero un piloto en un área de alto riesgo", "Empieza con un área piloto"),
                   ("Días 1–30: disparadores, niveles, tablero", "En los primeros treinta días"),
                   ("Días 31–60: entrena a los líderes, haz las juntas", "En los siguientes treinta"),
                   ("Días 61–90: audita, liga al FMEA, extiende", "En los últimos treinta")],
        "example": "Implementa el QRQC como un sistema operativo, no como un formato aislado.",
        "example_cue": "implementa el QRQC como un sistema operativo",
        "script": "Ahora, implementa el QRQC como un sistema operativo, no como un formato aislado. Empieza "
                  "con un área piloto de alto riesgo, y estabiliza ahí el método. En los primeros treinta "
                  "días, fija los disparadores, los niveles y el tablero. En los siguientes treinta, "
                  "entrena a tus líderes de línea y haz las juntas. En los últimos treinta, audita las "
                  "acciones, lígalas al FMEA, y extiéndelo a otras líneas. ¿Quién es dueño de qué?",
    },
    {
        "key": "p15", "num": 15, "title": "El registro del problema y los puestos",
        "points": [("El director de planta patrocina", "El director de planta lo patrocina"),
                   ("Calidad es dueña del método", "Calidad es dueña del método"),
                   ("Producción es dueña de la reacción", "Producción es dueña"),
                   ("Ingeniería es dueña de las soluciones técnicas", "E Ingeniería es dueña"),
                   ("Un registro para cada problema", "Lleva un registro")],
        "example": "La prueba: ¿alguien podría reconstruir todo el evento solo con tu registro?",
        "example_cue": "¿Alguien podría reconstruir",
        "script": "El director de planta lo patrocina. Calidad es dueña del método. Producción es dueña de "
                  "la reacción inmediata. E Ingeniería es dueña de las soluciones técnicas. Lleva un "
                  "registro para cada problema. Contiene el problema, las fotos y la ventana sospechosa. "
                  "Contiene la contención y el cuadre, las causas, las acciones y la prueba. Esta es la "
                  "prueba. ¿Alguien podría reconstruir todo el evento solo con tu registro? Reacciona "
                  "rápido, pero cierra siempre con evidencia.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Detectar, hacerlo visible", "icon": "sensor", "with": 0},
        {"label": "Contener: proteger al cliente", "icon": "lock", "with": 1},
        {"label": "Causa con hechos, comprobar la solución", "icon": "search", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Reiniciar el probador", "sub": "y seguir corriendo", "icon": "power"},
            {"label": "Aislar la orden de trabajo", "sub": "Aquí empieza el QRQC", "icon": "lock"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Lugar real, piezas reales", "icon": "walk"}, {"label": "Hechos, nunca culpa", "icon": "search"},
        {"label": "Reaccionar de inmediato", "icon": "warning"}, {"label": "La contención no es la solución", "icon": "lock"}]},
    "p03": {"type": "flow", "items": [
        {"label": "Nivel 1: línea o turno", "sub": "Detener, separar, registrar", "icon": "person", "with": 0},
        {"label": "Nivel 2: equipo de varias áreas", "sub": "Investigar y actuar", "icon": "gear", "with": 1},
        {"label": "Nivel 3: líderes de planta", "sub": "Recursos, el cliente", "icon": "shield", "with": 2}]},
    "p04": {"type": "timeline", "items": [
        {"label": "Detectar, ubicar estación y lote, aislar", "sub": "0–5", "span": 5, "icon": "sensor"},
        {"label": "Avisar al líder y a Calidad, guardar muestras", "sub": "Después", "span": 8, "icon": "person"},
        {"label": "Encontrar el último punto bueno conocido", "sub": "Luego", "span": 7, "icon": "search"},
        {"label": "Cuarentena, registro, asignación", "sub": "Para los 30", "span": 10, "icon": "lock"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Qué, dónde, cuándo, quién", "icon": "search", "with": 0},
        {"label": "Cómo se detectó, cuántos", "icon": "count", "with": 1},
        {"label": "Rechazos contra sospechosos", "icon": "stack", "with": 2}],
        "then": {"type": "stat", "value": 24, "suffix": " / 800", "icon": "camera", "label": "cámaras fallaron el enfoque",
                 "unit": "De las 10 al mediodía, justo después de un cambio de fixture de lentes", "with": "example"}},
    "p06": {"type": "icons", "items": [
        {"label": "Encontrar el alcance", "icon": "search"}, {"label": "Retenerlo", "icon": "lock"},
        {"label": "Revisar según el riesgo", "icon": "test"}, {"label": "Cuadrar", "icon": "count"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "2,000 cámaras sospechosas", "icon": "stack", "with": "example"},
            {"label": "Buenas + con falla + en espera", "icon": "count", "with": "example"},
            {"label": "= 2,000: no falta ninguna", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Abierto", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Verificando", "icon": "clock", "with": 1},
        {"label": "Comprobado", "sub": "Solo entonces: verde", "icon": "check", "tone": "good", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Problemas nuevos", "icon": "warning", "with": "example"},
            {"label": "Contención", "icon": "lock", "with": "example"},
            {"label": "Acciones, escalamientos", "icon": "sequence", "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Personas", "icon": "person", "with": 2}, {"label": "Máquina", "icon": "gear", "with": 2},
        {"label": "Método", "icon": "clipboard", "with": 2}, {"label": "Material", "icon": "box", "with": 2},
        {"label": "Medición", "icon": "scale", "with": 2}, {"label": "Medio ambiente", "icon": "wave", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Pasó + se escapó", "icon": "search"}, {"label": "Controles de ingeniería", "icon": "key"},
        {"label": "Tiempo de ciclo, seguridad", "icon": "clock"}, {"label": "FMEA, SOP, entrenamiento", "icon": "clipboard"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "“Revisa el fixture”", "sub": "Un recordatorio de palabra", "icon": "person"},
            {"label": "Escaneo del fixture", "sub": "Ligado a su receta aprobada", "icon": "barcode"}]}},
    "p10": {"type": "icons", "items": [
        {"label": "Instalado no es comprobado", "icon": "cross", "tone": "bad"}, {"label": "Rétala", "icon": "test"},
        {"label": "En varios turnos, modelos", "icon": "sequence"}, {"label": "Cada unidad decidida", "icon": "check"}],
        "then": {"type": "stat", "value": 10, "suffix": " días", "icon": "calendar", "label": "de producción sin repetición",
                 "unit": "antes de que el tablero se ponga en verde", "with": "example"}},
    "p11": {"type": "icons", "items": [
        {"label": "Tiempo de respuesta", "icon": "clock"}, {"label": "Cobertura de la contención", "icon": "count"},
        {"label": "Rendimiento, tasa de defectos", "icon": "chartUp"}, {"label": "Cierre a tiempo", "icon": "calendar"}],
        "then": {"type": "stat", "value": 5, "suffix": "%", "icon": "warning", "label": "de las unidades sospechosas siguen allá afuera",
                 "unit": "Encontrar el 95% no es terminar", "with": "example"}},
    "p12": {"type": "flow", "items": [
        {"label": "24 de 800 fallan el enfoque", "sub": "Normal: menos de 0.5%", "icon": "camera", "tone": "bad", "with": 0},
        {"label": "Retener desde el último ajuste bueno", "icon": "lock", "with": 1},
        {"label": "Comparar fixture, receta, tendencia", "icon": "search", "with": 2},
        {"label": "La receta equivocada la reprodujo", "sub": "Solo entonces: la causa", "icon": "test", "tone": "good", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Etiqueta de la caja ≠ equipo", "icon": "label", "tone": "bad", "with": 0},
        {"label": "Retener la tarima, comparar números de serie", "icon": "lock", "with": 1},
        {"label": "Comparación del MES apagada", "sub": "Durante una falla de la impresora, sin registro", "icon": "warning", "tone": "bad", "with": "example"},
        {"label": "Coincidencia serie-SKU forzada", "sub": "Cada brinco registrado", "icon": "barcode", "tone": "good", "with": 3}]},
    "p14": {"type": "timeline", "items": [
        {"label": "Disparadores, niveles, tablero", "sub": "Días 1–30", "icon": "clipboard", "with": 1},
        {"label": "Entrenar líderes, hacer juntas", "sub": "31–60", "icon": "person", "with": 2},
        {"label": "Auditar, ligar al FMEA, extender", "sub": "61–90", "icon": "chartUp", "with": 3}]},
    "p15": {"type": "icons", "items": [
        {"label": "Director de planta", "sub": "Patrocina", "icon": "person"}, {"label": "Calidad", "sub": "El método", "icon": "shield"},
        {"label": "Producción", "sub": "La reacción", "icon": "wrench"}, {"label": "Ingeniería", "sub": "Las soluciones", "icon": "gear"},
        {"label": "Un registro", "sub": "Cada problema", "icon": "clipboard"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Se encontraron y revisaron 1,900 de 2,000 unidades sospechosas. ¿Está completa la "
                    "contención?",
        "options": ["Sí — 95% es suficiente", "No — todavía faltan 100 unidades sospechosas por ubicar",
                    "Sí, si la solución está instalada"],
        "correct": 1,
        "explanation": "Una cobertura de contención de 95% significa que el 5% de la población sospechosa sigue "
                       "allá afuera. La contención está completa solo cuando cada unidad está ubicada.",
        "q_script": "Prueba rápida. Se encontraron y revisaron mil novecientas de dos mil unidades "
                    "sospechosas. ¿Está completa la contención? Tómate unos segundos.",
        "a_script": "No. Todavía faltan cien unidades sospechosas por ubicar. La contención está completa "
                    "solo cuando aparece cada unidad.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Las fallas de enfoque se disparan en la prueba justo después de un cambio de fixture. Se "
                    "reinicia el probador y pasa. ¿Qué debe pasar PRIMERO?",
        "options": ["Seguir corriendo — el probador pasó", "Aislar las unidades desde el último ajuste bueno y registrar la evidencia",
                    "Regresar el fixture y no decir nada", "Esperar la junta del final del día"],
        "correct": 1,
        "explanation": "Primero protege al cliente: retén todo desde el último ajuste verificado, guarda "
                       "muestras y registros, y luego investiga. Reiniciar el probador esconde la anormalidad.",
        "q_script": "Una más, y esta es un escenario. Las fallas de enfoque se disparan justo después de un "
                    "cambio de fixture. Alguien reinicia el probador, y pasa. ¿Qué debe pasar primero? "
                    "Piénsalo.",
        "a_script": "Aísla cada unidad desde el último ajuste bueno, y registra la evidencia. Luego "
                    "investiga. Reiniciar el probador solo esconde el problema.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
