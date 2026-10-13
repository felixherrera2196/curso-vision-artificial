# 15. Google Colab + GPU + Ultralytics

## Qué aprenderás

Prepararás conceptualmente el entorno remoto de entrenamiento: notebook, paquetes, archivos, GPU y verificaciones. Comprenderás por qué elegir una GPU en la interfaz no basta para demostrar que el entrenamiento la está usando.

## 1. Qué es Google Colab

Colab permite ejecutar notebooks desde el navegador en un entorno remoto. Un notebook combina celdas de texto, que documentan el proceso, con celdas ejecutables. Las celdas comparten variables y archivos mientras conservas la sesión.

El orden de ejecución importa. Si ejecutas una celda que usa una variable antes de la celda que la define, el programa falla aunque ambas aparezcan escritas en el notebook. Para revisar que el proceso sea reproducible, utiliza una sesión limpia y ejecuta de arriba hacia abajo.

## 2. Elegir y comprobar la GPU

En la configuración del entorno de ejecución puedes solicitar un acelerador GPU. Su disponibilidad y tipo pueden variar. Colab puede tener límites de uso o no asignar el recurso en un momento determinado.

Debes comprobar tres cosas: que la sesión tenga GPU asignada, que la biblioteca de cómputo pueda verla y que el entrenamiento utilice ese dispositivo. PyTorch, utilizado por Ultralytics, proporciona mecanismos como `torch.cuda.is_available()` para revisar disponibilidad CUDA en las configuraciones NVIDIA habituales.

Un resultado negativo no se corrige únicamente cambiando un argumento del entrenamiento. Puede significar que no se asignó GPU o que la instalación no tiene el soporte necesario. Primero identifica el nivel que falla.

## 3. Qué instala Ultralytics

Ultralytics proporciona una interfaz para cargar, entrenar, validar y usar modelos compatibles. El paquete también requiere otras bibliotecas. La instalación puede descargar dependencias y tardar más que un paquete pequeño.

Para reproducir el curso, registra la versión de Ultralytics y de las dependencias relevantes, especialmente PyTorch y Python. No necesitas actualizar todo en cada celda. Si cambias una biblioteca ya cargada, puede ser necesario reiniciar la sesión para que el intérprete utilice la versión nueva.

La familia o versión del modelo debe corresponder al archivo de pesos y a la API del ejemplo. Un nombre de modelo válido en un tutorial no es universal para cualquier instalación.

## 4. Archivos remotos y persistencia

La sesión tiene su propio sistema de archivos. Subir una imagen desde tu laptop crea una copia remota; escribir un nombre de archivo local de Windows en una celda no lo hace disponible.

Las carpetas temporales de Colab pueden desaparecer cuando termina o se reinicia el entorno. Google Drive puede utilizarse para guardar artefactos persistentes, pero debe montarse y sus rutas deben comprobarse. Guardar en Drive y descargar a la laptop son acciones distintas.

Antes de entrenar, decide dónde quedarán dataset, resultados y pesos. La estrategia puede ser entrenar en almacenamiento temporal y copiar resultados después, pero necesitas hacerlo antes de perder la sesión.

## 5. Colab no es el escritorio de tu computadora

Las funciones de ventana de OpenCV no funcionan igual que en un programa local. Tampoco puedes asumir que `VideoCapture(0)` accede a la webcam del navegador. Para el flujo de este curso, Colab prepara y entrena; la aplicación de cámara se ejecuta localmente después.

Esto evita mezclar un problema de acceso remoto a la cámara con un problema del detector. Primero obtendremos un modelo y verificaremos predicciones sobre imágenes; después usaremos el dispositivo físico local.

## 6. Orden recomendado del notebook

1. Documentar objetivo, clases y versión de los datos.
2. Comprobar GPU y entorno.
3. Instalar o verificar las bibliotecas necesarias.
4. Descargar o copiar el dataset.
5. Revisar YAML e imágenes anotadas.
6. Cargar el modelo inicial.
7. Entrenar y revisar resultados.
8. Validar el modelo seleccionado.
9. Guardar y descargar los pesos y la configuración.

Las rutas y variables definidas en un paso se usan en los siguientes. Mantener ese orden facilita identificar dónde se produjo un fallo.

## Actividad de comprensión

Explica qué perderías al reiniciar la sesión: variables, archivos temporales y bibliotecas instaladas durante la sesión pueden requerir preparación nuevamente. Distingue esos recursos del notebook guardado y de los archivos que ya conservaste en almacenamiento persistente.

## Comprobación del entorno

Antes de iniciar el entrenamiento, confirma la disponibilidad de GPU, la versión de Ultralytics y la ruta del dataset. Ejecuta las celdas en orden desde una sesión limpia y comprueba que las variables y archivos requeridos existan. Decide también dónde guardarás los pesos al terminar.

[Anterior](14-descargar-dataset-roboflow.md) · [Índice](../README.md) · [Siguiente: Entrenamiento](16-entrenar-yolo-gpu.md)
