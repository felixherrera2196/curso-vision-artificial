# 14. Descargar un dataset de Roboflow

En este tutorial obtendrás el **código para descargar un dataset etiquetado** desde Roboflow. Puedes utilizar las imágenes que etiquetaste en tu proyecto o el dataset de ejemplo de Coca-Cola. Elige una de las dos opciones del paso 1; después, continúa con el paso 2.

Un **dataset** contiene las imágenes y sus etiquetas. Una **versión** es una preparación concreta de esos datos, con su división y sus ajustes. Crear una versión permite descargar el mismo conjunto después para repetir el entrenamiento.

## 1. Preparar o elegir el dataset

### Opción A. Crear una versión de tu propio dataset

Si ya subiste tus imágenes y etiquetaste los objetos que quieres detectar, abre tu proyecto en Roboflow y haz clic en **Versions**. Si todavía no tienes una versión, selecciona la opción para crear una, que puede aparecer como **Create New Version**.

Durante la preparación encontrarás cinco secciones. Revísalas en este orden:

#### 1. Source Images: revisar las imágenes

Comprueba que estén las imágenes que quieres utilizar y que sus etiquetas sean correctas. Revisa que las cajas rodeen los objetos y que los nombres de las clases sean consistentes. Por ejemplo, evita utilizar dos nombres distintos para el mismo tipo de objeto.

#### 2. Train/Test Split: dividir los datos

Haz clic en **Rebalance** para ajustar cómo se repartirán las imágenes entre tres grupos:

| Grupo | Para qué sirve | Qué ocurre si cambias su proporción |
| --- | --- | --- |
| **Train — entrenamiento** | Son las imágenes con las que el modelo aprende a reconocer los objetos. | Más imágenes variadas pueden ayudarle a aprender, pero si asignas casi todo aquí, quedarán pocas para evaluar el resultado. |
| **Valid — validación** | Permite revisar cómo funciona el modelo durante el entrenamiento con imágenes que no usa para aprender directamente. | Con muy pocas imágenes, los resultados pueden variar mucho y ser poco representativos. Aumentarlo deja menos imágenes para entrenar. |
| **Test — prueba** | Sirve para evaluar el modelo al final con imágenes reservadas que no se usaron para ajustar el entrenamiento. | Un grupo mayor puede dar una evaluación más representativa, pero reduce los datos disponibles para entrenamiento y validación. |

Como punto de partida, puedes utilizar **70 % para entrenamiento, 20 % para validación y 10 % para prueba**. No es una regla fija: lo importante es que los tres grupos tengan suficientes ejemplos y representen las clases que quieres detectar.

Evita colocar imágenes idénticas o casi iguales en grupos distintos. Por ejemplo, varias fotos consecutivas del mismo video pueden ser tan parecidas que el resultado de evaluación parezca mejor de lo que será con imágenes nuevas.

#### 3. Preprocessing: conservar los ajustes iniciales

Esta sección aplica preparaciones a las imágenes, como corregir su orientación o ajustar su tamaño. Para esta práctica, **deja los valores predeterminados**.

#### 4. Augmentation: conservar los ajustes iniciales

El aumento de datos permite generar variaciones de las imágenes de entrenamiento, por ejemplo con cambios de brillo o giros. Puede ayudar al modelo a reconocer objetos en distintas condiciones. Por ahora, **deja esta sección como está**, sin agregar transformaciones.

#### 5. Create: generar la versión

Conserva las opciones predeterminadas de esta sección y haz clic en **Create**. Espera a que Roboflow termine de generar la versión.

Ya tienes una versión preparada de tu dataset. Ábrela si es necesario y haz clic en **Download Dataset**. Continúa con el paso 2.

### Opción B. Utilizar el dataset de ejemplo de Coca-Cola

Si todavía no has etiquetado tus propias imágenes, puedes practicar con un dataset público que ya contiene anotaciones:

[Dataset de Coca-Cola en Roboflow Universe](https://universe.roboflow.com/objdetection-j3gr3/cocacola-mchfa/dataset/1)

1. Abre el enlace y haz clic en **Dataset**.
2. Selecciona la versión que utilizarás, si la página te lo solicita.
3. Haz clic en **Download Dataset**.
4. Si aparece una ventana con distintas formas de utilizar los datos, selecciona la última opción, **Download Dataset**, y pulsa **Continue**.

Si Roboflow solicita iniciar sesión, utiliza tu cuenta para continuar. Los nombres o el orden de algunas opciones pueden variar según la interfaz.

Lo que obtendrás son **imágenes etiquetadas para entrenar**, no un modelo que ya detecte objetos. El entrenamiento lo realizaremos más adelante.

## 2. Obtener el código de descarga

Desde la ventana de descarga del dataset que elegiste:

1. En **Image and Annotation Format**, selecciona **YOLOv11**. Este formato organiza las imágenes y las anotaciones para el entrenamiento con YOLO que utilizaremos en el curso.
2. En **Download Options**, selecciona **Show Download Code**.
3. Haz clic en **Continue**.
4. Roboflow mostrará un bloque de código. Cópialo y guárdalo temporalmente para utilizarlo después en tu Jupyter Notebook de Google Colab.

Para el dataset de ejemplo, el código tendrá una estructura similar a esta:

```python
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="TU_API_KEY")
project = rf.workspace("objdetection-j3gr3").project("cocacola-mchfa")
version = project.version(1)
dataset = version.download("yolov11")
```

**Copia el código que genere Roboflow para tu dataset.** La clave, el espacio de trabajo, el proyecto y el número de versión pueden ser distintos de los del ejemplo. Si seleccionaste otra versión, conserva el número que aparezca en tu código.

### ¿Qué hace cada parte?

- **`!pip install roboflow`** instala la biblioteca de Roboflow en el entorno del notebook. El signo `!` permite ejecutar un comando de terminal desde una celda.
- **`from roboflow import Roboflow`** importa la herramienta que se comunica con Roboflow.
- **`api_key`** es la clave que autoriza el acceso desde el código. `TU_API_KEY` es un marcador de ejemplo: el código real debe utilizar tu clave. No la publiques en GitHub ni en capturas compartidas.
- **`workspace(...).project(...)`** identifica el espacio de trabajo y el proyecto que contienen los datos.
- **`project.version(1)`** selecciona la versión del dataset que se descargará; en el ejemplo, la versión 1.
- **`version.download("yolov11")`** descarga las imágenes, sus etiquetas y la configuración en el formato seleccionado. La variable `dataset` permite consultar información sobre esa descarga.

**El código no es el dataset en sí: son las instrucciones para descargarlo.** Los archivos se descargarán cuando lo ejecutes en el notebook. Si utilizas Google Colab, quedarán en el almacenamiento de la sesión de Colab, no en la carpeta Descargas de tu computadora.

## 3. Guardar el código para el entrenamiento

Por ahora, conserva el bloque de descarga en una nota privada. Más adelante lo pegarás en una celda de código del notebook y lo ejecutarás después de preparar el entorno.

Cuando lo ejecutes, obtendrás las imágenes, sus archivos de etiquetas y un archivo llamado **`data.yaml`**, que indica dónde están los datos y cuáles son las clases. Utilizaremos ese archivo para iniciar el entrenamiento.

Antes de continuar, comprueba que:

- El código corresponde al proyecto y la versión que elegiste.
- El formato de descarga es `yolov11`.
- Guardaste el bloque completo y mantuviste privada tu clave de acceso.

En los siguientes capítulos prepararemos Google Colab y utilizaremos este código para descargar los datos y entrenar el modelo.

[Anterior](13-que-es-roboflow.md) · [Índice](../README.md) · [Siguiente: Colab](15-colab-gpu-ultralytics.md)
