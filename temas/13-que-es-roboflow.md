# 13. Roboflow y tutorial de etiquetado

## Qué es Roboflow y cómo sirve para etiquetar

**Roboflow** es una plataforma web que permite organizar imágenes y etiquetar los objetos que aparecen en ellas. En este curso la utilizaremos para subir nuestras fotografías, dibujar una **bounding box** alrededor de cada objeto y asignarle su clase.

Al terminar, podremos descargar las imágenes y sus etiquetas en **formato YOLO** para entrenar nuestro detector. La plataforma genera los archivos de etiquetas: no tendremos que escribir a mano las coordenadas de cada caja.

## Tutorial de etiquetado

Los nombres y la ubicación de los botones pueden variar según la versión de la interfaz. Sigue el orden de estos pasos y busca la opción equivalente si cambia algún texto.

### 1. Preparar las imágenes de tu dataset

Utiliza **la carpeta con fotografías que creaste en el [capítulo de datasets](11-que-es-un-dataset.md)**, por ejemplo `mi_dataset_imagenes`. No necesitas descargar ni ejecutar otro programa de captura para este tutorial.

1. Localiza esa carpeta en tu computadora y abre algunas imágenes para comprobar su contenido.
2. Revisa que los objetos se vean con claridad y que haya variación de posiciones, distancias, fondos e iluminación.
3. Elimina las imágenes borrosas o dañadas y evita conservar muchas fotografías casi idénticas.
4. Conserva la carpeta a mano: en el paso 4 seleccionarás sus imágenes para subirlas a Roboflow.

Para esta práctica, parte de **al menos 100 imágenes variadas**. Si tu colección todavía no cubre las condiciones que necesitas, puedes ampliarla con el programa del capítulo de datasets. Unas **300 imágenes** son una meta para ampliar la práctica si hay tiempo; **500–1000 imágenes** pueden ser una referencia para un proyecto más completo, sin ser un requisito de este curso. Ninguna cantidad garantiza por sí sola una buena detección: importan la variedad, los ejemplos de cada clase y el etiquetado correcto.

### 2. Crear una cuenta

1. Entra a [Roboflow](https://app.roboflow.com/login).
2. Crea tu cuenta o inicia sesión si ya tienes una.
3. Entra a tu espacio de trabajo (*workspace*) para crear el proyecto.

### 3. Crear un proyecto de detección

1. Abre **Projects → New Project**.
2. En **Project Name**, escribe `custom_object_detector_yolo11` o un nombre que identifique tu práctica.
3. En **Project Type**, selecciona **Object Detection**: utilizaremos cajas para localizar los objetos.
4. Pulsa **Create Public Project**. Esta opción crea un proyecto público; utiliza imágenes que puedas compartir públicamente.

### 4. Subir las imágenes

1. Abre la sección para cargar imágenes del proyecto, normalmente **Upload Data**.
2. Asigna un nombre al **batch**, es decir, al lote de imágenes. Por ejemplo, `09/29/26-1`: una fecha y un número para identificar esa sesión. Puedes usar la fecha de tu propia captura.
3. Selecciona las imágenes de la carpeta que preparaste en el capítulo de datasets y espera a que terminen de cargarse.
4. Pulsa **Save and Continue**.
5. Selecciona el modo de **etiquetado manual** cuando la plataforma te pregunte cómo quieres anotarlas.

### 5. Definir las clases y etiquetar

1. En **Classes and Tags**, escribe los nombres de las clases separados por comas, por ejemplo `vaso, botella`, y pulsa **Add Classes**.
2. Entra a **Annotate**, selecciona el lote que subiste y pulsa **Start Annotating**.
3. Abre una imagen y dibuja una caja ajustada alrededor de un objeto de interés.
4. Asigna la clase correspondiente a esa caja.
5. Repite con **todos los objetos de las clases del proyecto** que aparezcan en la imagen. Si hay dos vasos y una botella, debes dibujar tres cajas.
6. Guarda la anotación y continúa con las demás imágenes hasta terminar el lote.

Antes de continuar, revisa algunas imágenes: las cajas deben rodear los objetos y tener la clase correcta. Si encuentras errores, corrígelos antes de generar el dataset.

### 6. Agregar las imágenes al dataset

1. Con el lote etiquetado, selecciona **Add Images to Dataset**.
2. En **Method**, busca la opción para distribuir imágenes entre **Train, Valid y Test**; puede aparecer como **Split Images Between Train/Valid/Test**.
3. Define el reparto indicado por el instructor. **Train** se usa para aprender, **Valid** para revisar el modelo durante su desarrollo y **Test** para evaluarlo al final.
4. Pulsa **Add Images**.

Si capturaste secuencias de fotos casi idénticas, mantenlas en la misma división. Cuando tengas varias sesiones, sepáralas por sesión para evitar evaluar con imágenes casi iguales a las de entrenamiento.

### 7. Crear una versión

1. Abre **Versions** y comienza la creación de una nueva versión, con **Create New Version** o la opción equivalente.
2. Revisa el preprocesamiento y pulsa **Continue**.
3. Revisa los aumentos de datos y pulsa **Continue**. Para esta primera práctica, conserva los ajustes indicados por el instructor; no necesitas agregar transformaciones para completar el etiquetado.
4. Revisa el resumen, pulsa **Create** y espera a que termine la generación.

Una versión es una preparación del dataset lista para descargar. Si después corriges etiquetas, genera una nueva versión que incluya esas correcciones.

### 8. Descargar en formato YOLO

1. En **Versions**, abre la versión que acabas de crear.
2. Pulsa **Download Dataset**.
3. Selecciona el formato **YOLOv11**, correspondiente al flujo de detección del curso. Si la interfaz muestra **YOLO11** u otra denominación, comprueba que sea el formato de detección compatible con YOLO11 y Ultralytics.
4. Descarga el archivo comprimido a tu computadora y extráelo en una carpeta que puedas localizar.

Al terminar tendrás tus fotografías y sus etiquetas en formato YOLO. En el [siguiente capítulo](14-descargar-dataset-roboflow.md) revisaremos los archivos descargados antes de utilizarlos para entrenar.

[Anterior](12-etiquetado-bounding-boxes.md) · [Índice](../README.md) · [Siguiente: Descargar dataset](14-descargar-dataset-roboflow.md)
