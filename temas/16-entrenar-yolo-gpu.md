# 16. Entrenar modelo YOLO usando GPU

## Entrenaremos con nuestro propio dataset

En esta práctica entrenaremos **YOLO con el dataset que preparaste y obtuviste de Roboflow**: tus fotografías y las etiquetas que indican qué objetos aparecen y dónde están. Durante el entrenamiento, el modelo utilizará esos ejemplos para ajustar sus parámetros y aprender a detectar las clases de tu proyecto.

Para entrenar utilizaremos **Google Colab**, que permite ejecutar código desde el navegador en una computadora remota y puede proporcionarnos una **GPU**. El entrenamiento se realizará en los recursos de Colab, por lo que no necesitas tener una tarjeta gráfica dedicada en tu computadora. La asignación de GPU depende de su disponibilidad; comprobaremos que esté activa antes de empezar.

### ¿Por qué utilizamos una GPU?

Para una computadora, una imagen es un conjunto de números organizado en **matrices**: cada posición representa un píxel y una imagen de color suele tener tres canales. Por ejemplo, una imagen de 640 × 480 píxeles tiene 307 200 posiciones y, con tres canales, contiene 921 600 valores.

Al entrenar, la red realiza muchísimas operaciones con esos números y con sus parámetros: procesa las imágenes, compara sus predicciones con las etiquetas y calcula cómo ajustar lo aprendido. Este trabajo se repite con muchos ejemplos durante varias vueltas de entrenamiento.

Una **GPU** puede realizar muchas de estas operaciones en paralelo, lo que suele acelerar considerablemente el entrenamiento frente a una CPU. **La GPU no hace que el modelo aprenda mejor por sí sola: permite realizar los cálculos más rápido.** La calidad del resultado sigue dependiendo de las imágenes, las etiquetas y la configuración del entrenamiento.

## Pasos para entrenar en Google Colab

### Paso 1. Abrir sesión y crear un Jupyter Notebook en Google Colab

1. Entra a [Google Colab](https://colab.research.google.com/) e inicia sesión con tu **cuenta de Google**, solicitada en los requisitos obligatorios del curso.
2. Haz clic en **Nuevo Notebook** o **Nuevo cuaderno**, según el idioma de la interfaz. Colab creará un cuaderno de Jupyter Notebook.
3. En la parte superior, haz clic en el nombre inicial, normalmente `Untitled0.ipynb`, y cámbialo por uno que identifique tu práctica, por ejemplo **`curso.ipynb`**. Conserva la extensión **`.ipynb`**, que identifica este tipo de cuaderno.

Si no ves el encabezado donde aparece el nombre, utiliza la flecha de la esquina superior derecha para desplegarlo. Su orientación puede cambiar según esté oculto o visible.

Un notebook permite escribir y ejecutar código Python por bloques llamados **celdas**. Esto facilita experimentar: puedes ejecutar una parte, observar el resultado y continuar con la siguiente sin ejecutar todo el programa de nuevo.

En una celda de código escribe:

```python
x = "curso vision"
print(x)
```

Ejecuta la celda con el botón **▶** situado a su izquierda o con **Shift + Enter**. Debajo aparecerá:

```text
curso vision
```

Las celdas comparten variables mientras se conserve la sesión. Ejecútalas en orden: si una celda utiliza una variable creada en otra, primero debes ejecutar la que la define.

### Paso 2. Activar la GPU

En el menú del notebook, sigue esta ruta:

**Entorno de ejecución → Cambiar tipo de entorno de ejecución → Acelerador por hardware → GPU → Guardar**.

Según la versión de Colab, puede aparecer un modelo concreto, como **T4 GPU**, en lugar de una opción llamada solo «GPU». Selecciona la GPU disponible para la práctica y guarda el cambio. La asignación depende de la disponibilidad y de los límites de tu cuenta.

Haz este cambio antes de preparar los datos y entrenar, porque puede reiniciar o reemplazar la sesión. A continuación comprobaremos que la GPU esté realmente disponible.

### Paso 3. Comprobar que Colab asignó una GPU

Crea una celda de código con **+ Código**, copia el siguiente bloque y ejecútalo:

```python
import torch

print("CUDA disponible:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("CUDA:", torch.version.cuda)
else:
    print("No hay GPU disponible")
```

`torch` es PyTorch, la biblioteca de cálculo que utiliza Ultralytics para trabajar con YOLO. **CUDA** permite utilizar las GPU NVIDIA para estos cálculos.

Si aparece **`CUDA disponible: True`**, PyTorch puede utilizar una GPU. También verás su nombre y la versión de CUDA con la que se compiló PyTorch; esta última no es necesariamente la versión del controlador de la GPU.

Si aparece **`CUDA disponible: False`** y «No hay GPU disponible», vuelve al paso 2 y comprueba el acelerador seleccionado. Si Colab no puede asignarte una GPU, espera a que haya disponibilidad o sigue las indicaciones del instructor antes de continuar con el entrenamiento. Elegir GPU en el menú no basta: esta celda confirma que PyTorch puede acceder a ella.

### Paso 4. Instalar Roboflow

Agrega una nueva celda con **+ Código**, escribe el siguiente comando y ejecútalo:

```python
!pip install roboflow
```

Este comando instala la biblioteca de Roboflow en la sesión de Colab. La utilizaremos para descargar nuestro dataset desde el notebook. El signo `!` permite ejecutar un comando de terminal dentro de una celda.

Espera a que termine la instalación antes de ejecutar la siguiente celda. Si Colab crea una nueva sesión, puede ser necesario volver a instalarla.

### Paso 5. Descargar tu dataset desde Roboflow

En una nueva celda, pega y ejecuta el **código de descarga de tu dataset**, que aprendiste a obtener en el capítulo anterior. Tendrá una estructura como esta, con tus propios datos:

```python
from roboflow import Roboflow

rf = Roboflow(api_key="TU_API_KEY")
project = rf.workspace("TU_WORKSPACE").project("TU_PROYECTO")
version = project.version(1)
dataset = version.download("yolov11")
```

Espera a que termine la descarga antes de continuar.

### Paso 6. Indicar la ruta de `data.yaml`

Al terminar de ejecutar la celda de descarga, los archivos de tu dataset aparecerán en el panel **Archivos**, a la izquierda de Colab. Ábrelo con el icono de carpeta y, si todavía no ves los archivos, pulsa **Actualizar**.

Busca `data.yaml` dentro de la carpeta del dataset descargado. Suele estar directamente en esa carpeta, junto a las carpetas de imágenes de entrenamiento, validación y prueba. La descarga normalmente queda dentro de `/content/`, en una carpeta cuyo nombre identifica el proyecto y la versión.

El archivo **`data.yaml`** indica dónde están las imágenes y cuáles son las clases del dataset. Para utilizarlo en el entrenamiento necesitamos su ruta completa:

1. Localiza `data.yaml` en el panel de archivos.
2. Haz clic en los **tres puntos** que aparecen a la derecha del archivo.
3. Selecciona **Copiar ruta de acceso**.
4. En una nueva celda, pega esa ruta entre comillas y guárdala en `data_path`.

Por ejemplo:

```python
data_path = "/content/mi_detector_objetos-1/data.yaml"
```

**Utiliza la ruta de tu propio proyecto**, no la del ejemplo. Ejecuta la celda para guardar esa dirección en la variable `data_path`; la usaremos al iniciar el entrenamiento.

### Paso 7. Instalar Ultralytics

En una nueva celda, ejecuta:

```python
!pip install -q ultralytics
```

Este comando instala **Ultralytics**, la biblioteca que utilizaremos para cargar YOLO y entrenarlo con nuestro dataset. La opción `-q` reduce los mensajes de la instalación. Espera a que termine antes de continuar.

### Paso 8. Cargar el modelo YOLO

En una nueva celda, escribe y ejecuta:

```python
from ultralytics import YOLO
model = YOLO("yolo11s.pt")
```

La primera línea importa la herramienta `YOLO` de Ultralytics. La segunda carga **YOLO11s**, la variante pequeña (*small*) de YOLO11, y guarda el modelo en la variable `model`.

El archivo `yolo11s.pt` contiene **pesos preentrenados**: parámetros que el modelo ya aprendió con otro conjunto de imágenes. Los utilizaremos como punto de partida para entrenar con nuestras propias clases, en lugar de comenzar desde cero. Si el archivo no está disponible en Colab, Ultralytics lo descargará automáticamente; espera a que termine.

**Esta celda carga el modelo, pero todavía no lo entrena con tu dataset.** Ese será el siguiente paso.

### Paso 9. Entrenar el modelo

En una nueva celda, ejecuta:

```python
results = model.train(data=data_path, epochs=15, imgsz=640)
```

- **`data=data_path`**: utiliza la ruta de tu archivo `data.yaml`, que indica las imágenes y las clases de tu dataset.
- **`epochs=15`**: realiza 15 vueltas de entrenamiento sobre el conjunto de imágenes destinado a entrenar.
- **`imgsz=640`**: establece 640 píxeles como tamaño de referencia para preparar las imágenes de entrada al modelo. No modifica tus archivos originales.

Espera a que termine el entrenamiento antes de continuar con la descarga del modelo.

[Anterior](15-colab-gpu-ultralytics.md) · [Índice](../README.md) · [Siguiente: Descargar el modelo](17-descargar-yolo-uso-local.md)
