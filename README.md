# Visión artificial: de OpenCV a Deep Learning con YOLO

Bienvenido al curso-taller de visión artificial. En esta guía aprenderás a trabajar con imágenes y video en Python, seleccionar colores y analizar figuras con OpenCV, y comprender el proceso de entrenamiento y uso de un detector de objetos con YOLO.

**Instructor:** M. C. Felix Alejandro Herrera Atilano.

El material sigue los **18 temas del curso**, con un archivo Markdown por tema. Puedes consultarlo antes de clase, seguirlo durante las explicaciones del instructor y utilizarlo para repasar o realizar las actividades en tu equipo.

## Qué necesitas para comenzar

- Conocimientos básicos de Python: variables, condiciones, ciclos e importación de bibliotecas.
- Una computadora con cámara web y conexión a internet.
- Python y VS Code instalados para las prácticas locales.
- Una cuenta de Google para utilizar Colab durante la preparación y el entrenamiento.
- Acceso a un proyecto de Roboflow cuando trabajes con el dataset.

Si necesitas preparar tu equipo, comienza por los tutoriales de [instalación de Python](Tutorial%20instalaci%C3%B3n%20de%20Python/Tutorial%20instalaci%C3%B3n%20de%20Python.md) e [instalación de VS Code](Tutorial%20de%20instalaci%C3%B3n%20de%20VSCode/Tutorial%20de%20instalaci%C3%B3n%20de%20VSCode.md). Después revisa el tema 03 para comprender qué bibliotecas utiliza el curso y cómo comprobar tu entorno.

## Cómo seguir la guía

1. Abre los capítulos desde el índice y avanza en orden. Cada uno explica qué aprenderás y termina con actividades o comprobaciones.
2. Relaciona las explicaciones con la práctica de clase. Identifica qué datos recibe cada operación y qué resultado produce.
3. Para ejecutar un ejemplo, copia su bloque de código en un archivo `.py`, guárdalo con el nombre sugerido y ejecútalo con el intérprete de tu proyecto.
4. Realiza las prácticas de cámara en tu computadora. Colab es un entorno remoto y no accede a la webcam mediante el mismo procedimiento local.
5. Guarda tus observaciones: parámetros, condiciones de iluminación, resultados y situaciones en las que el método falla.
6. Para YOLO, conserva también la versión del dataset, la configuración de entrenamiento y los pesos seleccionados.

Los capítulos **04 y 05** incluyen programas completos para captura de cámara y filtrado de color. Los demás capítulos ofrecen fundamentos, procedimientos y actividades para acompañar las prácticas del taller; no todos contienen un programa completo.

El taller presencial tiene una duración de cuatro horas. La guía amplía las explicaciones para que puedas consultar los detalles después de clase y repetir las actividades a tu ritmo.

## Primera parte: imágenes y OpenCV

Comenzarás con imágenes como arreglos numéricos y después utilizarás una cámara. A partir de sus fotogramas construirás máscaras de color y estudiarás cómo limpiar regiones, obtener contornos y describir figuras.

| Tema | Guía | Qué aprenderás |
| --- | --- | --- |
| 01 | [Introducción a la Visión Artificial y el Procesamiento de Imágenes](temas/01-introduccion-vision-artificial.md) | Definir una tarea y reconocer las etapas de una aplicación. |
| 02 | [¿Qué es una Imagen?](temas/02-que-es-una-imagen.md) | Interpretar píxeles, canales, dimensiones y coordenadas. |
| 03 | [Instalación de Python y bibliotecas a utilizar](temas/03-instalacion-python-bibliotecas.md) | Preparar y comprobar el entorno de trabajo. |
| 04 | [Obtener video de una cámara con Python](temas/04-video-camara-python.md) | Capturar fotogramas, mostrarlos y liberar la cámara. |
| 05 | [Filtros de color](temas/05-filtros-color.md) | Comparar BGR directo, HSV con un intervalo y HSV con dos intervalos de rojo. |
| 06 | [Modelos de color](temas/06-modelos-color.md) | Distinguir BGR, RGB, grises y HSV. |
| 07 | [Operaciones morfológicas](temas/07-operaciones-morfologicas.md) | Comprender erosión, dilatación, apertura y cierre. |
| 08 | [Contornos](temas/08-contornos.md) | Analizar fronteras, áreas, perímetros y centros. |
| 09 | [Detectar figuras](temas/09-detectar-figuras.md) | Proponer clases geométricas y reconocer los límites de las reglas. |

## Segunda parte: datos, entrenamiento y YOLO

Después estudiarás cómo preparar imágenes etiquetadas, utilizar un dataset y entrenar un detector. El recorrido termina con la descarga de los pesos y su uso local sobre video de cámara.

| Tema | Guía | Qué aprenderás |
| --- | --- | --- |
| 10 | [Introducción a Deep Learning](temas/10-introduccion-deep-learning.md) | Distinguir aprendizaje, entrenamiento e inferencia. |
| 11 | [¿Qué es un dataset?](temas/11-que-es-un-dataset.md) | Organizar datos representativos y separar entrenamiento, validación y prueba. |
| 12 | [Etiquetado y bounding boxes](temas/12-etiquetado-bounding-boxes.md) | Anotar objetos e interpretar cajas y coordenadas normalizadas. |
| 13 | [¿Qué es Roboflow?](temas/13-que-es-roboflow.md) | Relacionar proyectos, anotaciones y versiones. |
| 14 | [Descargar un dataset de Roboflow](temas/14-descargar-dataset-roboflow.md) | Verificar formato, rutas y configuración de los datos. |
| 15 | [Google Colab + GPU + Ultralytics](temas/15-colab-gpu-ultralytics.md) | Preparar el entorno remoto y comprobar la GPU. |
| 16 | [Entrenar modelo YOLO usando GPU](temas/16-entrenar-yolo-gpu.md) | Comprender parámetros, métricas y selección de pesos. |
| 17 | [Descargar YOLO entrenado para uso local](temas/17-descargar-yolo-uso-local.md) | Trasladar el modelo y comprobar su carga en tu equipo. |
| 18 | [Detectar objeto con cámara web usando YOLO](temas/18-detectar-objeto-webcam-yolo.md) | Integrar captura, predicción y visualización. |

## Actividad integradora

Durante el taller desarrollarás aplicaciones de Python para detectar colores y formas con OpenCV y utilizar un detector YOLO entrenado sobre video de cámara. Consulta las secciones correspondientes mientras completas cada etapa con el instructor.

Para documentar tus resultados, describe el objetivo, los datos utilizados, los parámetros elegidos y las condiciones de prueba. Incluye aciertos y errores: una detección que funciona con un fondo limpio puede fallar al cambiar la luz, la distancia o el entorno.

Antes de pasar de una etapa a la siguiente, comprueba su resultado por separado: primero captura de cámara, después máscara y contornos; en YOLO, primero datos y entrenamiento, después carga local y finalmente video. Este orden te ayudará a localizar los problemas.
