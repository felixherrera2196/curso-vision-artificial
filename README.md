
# Visión artificial: de OpenCV a Deep Learning con YOLO

Curso de Felix Alejandro Herrera Atilano. Estas notas desarrollan los **18 temas**, en el orden del PDF **«Temario - Felix Herrera.pdf»**, con un archivo Markdown por tema.

El material está pensado para estudiantes que comienzan en visión artificial y tienen conocimientos básicos de Python. Incluye fundamentos, procedimientos, límites de los métodos, errores frecuentes y actividades de comprensión. Su lectura detallada puede requerir más tiempo que las cuatro horas del taller presencial: sirve también como material de consulta y repaso.

## Estado del material y procedencia de los códigos

La explicación conceptual de los 18 temas está redactada. La integración de ejemplos está **en proceso**: el capítulo 04 contiene el código de cámara proporcionado por el usuario, y el capítulo 05 incluye primero un filtro directo en BGR creado a petición del usuario y después sus códigos originales en HSV con uno y dos intervalos, con una explicación de la circularidad del tono y la unión de máscaras mediante OR. Los códigos recibidos se conservan sin modificar y se explican por bloques. Los demás ejemplos se incorporarán conforme el usuario los comparta.

El enlace indicado como fuente es [la conversación compartida de ChatGPT](https://chatgpt.com/share/6ace9421-a6a0-83e8-a2fe-1e69ed3e6a18), titulada «Sugerencia de curso YOLO». La consulta disponible no mostró sus mensajes ni sus bloques de código. Por eso no se atribuyen ejemplos nuevos a esa conversación. Las adaptaciones solicitadas por el usuario se identifican como tales. El usuario está proporcionando los códigos directamente, uno por uno.

El PDF se utiliza como fuente del temario y del objetivo docente. Las explicaciones amplían esos temas; no se presentan como una transcripción del PDF. El contenido de los documentos se trata como material de referencia, separado de las instrucciones del usuario.

## Cómo utilizar estas notas

1. Revisa la instalación de Python y del editor antes de las prácticas.
2. Sigue los temas en el orden del índice, aunque puedes regresar a una explicación cuando la necesites.
3. Distingue las actividades conceptuales de los ejemplos ejecutables: algunos capítulos todavía no tienen código.
4. Ejecuta las prácticas de cámara en una computadora local con webcam y escritorio gráfico.
5. Utiliza Colab para preparar y entrenar; descarga después los pesos para la aplicación local.
6. Registra datos, versiones, parámetros y resultados para que tu experimento pueda repetirse.

## Índice: primera parte, OpenCV

| Tema del PDF | Archivo | Ejemplo original |
| --- | --- | --- |
| Introducción a la Visión Artificial y el Procesamiento de Imágenes. | [01. Introducción](temas/01-introduccion-vision-artificial.md) | Tema conceptual. |
| ¿Qué es una Imagen? | [02. Imagen digital](temas/02-que-es-una-imagen.md) | Pendiente, si existe en la conversación. |
| Instalación de Python y bibliotecas a utilizar (OpenCV y Roboflow). | [03. Instalación](temas/03-instalacion-python-bibliotecas.md) | Pendiente de comandos originales. |
| Obtener video de una cámara con Python | [04. Captura de cámara](temas/04-video-camara-python.md) | Incorporado y explicado. |
| Filtros de color | [05. Filtros de color](temas/05-filtros-color.md) | BGR didáctico y HSV original con uno y dos intervalos, explicados y comparados. |
| Modelos de color | [06. Modelos de color](temas/06-modelos-color.md) | Pendiente. |
| Operaciones morfológicas | [07. Morfología](temas/07-operaciones-morfologicas.md) | Pendiente. |
| Contornos | [08. Contornos](temas/08-contornos.md) | Pendiente. |
| Detectar figuras | [09. Figuras geométricas](temas/09-detectar-figuras.md) | Pendiente. |

## Índice: segunda parte, datos y YOLO

| Tema del PDF | Archivo | Ejemplo original |
| --- | --- | --- |
| Introducción a Deep Learning | [10. Deep Learning](temas/10-introduccion-deep-learning.md) | Tema conceptual. |
| ¿Qué es un dataset? | [11. Dataset](temas/11-que-es-un-dataset.md) | Tema conceptual. |
| Etiquetado y bounding boxes | [12. Anotaciones y cajas](temas/12-etiquetado-bounding-boxes.md) | Pendiente, si hay código original. |
| ¿Qué es Roboflow? | [13. Roboflow](temas/13-que-es-roboflow.md) | Pendiente, si hay ejemplo original. |
| Descargar un dataset de Roboflow | [14. Descarga de datos](temas/14-descargar-dataset-roboflow.md) | Pendiente. |
| Google Colab + GPU + Ultralytics | [15. Preparación de Colab](temas/15-colab-gpu-ultralytics.md) | Pendiente. |
| Entrenar modelo YOLO usando GPU | [16. Entrenamiento](temas/16-entrenar-yolo-gpu.md) | Pendiente. |
| Descargar YOLO entrenado para uso local | [17. Traslado del modelo](temas/17-descargar-yolo-uso-local.md) | Pendiente. |
| Detectar objeto con cámara web usando YOLO | [18. Detección por webcam](temas/18-detectar-objeto-webcam-yolo.md) | Pendiente. |

## Tutoriales de instalación existentes

- [Instalación de Python](Tutorial%20instalaci%C3%B3n%20de%20Python/Tutorial%20instalaci%C3%B3n%20de%20Python.md).
- [Instalación de VS Code](Tutorial%20de%20instalaci%C3%B3n%20de%20VSCode/Tutorial%20de%20instalaci%C3%B3n%20de%20VSCode.md).

Estos tutoriales ya estaban en el proyecto. No se modificaron ni se presentan como códigos recuperados de la conversación.

## Actividad práctica del temario

El recorrido termina en dos resultados: una aplicación de OpenCV para detectar colores y formas mediante una webcam, y un detector YOLO entrenado que se usa localmente sobre video de cámara.

Para documentar tu práctica, explica el objetivo de cada aplicación, cómo se preparan los datos, qué parámetros utilizas, cómo se sale del programa y en qué condiciones funciona o falla. En YOLO conserva también la versión del dataset, el archivo de pesos seleccionado y las métricas de evaluación.

## Verificación realizada y límites

Se comprobó la correspondencia de los 18 capítulos con el temario, la resolución de los enlaces locales y la sintaxis de Python de los códigos incorporados. La captura real no se ejecutó en este entorno remoto; debe probarse con la cámara y la interfaz gráfica del equipo del participante. Tampoco se ha ejecutado entrenamiento, porque todavía no se han proporcionado esos ejemplos ni el dataset concreto.

