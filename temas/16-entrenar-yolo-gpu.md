# 16. Entrenar modelo YOLO usando GPU

## Qué aprenderás

Comprenderás los parámetros básicos del entrenamiento, cómo interpretar resultados y cómo seleccionar pesos sin confundir el desempeño sobre datos conocidos con el desempeño sobre escenas nuevas.

## La idea en palabras sencillas

Entrenar significa mostrar ejemplos al modelo y ajustar sus parámetros cuando se equivoca. Verás pasar grupos de imágenes y varias vueltas de entrenamiento. No necesitas interpretar todas las cifras para empezar: primero comprueba que se están utilizando los datos correctos y que el proceso avanza.

Después observaremos qué objetos detecta, cuáles omite y qué falsas alarmas produce. Una puntuación alta no sustituye mirar los resultados. Al terminar guardarás los pesos, que son el archivo que necesitará la siguiente práctica para utilizar lo aprendido.

## 1. Qué cambia al entrenar

Durante el entrenamiento se ajustan los parámetros del detector para relacionar imágenes con clases y cajas. En un flujo de transferencia de aprendizaje, el punto inicial son pesos preentrenados compatibles con el modelo elegido.

El archivo de datos describe las clases nuevas y las rutas. El archivo de pesos inicial describe una red y sus parámetros. Son recursos diferentes: pasar el YAML del dataset no equivale a cargar un detector, y cargar pesos preentrenados no define por sí solo tus clases personalizadas.

## 2. Parámetros que debes entender

| Parámetro habitual | Propósito | Consecuencia práctica |
| --- | --- | --- |
| `data` | Configuración del dataset. | Una ruta o clases incorrectas invalidan el experimento. |
| `epochs` | Número máximo de pasadas de entrenamiento. | Más entrenamiento puede ayudar o favorecer sobreajuste. |
| `imgsz` | Tamaño de entrada de entrenamiento. | Influye en detalle, costo y memoria. |
| `batch` | Ejemplos por paso. | Un valor grande puede superar la memoria de GPU. |
| `device` | Dispositivo de cómputo. | Debe corresponder a un recurso disponible. |
| `project` y `name` | Organización de resultados. | Ayudan a identificar la ejecución y sus archivos. |

Los nombres, tipos y opciones exactas dependen de la versión instalada. Consulta la documentación de tu versión para confirmar los argumentos admitidos y registra los valores que utilices en tu experimento.

## 3. Elegir un primer experimento

Para un taller, empieza con un modelo pequeño compatible y parámetros moderados. El objetivo inicial es comprobar que datos, etiquetas y entrenamiento forman un flujo válido. No necesita ser el mejor detector posible.

Después modifica un aspecto a la vez y conserva el resultado anterior. Si cambias simultáneamente dataset, arquitectura, tamaño de entrada y épocas, será difícil explicar qué produjo una mejora o empeoramiento.

## 4. Leer la pérdida

El entrenamiento suele informar pérdidas relacionadas con localización y clasificación; sus componentes exactos varían entre modelos. Una tendencia descendente puede indicar que el modelo se adapta a entrenamiento, pero no basta para evaluar generalización.

Compara con validación y revisa ejemplos visuales. Una pérdida que baja mientras las métricas de validación se estancan o empeoran puede señalar sobreajuste. También puede haber ruido en mediciones de conjuntos pequeños; evita conclusiones basadas en una sola época.

## 5. Precision, recall e IoU

La **precision** mide qué proporción de las detecciones aceptadas corresponde a objetos correctos, bajo los criterios de evaluación. Si aparecen muchas detecciones falsas, disminuye.

El **recall** mide qué proporción de los objetos anotados se detectó correctamente. Si el modelo omite muchas instancias, disminuye.

La **IoU** es la intersección entre dos cajas dividida por su unión. Mide su superposición. Una predicción necesita una clase correcta y una localización suficientemente coincidente según el criterio utilizado. También debe considerarse el emparejamiento entre predicciones e instancias: varias cajas sobre el mismo objeto no representan varios aciertos independientes.

## 6. AP y mAP

La **AP** resume la relación entre precision y recall al variar umbrales, según un protocolo de evaluación. La **mAP** promedia AP entre clases y, según la métrica, entre criterios de IoU.

`mAP50` utiliza un criterio de IoU de 0,50. `mAP50-95` considera varios umbrales desde 0,50 hasta 0,95 y exige también localización más precisa. Sus valores no deben compararse como si fueran la misma métrica.

Revisa resultados por clase. Un promedio alto puede esconder una clase con desempeño pobre. También examina ejemplos de objetos pequeños, iluminación difícil y fondos parecidos a los del uso real.

## 7. Archivos de resultados

Ultralytics suele guardar curvas, métricas y pesos en una carpeta de ejecución. En los flujos habituales aparece `last.pt` para el estado final y `best.pt` para el seleccionado según el criterio de validación del entrenador. El criterio exacto depende de la versión y configuración.

El último archivo no es necesariamente el mejor. El mejor de validación tampoco garantiza buen desempeño fuera del dataset. Registra el archivo elegido y verifica dónde se guardó realmente; ejecuciones repetidas pueden generar carpetas con nombres distintos.

## 8. Problemas y ajustes

**Memoria insuficiente:** prueba un batch menor y revisa tamaño de entrada o modelo. **Entrenamiento en CPU:** comprueba GPU y dispositivo seleccionado. **Sin etiquetas válidas:** revisa exportación y rutas. **Métricas bajas:** revisa ejemplos, etiquetas, diversidad y clases antes de aumentar épocas indiscriminadamente.

No optimices reiteradamente sobre el conjunto de prueba. Usa validación para decisiones y reserva prueba para una estimación final. Si ajustas decisiones a partir de prueba, deja de ser una evaluación independiente.

## Actividad de comprensión

Compara dos modelos hipotéticos: uno detecta casi todos los objetos pero genera muchas falsas alarmas; el otro detecta pocos, aunque suele acertar. Relaciona cada caso con precision y recall y explica cuál preferirías según una tarea concreta.

## Registro del experimento

Anota el modelo inicial, la versión del dataset y los valores de los parámetros antes de entrenar. Al terminar, conserva la carpeta de resultados, revisa métricas por clase y registra qué pesos seleccionaste. Utiliza imágenes nuevas para examinar errores que los promedios pueden ocultar.

## Leer el entrenamiento sin perderte entre cifras

Durante una ejecución, empieza por tres preguntas: ¿está usando el dataset correcto?, ¿avanzan las épocas?, ¿dónde se guardarán los resultados? Después revisa las medidas.

Piensa en una imagen con diez objetos anotados. Si el detector encuentra correctamente ocho y no añade falsas alarmas, omitió dos. Si encuentra esos ocho pero también marca cuatro lugares sin objeto, además produjo cuatro falsas alarmas. Este ejemplo ilustra por qué necesitamos observar tanto objetos omitidos como detecciones incorrectas; no son el mismo problema.

Los valores de entrenamiento reales utilizan criterios de clase, localización y emparejamiento, explicados en esta sección. Para comenzar, observa imágenes anotadas con las predicciones y busca esos dos tipos de error. No interpretes cada número como un porcentaje de «inteligencia» del modelo.

Al terminar, anota la carpeta de resultados y el archivo de pesos elegido. Si cambias parámetros para una nueva prueba, registra qué modificaste. No mezcles resultados de ejecuciones diferentes como si pertenecieran al mismo experimento.

## Ejemplo numérico: errores distintos, medidas distintas

Supón que una evaluación tiene diez instancias anotadas. Bajo su criterio de coincidencia, el modelo acierta ocho y añade dos detecciones falsas. Tendría ocho aciertos, dos objetos omitidos y dos falsas alarmas. Su precision sería 8 / 10 = 0.8 y su recall también 8 / 10 = 0.8 en este ejemplo simplificado.

Si ahora conserva esos ocho aciertos pero añade seis falsas alarmas, su precision pasa a 8 / 14, aproximadamente 0.57, mientras el recall permanece en 0.8. Eso muestra por qué detectar muchos objetos y evitar falsas alarmas son objetivos relacionados pero diferentes.

En una evaluación real también cuentan la clase, el emparejamiento y la localización según IoU. No puedes contar dos cajas del mismo objeto como dos instancias correctas por conveniencia. Las herramientas realizan esa evaluación bajo un protocolo definido.

## Ejemplo de configuración que debes poder explicar

Si una práctica utiliza 20 épocas y un batch de 8, significa un máximo de veinte pasadas por entrenamiento y grupos de ocho ejemplos por paso, con los detalles del cargador de datos y la configuración. No significa veinte fotografías ni que solo se admitan ocho clases.

Estos números ilustran los conceptos; no fijan los parámetros del experimento del taller. El tamaño de imagen y el batch deben caber en la memoria disponible. Una GPU más rápida no vuelve correctas las anotaciones equivocadas.

## Cómo decidir si repetir un entrenamiento

Antes de aumentar épocas, inspecciona imágenes con predicciones: ¿falla una clase concreta?, ¿son objetos muy pequeños?, ¿faltan condiciones del laboratorio?, ¿hay etiquetas incorrectas? Esos hallazgos indican si necesitas corregir datos, reunir variación o ajustar la configuración.

Conserva el experimento anterior y cambia una decisión identificable. Compara en validación y evita elegir cambios mirando repetidamente el conjunto final de prueba. Después revisa también la cámara real: las métricas del dataset no describen automáticamente cualquier entorno.

## Para dar el siguiente paso

El entrenamiento produjo archivos y métricas. **¿Cuál de esos archivos debemos conservar para utilizar el detector en la computadora de Windows?** En el siguiente capítulo seleccionaremos y trasladaremos los pesos.

[Anterior](15-colab-gpu-ultralytics.md) · [Índice](../README.md) · [Siguiente: Descargar modelo](17-descargar-yolo-uso-local.md)
