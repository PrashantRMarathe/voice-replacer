"""skill_matrix in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh skill_matrix_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "sk_es"
NAME = "skill_matrix_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Skill Training Matrix": "eskil tréinin mátrix",
    "One Point Lesson": "uán póint léson",
    "Dojo": "Doyo",
    "TAKT": "takt",
    "SOP": "ese o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Lunes en la mañana. Bala se reporta enfermo. Es la única persona que sabe ajustar el "
    "enfoque del lente. Para las diez, toda la celda de cámaras está parada. ¿Te suena "
    "familiar? En esta lección aprenderás la Skill Training Matrix. Verás quién puede de "
    "verdad hacer cada trabajo, dónde están las brechas, y cómo cerrarlas. Seguiremos a "
    "Vikram, líder de celda, mientras arma una para su equipo."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Una matriz de habilidades muestra la capacidad demostrada, "
    "no la asistencia. Cuenta los respaldos calificados para cada trabajo crítico, en cada "
    "turno. Y mantenla viva, con evidencia detrás de cada calificación. Esta es tu acción "
    "para esta semana. Enlista tus tres estaciones más críticas, y cuenta las personas "
    "calificadas para cada una. Excelente trabajo al completar esta lección. Ahora aprenderás "
    "el tiempo TAKT, el pulso de tu línea."
)

# One story thread: Vikram's network-camera cell. Operators Asha, Bala, Chitra,
# Deepa; skills ESD, PCB assembly, lens focus, test, packing; L0-L4, L3 = qualified.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es una matriz de habilidades",
        "points": [("Quién puede hacer qué trabajo, y qué tan bien", "quién puede hacer"),
                   ("El nivel comprobado de cada persona", "Muestra el nivel comprobado"),
                   ("Las brechas", "Y muestra las brechas"),
                   ("No es una lista de asistencia", "No es una lista de asistencia")],
        "example": "La celda de Vikram: ensamble de tarjetas, enfoque del lente, prueba y empaque — con "
                   "respaldos aprobados para cada uno.",
        "example_cue": "La celda de Vikram tiene",
        "script": "Esta es la idea central. Una Skill Training Matrix es un registro visual de quién puede "
                  "hacer qué trabajo, y qué tan bien. Muestra el nivel comprobado de cada persona, en cada "
                  "operación. Y muestra las brechas. No es una lista de asistencia, ni una lista de cursos. "
                  "La celda de Vikram tiene ensamble de tarjetas, enfoque del lente, prueba y empaque. Su "
                  "matriz muestra los respaldos aprobados para cada uno. ¿Por qué importa tanto eso en tu "
                  "línea?",
    },
    {
        "key": "p02", "num": 2, "title": "Por qué importa",
        "points": [("Planear personal, cubrir ausencias, balancear", "Los supervisores la usan"),
                   ("Confirmar la competencia en pasos críticos", "Calidad la usa"),
                   ("Un camino claro para crecer", "Y las personas ven")],
        "example": "Hábil en ajustar alimentadores ≠ autorizado para liberar un programa. Son dos "
                   "habilidades distintas.",
        "example_cue": "Un técnico puede ser hábil",
        "script": "Porque conecta a tu gente con tus resultados. Los supervisores la usan para planear el "
                  "personal, cubrir ausencias, y balancear la línea. Calidad la usa para confirmar quién es "
                  "competente en los pasos críticos. Y las personas ven un camino claro para crecer. Aquí "
                  "hay un punto sutil. Un técnico puede ser hábil en ajustar alimentadores, pero no estar "
                  "autorizado para liberar un programa. Son dos habilidades distintas. ¿Qué tres estaciones "
                  "dolerían más si faltara su único experto?",
    },
    {
        "key": "p03", "num": 3, "title": "Estructura de la matriz",
        "points": [("Filas: personas", "Las personas van en las filas"),
                   ("Columnas: habilidades", "Las habilidades van en las columnas"),
                   ("Cada celda: nivel + última evaluación", "Cada celda muestra"),
                   ("Cada habilidad ligada a su SOP", "Cada habilidad se liga"),
                   ("No juntes tareas en una sola habilidad", "Nunca juntes tareas distintas")],
        "example": "Producción la mantiene al día; los instructores evalúan; Calidad valida las habilidades "
                   "críticas.",
        "example_cue": "Producción mantiene la matriz",
        "script": "El formato es simple. Las personas van en las filas. Las habilidades van en las "
                  "columnas. Cada celda muestra el nivel de la persona, y cuándo se evaluó por última vez. "
                  "Cada habilidad se liga a su SOP, y muestra qué tan crítica es. Producción mantiene la "
                  "matriz al día. Los instructores evalúan, y Calidad valida las habilidades críticas. Y "
                  "aquí va una regla. Nunca juntes tareas distintas en una sola habilidad, solo para que la "
                  "gráfica se vea llena. ¿Y qué significan los niveles?",
    },
    {
        "key": "p04", "num": 4, "title": "Niveles de dominio L0–L4",
        "points": [("L0 sin entrenar", "El nivel cero significa"),
                   ("L1 entiende la seguridad y la secuencia", "El nivel uno significa"),
                   ("L2 trabaja con supervisión", "El nivel dos significa"),
                   ("L3 calificado para trabajar solo", "El nivel tres significa"),
                   ("L4 entrena a otros, resuelve problemas", "El nivel cuatro significa")],
        "example": "Un nivel no es un permiso: la autorización de máquina y de seguridad se registra aparte.",
        "example_cue": "Pero un nivel no es un permiso",
        "script": "Usa una escala de cinco niveles. El nivel cero significa sin entrenar. El nivel uno "
                  "significa que entiendes la seguridad, la secuencia y los riesgos principales. El nivel "
                  "dos significa que puedes hacerlo con supervisión. El nivel tres significa que estás "
                  "calificado para trabajar solo, dentro del tiempo de ciclo y los límites de calidad. El "
                  "nivel cuatro significa que puedes entrenar a otros y resolver problemas. Pero un nivel "
                  "no es un permiso. La autorización de máquina y de seguridad se registra aparte. ¿Qué "
                  "habilidades van primero?",
    },
    {
        "key": "p05", "num": 5, "title": "Encontrar las habilidades críticas",
        "points": [("Mapea cada paso y su SOP", "Enlista cada paso"),
                   ("Marca el impacto en seguridad, calidad, cliente", "Luego marca las habilidades"),
                   ("Califica impacto, dificultad, respaldos", "Califica el impacto"),
                   ("Mínimo de personas calificadas por turno", "fija un mínimo de personas calificadas")],
        "example": "La celda de Vikram: el enfoque del lente y la carga de firmware califican más alto; el "
                   "manejo de cajas, más bajo.",
        "example_cue": "En la celda de Vikram",
        "script": "Empieza con tu mapa del proceso. Enlista cada paso, y el SOP que lo rige. Luego marca "
                  "las habilidades donde un error pega en la seguridad, la calidad o el cliente. Califica "
                  "el impacto, qué tan difícil es aprender la habilidad, y cuántos respaldos tienes. En la "
                  "celda de Vikram, el enfoque del lente y la carga de firmware califican más alto. Un "
                  "ajuste equivocado ahí llega al cliente. El manejo de cajas califica más bajo. Para cada "
                  "habilidad crítica, fija un mínimo de personas calificadas por turno.",
    },
    {
        "key": "p06", "num": 6, "title": "Evaluar la habilidad real",
        "points": [("Breve revisión de teoría", "Revisa la teoría brevemente"),
                   ("Observa ciclos reales + una situación anormal", "Observa varios ciclos reales"),
                   ("Registra fecha, evaluador, resultados", "Registra la fecha")],
        "example": "Una operadora de prueba pasó la teoría pero seguía sin ver escaneos de series con falla "
                   "— se queda en nivel dos.",
        "example_cue": "Una de las operadoras de prueba de Vikram",
        "script": "Ahora, ¿cómo sabes que alguien de verdad está en el nivel tres? Pruebas lo que de verdad "
                  "puede hacer. Revisa la teoría brevemente, y luego observa el trabajo práctico. Observa "
                  "varios ciclos reales, y al menos una situación anormal. Registra la fecha, el evaluador "
                  "y los resultados. Una de las operadoras de prueba de Vikram pasó la teoría fácilmente. "
                  "Pero seguía sin ver escaneos de series con falla. Así que se queda en nivel dos por "
                  "ahora. ¿Cuándo debes volver a evaluar?",
    },
    {
        "key": "p07", "num": 7, "title": "Necesidades de entrenamiento y brechas",
        "points": [("Vuelve a evaluar tras ausencias o cambios", "Vuelve a evaluar después"),
                   ("Necesidad = nivel requerido − nivel comprobado", "Una necesidad es la brecha"),
                   ("Cuenta personas calificadas contra puestos", "Cuenta tus personas calificadas"),
                   ("Encuentra los puntos únicos de falla", "Busca con cuidado los puntos únicos")],
        "example": "El turno de Vikram necesita 4 operadores de firmware calificados y tiene 2: una brecha "
                   "de 2.",
        "example_cue": "El turno de Vikram necesita",
        "script": "Vuelve a evaluar después de una ausencia larga, un cambio de proceso o defectos "
                  "repetidos. Luego calcula tus necesidades de entrenamiento. Una necesidad es la brecha "
                  "entre el nivel que requieres y el nivel comprobado. Cuenta tus personas calificadas "
                  "contra los puestos que debes cubrir. El turno de Vikram necesita cuatro operadores de "
                  "firmware calificados. Tiene dos. Es una brecha de dos. Busca con cuidado los puntos "
                  "únicos de falla, como Bala en el enfoque del lente. ¿Cómo cierras la brecha?",
    },
    {
        "key": "p08", "num": 8, "title": "Métodos de entrenamiento",
        "points": [("Entrenamiento estructurado en el puesto", "entrenamiento estructurado en el puesto"),
                   ("Un evaluador independiente revisa el resultado", "Un evaluador independiente"),
                   ("Dojo: práctica segura fuera de la línea", "Un Dojo es"),
                   ("One Point Lesson para los puntos clave", "Las One Point Lesson refuerzan")],
        "example": "El Dojo de empaque de Vikram usa etiquetas equivocadas y accesorios faltantes a "
                   "propósito.",
        "example_cue": "El Dojo de empaque de Vikram",
        "script": "Entrena a tu gente con entrenamiento estructurado en el puesto. El instructor prepara, "
                  "demuestra a ritmo estándar, y luego quien aprende practica con retroalimentación. Un "
                  "evaluador independiente revisa el resultado. Un Dojo es un área de entrenamiento fuera "
                  "de la línea, donde la gente puede practicar con seguridad. El Dojo de empaque de Vikram "
                  "usa etiquetas equivocadas y accesorios faltantes a propósito. Las One Point Lesson "
                  "refuerzan puntos clave sueltos. Y recuerda enseñar la reacción ante los problemas, no "
                  "solo los pasos normales.",
    },
    {
        "key": "p09", "num": 9, "title": "El plan de entrenamiento de 90 días",
        "points": [("Días 1–30: mapear, definir niveles, evaluar", "En los primeros treinta días"),
                   ("Días 31–60: entrenar las brechas críticas", "En los siguientes treinta"),
                   ("Días 61–90: certificar respaldos, crecer", "En los últimos treinta")],
        "example": "La primera prioridad de Vikram: calificar a un segundo experto en enfoque del lente.",
        "example_cue": "La primera prioridad de Vikram",
        "script": "Todo plan de entrenamiento necesita responsables, fechas y un resultado claro. Esta es "
                  "una versión de noventa días. En los primeros treinta días, mapea las habilidades, define "
                  "los niveles, y evalúa dónde estás. En los siguientes treinta, entrena las brechas "
                  "críticas, y verifica a quienes suben a nivel tres. En los últimos treinta, certifica "
                  "respaldos y crece. La primera prioridad de Vikram era obvia. Calificar a un segundo "
                  "experto en enfoque del lente. ¿Cuál sería la tuya?",
    },
    {
        "key": "p10", "num": 10, "title": "KPI de la matriz",
        "points": [("Cobertura de calificación", "La cobertura de calificación pregunta"),
                   ("Logro de habilidades", "El logro de habilidades sigue"),
                   ("Tasa de entrenamiento cruzado", "La tasa de entrenamiento cruzado cuenta"),
                   ("Calificaciones vencidas", "cuenta las calificaciones vencidas")],
        "example": "18 de 24 puestos críticos cubiertos = 75%. Calcúlalo por turno.",
        "example_cue": "Vikram tiene dieciocho",
        "script": "Mide tu resistencia real, no las horas de entrenamiento. La cobertura de calificación "
                  "pregunta cuántos puestos requeridos tienen una persona calificada. El logro de "
                  "habilidades sigue las mejoras planeadas que ya se verificaron. La tasa de entrenamiento "
                  "cruzado cuenta a las personas calificadas en dos trabajos o más. Y cuenta las "
                  "calificaciones vencidas. Vikram tiene dieciocho de veinticuatro puestos críticos "
                  "cubiertos. Es el setenta y cinco por ciento. Calcúlalo por turno, porque una persona no "
                  "puede cubrir dos estaciones a la vez.",
    },
    {
        "key": "p11", "num": 11, "title": "Ejemplo práctico: la celda de Vikram",
        "points": [("Asha: ensamble de tarjetas L4", "Asha es nivel cuatro"),
                   ("Chitra ahora se une a Bala: enfoque del lente L3", "Chitra ahora se unió"),
                   ("Chitra, Deepa: prueba L3+", "Chitra y Deepa están"),
                   ("Siguiente prioridad: otro respaldo de enfoque", "Entonces, ¿cuál es la siguiente")],
        "example": "Enfoque + prueba a la vez: Bala en enfoque, Deepa en prueba. Chitra no puede hacer las "
                   "dos.",
        "example_cue": "Entonces, ¿quién cubre el enfoque",
        "script": "Esta es la matriz de Vikram después de noventa días. Asha es nivel cuatro en ensamble de "
                  "tarjetas. Chitra ahora se unió a Bala en nivel tres en enfoque del lente. Chitra y Deepa "
                  "están calificadas en prueba. Entonces, ¿quién cubre el enfoque y la prueba al mismo "
                  "tiempo? Bala en enfoque, y Deepa en prueba. Chitra no puede hacer las dos a la vez. Si "
                  "Bala falta, Chitra debe pasar a enfoque. Entonces, ¿cuál es la siguiente prioridad de "
                  "entrenamiento? Otro respaldo en enfoque del lente.",
    },
    {
        "key": "p12", "num": 12, "title": "Ligar con la calidad y la seguridad",
        "points": [("Nivel + autorización + entrenamiento en el SOP", "solo cuando tres cosas"),
                   ("Cada habilidad ligada a la revisión de su SOP", "Liga cada habilidad"),
                   ("Cambio de proceso → volver a evaluar", "Cuando el proceso cambia"),
                   ("El entrenamiento nunca reemplaza el diseño del proceso", "el entrenamiento nunca reemplaza")],
        "example": "El técnico de firmware de Vikram era L3 con la receta vieja — la nueva cambió pasos "
                   "críticos, así que se le volvió a evaluar.",
        "example_cue": "El técnico de firmware de Vikram",
        "script": "Una matriz de habilidades es una protección de la calidad. Alguien debe trabajar solo en "
                  "un paso crítico solo cuando tres cosas están vigentes. Su nivel, su autorización, y su "
                  "entrenamiento en el SOP. Liga cada habilidad a la revisión de su SOP. Cuando el proceso "
                  "cambia, vuelve a evaluar. El técnico de firmware de Vikram era nivel tres con la receta "
                  "vieja. La nueva cambió pasos críticos, así que se le volvió a evaluar. Y recuerda, el "
                  "entrenamiento nunca reemplaza un buen diseño del proceso. ¿Puede ayudar el software?",
    },
    {
        "key": "p13", "num": 13, "title": "Matriz digital y tablero visual",
        "points": [("Códigos únicos para personas y habilidades", "Usa códigos únicos"),
                   ("Rastro de auditoría de cada cambio", "guarda un rastro de auditoría"),
                   ("Recordatorios de calificaciones por vencer", "Pon recordatorios"),
                   ("Nadie aprueba sus propias habilidades críticas", "Nunca dejes que alguien apruebe")],
        "example": "El tablero de Vikram le avisa cuando una autorización está por vencer.",
        "example_cue": "El tablero de Vikram le avisa",
        "script": "Sí, si los datos son confiables. Una matriz digital liga las evaluaciones, las "
                  "revisiones del SOP y los planes de turno. Usa códigos únicos para personas y "
                  "habilidades, y guarda un rastro de auditoría de cada cambio. Pon recordatorios para las "
                  "calificaciones por vencer. Nunca dejes que alguien apruebe su propia habilidad crítica. "
                  "El tablero de Vikram le avisa cuando una autorización está por vencer. Y aquí va una "
                  "pregunta de auditoría. ¿Puedes mostrar la evidencia detrás de cualquier calificación de "
                  "nivel tres?",
    },
    {
        "key": "p14", "num": 14, "title": "Gobierno y revisión",
        "points": [("Diario: personal calificado al arranque", "Cada día"),
                   ("Semanal: brechas, entrenamiento cruzado, pendientes", "Cada semana"),
                   ("Mensual: cobertura, gente que se va", "Cada mes"),
                   ("Trimestral: consistencia de los evaluadores", "Cada trimestre")],
        "example": "La antigüedad y la asistencia no equivalen a calificación.",
        "example_cue": "La antigüedad y la asistencia",
        "script": "Mantén viva la matriz con un ritmo de revisión constante. Cada día, revisa que las "
                  "estaciones críticas tengan personal calificado al arranque. Cada semana, revisa las "
                  "brechas, el entrenamiento cruzado y las evaluaciones pendientes. Cada mes, mira la "
                  "cobertura y el riesgo de que la gente se vaya. Cada trimestre, revisa que los "
                  "evaluadores califiquen de forma consistente. Y actualiza los niveles cuando la capacidad "
                  "de verdad cambia, no según el calendario. La antigüedad y la asistencia no equivalen a "
                  "calificación. ¿Listo para armar la tuya?",
    },
    {
        "key": "p15", "num": 15, "title": "Plantillas y auditoría",
        "points": [("Matriz: habilidad, revisión del SOP, nivel, vencimiento", "La matriz contiene"),
                   ("Formato de evaluación: teoría, ciclos, seguridad", "El formato de evaluación"),
                   ("Un plan de entrenamiento para cada brecha", "Cada brecha recibe"),
                   ("Audita las celdas contra el trabajo real", "Luego audítala")],
        "example": "Otro supervisor debe ver de un vistazo quién está calificado hoy.",
        "example_cue": "Otro supervisor debe ver",
        "script": "Usa una plantilla controlada para tu matriz. La matriz contiene cada persona, habilidad, "
                  "revisión del SOP, nivel, fecha de evaluación y vencimiento. El formato de evaluación "
                  "registra la teoría, los ciclos observados, las revisiones de seguridad y el resultado. "
                  "Cada brecha recibe un plan de entrenamiento. Luego audítala. Elige unas celdas, y revisa "
                  "la evidencia contra el trabajo real en el piso. Otro supervisor debe ver de un vistazo "
                  "quién está calificado hoy. Es un sistema de control vivo, no una decoración.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Quién hace qué trabajo", "icon": "person"}, {"label": "Nivel comprobado", "icon": "check"},
        {"label": "Las brechas", "icon": "warning", "tone": "bad"},
        {"label": "No asistencia", "icon": "cross", "tone": "bad"}]},
    "p02": {"type": "icons", "items": [
        {"label": "Personal, ausencias", "icon": "calendar"},
        {"label": "Competencia en pasos críticos", "icon": "shield"},
        {"label": "Un camino para crecer", "icon": "chartUp", "tone": "good"}]},
    "p03": {"type": "matrix", "cols": ["Lente", "Atornillar", "Prueba", "Empaque"], "note": "Ilustración: cada celda es un nivel comprobado", "items": [
        {"label": "Persona A", "cells": [3, 4, 2, None], "with": 0},
        {"label": "Persona B", "cells": [1, 3, 3, 2], "with": 1},
        {"label": "Persona C", "cells": [None, 2, 4, 3], "with": 2}]},
    "p04": {"type": "steps", "items": [
        {"label": "Sin entrenar", "sub": "L0"}, {"label": "Entiende", "sub": "L1"},
        {"label": "Con supervisión", "sub": "L2"}, {"label": "Trabaja solo", "sub": "L3"},
        {"label": "Entrena a otros", "sub": "L4"}]},
    "p05": {"type": "flow", "items": [
        {"label": "Mapea cada paso + SOP", "icon": "clipboard"},
        {"label": "Marca seguridad, calidad, cliente", "icon": "warning"},
        {"label": "Califica impacto, dificultad, respaldos", "icon": "scale"},
        {"label": "Mínimo calificado por turno", "icon": "person", "tone": "good"}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Enfoque del lente", "sub": "Riesgo más alto", "icon": "camera", "tone": "bad", "with": "example"},
            {"label": "Carga de firmware", "sub": "Riesgo más alto", "icon": "chip", "tone": "bad", "with": "example"},
            {"label": "Manejo de cajas", "sub": "Más bajo", "icon": "box", "with": "example"}]}},
    "p06": {"type": "icons", "items": [
        {"label": "Breve revisión de teoría", "icon": "clipboard", "with": 0},
        {"label": "Ciclos reales + uno anormal", "icon": "search", "with": 1},
        {"label": "Fecha, evaluador, resultado", "icon": "calendar", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Teoría: aprobada", "icon": "clipboard", "tone": "good", "with": "example"},
            {"label": "Trabajo real: no vio escaneos con falla", "icon": "search", "tone": "bad", "with": "example"},
            {"label": "Se queda en nivel 2", "icon": "person", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Volver a evaluar tras cambios", "icon": "sequence", "with": 0},
        {"label": "Necesidad = requerido − comprobado", "icon": "count", "with": 1}],
        "then": {"type": "bars", "label": "", "note": "Una brecha de 2", "unit": "operadores de firmware calificados por turno", "with": "example", "items": [
            {"label": "Necesarios", "value": 4, "with": "example"},
            {"label": "Disponibles", "value": 2, "tone": "bad", "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Entrenamiento en el puesto", "icon": "person"}, {"label": "Evaluador independiente", "icon": "shield"},
        {"label": "Dojo", "sub": "Práctica segura fuera de la línea", "icon": "tray"}, {"label": "One Point Lesson", "icon": "clipboard"}]},
    "p09": {"type": "timeline", "items": [
        {"label": "Mapear habilidades, definir niveles, evaluar", "sub": "Días 1–30", "icon": "clipboard"},
        {"label": "Entrenar las brechas críticas", "sub": "31–60", "icon": "person"},
        {"label": "Certificar respaldos, crecer", "sub": "61–90", "icon": "check"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Cobertura de calificación", "icon": "count"}, {"label": "Logro de habilidades", "icon": "chartUp"},
        {"label": "Tasa de entrenamiento cruzado", "icon": "sequence"}, {"label": "Calificaciones vencidas", "icon": "clock", "tone": "bad"}],
        "then": {"type": "stat", "value": 75, "suffix": "%", "icon": "person", "label": "de los puestos críticos cubiertos",
                 "unit": "18 de 24: calcúlalo por turno", "with": "example"}},
    "p11": {"type": "matrix", "cols": ["Tarjeta", "Enfoque", "Prueba"], "note": "Después de 90 días. Enfoque + prueba a la vez: Bala y Deepa. Siguiente: otro respaldo de "
                                                                                                         "enfoque.", "items": [
        {"label": "Asha", "cells": [4, None, None], "with": 0},
        {"label": "Bala", "cells": [None, 3, None], "with": 1},
        {"label": "Chitra", "cells": [None, 3, 3], "with": 1},
        {"label": "Deepa", "cells": [None, None, 3], "with": 2}]},
    "p12": {"type": "icons", "items": [
        {"label": "Nivel", "icon": "person", "with": 0}, {"label": "Autorización", "icon": "key", "with": 0},
        {"label": "Entrenamiento en el SOP", "icon": "clipboard", "with": 0},
        {"label": "Cambio de proceso: volver a evaluar", "icon": "sequence", "with": 2}]},
    "p13": {"type": "icons", "items": [
        {"label": "Códigos únicos", "icon": "barcode"}, {"label": "Rastro de auditoría", "icon": "sequence"},
        {"label": "Recordatorios de vencimiento", "icon": "clock"}, {"label": "Sin autoaprobación", "icon": "cross", "tone": "bad"}]},
    "p14": {"type": "timeline", "items": [
        {"label": "Personal calificado al arranque", "sub": "Diario", "icon": "person"},
        {"label": "Brechas, entrenamiento cruzado, pendientes", "sub": "Semanal", "icon": "calendar"},
        {"label": "Cobertura, gente que se va", "sub": "Mensual", "icon": "chartUp"},
        {"label": "Consistencia de los evaluadores", "sub": "Trimestral", "icon": "scale"}]},
    "p15": {"type": "doc", "items": [
        {"label": "Matriz de habilidades · Celda 2 · Rev C", "icon": "label", "with": 0},
        {"label": "Habilidad · rev. del SOP · nivel · vencimiento", "icon": "clipboard", "with": 0},
        {"label": "Evaluación: teoría, ciclos, seguridad", "icon": "test", "with": 1},
        {"label": "Un plan de entrenamiento para cada brecha", "icon": "calendar", "with": 2},
        {"label": "Auditada contra el trabajo real", "icon": "search", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Un operador terminó el curso de entrenamiento pero todavía no lo evalúan. ¿Se le puede "
                    "contar como L3?",
        "options": ["Sí — el curso está completo", "No — el L3 necesita un desempeño demostrado y evaluado",
                    "Sí, si lleva mucho tiempo ahí"],
        "correct": 1,
        "explanation": "La asistencia y la antigüedad no son competencia. El nivel 3 significa un desempeño "
                       "independiente comprobado con una evaluación con evidencia.",
        "q_script": "Prueba rápida. Un operador terminó el curso de entrenamiento, pero todavía no lo "
                    "evalúan. ¿Se le puede contar como nivel tres? Tómate unos segundos.",
        "a_script": "No. El nivel tres necesita un desempeño evaluado y comprobado. Asistir a un curso no es "
                    "lo mismo que estar calificado.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Solo una persona del turno está calificada en enfoque del lente, y la producción depende "
                    "de eso. ¿Qué debe hacer PRIMERO el líder de celda?",
        "options": ["Entrenar a todos en todas las habilidades", "Calificar un respaldo en enfoque del lente como la prioridad principal",
                    "Pedirle al experto que nunca falte", "Entrenar primero las habilidades de bajo riesgo porque son más rápidas"],
        "correct": 1,
        "explanation": "Depender de una sola persona en una habilidad crítica es el riesgo más grande. Da "
                       "prioridad a calificar un respaldo ahí, y luego amplía el entrenamiento cruzado.",
        "q_script": "Una más, y esta es un escenario. Solo una persona del turno está calificada en enfoque "
                    "del lente, y toda la celda depende de eso. ¿Qué debe hacer primero el líder de celda? "
                    "Piénsalo.",
        "a_script": "Califica primero un respaldo en enfoque del lente. Un punto único de falla en una "
                    "habilidad crítica es el riesgo más grande. Luego amplía el entrenamiento cruzado.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
