# 15. Google Colab + GPU + Ultralytics

## Qué aprenderás

Prepararás conceptualmente el entorno remoto de entrenamiento: notebook, paquetes, archivos, GPU y verificaciones. Comprenderás por qué elegir una GPU en la interfaz no basta para demostrar que el entrenamiento la está usando.

## La idea en palabras sencillas

Colab permite utilizar una computadora remota desde una página web. En vez de ejecutar todo en un archivo, trabajas con bloques llamados celdas. Cada celda puede contener instrucciones y mostrar resultados debajo.

La GPU es un recurso de esa computadora que puede acelerar el entrenamiento. No es la cámara ni una biblioteca de Python. Primero prepararás el notebook, luego comprobarás el recurso disponible y finalmente ejecutarás el trabajo. Lo que instalaste en tu laptop no se instala automáticamente en Colab: son dos computadoras distintas.

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

## Abrir y utilizar un notebook por primera vez

1. Entra a [Google Colab](https://colab.research.google.com/) e inicia sesión con tu cuenta de Google.
2. Abre el notebook indicado por el instructor o crea uno nuevo. Ponle un nombre que puedas reconocer después.
3. Si el notebook es compartido y necesitas conservar cambios propios, guarda una copia en tu Drive.
4. Busca **Entorno de ejecución → Cambiar tipo de entorno de ejecución**. Selecciona GPU si está disponible y guarda. Los nombres de las opciones pueden variar según el idioma y la interfaz.
5. Conecta la sesión y ejecuta las celdas de preparación en el orden de la práctica.
6. Para ejecutar una celda, pulsa su botón de reproducción o **Shift + Enter**. Espera a que termine antes de avanzar si la siguiente depende de ella.
7. Lee el resultado debajo de la celda: puede ser un mensaje, una tabla, una imagen o un error.
8. Si reinicias o cambias el entorno, vuelve a ejecutar la preparación. Que una salida vieja siga visible no significa que las variables sigan existiendo.

No necesitas pulsar muchas veces el botón de una celda que está trabajando. Una instalación o un entrenamiento puede tardar. Busca el indicador de ejecución y los mensajes de avance.

**Notebook y sesión son diferentes:** guardar el notebook conserva sus instrucciones y, según el guardado, sus salidas. No conserva automáticamente todos los archivos temporales ni el estado de la computadora remota. Copia los pesos antes de terminar.

## Orden de trabajo y ubicación de cada paso

| Acción | Dónde ocurre | Qué debes observar |
| --- | --- | --- |
| Abrir el notebook | Navegador de tu computadora. | El documento con sus celdas. |
| Ejecutar una celda | Equipo remoto de Colab. | Salida o error debajo de la celda. |
| Descargar datos desde una celda | Almacenamiento remoto de la sesión. | Carpeta del dataset en Colab. |
| Descargar pesos mediante el navegador | Transferencia del remoto a Windows. | Archivo en tu equipo al finalizar. |

**Python 3.12.10 es la versión del equipo Windows del curso.** Colab administra la versión de su entorno remoto y puede utilizar otra. No reemplaces su Python para que el número coincida: primero verifica que las bibliotecas del notebook sean compatibles con la sesión disponible.

## Si aparece un error, identifica la etapa

Si una celda no encuentra una variable, comprueba que ejecutaste la que la define. Si no encuentra un archivo, revisa dónde está descargado. Si no hay GPU disponible, revisa el acelerador asignado y las comprobaciones de la biblioteca. Un error de acceso al dataset no se corrige eligiendo otra GPU.

La selección del acelerador puede reiniciar o reemplazar la sesión. Por eso conviene configurarlo antes de preparar datos y ejecutar el entrenamiento. Si la sesión se pierde, vuelve a ejecutar la preparación en orden y no supongas que una salida guardada representa el estado actual.

## Antes de pulsar entrenar

Comprueba datos y clases, GPU disponible y utilizada, biblioteca compatible y destino de resultados. Guarda el notebook con un nombre reconocible. Espera a que termine cada paso del que dependa el siguiente.

No necesitas que cada celda sea un programa independiente: algunas preparan variables que usan las siguientes. Esta es la diferencia práctica entre ejecutar un notebook en orden y copiar una celda suelta en cualquier lugar.

## Para dar el siguiente paso

Ya tenemos entorno, datos y recursos preparados. **¿Cómo indicamos al modelo que aprenda de este dataset y cómo sabremos si mejora?** En el siguiente capítulo revisaremos el entrenamiento y sus resultados.

[Anterior](14-descargar-dataset-roboflow.md) · [Índice](../README.md) · [Siguiente: Entrenamiento](16-entrenar-yolo-gpu.md)
