"""root_cause in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh root_cause_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "rc_es"
NAME = "root_cause_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Root Cause Analysis": "rut cos análisis",
    "Skill Training Matrix": "eskil tréinin mátrix",
    "Poka Yoke": "Poka Yoke",
    "Ishikawa": "Ishikawa",
    "Pareto": "Pareto",
    "5W2H": "cinco doble u dos hache",
    "QRQC": "cu erre cu ce",
    "FMEA": "efe eme e a",
    "RCA": "erre ce a",
    "DOE": "de o e",
    "MES": "eme e ese",
    "SOP": "ese o pe",
    "SKU": "ese ka u",
    "AOI": "a o i",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Treinta y seis cámaras fallaron la prueba de enfoque en una mañana. En menos de una "
    "hora, tres personas tenían tres respuestas distintas. El fixture. El lente. El probador. "
    "¿Quién tenía razón? En esta lección aprenderás Root Cause Analysis. Verás cómo pasar de "
    "un síntoma a una causa que puedas comprobar, y detenerla para siempre. Seguiremos a "
    "Lakshmi, ingeniera de calidad en una planta de cámaras, mientras lo averigua."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Define el problema con precisión, y protege primero a tu "
    "cliente. Trata cada causa como una hipótesis hasta que una prueba la compruebe. Y "
    "corrige por qué pasó, y también por qué se escapó. Esta es tu acción para esta semana. "
    "Toma un problema cerrado, y revisa si su causa raíz de verdad se probó alguna vez. "
    "Excelente trabajo al completar esta lección. Ahora aprenderás la Skill Training Matrix."
)

# One story thread: Lakshmi's network-camera plant. Line 3: 36 of 1,200 units fail
# focus after the 10:00 changeover (3.0% vs 0.5% baseline); Line 2 has no failures.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es el RCA",
        "points": [("Síntoma: lo que observas", "El síntoma es"),
                   ("Mecanismo: cómo pasó", "El mecanismo es"),
                   ("Causa raíz: controlable, con evidencia", "La causa raíz es")],
        "example": "Imagen borrosa = el síntoma. Un separador equivocado podría ser la causa — no se "
                   "confirma hasta probarlo.",
        "example_cue": "En la línea de Lakshmi",
        "script": "Esta es la idea central. El Root Cause Analysis es una investigación basada en evidencia "
                  "de por qué algo salió mal. Separa tres cosas. El síntoma es lo que observas. El "
                  "mecanismo es cómo pasó. La causa raíz es una condición que puedes controlar, respaldada "
                  "por evidencia. En la línea de Lakshmi, una imagen borrosa es el síntoma. Un separador "
                  "equivocado podría ser la causa. Pero nada se confirma hasta que se prueba. ¿Dónde encaja "
                  "esto?",
    },
    {
        "key": "p02", "num": 2, "title": "El RCA en el sistema de calidad",
        "points": [("Detecta una desviación", "Primero, detectas"),
                   ("Contén para proteger al cliente", "Luego la contienes"),
                   ("Investiga con datos reales", "Después, investigas"),
                   ("Corrige, luego verifica con el tiempo", "Corriges las causas verificadas")],
        "example": "Una separación exitosa protege al cliente — no prueba que la causa desapareció.",
        "example_cue": "Una separación exitosa protege",
        "script": "El RCA es un eslabón de un ciclo cerrado. Primero, detectas una desviación. Luego la "
                  "contienes, para proteger a tu cliente. Después, investigas con datos reales. Corriges "
                  "las causas verificadas, y verificas el resultado con el tiempo. Va junto al QRQC, el "
                  "FMEA, los planes de control y el Poka Yoke. Y aquí hay un punto clave. Una separación "
                  "exitosa protege al cliente. ¿Pero prueba que la causa desapareció? Para nada.",
    },
    {
        "key": "p03", "num": 3, "title": "Definir: 5W2H e Is / Is Not",
        "points": [("Un problema preciso y medible", "empieza con un problema preciso"),
                   ("El 5W2H reúne los hechos", "Usa el 5W2H"),
                   ("Is / Is Not: dónde ocurre, y dónde no", "llamada Es, No es")],
        "example": "Línea 3: 36 de 1,200 cámaras fallaron el enfoque después del cambio de las 10:00. Línea "
                   "2, otro fixture: ninguna.",
        "example_cue": "El planteamiento de Lakshmi era claro",
        "script": "Todo buen RCA empieza con un problema preciso y medible. Usa el 5W2H para reunir los "
                  "hechos. Luego agrega una comparación poderosa, llamada Es, No es. ¿Dónde ocurre el "
                  "problema, y dónde no? El planteamiento de Lakshmi era claro. En la Línea tres, treinta y "
                  "seis de mil doscientas cámaras fallaron el enfoque. Empezó después del cambio de las "
                  "diez. La Línea dos, con otro fixture, no tuvo ninguna. ¿Qué te dice esa comparación?",
    },
    {
        "key": "p04", "num": 4, "title": "Evidencia y trazabilidad",
        "points": [("Reúne evidencia antes de cambiar ajustes", "reúne la evidencia"),
                   ("Guarda muestras con falla y buenas conocidas", "Guarda las piezas con falla"),
                   ("Saca los registros del MES, los de prueba, las alarmas", "Saca los registros del MES"),
                   ("Registra cada cambio reciente", "Registra cada cambio reciente"),
                   ("Revisa la calibración de los calibradores", "Y confirma que tus calibradores")],
        "example": "Lakshmi embolsó diez cámaras con falla y diez buenas antes de que alguien tocara el "
                   "fixture.",
        "example_cue": "Lakshmi embolsó diez",
        "script": "Apunta al cambio de modelo. Pero primero, reúne la evidencia, antes de que alguien "
                  "cambie un ajuste. Guarda las piezas con falla y muestras buenas conocidas. Saca los "
                  "registros del MES, los registros de prueba y las alarmas de las máquinas. Registra cada "
                  "cambio reciente, en herramental, firmware, receta y lote de material. Y confirma que tus "
                  "calibradores están calibrados antes de confiar en diferencias pequeñas. Lakshmi embolsó "
                  "diez cámaras con falla y diez buenas. ¿Otro ingeniero podría repetir tus hallazgos con "
                  "tu evidencia?",
    },
    {
        "key": "p05", "num": 5, "title": "Pareto: elige tu batalla",
        "points": [("Ordena por cantidad, costo o riesgo", "Ordena tus tipos de defecto"),
                   ("Ordena y suma el % acumulado", "Ordénalos"),
                   ("Separa el primero por turno, estación, proveedor", "Luego separa el primero"),
                   ("Los riesgos graves se saltan la fila", "Un riesgo grave de seguridad")],
        "example": "PCB equivocado 40 · tornillo faltante 25 · enfoque 20 · etiqueta 10 · otros 5 → los tres "
                   "primeros = 85%.",
        "example_cue": "En la línea de Lakshmi, tres",
        "script": "Cuando enfrentas muchos problemas, el Pareto te ayuda a elegir. Ordena tus tipos de "
                  "defecto por cantidad, costo o riesgo. Ordénalos, y suma el porcentaje acumulado. Muchas "
                  "veces unas pocas causas hacen la mayor parte de la pérdida. En la línea de Lakshmi, tres "
                  "tipos de defecto sumaban el ochenta y cinco por ciento. Luego separa el primero por "
                  "turno, estación o proveedor. Pero una advertencia. Un riesgo grave de seguridad o para "
                  "el cliente se salta la fila, sin importar su lugar. ¿Y cómo profundizas?",
    },
    {
        "key": "p06", "num": 6, "title": "5 Why: prueba la cadena",
        "points": [("Cinco no es una regla", "Cinco no es una regla"),
                   ("Evidencia para cada eslabón", "Cada eslabón necesita evidencia"),
                   ("Ramifica cuando hay más de una causa", "Ramifica cuando"),
                   ("Nunca te detengas en 'error del operador'", "nunca te detengas en error del operador")],
        "example": "Tornillo faltante → el ciclo terminó sin confirmarlo → la señal de torque no estaba "
                   "ligada al MES.",
        "example_cue": "Toma un tornillo faltante",
        "script": "Usa los cinco porqués, pero trátalos como una cadena de afirmaciones que hay que "
                  "revisar. Cinco no es una regla. Cada eslabón necesita evidencia. Ramifica cuando hay más "
                  "de una causa. Y nunca te detengas en error del operador, o falta de entrenamiento. "
                  "Pregunta qué en el diseño del trabajo lo permitió. Toma un tornillo faltante. La "
                  "estación dejó terminar el ciclo sin confirmar el tornillo. ¿Por qué? La señal de torque "
                  "no estaba ligada al MES. Una historia creíble no es una prueba. ¿Ya revisaste los "
                  "registros?",
    },
    {
        "key": "p07", "num": 7, "title": "Espina de pescado y las 6M",
        "points": [("Espina de pescado = diagrama de Ishikawa", "La espina de pescado, o diagrama de Ishikawa"),
                   ("Personas · máquina · método", "Personas, máquina, método"),
                   ("Material · medición · medio ambiente", "material, medición y medio ambiente"),
                   ("No prueba qué causa es la verdadera", "Una espina de pescado no prueba")],
        "example": "La espina de Lakshmi: desgaste del fixture, receta equivocada, tolerancia del lente, "
                   "repetibilidad del probador, manejo, calor.",
        "example_cue": "El equipo de Lakshmi la llenó",
        "script": "La espina de pescado, o diagrama de Ishikawa, organiza tus ideas. Tiene seis ramas. "
                  "Personas, máquina, método, material, medición y medio ambiente. El equipo de Lakshmi la "
                  "llenó. Desgaste del fixture, una receta equivocada, la tolerancia del lente, la "
                  "repetibilidad del probador, el manejo, y el calor. Es una gran lista de sospechosos. "
                  "Pero esto es lo clave. Una espina de pescado no prueba qué causa es la verdadera. Para "
                  "cada rama, escribes la prueba que la confirmaría o la descartaría. ¿Qué cambió?",
    },
    {
        "key": "p08", "num": 8, "title": "Análisis de cambios y árboles de falla",
        "points": [("Análisis de cambios: lo que falla contra lo último estable", "Eso es el análisis de cambios"),
                   ("Árbol de falla: trabaja hacia atrás con AND / OR", "usa un árbol de falla"),
                   ("Juntos ≠ causa", "Que dos cosas")],
        "example": "Sin imagen se escapa solo si el firmware está mal AND falta el interbloqueo.",
        "example_cue": "Una grabadora de video se escapa",
        "script": "Eso es el análisis de cambios. Comparas la condición que falla con la última estable, y "
                  "enlistas cada cambio entre las dos. Para problemas complejos, usa un árbol de falla. "
                  "Trabaja hacia atrás desde la falla, con lógica de y, o. Una grabadora de video se escapa "
                  "sin imagen solo si el firmware está mal, y falta el interbloqueo. Pero cuidado. Que dos "
                  "cosas pasaran juntas no significa que una causó la otra. ¿Y cómo lo compruebas?",
    },
    {
        "key": "p09", "num": 9, "title": "Prueba tu hipótesis",
        "points": [("Escribe una predicción", "Escribe una predicción"),
                   ("Un factor a la vez, o un DOE", "Cambia un factor"),
                   ("Suficientes muestras, repetido", "Usa suficientes muestras"),
                   ("Revisa primero el calibrador", "revisó primero el calibrador")],
        "example": "Separadores aprobados contra sospechosos, con la misma cámara, receta y sala.",
        "example_cue": "Lakshmi comparó separadores aprobados",
        "script": "Escribe una predicción. Si el separador está mal, las fallas de enfoque deben subir. "
                  "Luego pruébala. Cambia un factor a la vez, o usa un experimento planeado, llamado DOE, "
                  "cuando los factores interactúan. Usa suficientes muestras, y repite la prueba. Lakshmi "
                  "comparó separadores aprobados y sospechosos, con la misma cámara, receta y sala. Y "
                  "revisó primero el calibrador. Si tu medición varía mucho, hasta una diferencia real se "
                  "puede esconder. ¿Listo para la solución?",
    },
    {
        "key": "p10", "num": 10, "title": "Contener contra corregir contra prevenir",
        "points": [("Contener: proteger al cliente ahora", "La contención protege"),
                   ("Corregir: eliminar la causa verificada", "La acción correctiva elimina"),
                   ("Prevenir: extenderlo a líneas parecidas", "Y la acción preventiva"),
                   ("Corrige también la causa de la fuga", "Corrige también la causa de la fuga")],
        "example": "Tarjeta equivocada: escanea el inventario retenido → agrega una comparación en el MES → "
                   "cópiala a otras variantes.",
        "example_cue": "Para una tarjeta equivocada",
        "script": "Mantén separadas tres acciones. La contención protege a tu cliente ahora. La acción "
                  "correctiva elimina la causa verificada. Y la acción preventiva extiende la lección a "
                  "líneas parecidas. Corrige también la causa de la fuga, con un interbloqueo o una "
                  "revisión de presencia. Para una tarjeta equivocada, escaneas el inventario retenido. "
                  "Luego agregas una comparación en el MES, y la copias a otras variantes. Una regla. Nunca "
                  "liberes inventario retenido solo porque ya se pidió la solución. ¿Cómo haces que dure?",
    },
    {
        "key": "p11", "num": 11, "title": "Ligar con el FMEA y el Poka Yoke",
        "points": [("Liga cada causa a un modo de falla", "Liga cada causa confirmada"),
                   ("Actualiza el plan de control", "Actualiza el plan de control"),
                   ("Valida el Poka Yoke: bueno, malo, en el límite", "Valida cualquier Poka Yoke"),
                   ("Actualiza el SOP, el entrenamiento, las auditorías", "Luego actualiza el SOP")],
        "example": "Pregunta: ¿el nuevo control previene el error, lo detecta, o solo lo hace visible?",
        "example_cue": "El nuevo control previene",
        "script": "Regresa al sistema lo que aprendiste. Liga cada causa confirmada a un modo de falla en "
                  "tu FMEA, y vuelve a evaluar el riesgo. Actualiza el plan de control, con el método, la "
                  "reacción y el responsable. Valida cualquier Poka Yoke con piezas buenas conocidas, malas "
                  "conocidas y en el límite. Luego actualiza el SOP, el entrenamiento y las preguntas de "
                  "auditoría. Hazte una pregunta. ¿El nuevo control previene el error, lo detecta, o solo "
                  "lo hace visible?",
    },
    {
        "key": "p12", "num": 12, "title": "Métricas del RCA",
        "points": [("No cuentes formatos cerrados como éxito", "No declares el éxito"),
                   ("Tasa de defectos ≠ rendimiento a la primera", "Sigue la tasa de defectos"),
                   ("Sigue las repeticiones después del cierre", "Sigue qué tan seguido"),
                   ("Costo y recuperación", "Cuánto cuesta")],
        "example": "60 → 12 defectos por cada 20,000: una reducción de 80%. Un control de ₹90,000 que ahorra "
                   "₹15,000/mes = recuperación en 6 meses.",
        "example_cue": "Un control que reduce los defectos",
        "script": "Mide la calidad de tus investigaciones, y también su impacto en el negocio. No declares "
                  "el éxito solo porque se cerró un formato. Sigue la tasa de defectos, y el rendimiento a "
                  "la primera, pero nunca los confundas. Sigue qué tan seguido regresan los problemas "
                  "después del cierre. Un control que reduce los defectos un ochenta por ciento suena muy "
                  "bien. ¿Cuánto cuesta, y qué tan rápido se paga? El de Lakshmi se pagó en seis meses. "
                  "Ahora, su caso completo.",
    },
    {
        "key": "p13", "num": 13, "title": "Caso práctico: falla de enfoque",
        "points": [("Retuvo cada cámara desde la última primera pieza buena", "Lakshmi retuvo cada cámara"),
                   ("Cuatro sospechosos: separador, receta, asentado, probador", "Su equipo enlistó cuatro"),
                   ("Midieron, compararon registros, prueba cruzada", "Midieron los separadores"),
                   ("Separador con guía + escaneo del fixture ligado a la receta", "La solución fue un separador con guía")],
        "example": "Cambiar los separadores movió las fallas. Cambiar los probadores no. Esa fue la prueba.",
        "example_cue": "Cambiar los separadores movió",
        "script": "Lakshmi retuvo cada cámara desde la última primera pieza validada. Su equipo enlistó "
                  "cuatro sospechosos. El grosor del separador, una receta que no coincidía, el asentado "
                  "del lente, y la deriva del probador. Midieron los separadores, compararon los registros, "
                  "e hicieron una prueba cruzada. Cambiar los separadores movió las fallas. Cambiar los "
                  "probadores no. Ahora tenían la prueba. La solución fue un separador con guía, y un "
                  "escaneo del fixture ligado a la receta. ¿Qué evidencia habrías necesitado tú?",
    },
    {
        "key": "p14", "num": 14, "title": "Dos casos más: SMT y etiqueta",
        "points": [("Línea de tarjetas: componente equivocado colocado", "En la línea de tarjetas"),
                   ("Solución: interbloqueo del alimentador contra el BOM", "La solución fue un interbloqueo"),
                   ("Empaque: etiqueta de la caja ≠ equipo", "En empaque"),
                   ("Solución: la caja no cierra hasta que todo coincida", "Esa solución impidió")],
        "example": "Las dos soluciones se pusieron a prueba antes del cierre.",
        "example_cue": "Las dos soluciones se pusieron a prueba",
        "script": "Dos casos más cortos muestran el mismo patrón. En la línea de tarjetas, se colocó un "
                  "componente equivocado. El equipo comparó la lista de materiales, el ajuste del "
                  "alimentador, el código de barras del carrete y las imágenes del AOI. La solución fue un "
                  "interbloqueo del alimentador contra la lista. En empaque, una etiqueta de la caja no "
                  "coincidía con el equipo. Esa solución impidió que la caja cerrara hasta que el número de "
                  "serie, el SKU y la etiqueta coincidieran. Las dos soluciones se pusieron a prueba. "
                  "¿Podrías comprobar que se encontró cada unidad sospechosa?",
    },
    {
        "key": "p15", "num": 15, "title": "Implementación en 90 días",
        "points": [("Días 1–30: disparadores, puestos, formatos, pilotos", "En los primeros treinta días"),
                   ("Días 31–60: entrenar, investigar", "En los siguientes treinta"),
                   ("Días 61–90: auditar, actualizar el FMEA, extender", "En los últimos treinta"),
                   ("Cierre: cuadrado, verificado, probado", "Antes de cerrar cualquier problema")],
        "example": "Haz del RCA una rutina, no un taller de una vez.",
        "example_cue": "Haz del RCA una rutina",
        "script": "Haz del RCA una rutina, no un taller de una vez. En los primeros treinta días, define "
                  "tus disparadores, puestos, formatos y áreas piloto. En los siguientes treinta, entrena a "
                  "los equipos, y haz investigaciones reales. En los últimos treinta, audita los "
                  "resultados, actualiza tu FMEA y tus planes de control, y extiéndelo. Antes de cerrar "
                  "cualquier problema, revísalo. ¿La contención está cuadrada? ¿Las causas están "
                  "verificadas, y las acciones probadas? Comprueba la causa, y luego prevénla.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Síntoma", "sub": "Una imagen borrosa", "icon": "camera", "tone": "bad"},
        {"label": "Mecanismo", "sub": "Cómo pasó", "icon": "gear"},
        {"label": "Causa raíz", "sub": "¿Un separador equivocado? Pruébalo primero", "icon": "search"}]},
    "p02": {"type": "flow", "items": [
        {"label": "Detectar", "icon": "sensor"}, {"label": "Contener", "icon": "lock"},
        {"label": "Investigar con datos", "icon": "search"},
        {"label": "Corregir, verificar con el tiempo", "icon": "check", "tone": "good"}]},
    "p03": {"type": "compare", "before": {"label": "Línea 3", "value": 36}, "after": {"label": "Línea 2", "value": 0},
            "unit": "fallas de enfoque después del cambio (la Línea 2 tiene otro fixture)",
            "note": "Is / Is Not apunta al fixture", "with": "example"},
    "p04": {"type": "icons", "items": [
        {"label": "Primero la evidencia", "icon": "search"}, {"label": "Muestras con falla + buenas", "icon": "box"},
        {"label": "Registros y alarmas", "icon": "clipboard"}, {"label": "Cambios recientes", "icon": "sequence"},
        {"label": "Calibración", "icon": "scale"}]},
    "p05": {"type": "bars", "label": "", "note": "Los tres primeros = 85% de los defectos", "items": [
        {"label": "PCB equivocado", "value": 40, "tone": "bad", "with": "example"},
        {"label": "Tornillo faltante", "value": 25, "tone": "bad", "with": "example"},
        {"label": "Enfoque", "value": 20, "tone": "bad", "with": "example"},
        {"label": "Etiqueta", "value": 10, "with": "example"},
        {"label": "Otros", "value": 5, "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Cinco no es una regla", "icon": "count"}, {"label": "Evidencia por eslabón", "icon": "search"},
        {"label": "Ramifica cuando haga falta", "icon": "sequence"}, {"label": "Nunca 'error del operador'", "icon": "cross", "tone": "bad"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Un tornillo faltante", "icon": "screw", "tone": "bad", "with": "example"},
            {"label": "¿Por qué? El ciclo terminó de todos modos", "icon": "sequence", "with": "example"},
            {"label": "¿Por qué? El torque no estaba ligado al MES", "icon": "chip", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Personas", "sub": "Manejo", "icon": "person", "with": 1},
        {"label": "Máquina", "sub": "Desgaste del fixture", "icon": "gear", "with": 1},
        {"label": "Método", "sub": "Receta equivocada", "icon": "clipboard", "with": 1},
        {"label": "Material", "sub": "Tolerancia del lente", "icon": "box", "with": 2},
        {"label": "Medición", "sub": "Repetibilidad del probador", "icon": "scale", "with": 2},
        {"label": "Medio ambiente", "sub": "Calor", "icon": "wave", "with": 2}]},
    "p08": {"type": "icons", "items": [
        {"label": "Análisis de cambios", "sub": "Lo que falla contra lo último estable", "icon": "sequence", "with": 0},
        {"label": "Árbol de falla", "sub": "AND / OR, hacia atrás", "icon": "gear", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "El firmware está mal", "icon": "chip", "tone": "bad", "with": "example"},
            {"label": "AND falta el interbloqueo", "icon": "lock", "tone": "bad", "with": "example"},
            {"label": "Se escapa una unidad sin imagen", "icon": "box", "tone": "bad", "with": "example"}]}},
    "p09": {"type": "icons", "items": [
        {"label": "Escribe una predicción", "icon": "clipboard"}, {"label": "Un factor, o un DOE", "icon": "gear"},
        {"label": "Suficientes muestras", "icon": "stack"}, {"label": "Revisa el calibrador", "icon": "scale"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Separador sospechoso", "sub": "Misma cámara, receta, sala", "icon": "shape"},
            {"label": "Separador aprobado", "sub": "Misma cámara, receta, sala", "icon": "shape"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "Contener", "sub": "Escanea el inventario retenido", "icon": "lock"},
        {"label": "Corregir", "sub": "Agrega una comparación en el MES", "icon": "barcode"},
        {"label": "Prevenir", "sub": "Cópiala a otras variantes", "icon": "sequence", "tone": "good"}]},
    "p11": {"type": "icons", "items": [
        {"label": "FMEA", "icon": "clipboard"}, {"label": "Plan de control", "icon": "shield"},
        {"label": "Valida el Poka Yoke", "icon": "test"}, {"label": "SOP, entrenamiento, auditorías", "icon": "person"}],
        "then": {"type": "ladder", "top": "LO MEJOR", "bottom": "LO MÁS DÉBIL", "with": "example", "items": [
            {"label": "Previene el error", "icon": "key", "with": "example"},
            {"label": "Lo detecta", "icon": "sensor", "with": "example"},
            {"label": "Solo lo hace visible", "icon": "search", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Formato cerrado ≠ éxito", "icon": "cross", "tone": "bad"},
        {"label": "Tasa de defectos contra FPY", "icon": "chartUp"},
        {"label": "Repeticiones después del cierre", "icon": "sequence"}, {"label": "Costo y recuperación", "icon": "calendar"}],
        "then": {"type": "compare", "before": {"label": "Antes", "value": 60}, "after": {"label": "Después", "value": 12},
                 "unit": "defectos por cada 20,000 cámaras", "note": "80% menos, recuperación en 6 meses", "with": "example"}},
    "p13": {"type": "flow", "items": [
        {"label": "Retener desde la última primera pieza buena", "icon": "lock"},
        {"label": "Cuatro sospechosos enlistados", "icon": "search"},
        {"label": "Prueba cruzada", "sub": "Los separadores la movieron; los probadores no", "icon": "test"},
        {"label": "Separador con guía + escaneo del fixture", "icon": "key", "tone": "good"}]},
    "p14": {"type": "icons", "items": [
        {"label": "Componente equivocado", "sub": "Línea de tarjetas", "icon": "chip", "tone": "bad"},
        {"label": "Interbloqueo del alimentador", "sub": "Revisado contra el BOM", "icon": "lock", "tone": "good"},
        {"label": "Etiqueta ≠ equipo", "sub": "Empaque", "icon": "label", "tone": "bad"},
        {"label": "La caja no cierra", "sub": "Hasta que coincidan los tres", "icon": "box", "tone": "good"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Disparadores, puestos, formatos, pilotos", "sub": "Días 1–30", "icon": "clipboard", "with": 0},
        {"label": "Entrenar, hacer investigaciones reales", "sub": "31–60", "icon": "person", "with": 1},
        {"label": "Auditar, actualizar el FMEA, extender", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "La espina de pescado de un equipo enlista seis posibles causas. ¿Qué prueba?",
        "options": ["La rama más grande es la causa raíz", "Nada todavía — cada causa debe probarse",
                    "Las seis causas son ciertas"],
        "correct": 1,
        "explanation": "Una espina de pescado organiza hipótesis. No prueba nada hasta que cada candidata se "
                       "confirma o se descarta con una prueba.",
        "q_script": "Prueba rápida. La espina de pescado de un equipo enlista seis posibles causas. ¿Qué "
                    "prueba? Tómate unos segundos.",
        "a_script": "Nada todavía. Una espina de pescado es una lista de hipótesis. Cada una debe probarse "
                    "antes de llamarla causa.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Se encuentra un defecto de PCB equivocado. El nuevo interbloqueo del MES ya se pidió "
                    "pero no está instalado. ¿Se puede liberar el WIP retenido?",
        "options": ["Sí — la solución ya viene", "No — liberarlo solo después de revisarlo y con una decisión autorizada",
                    "Sí, si se vuelve a entrenar al operador", "Sí, si se avisa al siguiente turno"],
        "correct": 1,
        "explanation": "Pedir una solución no protege al cliente. El inventario retenido se libera solo después "
                       "de revisarse y decidirse por el proceso de Calidad.",
        "q_script": "Una más, y esta es un escenario. Se encuentra un defecto de tarjeta equivocada. El nuevo "
                    "interbloqueo ya se pidió, pero no está instalado. ¿Se puede liberar el inventario "
                    "retenido? Piénsalo.",
        "a_script": "No. Libéralo solo después de revisarlo, y con una decisión autorizada. Pedir una "
                    "solución no protege a tu cliente.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
