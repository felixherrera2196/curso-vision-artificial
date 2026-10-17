# 13. Roboflow y tutorial de etiquetado

## Qué es Roboflow y cómo sirve para etiquetar

**Roboflow** es una plataforma web que permite organizar imágenes y etiquetar los objetos que aparecen en ellas. En este curso la utilizaremos para subir nuestras fotografías, dibujar una **bounding box** alrededor de cada objeto y asignarle su clase.

Al terminar, podremos descargar las imágenes y sus etiquetas en **formato YOLO** para entrenar nuestro detector. La plataforma genera los archivos de etiquetas: no tendremos que escribir a mano las coordenadas de cada caja.

## Tutorial de etiquetado

Los nombres y la ubicación de los botones pueden variar según la versión de la interfaz. Sigue el orden de estos pasos y busca la opción equivalente si cambia algún texto.

### 1. Capturar las fotografías

Descarga [muestreo.py](https://raw.githubusercontent.com/felixherrera2196/curso-vision-artificial/main/ejemplos/muestreo.py), el mismo programa de captura del capítulo de datasets. Si el navegador muestra el código como texto, guárdalo con **Ctrl + S** y comprueba que el nombre termine en `.py`, no en `.txt`.

Ejecuta el archivo con el Python y OpenCV de las prácticas anteriores:

```bash
python muestreo.py
```

El programa captura fotografías automáticamente cada **0.5 segundos**. Puedes cambiar ese tiempo en `INTERVALO_SEGUNDOS`, tomar una foto adicional con **espacio** y terminar con **ESC**. Haz clic en la ventana de cámara para que reciba las teclas. Las fotografías se guardan en la carpeta indicada en `OUTPUT_DIR`.

Para esta práctica, reúne **al menos 100 imágenes variadas** como punto de partida. Si el tiempo lo permite, apunta a **unas 300 imágenes** para ampliar la colección. Un conjunto de **500 a 1000 imágenes** puede ser una meta para un proyecto más completo, pero queda fuera del objetivo inicial del curso. Estas cantidades son referencias de trabajo: **ninguna garantiza por sí sola una buena detección**.

Cambia posición, distancia, fondo e iluminación y utiliza distintos ejemplares de tus clases. Si trabajarás con varias clases, procura reunir suficientes ejemplos de cada una. Evita alcanzar la cantidad repitiendo casi la misma foto; la variedad y el etiquetado correcto importan más que acumular archivos.

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
3. Selecciona todas las imágenes de la colección que vas a etiquetar y espera a que terminen de cargarse.
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
