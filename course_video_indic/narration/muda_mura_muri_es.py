"""muda_mura_muri in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh muda_mura_muri_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "mm_es"
NAME = "muda_mura_muri_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Next Inspection": "nekst inspékshon",
    "Poka Yoke": "Poka Yoke",
    "TIMWOODS": "tim uúds",
    "Heijunka": "Jeiyunka",
    "Gemba": "Guemba",
    "CCTV": "ce ce te ve",
    "SMED": "esméd",
    "TAKT": "takt",
    "Muda": "Muda",
    "Mura": "Mura",
    "Muri": "Muri",
    "TPM": "te pe eme",
    "WIP": "doble u i pe",
    "3M": "tres eme",
    "5S": "cinco eses",
    "M": "eme",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Seis de la tarde. El turno termina en una hora, y la línea de Sanjay va cuarenta cámaras "
    "atrás. Todos corren. Los errores se acumulan en la prueba. Mañana, vuelve a pasar. ¿Te "
    "suena familiar? En esta lección aprenderás las 3M de Lean: Muda, Mura y Muri. Verás cómo "
    "el desperdicio, la disparidad y la sobrecarga se alimentan entre sí. Y seguiremos a "
    "Sanjay, supervisor de línea en una línea de cámaras CCTV, mientras rompe ese ciclo."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Muda es desperdicio, Mura es disparidad, y Muri es "
    "sobrecarga. Se alimentan entre sí, así que mejóralas juntas. Y la meta es un flujo "
    "estable, no gente trabajando más rápido. Esta es tu acción para esta semana. Sigue un "
    "producto por tu línea, y marca un ejemplo de cada M. Excelente trabajo al completar esta "
    "lección. Ahora aprenderás Next Inspection, para proteger el proceso que sigue al tuyo."
)

# One story thread: Sanjay's CCTV camera assembly line. Big work-order releases,
# WIP waves before test, walking for parts, end-of-shift rush and overtime.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Conoce las 3M",
        "points": [("Muda: desperdicio — sin valor para el cliente", "Muda es desperdicio"),
                   ("Mura: disparidad — la carga sube y baja", "Mura es disparidad"),
                   ("Muri: sobrecarga — más allá de la capacidad segura", "Muri es sobrecarga")],
        "example": "La línea de Sanjay, en una hora: los operadores esperan kits (Muda), la producción sube "
                   "y baja (Mura), luego todos corren (Muri).",
        "example_cue": "En la línea de Sanjay",
        "script": "Esta es la idea central. Lean busca tres enemigos del buen flujo. Muda es desperdicio, "
                  "trabajo que no agrega valor para tu cliente. Mura es disparidad, una carga que sube y "
                  "baja. Muri es sobrecarga, pedirles a las personas o a las máquinas más de lo que pueden "
                  "dar con seguridad. En la línea de Sanjay, puedes ver las tres en una hora. Los "
                  "operadores esperan kits, la producción sube y baja, y luego todos corren. ¿Y cuál debes "
                  "atacar primero?",
    },
    {
        "key": "p02", "num": 2, "title": "Cómo se conectan las 3M",
        "points": [("No puedes corregirlas una por una", "No puedes corregirlas"),
                   ("Mura crea Muri, Muri crea Muda", "Mura muchas veces crea"),
                   ("Persigue solo el desperdicio y regresa", "Si solo persigues")],
        "example": "El gran lote del lunes (Mura) → operadores y probador a las carreras (Muri) → defectos, "
                   "retrabajo, horas extra (Muda).",
        "example_cue": "El planeador de Sanjay liberó",
        "script": "Aquí está la sorpresa. No puedes corregirlas una por una. Mura muchas veces crea Muri, y "
                  "Muri crea Muda. El planeador de Sanjay liberó un lote enorme el lunes en la mañana. Eso "
                  "es Mura. Para alcanzar, los operadores se apuraron y el probador nunca descansó. Eso es "
                  "Muri. Luego llegaron los defectos, el retrabajo y las horas extra. Eso es Muda. Si solo "
                  "persigues el desperdicio, regresa de inmediato. Así que veamos de cerca cada una, "
                  "empezando por el desperdicio.",
    },
    {
        "key": "p03", "num": 3, "title": "Muda: la prueba del valor",
        "points": [("¿Cambia el producto que el cliente necesita?", "¿Este paso cambia"),
                   ("¿Se hace bien a la primera?", "¿Se hace bien"),
                   ("¿El cliente pagaría por ello?", "¿El cliente pagaría con gusto"),
                   ("Si no — cuestiónalo", "Si la respuesta es no")],
        "example": "Colocar el lente agrega valor. Caminar por etiquetas, esperar un kit y probar dos veces "
                   "no.",
        "example_cue": "En la línea de Sanjay, colocar",
        "script": "¿Cómo detectas el desperdicio? Usa una prueba simple del valor. ¿Este paso cambia el "
                  "producto de una forma que tu cliente necesita? ¿Se hace bien a la primera? ¿El cliente "
                  "pagaría con gusto por ello? Si la respuesta es no, cuestiónalo. En la línea de Sanjay, "
                  "colocar el lente agrega valor. Caminar por etiquetas no. Tampoco esperar un kit, ni "
                  "probar una cámara dos veces. ¿Pero puedes quitar cada paso que no pasa la prueba?",
    },
    {
        "key": "p04", "num": 4, "title": "Necesario contra puro desperdicio",
        "points": [("Tipo 1: se necesita hoy — simplifícalo", "Algunos pasos no agregan valor"),
                   ("Tipo 2: puro desperdicio — quítalo", "El tipo dos es puro desperdicio"),
                   ("Nunca llames desperdicio a una persona", "Nunca llames desperdicio a una persona")],
        "example": "Tipo 1: una revisión de seguridad obligatoria. Tipo 2: capturar el mismo número de serie "
                   "en dos sistemas.",
        "example_cue": "Una revisión de seguridad obligatoria",
        "script": "No siempre. Algunos pasos no agregan valor, pero hoy todavía los necesitas. Una revisión "
                  "de seguridad obligatoria es uno. Ese es desperdicio tipo uno. Simplifícalo, o rediseña "
                  "para que ya no se necesite. El tipo dos es puro desperdicio, como capturar el mismo "
                  "número de serie en dos sistemas. Quítalo. Y esta es una regla que debes respetar. Nunca "
                  "llames desperdicio a una persona. El desperdicio vive en el proceso. Tu trabajo es hacer "
                  "el trabajo más fácil y más seguro. ¿Y cómo se ve el desperdicio?",
    },
    {
        "key": "p05", "num": 5, "title": "Los 8 desperdicios: TIMWOODS",
        "points": [("Transporte · Inventario · Movimiento · Espera", "Transporte, inventario"),
                   ("Sobreproducción · Sobreproceso", "Sobreproducción y sobreproceso"),
                   ("Defectos · Habilidades sin usar", "Defectos, y habilidades sin usar"),
                   ("Recorrido de desperdicios: sigue un producto", "Sanjay hizo un recorrido de desperdicios")],
        "example": "El recorrido de Sanjay: 3 esperas de kits en 2 horas, caminatas largas por etiquetas, "
                   "una pared de WIP antes de la prueba.",
        "example_cue": "Tres esperas de kits",
        "script": "Recuerda los ocho desperdicios con una palabra, TIMWOODS. Transporte, inventario, "
                  "movimiento y espera. Sobreproducción y sobreproceso. Defectos, y habilidades sin usar. "
                  "Sanjay hizo un recorrido de desperdicios. Siguió una cámara desde el armado de kits "
                  "hasta el empaque, y anotó lo que vio. Tres esperas de kits en dos horas. Caminatas "
                  "largas por etiquetas. Y una pared de WIP frente a la prueba. ¿Cuál de esos ocho "
                  "encontrarías primero en tu línea?",
    },
    {
        "key": "p06", "num": 6, "title": "Mura: disparidad",
        "points": [("Lotes grandes, luego nada", "Llegan lotes grandes"),
                   ("Material a ratos", "El material llega a ratos"),
                   ("Mismo trabajo, métodos distintos", "Dos operadores hacen"),
                   ("Los promedios esconden picos y valles", "El promedio se ve bien")],
        "example": "El tablero por hora de Sanjay: 60, luego 105, luego 70. El promedio se ve bien; la línea "
                   "no.",
        "example_cue": "Mira el tablero por hora de Sanjay",
        "script": "Ahora, el Mura. Es la disparidad en la demanda, la carga de trabajo o el flujo. Llegan "
                  "lotes grandes, y luego nada. El material llega a ratos. Dos operadores hacen el mismo "
                  "trabajo de formas distintas. Mira el tablero por hora de Sanjay. Sesenta, luego ciento "
                  "cinco, luego setenta. El promedio se ve bien. Pero tu línea no vive en promedios. Vive "
                  "en esos picos y valles. Y los picos presionan a alguien. ¿Quién crees que paga?",
    },
    {
        "key": "p07", "num": 7, "title": "Muri: sobrecarga",
        "points": [("Personas: cargas, estiramientos, alarmas, poco entrenamiento", "Para las personas, son cargas pesadas"),
                   ("Máquinas: más allá de su carga nominal, mantenimiento saltado", "Para las máquinas, es correr"),
                   ("Lleva a fatiga, errores, descomposturas", "El Muri lleva a la fatiga")],
        "example": "Una operadora se estira arriba del hombro 120 veces por hora; el probador corre durante "
                   "cada descanso.",
        "example_cue": "Una de las operadoras de Sanjay",
        "script": "Pagan las personas y las máquinas. Eso es el Muri, la sobrecarga. Para las personas, son "
                  "cargas pesadas, estiramientos incómodos, demasiadas alarmas, o muy poco entrenamiento. "
                  "Para las máquinas, es correr más allá de su carga nominal, y saltarse el mantenimiento "
                  "para sacar la producción. Una de las operadoras de Sanjay se estira arriba del hombro "
                  "ciento veinte veces por hora. Y el probador corre sin parar durante cada descanso. El "
                  "Muri lleva a la fatiga, a errores y a descomposturas. ¿Y cómo se combinan las tres?",
    },
    {
        "key": "p08", "num": 8, "title": "Cuando las tres chocan",
        "points": [("4 horas de demanda en una sola liberación", "Cuatro horas de demanda"),
                   ("Estaciones adelantadas — se amontonó el WIP", "Las primeras estaciones se adelantaron"),
                   ("La prueba se volvió el cuello de botella", "La prueba se volvió el cuello de botella"),
                   ("Horas extra, prisas, defectos, retrabajo", "Los supervisores agregaron gente")],
        "example": "Parecía 'poca capacidad de prueba'. En realidad: liberación dispareja (Mura) + prisas "
                   "(Muri) + retrabajo (Muda).",
        "example_cue": "Parecía un problema de capacidad de prueba",
        "script": "Esto es lo que pasó el lunes. Cuatro horas de demanda llegaron en una sola liberación. "
                  "Las primeras estaciones se adelantaron, y el WIP se amontonó. La prueba se volvió el "
                  "cuello de botella. Los supervisores agregaron gente y horas extra. Los operadores se "
                  "apuraron, subieron los defectos, y el retrabajo cargó todavía más la prueba. Parecía un "
                  "problema de capacidad de prueba. Pero puedes ver las tres M en esa historia. ¿Y cómo las "
                  "encuentras en tu propia línea?",
    },
    {
        "key": "p09", "num": 9, "title": "Encontrar las 3M en el Gemba",
        "points": [("Observa antes de cambiar nada", "observa antes de cambiar"),
                   ("Registra tiempos, esperas, caminatas, WIP, retrabajo", "Registra los tiempos de ciclo"),
                   ("Pregunta a los operadores qué es difícil", "Luego pregúntales a los operadores"),
                   ("Revisa los datos antes de elegir una solución", "Luego revisa los datos")],
        "example": "Sanjay marcó cada hallazgo como Muda, Mura o Muri. Una espera de kits de 20 minutos "
                   "recibió dos marcas: desperdicio y disparidad.",
        "example_cue": "Sanjay marcó cada hallazgo",
        "script": "Ve al Gemba, y observa antes de cambiar nada. Elige una familia de productos, y síguela. "
                  "Registra los tiempos de ciclo, las esperas, las caminatas, el WIP y el retrabajo. Luego "
                  "pregúntales a los operadores qué hace el trabajo difícil, disparejo o inseguro. Casi "
                  "siempre lo saben. Sanjay marcó cada hallazgo como Muda, Mura o Muri. Algunos recibieron "
                  "dos marcas. Una espera de kits de veinte minutos es desperdicio y disparidad a la vez. "
                  "Luego revisa los datos antes de elegir una solución.",
    },
    {
        "key": "p10", "num": 10, "title": "Herramientas para quitar el Muda",
        "points": [("5S: menos búsquedas y caminatas", "Las 5S reducen"),
                   ("Trabajo estándar: el mejor método y el más seguro", "El trabajo estándar fija"),
                   ("Poka Yoke: detener errores en el origen", "El Poka Yoke detiene errores"),
                   ("SMED y TPM: cambios de modelo, confiabilidad", "El SMED reduce"),
                   ("Análisis de causa raíz: sin defectos repetidos", "El análisis de causa raíz detiene"),
                   ("No automatices un desperdicio", "No automatices un desperdicio")],
        "example": "Etiquetas y tornillos en racks en cada estación: la caminata bajó de 40 m a 8 m.",
        "example_cue": "Sanjay movió las etiquetas",
        "script": "Empecemos a quitar desperdicio. Las 5S reducen las búsquedas y las caminatas. El trabajo "
                  "estándar fija el mejor método y el más seguro. El Poka Yoke detiene errores en el "
                  "origen. El SMED reduce el tiempo de cambio de modelo, y el TPM mantiene confiables las "
                  "máquinas. El análisis de causa raíz detiene los defectos repetidos. Sanjay movió las "
                  "etiquetas y los tornillos a racks en cada estación. La caminata bajó de cuarenta metros "
                  "a ocho. Una advertencia, eso sí. No automatices un desperdicio. Solo lo harás más "
                  "rápido.",
    },
    {
        "key": "p11", "num": 11, "title": "Herramientas para nivelar el Mura",
        "points": [("Heijunka: nivela el volumen y la mezcla", "El Heijunka nivela"),
                   ("El TAKT une tu ritmo a la demanda", "El tiempo TAKT une"),
                   ("Libera cada pitch, no en oleadas", "libera trabajo cada pitch"),
                   ("Jalar y carriles de primero en entrar, primero en salir", "Las señales de jalar")],
        "example": "TAKT = 27,000 s ÷ 450 cámaras = una cámara cada 60 segundos.",
        "example_cue": "El turno de Sanjay tiene",
        "script": "Luego, suaviza el flujo. El Heijunka nivela el volumen y la mezcla. El tiempo TAKT une "
                  "tu ritmo a la demanda del cliente. El turno de Sanjay tiene veintisiete mil segundos de "
                  "tiempo de trabajo. El cliente necesita cuatrocientas cincuenta cámaras. Es una cámara "
                  "cada sesenta segundos. Así que ahora libera trabajo cada pitch, no en oleadas. Las "
                  "señales de jalar y los carriles de primero en entrar, primero en salir lo mantienen "
                  "estable. El TAKT es un ritmo, no un látigo. ¿Y cómo proteges a tu gente?",
    },
    {
        "key": "p12", "num": 12, "title": "Herramientas para aliviar el Muri",
        "points": [("Balancea cada estación al TAKT", "Balancea cada estación"),
                   ("Estiramientos y cargas en zona segura", "Mantén los estiramientos"),
                   ("Fixtures donde las manos sostienen piezas", "Agrega fixtures"),
                   ("Respeta los límites de la máquina y el mantenimiento", "Respeta los límites de la máquina")],
        "example": "Ahora un fixture sostiene la cámara al atornillar; el contenedor alto bajó al alcance "
                   "fácil.",
        "example_cue": "Sanjay agregó un fixture",
        "script": "Diseña el trabajo para que se ajuste a las personas y a las máquinas. Balancea cada "
                  "estación al TAKT, con tiempos de ciclo reales. Mantén los estiramientos y las cargas en "
                  "una zona segura. Agrega fixtures y plantillas donde las manos sostienen piezas. Respeta "
                  "los límites de la máquina, y nunca te saltes el mantenimiento para proteger la "
                  "producción. Sanjay agregó un fixture que sostiene la cámara al atornillar. El contenedor "
                  "alto bajó al alcance fácil. Nunca planees para un cien por ciento de utilización. ¿Y "
                  "cómo juntas todo?",
    },
    {
        "key": "p13", "num": 13, "title": "Un método 3M de 8 pasos",
        "points": [("Define, luego observa en el Gemba", "Define el problema"),
                   ("Clasifica en las tres M", "Clasifica lo que ves"),
                   ("Mide una base, encuentra causas raíz", "Mide una base"),
                   ("Prueba cambios pequeños con PDCA", "Prueba cambios pequeños"),
                   ("Estandariza, sigue auditando", "Cuando un cambio funciona")],
        "example": "La base de Sanjay: producción por hora muy dispareja, 2.5 horas extra al día.",
        "example_cue": "La base de Sanjay era clara",
        "script": "Usa un método simple de ocho pasos. Define el problema, luego observa en el Gemba. "
                  "Clasifica lo que ves en las tres M. Mide una base, luego encuentra las causas raíz. "
                  "Prueba cambios pequeños con planear, hacer, verificar y actuar. Cuando un cambio "
                  "funciona, hazlo el nuevo estándar, y sigue auditándolo. La base de Sanjay era clara. La "
                  "producción por hora subía y bajaba mucho, y las horas extra eran dos y media al día. "
                  "Ahora, veamos sus resultados.",
    },
    {
        "key": "p14", "num": 14, "title": "Caso práctico: línea de CCTV",
        "points": [("Liberaciones pequeñas y constantes + carril de primero en entrar, primero en salir", "Liberaciones pequeñas y constantes"),
                   ("Piezas y etiquetas en el punto de uso", "Piezas y etiquetas"),
                   ("Liberación según la capacidad de prueba", "Trabajo liberado según"),
                   ("Tablero por hora, problemas levantados a tiempo", "Y un tablero por hora")],
        "example": "Después de 6 semanas: casi sin variación por hora, horas extra cerca de cero, "
                   "rendimiento a la primera hasta 98%.",
        "example_cue": "Después de seis semanas",
        "script": "Esto es lo que cambió Sanjay. Liberaciones pequeñas y constantes, con un carril de "
                  "primero en entrar, primero en salir antes de la prueba. Piezas y etiquetas en el punto "
                  "de uso. Trabajo liberado según la capacidad de prueba. Y un tablero por hora, para "
                  "levantar los problemas a tiempo, no a las seis. Después de seis semanas, la variación "
                  "por hora casi desapareció. Las horas extra bajaron cerca de cero. El rendimiento a la "
                  "primera subió a noventa y ocho por ciento. Nota que no le pidió a nadie trabajar más "
                  "rápido. ¿Y cómo compruebas que dura?",
    },
    {
        "key": "p15", "num": 15, "title": "KPI y sostenimiento",
        "points": [("Flujo: tiempo de entrega, WIP", "Para el flujo"),
                   ("Mura: rango de producción por hora", "Para el Mura"),
                   ("Calidad: FPY, retrabajo", "Para la calidad"),
                   ("Muri: horas extra, riesgo ergonómico", "Para el Muri")],
        "example": "¿Más unidades por hora, pero menos calidad y más horas extra? Solo moviste la pérdida.",
        "example_cue": "Si las unidades por hora",
        "script": "Mide las tres M, no solo la producción. Para el flujo, sigue el tiempo de entrega y el "
                  "WIP. Para el Mura, sigue el rango de producción por hora, no solo el promedio. Para la "
                  "calidad, sigue el rendimiento a la primera y el retrabajo. Para el Muri, vigila las "
                  "horas extra y los riesgos ergonómicos. Y nunca persigas un solo número. Si las unidades "
                  "por hora suben, pero la calidad baja y las horas extra crecen, solo moviste la pérdida. "
                  "Sigue revisándolo en el Gemba, cada semana.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Muda", "sub": "Desperdicio: esperar kits", "icon": "trash", "tone": "bad"},
        {"label": "Mura", "sub": "Disparidad: la producción sube y baja", "icon": "wave", "tone": "bad"},
        {"label": "Muri", "sub": "Sobrecarga: todos corren", "icon": "weight", "tone": "bad"}]},
    "p02": {"type": "flow", "items": [
        {"label": "Mura", "sub": "Un lote enorme el lunes", "icon": "wave", "tone": "bad", "with": 1},
        {"label": "Muri", "sub": "Prisas; el probador nunca descansa", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Muda", "sub": "Defectos, retrabajo, horas extra", "icon": "trash", "tone": "bad", "with": "example"}]},
    "p03": {"type": "versus", "items": [
        {"label": "Caminar por etiquetas", "sub": "Sin valor (ni esperar, ni probar dos veces)", "icon": "walk", "with": "example"},
        {"label": "Colocar el lente", "sub": "Agrega valor", "icon": "camera", "with": "example"}]},
    "p04": {"type": "icons", "items": [
        {"label": "Tipo 1: simplificar", "sub": "Una revisión de seguridad obligatoria", "icon": "shield"},
        {"label": "Tipo 2: quitar", "sub": "Un número de serie capturado dos veces", "icon": "cross", "tone": "bad"},
        {"label": "Las personas nunca son desperdicio", "sub": "El desperdicio vive en el proceso", "icon": "person", "tone": "good"}]},
    "p05": {"type": "steps", "items": [
        {"label": "Transporte", "sub": "T", "with": 0}, {"label": "Inventario", "sub": "I", "with": 0},
        {"label": "Movimiento", "sub": "M", "with": 0}, {"label": "Espera", "sub": "W", "with": 0},
        {"label": "Sobreproducción", "sub": "O", "with": 1}, {"label": "Sobreproceso", "sub": "O", "with": 1},
        {"label": "Defectos", "sub": "D", "with": 2}, {"label": "Habilidades sin usar", "sub": "S", "with": 2}]},
    "p06": {"type": "bars", "label": "Promedio", "note": "se ve bien, esconde las variaciones", "unit": "Tablero por hora de Sanjay: cámaras por hora", "items": [
        {"label": "Hora 1", "value": 60, "with": "example"},
        {"label": "Hora 2", "value": 105, "tone": "bad", "with": "example"},
        {"label": "Hora 3", "value": 70, "with": "example"}]},
    "p07": {"type": "icons", "items": [
        {"label": "Personas", "sub": "Cargas, estiramientos, alarmas", "icon": "person", "tone": "bad", "with": 0},
        {"label": "Máquinas", "sub": "Más allá de su carga nominal", "icon": "gear", "tone": "bad", "with": 1}],
        "then": {"type": "stat", "value": 120, "icon": "hand", "label": "estiramientos arriba del hombro",
                 "unit": "cada hora, para una operadora", "with": "example"}},
    "p08": {"type": "flow", "items": [
        {"label": "4 horas de demanda de golpe", "icon": "wave", "tone": "bad"},
        {"label": "El WIP se amontona", "icon": "stack", "tone": "bad"},
        {"label": "La prueba se vuelve el cuello de botella", "icon": "test", "tone": "bad"},
        {"label": "Horas extra, prisas, retrabajo", "icon": "clock", "tone": "bad"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Primero observar", "icon": "search"}, {"label": "Registrarlo", "icon": "clipboard"},
        {"label": "Preguntar a los operadores", "icon": "person"}, {"label": "Revisar los datos", "icon": "chartUp"}]},
    "p10": {"type": "icons", "items": [
        {"label": "5S", "icon": "tray", "with": 0}, {"label": "Trabajo estándar", "icon": "clipboard", "with": 1},
        {"label": "Poka Yoke", "icon": "key", "with": 2}, {"label": "SMED + TPM", "icon": "wrench", "with": 3},
        {"label": "Causa raíz", "icon": "search", "with": 4}],
        "then": {"type": "compare", "before": {"label": "Antes", "value": 40}, "after": {"label": "Después", "value": 8},
                 "suffix": " m", "unit": "caminata por cámara", "note": "80% menos caminata", "with": "example"}},
    "p11": {"type": "icons", "items": [
        {"label": "Heijunka", "sub": "Nivelar volumen y mezcla", "icon": "sequence", "with": 0},
        {"label": "TAKT", "sub": "Ritmo marcado por la demanda", "icon": "clock", "with": 1}],
        "then": {"type": "stat", "value": 60, "suffix": " s", "icon": "camera", "label": "una cámara cada 60 segundos",
                 "unit": "27,000 s de tiempo de trabajo ÷ 450 cámaras", "with": "example"}},
    "p12": {"type": "icons", "items": [
        {"label": "Balancear al TAKT", "icon": "scale"}, {"label": "Zona de alcance segura", "icon": "person"},
        {"label": "Fixtures y plantillas", "icon": "wrench"}, {"label": "Límites de la máquina", "icon": "gear"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Las manos sostienen la cámara", "sub": "Contenedor alto arriba del hombro", "icon": "hand"},
            {"label": "Un fixture la sostiene", "sub": "Contenedor al alcance fácil", "icon": "wrench"}]}},
    "p13": {"type": "steps", "items": [
        {"label": "Definir", "with": 0}, {"label": "Observar", "with": 0}, {"label": "Clasificar 3M", "with": 1},
        {"label": "Medir", "with": 2}, {"label": "Encontrar causas", "with": 2}, {"label": "Probar (PDCA)", "with": 3},
        {"label": "Estandarizar", "with": 4}, {"label": "Auditar", "with": 4}]},
    "p14": {"type": "flow", "items": [
        {"label": "Liberaciones pequeñas y constantes", "icon": "sequence", "tone": "good"},
        {"label": "Piezas en el punto de uso", "icon": "tray", "tone": "good"},
        {"label": "Liberación = capacidad de prueba", "icon": "test", "tone": "good"},
        {"label": "Tablero por hora", "icon": "chartUp", "tone": "good"}],
        "then": {"type": "stat", "value": 98, "suffix": "%", "icon": "check", "label": "rendimiento a la primera después de 6 semanas",
                 "unit": "Horas extra cerca de cero. Nadie trabajó más rápido.", "with": "example"}},
    "p15": {"type": "icons", "items": [
        {"label": "Flujo", "sub": "Tiempo de entrega, WIP", "icon": "clock"},
        {"label": "Mura", "sub": "Rango por hora", "icon": "wave"},
        {"label": "Calidad", "sub": "FPY, retrabajo", "icon": "check"},
        {"label": "Muri", "sub": "Horas extra, ergonomía", "icon": "weight"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "La producción por hora de una línea marca 60, 105, 70, 110. ¿Qué M muestra esto con más "
                    "claridad?",
        "options": ["Muda — desperdicio", "Mura — disparidad", "Muri — sobrecarga"],
        "correct": 1,
        "explanation": "Que la producción suba y baje de hora en hora es Mura: disparidad en la carga y el "
                       "flujo. Si se deja así, casi siempre crea Muri (prisas) y luego Muda (defectos, horas "
                       "extra).",
        "q_script": "Prueba rápida. La producción por hora de una línea sigue subiendo y bajando, entre "
                    "sesenta y ciento diez. ¿Qué M muestra eso con más claridad? Tómate unos segundos.",
        "a_script": "Es Mura, la disparidad. La carga sube y baja de hora en hora. Si se deja así, casi "
                    "siempre crea prisas, y luego desperdicio.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un supervisor cumple el plan diario agregando dos horas extra todos los días. ¿Qué debe "
                    "hacer PRIMERO el equipo?",
        "options": ["Pedirles a los operadores que trabajen más rápido", "Agregar más horas extra para crear un colchón",
                    "Observar el flujo y encontrar el Mura y el Muri detrás del faltante",
                    "Comprar otro probador"],
        "correct": 2,
        "explanation": "Las horas extra esconden el problema. Ve al Gemba y encuentra la disparidad y la "
                       "sobrecarga que causan la pérdida, luego nivela y rebalancea. Acelerar, poner colchones o "
                       "comprar máquinas nuevas solo mueve la pérdida.",
        "q_script": "Una más, y esta es un escenario. Un supervisor cumple el plan todos los días agregando "
                    "dos horas extra. ¿Qué debe hacer primero el equipo? Piénsalo.",
        "a_script": "Primero ve a observar el flujo. Encuentra la disparidad y la sobrecarga detrás del "
                    "faltante, luego nivela y rebalancea. Las horas extra solo esconden el problema.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
