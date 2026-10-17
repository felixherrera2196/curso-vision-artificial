# 13. ¿Qué es Roboflow?

## Qué aprenderás

Comprenderás qué papel desempeña Roboflow en el flujo del curso y cómo se relacionan workspace, proyecto, anotaciones, versiones y exportaciones.

## La idea en palabras sencillas

Roboflow será el lugar donde organizarás las imágenes y sus etiquetas. Puedes pensar en un workspace como un espacio de trabajo, en un proyecto como una colección para una tarea y en una versión como una preparación concreta de esa colección.

Primero revisas las fotografías y cajas; después generas o eliges una versión que puedes descargar. No necesitas entrenar para comprender esa organización. Tu primera comprobación será que el proyecto contiene los objetos y las clases que quieres detectar, no simplemente que puedes abrirlo en el navegador.

## 1. Su función en el proyecto

**Roboflow** es una plataforma para trabajar con datos de visión artificial. Permite organizar imágenes, anotar objetos, revisar etiquetas y generar versiones exportables en formatos compatibles con diferentes herramientas.

En este curso lo utilizaremos como apoyo para preparar o descargar un dataset. El entrenamiento descrito en el temario se realizará con Ultralytics en Colab. Aunque la plataforma puede ofrecer otras funciones, organizar datos y entrenar el modelo son responsabilidades que conviene distinguir.

## 2. Workspace, proyecto y versión

Un **workspace** agrupa recursos y proyectos. Un **proyecto** define un conjunto de datos para una tarea, como detección de objetos. Una **versión** representa una preparación concreta del dataset con imágenes, anotaciones, divisiones y transformaciones determinadas.

El nombre del proyecto no es suficiente para reproducir un entrenamiento. Dos versiones pueden tener distinta cantidad de imágenes, diferentes etiquetas o cambios de preprocesamiento. Registra el identificador del proyecto y el número de versión que realmente descargaste.

Los nombres visibles y los identificadores utilizados por el SDK pueden no coincidir exactamente. Para una descarga reproducible, utiliza los valores que la plataforma proporciona en la exportación correspondiente.

## 3. Crear o elegir un proyecto

Para seguir el taller, la tarea debe ser **detección de objetos con cajas**. Un proyecto de clasificación o segmentación utiliza anotaciones diferentes y no debe tratarse como si fuera automáticamente un dataset de detección.

Si utilizas un dataset ya publicado, revisa sus clases, imágenes, anotaciones y condiciones de uso antes de entrenar. Tener acceso a una descarga no demuestra por sí solo que sus datos sean adecuados para tu cámara o que puedas redistribuirlos sin revisar su licencia.

Si preparas un proyecto propio, define las clases y la política de anotación del tema 12 antes de empezar a dibujar cajas. Esto reduce correcciones posteriores.

## 4. Flujo de preparación

1. Crear o abrir un proyecto de detección.
2. Subir imágenes representativas o revisar las disponibles.
3. Anotar todas las instancias relevantes.
4. Revisar clases, cajas y casos ambiguos.
5. Establecer divisiones que eviten fuga de datos.
6. Elegir preprocesamiento y aumentos apropiados.
7. Generar una versión.
8. Exportar en el formato requerido por el entrenamiento.

La interfaz puede cambiar de nombres o de ubicación. La idea importante es conservar ese orden lógico y revisar el resultado exportado, en lugar de confiar únicamente en que la plataforma generó un archivo.

## 5. Preprocesamiento y aumento

El **preprocesamiento** establece transformaciones de preparación, como ajustes de tamaño. El **aumento** produce variaciones útiles para entrenamiento. Ambos deben transformar también las cajas cuando modifican la geometría.

Cambiar la proporción de una imagen puede deformar el objeto; recortar puede eliminar parte de una instancia; voltear puede ser válido para algunos objetos e inválido para otros. Elige cada transformación según la escena final.

Además, Ultralytics puede aplicar transformaciones durante el entrenamiento. Revisa las dos etapas para comprender qué recibe el modelo. Acumular aumentos fuertes en ambos lugares puede crear ejemplos alejados del uso real.

## 6. API y credenciales

El SDK puede necesitar una clave de API para acceder a recursos autorizados. Esa clave identifica acceso, no es una clase del dataset ni un parámetro del modelo. Usa una credencial propia con el alcance necesario y evita pegarla en documentación pública.

Si compartes tu notebook o lo subes a GitHub, sustituye la clave real por un marcador o utiliza un mecanismo de secretos. En tu propia ejecución, configura los identificadores de workspace, proyecto y versión correspondientes al dataset que vas a utilizar.

## 7. Qué conservar para reproducir el trabajo

Registra proyecto, versión, clases, formato exportado, cantidad de imágenes por división y transformaciones. Esa información permite entender si un cambio de resultado proviene de los datos o de los parámetros de entrenamiento.

## Actividad de comprensión

Explica la diferencia entre cambiar una anotación del proyecto y descargar una versión ya generada. Describe por qué necesitas generar o seleccionar una versión coherente después de corregir datos y verificar qué versión usa realmente el notebook.

## Preparación para la descarga

Localiza el workspace, el proyecto y la versión que vas a utilizar. Comprueba que la tarea sea detección de objetos y revisa sus clases. En el [tema 14](14-descargar-dataset-roboflow.md) verificarás los archivos exportados antes de entrenar.

## Recorrido por la plataforma para empezar

1. Abre [Roboflow](https://roboflow.com/) e inicia sesión con tu cuenta o el acceso indicado por el instructor.
2. Entra al workspace de la práctica. Si vas a crear un proyecto, selecciona la tarea de detección de objetos, no clasificación.
3. Abre el proyecto y revisa sus nombres de clase y fotografías.
4. Si el proyecto es propio, sube imágenes y realiza el etiquetado descrito en el tema 12.
5. Revisa las divisiones de datos y las transformaciones antes de generar una versión.
6. Abre la versión que vas a utilizar y anota su identificación.

Si el instructor comparte un proyecto ya preparado, no necesitas crear otro para descargarlo: primero comprueba que tienes permiso para acceder a esa versión. Las etiquetas de botones pueden cambiar, pero debes reconocer las mismas etapas: proyecto, anotaciones, versión y exportación.

## Qué hace cada herramienta en esta parte del curso

| Herramienta | Para qué la utilizarás |
| --- | --- |
| Roboflow | Organizar imágenes, revisar anotaciones y preparar una versión exportable. |
| Colab | Ejecutar las instrucciones en un equipo remoto y solicitar GPU cuando esté disponible. |
| Ultralytics | Cargar, entrenar y utilizar un detector compatible. |
| OpenCV en Windows | Recibir la cámara y mostrar los resultados locales. |

No necesitas hacer todo en la misma página. Cada herramienta cubre una etapa. Tener el dataset en Roboflow no significa que ya esté descargado en Colab, y haber entrenado en Colab no coloca automáticamente los pesos en Windows.

## Antes de generar una versión

Revisa el tipo de tarea y las clases; observa cajas sobre varias imágenes; comprueba las divisiones. Después decide si necesitas redimensionar y si los aumentos representan cambios razonables para tu escena.

Si recortas o giras imágenes, las cajas deben seguir describiendo los objetos en la imagen transformada. Una exportación puede efectuar esa conversión, pero debes revisar el resultado, no asumir que todas las transformaciones mejoran tus datos.

Una versión facilita identificar qué preparación utilizaste. Si después corriges etiquetas, selecciona o genera una versión coherente con esas correcciones y confirma cuál descarga el notebook. Registra su número para que otra persona pueda repetir la misma práctica.

## Acceso y datos de tu proyecto

El workspace es el espacio de trabajo, el proyecto identifica la colección y la versión identifica su preparación. Si las instrucciones de descarga necesitan una clave de API, utiliza un mecanismo de secretos en el notebook y evita incluir la clave en archivos públicos o capturas.

Los identificadores de un ejemplo ajeno no apuntan a tus datos. Comprueba que los nombres visibles y los identificadores de la exportación corresponden al proyecto que tienes autorizado para la práctica. Si compartes un dataset existente, revisa también sus condiciones de uso.

## Para dar el siguiente paso

Las imágenes ya están organizadas en un proyecto. **¿Cómo llevamos una versión concreta al entorno donde entrenaremos, sin perder sus clases y anotaciones?** En el siguiente capítulo revisaremos la descarga y los archivos del dataset.

[Anterior](12-etiquetado-bounding-boxes.md) · [Índice](../README.md) · [Siguiente: Descargar dataset](14-descargar-dataset-roboflow.md)
