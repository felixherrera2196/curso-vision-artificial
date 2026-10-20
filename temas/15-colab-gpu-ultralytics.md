# 15. Entrenar y descargar un modelo YOLO con GPU en Google Colab

En esta práctica crearás un notebook en Google Colab, descargarás tu dataset de Roboflow y entrenarás un modelo YOLO con GPU. Al terminar, descargarás **`best.pt`** para utilizar tu modelo en tu computadora.

Colab ejecuta el código en una computadora remota. Su GPU permite acelerar los cálculos del entrenamiento; no necesitas tener una GPU dedicada en tu equipo. Su disponibilidad depende de los recursos y los límites de tu cuenta.

## Paso 1. Iniciar sesión y crear un Jupyter Notebook

1. Entra a [Google Colab](https://colab.research.google.com/).
2. Inicia sesión con tu **cuenta de Google**, solicitada en los requisitos obligatorios del curso.
3. Haz clic en **Nuevo Notebook** o **Nuevo cuaderno**, según el idioma de la interfaz.
4. En la parte superior, haz clic en el nombre inicial, normalmente `Untitled0.ipynb`, y cámbialo por **`curso.ipynb`**, por ejemplo. Conserva la extensión **`.ipynb`**, que identifica los cuadernos de Jupyter.

Si no aparece el encabezado donde se cambia el nombre, utiliza la flecha de la esquina superior derecha para desplegarlo. Su orientación puede variar según esté oculto o visible.

Un notebook permite escribir y ejecutar Python por bloques llamados **celdas**. Esto facilita experimentar: puedes ejecutar una parte, ver su resultado y continuar con la siguiente.

En una celda de código, escribe:

```python
x = "curso vision"
print(x)
```

Ejecuta la celda con el botón **▶** situado a su izquierda o con **Shift + Enter**. Debajo aparecerá:

```text
curso vision
```

Para agregar las siguientes celdas, utiliza **+ Código**. Ejecútalas en orden y espera a que termine cada una antes de continuar: las variables creadas en una celda se utilizan en las siguientes.

## Paso 2. Activar la GPU

En el menú del notebook, sigue esta ruta:

**Entorno de ejecución → Cambiar tipo de entorno de ejecución → Acelerador por hardware → GPU → Guardar**.

Según la interfaz, puede aparecer una opción concreta como **T4 GPU**. Selecciona la GPU disponible para la práctica. Si Colab solicita conectar la sesión, pulsa **Conectar**.

Haz este cambio antes de descargar los datos: cambiar el entorno puede reiniciar la sesión.

## Paso 3. Comprobar que Colab asignó una GPU

En una nueva celda, copia y ejecuta:

```python
import torch

print("CUDA disponible:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("CUDA:", torch.version.cuda)
else:
    print("No hay GPU disponible")
```

La salida puede ser similar a esta:

```text
CUDA disponible: True
GPU: Tesla T4
CUDA: 12.6
```

**El nombre de la GPU y la versión de CUDA pueden ser distintos.** Lo que debes comprobar es que aparezca **`CUDA disponible: True`**. PyTorch, la biblioteca de cálculo utilizada por YOLO, puede acceder a la GPU. CUDA permite realizar estos cálculos en las GPU NVIDIA; `torch.version.cuda` indica la versión con la que se compiló PyTorch.

Si aparece `False`, revisa la configuración del paso 2. Si Colab no puede asignarte una GPU, espera a que haya disponibilidad antes de continuar con este entrenamiento.

## Paso 4. Instalar Roboflow y descargar el dataset

Pega en una nueva celda el **código de descarga que guardaste en el capítulo anterior**. Incluye la instalación de Roboflow y ejecútalo completo:

```python
!pip install roboflow

from roboflow import Roboflow

rf = Roboflow(api_key="TU_API_KEY")
project = rf.workspace("objdetection-j3gr3").project("cocacola-mchfa")
version = project.version(1)
dataset = version.download("yolov11")
```

Este ejemplo corresponde al dataset público de Coca-Cola de la práctica. **Utiliza el código generado por Roboflow para el dataset que elegiste**, con tu clave de acceso y los identificadores correctos. `TU_API_KEY` es un marcador que debes sustituir; mantén tu clave privada cuando compartas el notebook.

`!pip install roboflow` instala la biblioteca en la sesión y `version.download("yolov11")` descarga las imágenes, las etiquetas y la configuración del dataset. Espera a que termine antes de avanzar.

Los archivos quedarán en **Colab**, no en la carpeta Descargas de tu computadora.

## Paso 5. Indicar la ruta de `data.yaml`

El archivo **`data.yaml`** indica dónde están las imágenes de entrenamiento, validación y prueba, y cuáles son las clases que aprenderá el modelo.

1. Abre el panel **Archivos**, a la izquierda de Colab, con el icono de carpeta.
2. Pulsa **Actualizar** si todavía no aparecen los datos descargados.
3. Busca `data.yaml` dentro de la carpeta del dataset, normalmente en `/content/nombre-del-proyecto/`.
4. Haz clic en los **tres puntos** a la derecha de `data.yaml` y selecciona **Copiar ruta de acceso**.
5. En una nueva celda, guarda esa ruta entre comillas en la variable `data_path` y ejecuta la celda.

Por ejemplo, si esa es la ubicación real de tu archivo:

```python
data_path = "/content/CocaCola-1/data.yaml"
```

**Sustituye la ruta del ejemplo por la que copiaste de tu sesión.** El nombre de la carpeta depende del proyecto y de su versión. No utilices una ruta de Windows: el entrenamiento se ejecutará en el sistema de archivos de Colab.

## Paso 6. Instalar Ultralytics

En una nueva celda, ejecuta:

```python
!pip install -q ultralytics
```

**Ultralytics** es la biblioteca que utilizaremos para cargar y entrenar YOLO. La opción `-q` reduce los mensajes de instalación. Espera a que termine.

## Paso 7. Cargar el modelo inicial

En una nueva celda, ejecuta:

```python
from ultralytics import YOLO

model = YOLO("yolo11s.pt")
```

La primera línea importa `YOLO`. La segunda carga **YOLO11s**, la variante pequeña (*small*) de YOLO11, y la guarda en la variable `model`.

`yolo11s.pt` contiene **pesos preentrenados**, es decir, parámetros aprendidos previamente con otras imágenes. Los usaremos como punto de partida para aprender las clases de nuestro dataset. Si el archivo no existe en la sesión, Ultralytics lo descargará automáticamente.

Esta celda prepara el modelo; el entrenamiento con tus imágenes comienza en el siguiente paso.

## Paso 8. Entrenar el modelo con GPU

En una nueva celda, ejecuta:

```python
results = model.train(
    data=data_path,
    epochs=30,
    imgsz=640,
    device=0
)
```

- **`data=data_path`** utiliza el archivo `data.yaml` que localizaste.
- **`epochs=30`** realiza 30 vueltas de entrenamiento sobre las imágenes destinadas a aprender. Más épocas requieren más tiempo y no garantizan un mejor resultado.
- **`imgsz=640`** establece 640 píxeles como tamaño de referencia de entrada. No modifica tus archivos originales.
- **`device=0`** selecciona la primera GPU visible para PyTorch. Utilízalo después de comprobar que CUDA está disponible.

Al comenzar, revisa que la salida del entrenamiento indique un dispositivo **CUDA** y el nombre de la GPU. Verás el avance de las épocas y resultados de validación, que permiten evaluar el modelo con imágenes que no utiliza para ajustar directamente sus parámetros.

Espera a que terminen las **30 épocas**. El tiempo depende de la GPU, la cantidad de imágenes y el modelo. Evita volver a ejecutar la celda mientras esté trabajando. Si aparece un error, resuélvelo antes de continuar; comprueba especialmente la ruta de `data.yaml` y la disponibilidad de GPU.

## Paso 9. Descargar el modelo entrenado: `best.pt`

Al finalizar, Ultralytics mostrará la carpeta donde guardó los resultados. El archivo **`best.pt`** contiene los pesos seleccionados por su mejor desempeño en validación durante el entrenamiento.

1. Abre el panel **Archivos** de Colab y pulsa **Actualizar**.
2. Busca la carpeta de resultados indicada al finalizar. Normalmente está en **`/content/runs/detect/train/`**.
3. Abre la subcarpeta **`weights`** y localiza **`best.pt`**. Su ruta habitual es:

   ```text
   /content/runs/detect/train/weights/best.pt
   ```

4. Haz clic en los **tres puntos** a la derecha de `best.pt` y selecciona **Descargar**.
5. Espera a que termine la descarga y guarda el archivo en la carpeta del proyecto de tu computadora.

Si realizaste varios entrenamientos, la carpeta puede llamarse `train2`, `train3`, etc. Descarga el `best.pt` correspondiente al entrenamiento que quieres conservar. `last.pt`, si aparece junto a él, corresponde a la última época y puede ser distinto del mejor modelo.

**Descarga `best.pt` antes de terminar la sesión de Colab**, porque sus archivos temporales pueden perderse. Guardar el notebook conserva el código, pero no guarda automáticamente el modelo entrenado en tu computadora.

Al terminar tendrás tu notebook **`curso.ipynb`** y el archivo **`best.pt`** descargado. Este último es el modelo que utilizaremos después para detectar objetos desde nuestra computadora.

[Anterior](14-descargar-dataset-roboflow.md) · [Índice](../README.md) · [Siguiente: Entrenamiento](16-entrenar-yolo-gpu.md)
