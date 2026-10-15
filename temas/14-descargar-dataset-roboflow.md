# 14. Descargar un dataset de Roboflow

## Qué aprenderás

Comprenderás cómo pasar de una versión preparada en Roboflow a archivos utilizables por el entrenamiento. Aprenderás a comprobar la estructura, la configuración y las rutas antes de consumir tiempo de GPU.

## La idea en palabras sencillas

Descargar el dataset significa llevar las imágenes y sus etiquetas al lugar donde vas a entrenar. Si trabajas en Colab, ese lugar es una computadora remota. La descarga no aparece automáticamente en la carpeta Descargas de tu laptop.

Además de las fotografías suele haber un archivo de configuración, como `data.yaml`. Puedes verlo como un índice: indica dónde buscar imágenes y cómo se llaman las clases. Antes de entrenar, abre algunas imágenes con sus cajas para comprobar que descargaste los datos correctos.

## 1. Qué se descarga

La descarga debe corresponder a una **versión específica** y a un **formato de exportación** compatible con el detector. Según el formato, puede contener carpetas de imágenes, archivos de etiquetas y un archivo de configuración del dataset.

No basta con que el archivo termine de descargarse. Debe ser la tarea correcta, incluir las clases deseadas y conservar parejas válidas de imagen y anotación. Un dataset de clasificación no se convierte en detección por cambiar el nombre de una carpeta.

## 2. Seleccionar el formato correcto

Para entrenar un detector YOLO con Ultralytics, utiliza el formato de detección que sea compatible con la versión y el ejemplo del curso. En las exportaciones habituales, las imágenes y etiquetas se organizan por divisiones y existe un archivo como `data.yaml` que describe rutas y clases.

La denominación de la opción de exportación puede cambiar entre versiones de la plataforma. Comprueba el identificador del formato que aparece en las instrucciones de exportación de tu proyecto y verifica que sea compatible con la versión de Ultralytics utilizada para entrenar.

## 3. Descarga manual y mediante SDK

Una descarga manual suele generar un archivo comprimido que se descomprime en el entorno de trabajo. La descarga mediante SDK utiliza los identificadores de workspace, proyecto y versión para solicitar los datos desde Python.

En ambos casos, el resultado útil son los archivos locales del entorno en el que vas a entrenar. Si ejecutas el SDK en Colab, la descarga queda en el sistema remoto de Colab; no aparece automáticamente en tu laptop.

La carpeta donde termina la descarga puede depender de la configuración y de la versión del SDK. Es preferible leer la ubicación informada por la operación y comprobarla, en lugar de asumir una ruta copiada de otro notebook.

## 4. Qué describe el YAML

El archivo de configuración suele indicar dónde están entrenamiento, validación y, si existe, prueba, además del mapa de nombres de clase. Algunas configuraciones incluyen una ruta base y rutas relativas; otras utilizan rutas absolutas.

El YAML no contiene los pesos entrenados ni todas las anotaciones. Funciona como un mapa que le dice al entrenador dónde encontrar los datos y cómo interpretar los identificadores de clase.

Si cambias la ubicación de carpetas, las referencias pueden quedar inválidas. Evita corregir una ruta al azar: primero identifica la ruta base y cómo el entrenador resuelve las rutas relativas.

## 5. Revisión antes del entrenamiento

1. Localiza la carpeta descargada y el YAML utilizado.
2. Confirma que existen imágenes para entrenamiento y validación.
3. Revisa los nombres e identificadores de clases.
4. Comprueba que las etiquetas corresponden a la tarea de detección.
5. Visualiza imágenes anotadas de cada división.
6. Busca cajas desplazadas, clases incorrectas y archivos ausentes.
7. Registra proyecto, versión y formato para el informe.

Comprobar unas pocas imágenes no garantiza que todas estén bien, pero detecta errores de formato y conversiones sistemáticas. Si encuentras un patrón de cajas mal ubicadas, revisa el conjunto antes de entrenar.

## 6. Problemas frecuentes

**Acceso rechazado:** revisa autorización del recurso y credencial; no lo confundas con un problema del modelo. **Proyecto o versión inexistente:** comprueba identificadores exactos. **Ruta no encontrada:** revisa carpeta de descarga, extracción y YAML. **Dataset vacío o distinto:** confirma versión y formato. **Etiquetas inesperadas:** verifica tipo de tarea y mapa de clases.

Si el error aparece antes de iniciar las épocas, suele corresponder a acceso, formato o rutas. Si el entrenamiento comienza pero el resultado es malo, revisa también diversidad y calidad de las etiquetas.

## 7. Conservación del dataset

Los archivos de la sesión de Colab son temporales. Si necesitas conservar exactamente la versión utilizada, guarda una copia o registra un mecanismo reproducible de descarga. Respeta las condiciones del dataset si compartes el material con otras personas.

## Actividad de comprensión

Explica por qué un YAML existente puede fallar después de mover las carpetas. Identifica qué información necesitas para repetir la misma descarga y cómo comprobarías que el mapa de clases coincide con los archivos de etiquetas.

## Antes de continuar

Anota la ruta de descarga y localiza el archivo de configuración del dataset. Revisa sus clases y abre imágenes anotadas de entrenamiento y validación. Conserva el identificador de la versión para poder repetir la descarga en otra sesión de Colab.

## Recorrido de descarga y comprobación

1. Abre la versión del proyecto indicada para la práctica.
2. Busca la opción de descargar o exportar el dataset.
3. Selecciona un formato de **detección** compatible con la versión de YOLO que utilizarás.
4. Elige el método de descarga de la práctica: archivo comprimido o instrucciones para el notebook.
5. Si recibes un comprimido, extráelo. Si lo descargaste en tu laptop y entrenarás en Colab, aún necesitas llevar esos archivos a Colab; son lugares diferentes.
6. Localiza el archivo de configuración, generalmente `data.yaml`, y revisa clases y rutas.
7. Examina imágenes y anotaciones antes de iniciar el entrenamiento.

**Qué debes poder señalar al terminar:** la carpeta con tus datos, la configuración que utilizará el entrenador y los nombres de las clases. Si no puedes encontrar esos tres elementos, detente y revisa la descarga.

No copies literalmente las rutas del equipo de otra persona. Una ruta es una dirección de archivo: debe corresponder al lugar donde están tus datos en la sesión actual.


[Anterior](13-que-es-roboflow.md) · [Índice](../README.md) · [Siguiente: Colab](15-colab-gpu-ultralytics.md)
