# Antes de empezar: guía para quien nunca ha programado

Puedes participar en este curso aunque vengas de otra área. Aprenderás a ejecutar ejemplos preparados, observar qué hacen y modificar algunos valores con ayuda del instructor. No necesitas escribir un programa desde cero para comenzar.

## 1. Qué vas a construir

Primero harás que la computadora muestre el video de una cámara. Después le indicarás qué colores debe seleccionar y cómo reconocer algunas figuras. Finalmente conocerás un modelo que aprende de fotografías para detectar objetos.

Piensa en dos formas de dar instrucciones: en la primera defines una regla, como «selecciona lo verde»; en la segunda muestras ejemplos etiquetados para que un modelo aprenda patrones. Las dos necesitan pruebas: que algo funcione una vez no significa que funcionará en cualquier lugar.

## 2. Programa, lenguaje y editor

Un **programa** es un conjunto de instrucciones. **Python** es el lenguaje en el que escribimos esas instrucciones. El **intérprete** es el programa que las lee y ejecuta. **VS Code** es el editor en el que las puedes abrir y cambiar.

Es parecido a trabajar con una receta: el archivo contiene los pasos, el lenguaje determina cómo se escriben y el intérprete los realiza. El editor te ayuda a prepararlos; tener el editor instalado no significa que Python esté instalado.

Una **biblioteca** es una colección de herramientas ya preparadas. OpenCV ofrece herramientas para imágenes y cámaras; NumPy, para conjuntos de números; Ultralytics, para modelos de detección. No necesitas construir esas herramientas: aprenderás a utilizarlas.

## 3. Abrir una guía en GitHub

1. En la página principal del repositorio, baja hasta el índice del curso.
2. Haz clic en el tema que quieres consultar.
3. Lee primero qué aprenderás y la explicación inicial.
4. Busca el ejemplo de código cuando el capítulo incluya uno.
5. Utiliza los enlaces «Anterior», «Índice» y «Siguiente» al final para desplazarte.

Los archivos `.md` contienen las explicaciones que GitHub muestra como páginas. No se ejecutan como programas Python. Los archivos `.py` contienen programas de Python que puedes ejecutar en tu computadora.

## 4. Preparar y ejecutar tu primer archivo

Completa primero los tutoriales de [Python](../Tutorial%20instalaci%C3%B3n%20de%20Python/Tutorial%20instalaci%C3%B3n%20de%20Python.md) y [VS Code](../Tutorial%20de%20instalaci%C3%B3n%20de%20VSCode/Tutorial%20de%20instalaci%C3%B3n%20de%20VSCode.md).

1. Crea una carpeta fácil de encontrar, por ejemplo `curso-vision`, dentro de Documentos.
2. Abre VS Code y selecciona **Archivo → Abrir carpeta**. Elige esa carpeta.
3. Instala la extensión **Python**, publicada por Microsoft, desde el panel de extensiones si todavía no está instalada.
4. Crea un archivo nuevo y guárdalo como `camara_web.py`. Comprueba que termine en `.py`, no en `.py.txt`.
5. Abre la [práctica de cámara](04-video-camara-python.md) y copia el bloque completo de Python, desde la importación hasta el cierre de ventanas. No copies los signos que delimitan el recuadro Markdown.
6. Pega el código en el archivo y guarda con **Ctrl + S**. Conserva los espacios al comienzo de las líneas.
7. Abre la paleta con **Ctrl + Shift + P**, busca **Python: Select Interpreter / Seleccionar intérprete** y elige Python 3.12, en el que instalaste las bibliotecas.
8. Con el archivo abierto, busca **Run Python File in Terminal / Ejecutar archivo Python en terminal**, mediante el botón de ejecución de Python o la paleta de comandos.
9. Observa la ventana de cámara. Haz clic en ella y pulsa **ESC** para terminar la práctica.

Si el editor no encuentra Python o aparece un error, revisa el tutorial de instalación y el mensaje completo antes de continuar.

## 5. Leer el código sin memorizarlo

Una **variable** es un nombre que permite conservar un dato para utilizarlo después. En los ejemplos, `frame` guarda la imagen que acaba de capturar la cámara. El signo `=` asigna un resultado a un nombre; no es una pregunta sobre igualdad. Para comparar igualdad se usa `==`.

Una **función** es una herramienta que recibe información y realiza una tarea. En `cv2.imshow("Camara web", frame)`, el nombre identifica la herramienta y los paréntesis contienen lo que necesita: el título de la ventana y la imagen. Los valores que le entregamos se llaman **argumentos**.

`import cv2` permite utilizar OpenCV. El punto en `cv2.imshow` indica que estamos utilizando una herramienta de esa biblioteca. Las comillas delimitan texto; por ejemplo, el nombre que aparece en una ventana.

Las líneas que empiezan con `#` son **comentarios**: explicaciones para quien lee. Python no las ejecuta. Puedes usarlas como guía para identificar qué hace cada grupo de instrucciones.

`if` significa «si se cumple esta condición». `while` repite instrucciones mientras se cumpla una condición. `break` termina esa repetición. `True` y `False` representan verdadero y falso. `not` invierte una condición.

La **sangría** son los espacios al comienzo de las líneas. En Python agrupa instrucciones: las líneas desplazadas bajo un `if` o un `while` pertenecen a ese bloque. No las alinees todas al pegar el ejemplo.

No necesitas entender todos los símbolos el primer día. Empieza respondiendo: ¿de dónde sale la imagen?, ¿qué operación la analiza?, ¿qué ventana muestra el resultado? Después estudia cada bloque.

## 6. Dónde escribir cada cosa

| Lugar | Qué haces ahí |
| --- | --- |
| Archivo `.py` en VS Code | Pegas y guardas el programa Python. |
| Terminal o Símbolo del sistema | Escribes comandos como `python --version` o la instalación de paquetes. |
| Celda de código de Colab | Ejecutas instrucciones en una computadora remota desde el navegador. |
| Página Markdown de GitHub | Lees explicaciones y copias los ejemplos que vas a utilizar. |

No pegues un comando de instalación como si fuera una línea del programa de cámara. Sigue el lugar indicado por cada capítulo. Tampoco copies un mensaje de resultado como si fuera una instrucción.

## 7. Qué hacer si aparece un error

Un error es una señal de que una instrucción no se pudo realizar. Lee la última parte del mensaje y busca el archivo o la línea señalada. No cambies muchas cosas a la vez.

| Mensaje o síntoma | Primera comprobación |
| --- | --- |
| `ModuleNotFoundError` | ¿Instalaste la biblioteca en el mismo Python que ejecuta el archivo? |
| `IndentationError` | ¿Se conservaron los espacios al comienzo de las líneas? |
| `SyntaxError` | ¿Faltan comillas, paréntesis o alguna parte del código? |
| `FileNotFoundError` | ¿El archivo existe en la ruta utilizada? |
| No se pudo abrir la cámara | ¿Está conectada, tiene permisos y está libre de otras aplicaciones? |
| El programa parece seguir activo | ¿Debes pulsar ESC con la ventana seleccionada? |

Para pedir ayuda, comparte el mensaje completo, qué archivo estabas ejecutando y qué esperabas ver. Si necesitas detener una ejecución desde la terminal, prueba **Ctrl + C**. Esta interrupción no garantiza que cualquier programa limpie sus recursos; en los ejemplos de cámara es preferible utilizar ESC cuando la ventana responde.

## 8. Cómo aprovechar cada práctica

Ejecuta primero el ejemplo sin modificarlo. Observa el resultado y después cambia un único valor indicado en la guía. Guarda qué cambiaste y qué ocurrió. Si deja de funcionar, vuelve al valor anterior antes de probar otro cambio.

Trabaja con una escena sencilla al principio: buena luz, un objeto y fondo contrastante. Cuando funcione, introduce dificultad poco a poco. Entender por qué falla es parte del aprendizaje.

Si encuentras términos técnicos, lee primero su explicación sencilla al inicio del capítulo. Las secciones posteriores amplían los detalles para que puedas volver a ellas después de la demostración del instructor.

[Ir al índice](../README.md) · [Comenzar el tema 01](01-introduccion-vision-artificial.md)
