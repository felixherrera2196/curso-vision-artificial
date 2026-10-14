# 17. Descargar YOLO entrenado para uso local

## Qué aprenderás

Comprenderás qué archivo trasladar desde Colab, cómo conservar su contexto de entrenamiento y qué comprobar antes de incorporarlo a una aplicación de cámara web.

## 1. Qué contiene el archivo de pesos

El modelo entrenado conserva parámetros aprendidos y, según el formato, información adicional necesaria para cargarlo. En el flujo habitual de Ultralytics se utilizan archivos `.pt`, como `best.pt` o `last.pt`.

No necesitas descargar todas las imágenes para realizar inferencia local, aunque debes conservar la versión de los datos para reproducir el entrenamiento. El YAML del dataset y los pesos cumplen propósitos diferentes: el YAML describe los datos, mientras el archivo de pesos permite cargar el detector entrenado.

No confíes únicamente en la extensión. Un archivo equivocado, incompleto o generado por una versión incompatible puede fallar al cargarlo.

## 2. Seleccionar la ejecución correcta

Localiza la carpeta de resultados del entrenamiento que deseas utilizar. Puede haber varias ejecuciones y varios archivos con el mismo nombre. Revisa el nombre de la ejecución, las clases, las métricas y la fecha del experimento registrada en tus notas.

En un flujo habitual elegirás el modelo seleccionado por validación, frecuentemente `best.pt`, pero la selección debe ser explícita. No descargues automáticamente el primer archivo encontrado si no sabes a qué entrenamiento pertenece.

## 3. Conservar antes de terminar la sesión

Los resultados en el almacenamiento temporal de Colab pueden desaparecer al cerrar o reiniciar la sesión. Copia los pesos a un lugar persistente y descárgalos a tu computadora antes de perder acceso.

La descarga desde el navegador puede quedar en la carpeta Descargas del equipo. Trasládala a la carpeta del proyecto y confirma que la transferencia terminó. Si el navegador cambia el nombre porque ya existe otro archivo, identifica cuál corresponde a la ejecución deseada.

## 4. Información que acompaña a los pesos

Conserva, al menos, nombre o familia del modelo, versión de Ultralytics, versión del dataset, clases, parámetros básicos de entrenamiento y métricas relevantes. Cuando dos archivos se llaman `best.pt`, esa información permite distinguirlos.

No presentes el archivo como un detector universal. Explica para qué clases y condiciones se entrenó y qué situaciones has evaluado. Esa información ayuda a interpretar los fallos del uso local.

## 5. Preparar el equipo local

El equipo necesita Python y una biblioteca compatible para cargar los pesos. Debe utilizar el intérprete correcto del tema 03. No es necesario disponer de GPU NVIDIA para todo uso de inferencia: muchos modelos pueden ejecutarse en CPU, con un rendimiento que depende del equipo y del modelo.

La GPU usada en Colab no se transfiere con los pesos. Si la laptop solo tiene CPU, el tiempo por fotograma puede ser mayor. Ajusta expectativas y mide la velocidad real antes de prometer detección fluida.

## 6. Comprobar la carga con una imagen

Antes de añadir cámara, utiliza una imagen conocida y otra nueva. Comprueba que el archivo carga, que las clases son las esperadas y que las cajas tienen sentido.

Este paso separa problemas de modelo de problemas de captura. Si el detector ya falla al cargar o produce clases inesperadas sobre una imagen, todavía no tiene sentido depurar el ciclo de cámara.

La ruta del archivo puede ser absoluta o relativa. Una ruta relativa se interpreta desde el directorio de trabajo del proceso, que no siempre coincide con la carpeta del archivo Python. Confirma cómo se ejecuta el programa en VS Code.

## 7. Fallos frecuentes

- **Archivo no encontrado:** verifica nombre, extensión y directorio de trabajo.
- **Clases diferentes:** probablemente cargaste otros pesos o una ejecución equivocada.
- **Error de compatibilidad:** revisa biblioteca, versión y procedencia del archivo.
- **Descarga incompleta:** comprueba que el archivo tenga contenido y vuelve a transferirlo si hace falta.
- **Inferencia lenta:** revisa modelo, tamaño de entrada y dispositivo local.

## Actividad de comprensión

Explica qué información guardarías junto a dos experimentos distintos cuyos archivos se llamen `best.pt`. Describe por qué una descarga correcta no demuestra todavía que el modelo detecte bien con la webcam.

## Comprobación antes de usar la cámara

Confirma que descargaste los pesos de la ejecución correcta y que el archivo puede cargarse en tu entorno local. Realiza una predicción sobre una imagen conocida y otra nueva. Comprueba las clases y las cajas antes de integrar la captura de video.

[Anterior](16-entrenar-yolo-gpu.md) · [Índice](../README.md) · [Siguiente: YOLO y webcam](18-detectar-objeto-webcam-yolo.md)
