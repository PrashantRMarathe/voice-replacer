"""design_thinking in Spanish, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft Spanish neural female voice (es-MX-DaliaNeural).

  bash tools/build_hindi.sh design_thinking_es --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "dt_es"
NAME = "design_thinking_es"
LANG = "es"
VOICE = "es-MX-DaliaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> Spanish script for the voice. Longest first.
SPOKEN = {
    "Elimination of Waste": "eliminéishon of uéist",
    "Design Thinking": "disáin tínkin",
    "Poka Yoke": "Poka Yoke",
    "SCAMPER": "escámper",
    "Kaizen": "Káizen",
    "Gemba": "Guemba",
    "TAKT": "takt",
    "A3": "a tres",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "La línea de empaque seguía sin cumplir su meta. Las etiquetas equivocadas se seguían "
    "colando. La primera idea fue una impresora más rápida, por mucho dinero. Nadie les había "
    "preguntado a los empacadores. ¿Te suena familiar? En esta lección aprenderás Design "
    "Thinking. Verás cómo entender a las personas que hacen el trabajo, resolver el problema "
    "correcto, y probar ideas con poco dinero. Seguiremos a Pooja, ingeniera de mejora en una "
    "planta de dispositivos médicos."
)
OUTRO_SCRIPT = (
    "Así que recuerda tres cosas. Empieza con las personas que hacen el trabajo, y observa "
    "antes de decidir. Define la necesidad sin esconder una solución dentro. Y prueba en "
    "pequeño, midiendo los resultados y si la gente de verdad lo usa. Esta es tu acción para "
    "esta semana. Observa diez ciclos de un trabajo difícil, y habla con tres personas que lo "
    "hacen. Excelente trabajo al completar esta lección. Ahora aprenderás Elimination of "
    "Waste."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Qué es Design Thinking",
        "points": [("Empieza con las personas del proceso", "empieza con las personas"),
                   ("Empatizar, definir, idear", "Empatizas"),
                   ("Prototipar y probar, luego repetir", "Luego haces un prototipo")],
        "example": "La estación de empaque de Pooja: bombas de infusión, etiquetas, y empacadores a los que "
                   "nadie había preguntado.",
        "example_cue": "El reto de Pooja",
        "script": "Design Thinking es una forma de resolver problemas que empieza con las personas del "
                  "proceso. Las que hacen el trabajo, lo apoyan, o lo reciben. Empatizas, observando el "
                  "trabajo real. Defines la necesidad real, e ideas muchas opciones. Luego haces un "
                  "prototipo pequeño, lo pruebas, y aprendes. Y repites. El reto de Pooja era la estación "
                  "de empaque de bombas de infusión. ¿Y cómo encaja esto con Lean?",
    },
    {
        "key": "p02", "num": 2, "title": "Design Thinking y Lean",
        "points": [("No reemplaza las herramientas Lean", "No reemplaza al A3"),
                   ("Primero encuentra el problema correcto", "Te ayuda a encontrar"),
                   ("La gente adopta lo que ayuda a diseñar", "la gente adopta")],
        "example": "El método de empaque nuevo del año pasado duró dos semanas. Los empacadores volvieron a "
                   "la forma vieja.",
        "example_cue": "El año pasado",
        "script": "No reemplaza al A3, al Kaizen ni al Poka Yoke. Te ayuda a encontrar el problema correcto "
                  "antes de elegir uno de ellos. Lean elimina desperdicio. Design Thinking se asegura de "
                  "que el cambio encaje con personas reales y trabajo real. Y aquí está el extra. La gente "
                  "adopta lo que ayudó a diseñar. El año pasado, un método de empaque nuevo duró dos "
                  "semanas. Luego los empacadores volvieron en silencio a la forma vieja. ¿Por qué crees "
                  "que pasó eso?",
    },
    {
        "key": "p03", "num": 3, "title": "Principios de trabajo",
        "points": [("Observa sin suponer", "Observa sin suponer"),
                   ("Separa hechos de opiniones", "Separa los hechos"),
                   ("Prototipos pequeños antes de grandes cambios", "Prueba las ideas en pequeño"),
                   ("Mide resultados y aceptación", "Mide las dos cosas")],
        "example": "La regla de Pooja: “Muéstrame” antes que “dime”.",
        "example_cue": "La regla de Pooja",
        "script": "Algunos principios te mantienen honesto. Observa sin suponer que ya sabes la respuesta. "
                  "Separa los hechos de las opiniones, y de las soluciones propuestas. Trata a los "
                  "operadores y a los equipos de apoyo como tus usuarios. Prueba las ideas en pequeño, "
                  "antes de cambiar todo el proceso. Mide las dos cosas, los resultados y si la gente de "
                  "verdad acepta el cambio. La regla de Pooja era simple. Muéstrame, antes que dime. ¿Cuál "
                  "de estos te saltas más seguido?",
    },
    {
        "key": "p04", "num": 4, "title": "Lo que evita",
        "points": [("Automatizar un proceso roto", "Automatizar un proceso roto"),
                   ("Corregir solo el síntoma visible", "Corregir solo"),
                   ("Soluciones que la gente no puede seguir", "Imponer una solución"),
                   ("Gastar mucho antes de probar", "Gastar mucho")],
        "example": "La impresora más rápida: un gasto grande, en un problema que nadie había revisado.",
        "example_cue": "La impresora más rápida",
        "script": "¿Para qué molestarse? Porque evita algunos errores caros. Automatizar un proceso roto "
                  "que no entiendes bien. Corregir solo el síntoma visible. Imponer una solución que la "
                  "gente no puede seguir en un turno pesado. Y gastar mucho, antes de probar un solo "
                  "supuesto. La impresora más rápida fue un ejemplo perfecto. Un gasto grande, en un "
                  "problema que nadie había revisado. ¿Y qué pasos vas a seguir?",
    },
    {
        "key": "p05", "num": 5, "title": "Cinco etapas, un ciclo",
        "points": [("Empatizar · Definir · Idear", "Empatizar pregunta"),
                   ("Prototipar · Probar", "Prototipar pregunta"),
                   ("Deseable, factible, viable", "Una buena respuesta es"),
                   ("Avanza con evidencia, no con juntas", "Pasa a la siguiente etapa")],
        "example": "La puerta de Pooja: ninguna idea hasta tener observaciones reales y una base.",
        "example_cue": "Pooja puso una puerta",
        "script": "Hay cinco etapas, y puedes regresar. Empatizar pregunta qué viven los usuarios. Definir "
                  "pregunta qué problema importa más. Idear pregunta qué podría resolverlo. Prototipar "
                  "pregunta cómo podría funcionar. Probar pregunta si crea valor. Una buena respuesta es "
                  "deseable, factible y viable. Pasa a la siguiente etapa con evidencia, no porque terminó "
                  "una junta. Pooja puso una puerta. Ninguna idea sin observaciones. ¿Listo para observar?",
    },
    {
        "key": "p06", "num": 6, "title": "Empatizar en el Gemba",
        "points": [("Observa en varios turnos", "Observa varios ciclos"),
                   ("Entrevista después de observar", "Luego haz preguntas abiertas"),
                   ("Acompaña un puesto de principio a fin", "Acompaña a una persona"),
                   ("Mapa de empatía: dice, piensa, hace, siente", "Un mapa de empatía")],
        "example": "Pooja observó diez ciclos en cada turno, y luego habló con cinco empacadores.",
        "example_cue": "Pooja observó",
        "script": "La empatía empieza en el Gemba. Observa varios ciclos, en turnos normales y pesados. "
                  "Luego haz preguntas abiertas, después de ver el trabajo. Acompaña a una persona durante "
                  "todo el trabajo, para ver las entregas. Un mapa de empatía te ayuda a ordenarlo todo. "
                  "¿Qué dicen, piensan, hacen y sienten? Pooja observó diez ciclos en cada turno. Luego "
                  "habló con cinco empacadores. ¿Qué crees que vio?",
    },
    {
        "key": "p07", "num": 7, "title": "Lo que vio Pooja",
        "points": [("Caminar por etiquetas", "empacadores caminaban"),
                   ("Dos etiquetas parecidas lado a lado", "Dos etiquetas que se veían"),
                   ("Esperar a la impresora", "la impresora a veces")],
        "example": "“No soy lento. Estoy buscando.” Un empacador, del turno de noche.",
        "example_cue": "Un empacador lo dijo",
        "script": "No eran empacadores lentos. Los empacadores caminaban a un rack compartido por cada "
                  "etiqueta. Dos etiquetas que se veían casi iguales estaban lado a lado. Y la impresora a "
                  "veces se pausaba, así que esperaban. Un empacador lo dijo perfecto. No soy lento. Estoy "
                  "buscando. ¿Notas lo que falta? Nadie culpó a nadie. Son hechos sobre el trabajo, no "
                  "sobre las personas. ¿Cómo los convertirías en un problema que valga la pena resolver?",
    },
    {
        "key": "p08", "num": 8, "title": "Definir la necesidad",
        "points": [("Usuario · necesidad · hallazgo", "usuario, una necesidad"),
                   ("Ninguna solución dentro de la frase", "No nombra"),
                   ("Una base que puedas medir", "Agrega una base")],
        "example": "Los empacadores necesitan la etiqueta correcta a la mano, porque las etiquetas parecidas "
                   "y las caminatas causan errores. Ahora: 52 s contra un TAKT de 45 s, 12 errores por cada "
                   "1,000.",
        "example_cue": "Pooja escribió",
        "script": "Ahora define la necesidad. Una buena frase nombra un usuario, una necesidad y un "
                  "hallazgo. No nombra la solución. Pooja escribió una frase. Los empacadores necesitan la "
                  "etiqueta correcta justo a la mano, porque las etiquetas parecidas y las caminatas causan "
                  "errores. Agrega una base. La estación tardaba cincuenta y dos segundos, contra un TAKT "
                  "de cuarenta y cinco. Y doce bombas de cada mil tenían un error de etiqueta. ¿Ves la "
                  "impresora en algún lugar de esa frase?",
    },
    {
        "key": "p09", "num": 9, "title": "Idear: primero abre el abanico",
        "points": [("Escribe ideas antes de discutir", "Escribir ideas en silencio"),
                   ("Pregunta “¿Cómo podríamos…?”", "Cómo podríamos"),
                   ("SCAMPER y la mirada de los desperdicios", "Prueba SCAMPER")],
        "example": "El equipo de Pooja: 23 ideas en 30 minutos, de empacadores, calidad y almacén.",
        "example_cue": "El equipo de Pooja",
        "script": "Ahora abre el abanico, antes de elegir. Escribir ideas en silencio significa que cada "
                  "quien escribe sus ideas solo, antes de que el grupo hable. Así, no gana la voz más "
                  "fuerte. Haz preguntas de cómo podríamos, para convertir límites en oportunidades. Prueba "
                  "SCAMPER, o revisa los ocho desperdicios. El equipo de Pooja escribió veintitrés ideas en "
                  "treinta minutos. Empacadores, calidad y almacén participaron. ¿Cómo eliges solo una?",
    },
    {
        "key": "p10", "num": 10, "title": "Elegir con una tabla de puntos",
        "points": [("Da peso a cada criterio", "Da peso a cada criterio"),
                   ("Califica cada concepto, suma los puntos", "Califica cada concepto"),
                   ("La seguridad y la calidad son filtros", "la seguridad y la calidad")],
        "example": "Ranuras de etiquetas + revisión por escaneo: 4.15. Impresora nueva en la estación: 4.10.",
        "example_cue": "Los dos primeros",
        "script": "Usa una tabla de puntos simple. Da peso a cada criterio, como calidad, aceptación de los "
                  "usuarios, impacto, factibilidad y costo. Califica cada concepto, del uno al cinco. "
                  "Multiplica y suma. Pero la seguridad y la calidad no son solo puntos. Son filtros. Si "
                  "una idea falla uno, queda fuera. Los dos primeros quedaron cerca. Ranuras de etiquetas "
                  "por modelo con revisión por escaneo, y una impresora nueva en la estación. Las ranuras "
                  "ganaron, por poco. ¿Qué probarías primero?",
    },
    {
        "key": "p11", "num": 11, "title": "Prototipos pequeños y baratos",
        "points": [("Primero papel, cartón o cinta", "Empieza con papel"),
                   ("Una estación antes que la línea", "Prueba una estación"),
                   ("Horas, no meses", "se mide en horas")],
        "example": "Ranuras de cartón para etiquetas, una por modelo, pegadas con cinta junto al empacador.",
        "example_cue": "El primer prototipo de Pooja",
        "script": "Haz la idea real, lo más barato que puedas. Empieza con papel, cartón o cinta en el "
                  "piso. Prueba una estación antes que toda la línea. Un buen prototipo se mide en horas, "
                  "no en meses. El primer prototipo de Pooja fue de cartón. Una ranura de etiqueta por "
                  "modelo, pegada con cinta justo junto al empacador, con el escáner a la mano. Casi no "
                  "costó nada. ¿Pero cómo sabría si funcionaba?",
    },
    {
        "key": "p12", "num": 12, "title": "Planear la prueba",
        "points": [("Una hipótesis clara", "Escribe una hipótesis"),
                   ("Alcance, medidas y comparación", "Fija el alcance"),
                   ("Una regla de decisión acordada desde el inicio", "Acuerda una regla de decisión")],
        "example": "Hipótesis: las ranuras + la revisión por escaneo ponen el tiempo de ciclo dentro del "
                   "TAKT y bajan los errores de etiqueta al menos 75%.",
        "example_cue": "La hipótesis de Pooja",
        "script": "Planea la prueba antes de empezarla. Escribe una hipótesis. Si cambiamos esto, esperamos "
                  "aquello. Fija el alcance, las medidas, y contra qué vas a comparar. Acuerda una regla de "
                  "decisión desde el inicio. Adoptar, adaptar o parar. La hipótesis de Pooja era clara. Las "
                  "ranuras y una revisión por escaneo pondrían el tiempo de ciclo dentro del TAKT. Y los "
                  "errores de etiqueta bajarían al menos tres cuartas partes. ¿Qué crees que pasó?",
    },
    {
        "key": "p13", "num": 13, "title": "Los resultados",
        "points": [("Tiempo de ciclo: de 52 s a 44 s", "El tiempo de ciclo bajó"),
                   ("Bombas buenas por turno: de 500 a 610", "Las bombas buenas por turno"),
                   ("Errores de etiqueta: de 12 a 2 por cada 1,000", "Los errores de etiqueta bajaron"),
                   ("Caminata: de 4 m a 1.2 m", "La caminata bajó")],
        "example": "18 de 20 empacadores usaron el método nuevo: 90% de adopción.",
        "example_cue": "Dieciocho de veinte",
        "script": "La prueba funcionó, casi del todo. El tiempo de ciclo bajó de cincuenta y dos a cuarenta "
                  "y cuatro segundos. Eso ya está dentro del TAKT. Las bombas buenas por turno subieron de "
                  "quinientas a seiscientas diez. Los errores de etiqueta bajaron de doce a dos por cada "
                  "mil. La caminata bajó más de la mitad. Y dieciocho de veinte empacadores usaron el "
                  "método nuevo. Es el noventa por ciento. ¿Entonces Pooja debe extenderlo mañana?",
    },
    {
        "key": "p14", "num": 14, "title": "Adapta antes de extender",
        "points": [("¿No hay 100% de adopción? Averigua por qué", "Dos empacadores"),
                   ("Simplifica el paso difícil, prueba otra vez", "simplificó ese paso"),
                   ("Revisa que no lo hayan causado otros factores", "Y revisa que")],
        "example": "Los dos empacadores eran zurdos. Las ranuras estaban a la derecha. Refleja el acomodo.",
        "example_cue": "Resultó que",
        "script": "Todavía no. Dos empacadores no siguieron el método. Así que les preguntó por qué. "
                  "Resultó que trabajaban con la mano izquierda, y las ranuras estaban a la derecha. Ella "
                  "simplificó ese paso, con un acomodo en espejo, y probó otra vez. Y revisa que otros "
                  "factores no hayan causado la mejora, como una mezcla de modelos más fácil o personal "
                  "extra. Solo entonces estandarizas. ¿Cómo medirías el éxito?",
    },
    {
        "key": "p15", "num": 15, "title": "Medir, estandarizar, empezar",
        "points": [("Resultado, proceso, adopción, equilibrio", "Mide el resultado"),
                   ("Estandariza, entrena, revisa a los 30/60/90", "Luego estandariza"),
                   ("Empieza mañana: 10 ciclos, 3 personas", "Empieza mañana")],
        "example": "La revisión de Pooja a los 90 días: errores en 2 por cada 1,000, adopción del 100%.",
        "example_cue": "A los noventa días",
        "script": "Mide el resultado, el proceso, la adopción y el equilibrio. ¿Empeoró algo más, como la "
                  "seguridad o el costo? Luego estandariza, entrena a cada turno, y revisa a los treinta, "
                  "sesenta y noventa días. A los noventa días, los errores de Pooja seguían en dos por cada "
                  "mil, y cada empacador usaba el método. Empieza mañana. Observa diez ciclos de un trabajo "
                  "difícil, habla con tres personas, y escribe una necesidad.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "steps", "items": [
        {"label": "Empatizar", "with": 1}, {"label": "Definir", "with": 1},
        {"label": "Idear", "with": 1}, {"label": "Prototipar", "with": 2},
        {"label": "Probar", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Las herramientas Lean se quedan", "icon": "wrench", "with": 0},
        {"label": "Primero el problema correcto", "icon": "search", "with": 1},
        {"label": "De los usuarios", "icon": "hand", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Método impuesto", "sub": "Se fue en dos semanas", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Método diseñado juntos", "sub": "La gente lo conserva", "icon": "check", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Observar", "icon": "search", "with": 0},
        {"label": "Primero los hechos", "icon": "clipboard", "with": 1},
        {"label": "Pruebas pequeñas", "icon": "shape", "with": 2},
        {"label": "Aceptación", "icon": "person", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Automatizar un desorden", "icon": "gear", "tone": "bad", "with": 0},
        {"label": "Solo el síntoma", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "No se puede seguir", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Gasto grande, sin prueba", "icon": "trash", "tone": "bad", "with": 3}]},
    "p05": {"type": "steps", "items": [
        {"label": "Empatizar", "with": 0}, {"label": "Definir", "with": 0},
        {"label": "Idear", "with": 0}, {"label": "Prototipar", "with": 1},
        {"label": "Probar", "with": 1}],
        "then": {"type": "icons", "with": 2, "items": [
            {"label": "Deseable", "sub": "Los usuarios lo necesitan", "icon": "person", "with": 2},
            {"label": "Factible", "sub": "Podemos hacerlo", "icon": "wrench", "with": 2},
            {"label": "Viable", "sub": "Vale lo que cuesta", "icon": "scale", "tone": "good", "with": 2}]}},
    "p06": {"type": "icons", "items": [
        {"label": "Observar", "icon": "search", "with": 0},
        {"label": "Entrevistar", "icon": "person", "with": 1},
        {"label": "Acompañar", "icon": "walk", "with": 2},
        {"label": "Dice · piensa · hace · siente", "icon": "clipboard", "with": 3}]},
    "p07": {"type": "flow", "items": [
        {"label": "Caminar al rack", "icon": "walk", "tone": "bad", "with": 0},
        {"label": "Etiquetas parecidas", "icon": "label", "tone": "bad", "with": 1},
        {"label": "Esperar a la impresora", "icon": "clock", "tone": "bad", "with": 2}]},
    "p08": {"type": "doc", "items": [
        {"label": "Usuario: los empacadores", "icon": "person", "with": 0},
        {"label": "Necesidad: la etiqueta correcta a la mano", "icon": "label", "with": "example"},
        {"label": "Hallazgo: etiquetas parecidas y caminatas", "icon": "search", "with": "example"},
        {"label": "Base: 52 s contra 45 s, 12 por cada 1,000", "icon": "chartUp", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Ideas en silencio", "icon": "clipboard", "with": 0},
        {"label": "¿Cómo podríamos…?", "icon": "key", "with": 1},
        {"label": "SCAMPER, 8 desperdicios", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 23, "icon": "key", "label": "ideas en 30 minutos",
                 "unit": "empacadores, calidad y almacén", "with": "example"}},
    "p10": {"type": "versus", "items": [
        {"label": "Impresora nueva", "sub": "Puntaje 4.10 de 5", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "Ranuras de etiquetas + revisión por escaneo", "sub": "Puntaje 4.15 de 5", "icon": "check", "tone": "good", "with": "example"}]},
    "p11": {"type": "ladder", "top": "LO MÁS BARATO", "bottom": "LO MÁS GRANDE", "items": [
        {"label": "Papel, cartón, cinta", "icon": "shape", "with": 0},
        {"label": "Piloto en una estación", "icon": "pin", "with": 1},
        {"label": "Prueba en la línea", "icon": "sequence", "with": 1}],
        "then": {"type": "stat", "value": 1, "suffix": " ranura por modelo", "icon": "label", "label": "de cartón, pegada junto al empacador",
                 "unit": "escáner al alcance", "with": "example"}},
    "p12": {"type": "flow", "items": [
        {"label": "Hipótesis", "icon": "key", "with": 0},
        {"label": "Alcance y medidas", "icon": "clipboard", "with": 1},
        {"label": "Adoptar · adaptar · parar", "icon": "scale", "tone": "good", "with": 2}]},
    "p13": {"type": "compare", "before": {"label": "Antes", "value": 12}, "after": {"label": "Prueba", "value": 2},
            "unit": "errores de etiqueta por cada 1,000 bombas", "note": "Ciclo 52 s → 44 s · 500 → 610 bombas buenas", "with": 2,
            "then": {"type": "stat", "value": 90, "suffix": "%", "icon": "person", "label": "adopción",
                     "unit": "18 de 20 empacadores", "with": "example"}},
    "p14": {"type": "flow", "items": [
        {"label": "Pregunta por qué", "icon": "person", "with": 0},
        {"label": "Acomodo en espejo", "icon": "shape", "with": 1},
        {"label": "Revisa la mezcla de modelos", "icon": "search", "with": 2},
        {"label": "Luego estandariza", "icon": "check", "tone": "good", "with": 2}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Estandarizar, entrenar", "sub": "Día 0", "icon": "clipboard", "with": 1},
        {"label": "Revisión", "sub": "30 · 60", "icon": "search", "with": 1},
        {"label": "Errores en 2", "sub": "90 días", "icon": "check", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "¿Cuál es el mejor planteamiento de reto en Design Thinking?",
        "options": ["Necesitamos una impresora de etiquetas más rápida en empaque",
                    "Los empacadores necesitan la etiqueta correcta a la mano, porque las etiquetas parecidas "
                    "y las caminatas causan errores",
                    "Los empacadores deben tener más cuidado con las etiquetas"],
        "correct": 1,
        "explanation": "Nombra al usuario, la necesidad y el hallazgo, sin elegir una solución ni culpar a "
                       "nadie. Los otros son una solución y una culpa.",
        "q_script": "Prueba rápida. ¿Cuál de estos es el mejor planteamiento de reto? Tómate unos segundos.",
        "a_script": "Es el segundo. Nombra al usuario, la necesidad y el hallazgo. El primero ya es una "
                    "solución, y el último es solo culpa.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un piloto baja el tiempo de ciclo, pero solo 6 de 10 operadores usan el método nuevo. "
                    "¿Qué sigue?",
        "options": ["Extenderlo: los números mejoraron",
                    "Preguntarles a los otros cuatro por qué, simplificar, y probar otra vez",
                    "Hacerlo obligatorio y auditar a diario"],
        "correct": 1,
        "explanation": "La baja adopción también es evidencia. Averigua qué hace difícil el método para esos "
                       "usuarios, mejóralo, y vuelve a probar antes de estandarizar.",
        "q_script": "Una más, y esta es un escenario. Un piloto baja el tiempo de ciclo. Pero solo seis de "
                    "diez operadores usan el método nuevo. ¿Qué debe hacer el equipo? Piénsalo.",
        "a_script": "Pregúntales a los otros cuatro por qué, simplifica la parte difícil, y prueba otra vez. "
                    "La baja adopción también es evidencia, así que trátala como cualquier otro resultado.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
