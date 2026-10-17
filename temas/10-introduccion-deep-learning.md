# 10. Introducción a Deep Learning

## Qué aprenderás

Comprenderás cómo un modelo aprende a partir de ejemplos, qué diferencia existe entre entrenamiento e inferencia y por qué los datos etiquetados son esenciales para entrenar un detector.

## La idea en palabras sencillas

Hasta ahora hemos escrito las reglas. Otra posibilidad es mostrar muchas fotografías con respuestas correctas y ajustar un modelo para que encuentre patrones que ayuden a predecir esas respuestas.

Piensa en practicar con ejercicios resueltos y después intentar otros nuevos. La comparación ayuda a entender entrenamiento y evaluación, aunque un modelo no aprende ni comprende exactamente como una persona. En este curso aprenderá a proponer cajas y nombres de objetos. Entrenar es ajustar el modelo; usarlo sobre una imagen nueva es hacer una predicción, también llamada inferencia.

## 1. De reglas explícitas a parámetros aprendidos

En las prácticas anteriores elegimos colores, tamaños de kernel y reglas geométricas. La aplicación seguía esas decisiones. Si cambiaba mucho la apariencia del objeto, debíamos adaptar las reglas.

En **aprendizaje automático**, un modelo ajusta parámetros a partir de datos para resolver una tarea. **Deep Learning** utiliza redes neuronales con múltiples etapas de transformación. En visión, esas transformaciones pueden aprender representaciones relacionadas con bordes, texturas, formas y patrones más complejos, aunque no todas las capas tienen una interpretación humana sencilla.

Aprender no significa comprender el mundo como una persona. El modelo encuentra regularidades útiles para la tarea y puede equivocarse si los ejemplos no representan las condiciones de uso.

## 2. Entrenamiento supervisado

En este curso trabajaremos con detección supervisada: cada imagen de entrenamiento tiene anotaciones que indican qué objetos hay y dónde están. El modelo produce predicciones y estas se comparan con las etiquetas mediante una función de pérdida.

De manera simplificada, un paso de entrenamiento consiste en presentar un grupo de ejemplos, calcular predicciones, medir el error, calcular cómo influye cada parámetro y ajustar esos parámetros con un optimizador. El proceso se repite sobre muchos grupos y durante varias pasadas por los datos.

La **pérdida** es una medida usada para orientar el ajuste. Una pérdida baja en entrenamiento no prueba que el modelo funcione bien con imágenes nuevas. Por eso necesitamos datos de validación y de prueba.

## 3. Conceptos del entrenamiento

- **Pesos:** parámetros numéricos que determinan el comportamiento de la red.
- **Batch:** grupo de ejemplos procesado en un paso.
- **Época:** una pasada por el conjunto de entrenamiento en el esquema habitual.
- **Tasa de aprendizaje:** controla la magnitud de los ajustes del optimizador.
- **Validación:** evaluación durante el desarrollo sobre datos separados del entrenamiento.

Más épocas no garantizan mejores resultados. Si el modelo empieza a adaptarse demasiado a los ejemplos conocidos, puede empeorar con otros: eso se llama **sobreajuste**. Si no logra aprender patrones útiles ni siquiera en entrenamiento, puede existir **subajuste**, datos insuficientes o un problema de configuración.

## 4. Entrenamiento e inferencia

**Entrenar** modifica los pesos usando datos y etiquetas. **Inferir** utiliza los pesos ya obtenidos para predecir sobre una imagen nueva. Durante la detección normal por cámara web no necesitas etiquetar cada fotograma ni volver a entrenar.

Esta separación permite entrenar con GPU en Colab y ejecutar después en una computadora local. La computadora local necesita cargar el modelo y contar con suficiente capacidad para la velocidad deseada; no necesita repetir el entrenamiento para usarlo.

## 5. Clasificación, detección y segmentación

| Tarea | Respuesta habitual |
| --- | --- |
| Clasificación | Qué clase corresponde a la imagen o recorte. |
| Detección | Qué objetos hay, con una caja para cada instancia. |
| Segmentación | Qué píxeles pertenecen a objetos o clases. |

El temario se centra en **detección**. No basta con etiquetar una imagen como «taza» si necesitamos saber dónde está cada taza. Utilizaremos bounding boxes para supervisar la posición.

## 6. Qué aporta YOLO

YOLO es una familia de detectores que realiza predicciones de localización y clase en un flujo diseñado para ser eficiente. Los detalles de arquitectura y pérdidas cambian entre versiones. Al realizar la práctica, utiliza un modelo compatible con la versión de Ultralytics de tu entorno y registra su nombre para poder repetir el experimento.

Para un taller breve suele ser útil partir de pesos **preentrenados** y ajustarlos a las clases nuevas. Es una forma de transferencia de aprendizaje: se aprovecha una representación obtenida con otros datos. Esto no elimina la necesidad de un dataset adecuado ni hace que el detector conozca automáticamente las clases de tu proyecto.

## 7. GPU y límites prácticos

Una GPU puede ejecutar muchas operaciones numéricas en paralelo y acelerar el entrenamiento. La velocidad también depende del modelo, el tamaño de imagen, el batch y el movimiento de datos. Disponer de GPU no corrige etiquetas incorrectas ni garantiza generalización.

## Actividad de comprensión

Explica qué cambia entre entrenar un detector y cargarlo para analizar una cámara. Describe por qué un modelo que detecta bien todos los ejemplos usados durante entrenamiento puede fallar en un salón distinto.

## Del filtro de la hoja a un detector aprendido

En la primera parte, si retirabas la hoja verde y colocabas una hoja azul, el filtro podía dejar de seleccionarla aunque tuviera la misma forma. La regla preguntaba por valores de color, no por la idea general de «hoja».

Para reconocer objetos con más apariencias, podemos preparar ejemplos etiquetados y ajustar un modelo. Este cambio no elimina todos los problemas: sustituye parte del diseño manual de reglas por una preparación cuidadosa de datos y entrenamiento.

| Enfoque | Qué preparas | Qué utiliza el programa al funcionar |
| --- | --- | --- |
| Regla de color | Límites HSV y condiciones geométricas. | Los valores y condiciones que escribiste. |
| Detector aprendido | Imágenes con clases y cajas; configuración de entrenamiento. | Los pesos ajustados a partir de esos ejemplos. |

Un detector podría encontrar un vaso sin que todos los vasos sean verdes, si sus datos permiten aprender patrones útiles. También puede confundirse con fondos o formas parecidas. No hay una mejora garantizada para cualquier tarea: las pruebas indican qué enfoque funciona en tus condiciones.

## Ejemplo cotidiano: aprender no es evaluar

Imagina una colección de fotografías de vasos y botellas. Durante el entrenamiento, el modelo compara sus predicciones con las cajas y clases correctas. Sus parámetros cambian para reducir el error según la función de pérdida.

Después lo evalúas con fotografías distintas. Si solo acierta en las utilizadas para ajustar parámetros, no ha demostrado que funcione con tu cámara. Esa es la razón de separar los datos y de no medir el resultado final únicamente con lo que ya vio durante entrenamiento.

Las palabras «aprender» y «evaluar» describen operaciones diferentes. No necesitas comprender el cálculo de cada parámetro para seguir el taller; sí necesitas reconocer qué imágenes modifican el modelo y cuáles sirven para comprobarlo.

## Entrenar desde cero o aprovechar un modelo previo

Entrenar desde cero comienza con parámetros sin el aprendizaje previo de otros datos y suele necesitar más recursos y ejemplos. Ajustar pesos preentrenados aprovecha una representación ya aprendida y la adapta a la tarea nueva. Para un taller corto, este segundo enfoque suele ser más práctico.

El modelo inicial y el modelo personalizado pueden reconocer clases distintas. No asumas que cargar cualquier archivo de YOLO ya incluye las clases de tu proyecto. El entrenamiento y el archivo de pesos que finalmente uses deben corresponder a tu tarea.

**Comprueba que lo entendiste:** explica por qué descargar un modelo y entrenar uno no son lo mismo. Después describe qué necesitarías para enseñarle una clase nueva: un nombre escrito en el programa no basta; hacen falta datos anotados y un proceso de ajuste adecuado.

## Para dar el siguiente paso

Si el modelo aprende a partir de ejemplos, **¿qué fotografías debemos reunir y cómo las organizamos para saber si realmente aprende?** En el siguiente capítulo prepararemos un dataset y separaremos los datos que se usan para ajustar del material con el que comprobamos el resultado.

[Anterior](09-detectar-figuras.md) · [Índice](../README.md) · [Siguiente: Dataset](11-que-es-un-dataset.md)
