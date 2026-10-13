# 16. Entrenar modelo YOLO usando GPU

## Qué aprenderás

Comprenderás los parámetros básicos del entrenamiento, cómo interpretar resultados y cómo seleccionar pesos sin confundir el desempeño sobre datos conocidos con el desempeño sobre escenas nuevas.

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

Los nombres, tipos y opciones exactas dependen de la versión instalada. Se explicarán los argumentos del código original cuando lo recibamos. Esta tabla describe conceptos habituales de Ultralytics, no un comando transcrito de la conversación.

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

## Código original

Pendiente de recibir las celdas de carga y entrenamiento. Se explicarán modelo inicial, argumentos, registro de resultados y archivos producidos.

[Anterior](15-colab-gpu-ultralytics.md) · [Índice](../README.md) · [Siguiente: Descargar modelo](17-descargar-yolo-uso-local.md)
