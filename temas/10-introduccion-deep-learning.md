# 10. Introducción a Deep Learning

## Qué aprenderás

Comprenderás cómo un modelo aprende a partir de ejemplos, qué diferencia existe entre entrenamiento e inferencia y por qué los datos etiquetados son esenciales para entrenar un detector.

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

YOLO es una familia de detectores que realiza predicciones de localización y clase en un flujo diseñado para ser eficiente. Los detalles de arquitectura y pérdidas cambian entre versiones. En este curso usaremos una versión compatible con Ultralytics y con los ejemplos que proporciones; no se asumirá una arquitectura concreta hasta conocer el código.

Para un taller breve suele ser útil partir de pesos **preentrenados** y ajustarlos a las clases nuevas. Es una forma de transferencia de aprendizaje: se aprovecha una representación obtenida con otros datos. Esto no elimina la necesidad de un dataset adecuado ni hace que el detector conozca automáticamente las clases de tu proyecto.

## 7. GPU y límites prácticos

Una GPU puede ejecutar muchas operaciones numéricas en paralelo y acelerar el entrenamiento. La velocidad también depende del modelo, el tamaño de imagen, el batch y el movimiento de datos. Disponer de GPU no corrige etiquetas incorrectas ni garantiza generalización.

## Actividad de comprensión

Explica qué cambia entre entrenar un detector y cargarlo para analizar una cámara. Describe por qué un modelo que detecta bien todos los ejemplos usados durante entrenamiento puede fallar en un salón distinto.

[Anterior](09-detectar-figuras.md) · [Índice](../README.md) · [Siguiente: Dataset](11-que-es-un-dataset.md)
