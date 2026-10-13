# 13. ¿Qué es Roboflow?

## Qué aprenderás

Comprenderás qué papel desempeña Roboflow en el flujo del curso y cómo se relacionan workspace, proyecto, anotaciones, versiones y exportaciones.

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

Cuando nos pases el ejemplo de descarga, sustituye cualquier clave real por un marcador. Los valores de workspace, proyecto y versión sí deben quedar explicados para que cada participante pueda reemplazarlos por los de su proyecto.

## 7. Qué conservar para reproducir el trabajo

Registra proyecto, versión, clases, formato exportado, cantidad de imágenes por división y transformaciones. Esa información permite entender si un cambio de resultado proviene de los datos o de los parámetros de entrenamiento.

## Actividad de comprensión

Explica la diferencia entre cambiar una anotación del proyecto y descargar una versión ya generada. Describe por qué necesitas generar o seleccionar una versión coherente después de corregir datos y verificar qué versión usa realmente el notebook.

## Ejemplo original

Pendiente de recibir los ejemplos de Roboflow. Se documentará el flujo que utilicen, sin asumir nombres de proyecto ni credenciales.

[Anterior](12-etiquetado-bounding-boxes.md) · [Índice](../README.md) · [Siguiente: Descargar dataset](14-descargar-dataset-roboflow.md)
