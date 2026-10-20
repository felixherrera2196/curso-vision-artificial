# 14. Descargar un dataset de Roboflow

En este tutorial obtendrás el **código para descargar un dataset etiquetado** desde Roboflow. Primero practicarás con el dataset de Coca-Cola, que ya está etiquetado, para aprender el flujo de descarga y entrenamiento. Después de completar esa práctica en Colab, aplicarás el mismo procedimiento a tus propias imágenes siguiendo la sección final de este capítulo.

Un **dataset** contiene las imágenes y sus etiquetas. Una **versión** es una preparación concreta de esos datos, con su división y sus ajustes. Crear una versión permite descargar el mismo conjunto después para repetir el entrenamiento.

## 1. Practicar con el dataset de Coca-Cola

Para esta primera práctica, utiliza el siguiente dataset público, que ya contiene imágenes y anotaciones. Así podrás aprender el proceso antes de preparar tus propios datos:

[Dataset de Coca-Cola en Roboflow Universe](https://universe.roboflow.com/objdetection-j3gr3/cocacola-mchfa/dataset/1)

1. Abre el enlace y haz clic en **Dataset**.
2. Comprueba que estés en la **versión 1**, incluida en el enlace.
3. Haz clic en **Download Dataset**.
4. Si aparece una ventana con distintas formas de utilizar los datos, selecciona la última opción, **Download Dataset**, y pulsa **Continue**.

Si Roboflow solicita iniciar sesión, utiliza tu cuenta para continuar. Los nombres o el orden de algunas opciones pueden variar según la interfaz.

Lo que obtendrás son **imágenes etiquetadas para entrenar**, no un modelo que ya detecte objetos. El entrenamiento lo realizaremos más adelante.

## 2. Obtener el código de descarga

Desde la ventana de descarga del dataset de Coca-Cola:

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

**Copia el código que genere Roboflow para esta versión de Coca-Cola**, con tu propia clave de acceso. Cuando después utilices tu dataset, el espacio de trabajo, el proyecto y la versión serán los de tu proyecto; conserva los valores que genere Roboflow en cada caso.

### ¿Qué hace cada parte?

- **`!pip install roboflow`** instala la biblioteca de Roboflow en el entorno del notebook. El signo `!` permite ejecutar un comando de terminal desde una celda.
- **`from roboflow import Roboflow`** importa la herramienta que se comunica con Roboflow.
- **`api_key`** es la clave que autoriza el acceso desde el código. `TU_API_KEY` es un marcador de ejemplo: el código real debe utilizar tu clave. No la publiques en GitHub ni en capturas compartidas.
- **`workspace(...).project(...)`** identifica el espacio de trabajo y el proyecto que contienen los datos.
- **`project.version(1)`** selecciona la versión del dataset que se descargará; en el ejemplo, la versión 1.
- **`version.download("yolov11")`** descarga las imágenes, sus etiquetas y la configuración en el formato seleccionado. La variable `dataset` permite consultar información sobre esa descarga.

**El código no es el dataset en sí: son las instrucciones para descargarlo.** Los archivos se descargarán cuando lo ejecutes en el notebook. Si utilizas Google Colab, quedarán en el almacenamiento de la sesión de Colab, no en la carpeta Descargas de tu computadora.

## 3. Guardar el código para el entrenamiento

Por ahora, conserva el bloque de descarga de Coca-Cola en una nota privada e identifícalo con el nombre del dataset. Más adelante lo pegarás en una celda de código del notebook y lo ejecutarás después de preparar el entorno.

Cuando lo ejecutes, obtendrás las imágenes, sus archivos de etiquetas y un archivo llamado **`data.yaml`**, que indica dónde están los datos y cuáles son las clases. Utilizaremos ese archivo para iniciar el entrenamiento.

Antes de continuar, comprueba que:

- El código corresponde al proyecto y la versión que elegiste.
- El formato de descarga es `yolov11`.
- Guardaste el bloque completo y mantuviste privada tu clave de acceso.

Continúa con el capítulo de **Google Colab** para descargar el dataset de Coca-Cola, entrenar y guardar el modelo. Al terminar esa práctica, regresa al paso 4 para repetir el proceso con tus propias imágenes.

## 4. Después de la práctica: utilizar tu propio dataset

Cuando hayas completado la práctica de Coca-Cola en Colab, vuelve a esta sección para trabajar con tus propios datos. Primero sube tus imágenes y etiqueta los objetos que quieres detectar, si aún no lo has hecho. Después, abre tu proyecto en Roboflow y haz clic en **Versions**. Si todavía no tienes una versión, selecciona la opción para crear una, que puede aparecer como **Create New Version**.

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

Ya tienes una versión preparada de tu dataset. Ábrela si es necesario y haz clic en **Download Dataset**. Repite el paso 2 para obtener su código de descarga y guárdalo por separado del código de Coca-Cola. Luego repite el tutorial de Colab con este nuevo código y con la ruta de `data.yaml` de tu dataset. Así entrenarás un modelo para tus propias clases.

[Anterior](13-que-es-roboflow.md) · [Índice](../README.md) · [Siguiente: Colab](15-colab-gpu-ultralytics.md)
