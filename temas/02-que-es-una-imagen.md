# 02. ¿Qué es una Imagen?

## Qué aprenderás

Entenderás cómo se representa una imagen digital, qué es un píxel, cómo se organizan sus canales y por qué importan las coordenadas y el tipo de dato. Estas ideas explican muchos errores habituales al utilizar OpenCV.

## La idea en palabras sencillas

Amplía mucho una fotografía y empezarás a distinguir pequeños cuadros: los píxeles. Para la computadora, la imagen es una tabla de números que describe esos cuadros. Una imagen de color tiene varios números por posición para representar sus componentes.

Piensa en una hoja cuadriculada: para localizar un cuadro necesitas saber su fila y su columna. En el curso hablaremos también de x e y para marcar posiciones. Antes de utilizar esos números, recuerda esta idea: una imagen visible en pantalla es, al mismo tiempo, información que el programa puede medir y comparar.

## 1. Una imagen como cuadrícula de datos

Una imagen digital está formada por una cuadrícula de **píxeles**. Cada píxel representa una muestra de la escena en una posición. La cantidad de columnas es el ancho y la cantidad de filas es el alto. Una imagen de 640 × 480 tiene 640 columnas, 480 filas y 307 200 posiciones.

La resolución describe cuántas posiciones hay, no garantiza que la imagen sea nítida. Una imagen grande puede estar desenfocada, sobreexpuesta o comprimida. Aumentar sus dimensiones por interpolación agrega muestras calculadas; no recupera automáticamente detalles que la cámara no capturó.

## 2. Intensidad y canales

En una imagen de escala de grises hay, normalmente, un valor de intensidad por píxel. En la representación de 8 bits más común, 0 corresponde a negro y 255 a blanco; los valores intermedios representan distintos niveles de gris.

Una imagen de color suele tener tres canales. RGB representa rojo, verde y azul. Cada píxel es una combinación de intensidades y no una etiqueta como «azul» o «amarillo». Un rojo intenso ideal en RGB se representa por valores altos de rojo y bajos de verde y azul, pero una superficie roja real cambia con la luz, las sombras y la cámara.

OpenCV suele entregar imágenes en **BGR** al leer archivos de color o fotogramas de una cámara: azul, verde y rojo. La información es equivalente a RGB, pero el orden es diferente. Si otra herramienta interpreta una matriz BGR como RGB, algunos colores se mostrarán intercambiados.

## 3. Forma del arreglo y coordenadas

En el caso habitual de una imagen de color, la forma del arreglo es **alto × ancho × canales**. Para una imagen de 640 × 480, la forma sería 480 × 640 × 3. Esta convención explica por qué el primer número de la forma no es el ancho.

Hay dos formas de referirse a una posición que debes mantener separadas:

- En una matriz se accede primero a la **fila** y después a la **columna**.
- En una coordenada geométrica se expresa primero **x** y después **y**.

La columna corresponde a x y la fila a y. Por lo general, el origen está en la esquina superior izquierda: x aumenta hacia la derecha y y hacia abajo. En una imagen de ancho 640, las columnas válidas van de 0 a 639.

## 4. Tipo de dato y rango

El tipo `uint8` representa enteros sin signo entre 0 y 255. Muchas operaciones de lectura y visualización trabajan con este formato. Sin embargo, otras operaciones utilizan números decimales; algunas esperan intensidades entre 0 y 1 y otras conservan el rango original.

Por eso no basta con conocer el contenido visual: hay que conocer la forma, el tipo y la escala del arreglo. Restar o sumar directamente en un arreglo de enteros sin signo puede causar desbordamientos según la operación. Las funciones de OpenCV y las operaciones de NumPy no siempre manejan esos casos de la misma manera.

Una **máscara binaria** utiliza dos estados para indicar pertenencia a una selección. En OpenCV es común usar 0 para fondo y 255 para primer plano. Ese 255 no mide la confianza de una clasificación; simplemente marca los píxeles incluidos.

## 5. Fotogramas y video

Un video es una secuencia de imágenes ordenadas en el tiempo. Cada imagen se llama **fotograma**. Trabajar con una cámara consiste, en buena parte, en repetir el mismo análisis sobre fotogramas nuevos.

Una frecuencia de 30 fotogramas por segundo implica aproximadamente 33,3 milisegundos entre imágenes. Si el procesamiento de cada una tarda mucho más, el programa deberá trabajar a menor velocidad, descartar imágenes o acumular retraso, dependiendo de cómo capture el video.

## 6. Por qué cambiar de tamaño afecta el resultado

Reducir la resolución disminuye el trabajo de procesamiento, pero también puede hacer desaparecer objetos pequeños. Si un objeto ocupa apenas unos píxeles, será difícil medir su contorno o detectarlo de manera estable. Además, las medidas de área y longitud cambian al redimensionar: reducir ancho y alto a la mitad reduce aproximadamente el área a una cuarta parte.

Si dibujas una caja calculada sobre una imagen reducida en la imagen original, debes transformar sus coordenadas. Este problema reaparecerá cuando revisemos bounding boxes.

## Actividad de comprensión

Para una imagen de 800 × 600 con tres canales, identifica ancho, alto, forma del arreglo y coordenadas de la esquina inferior derecha. Explica qué ocurriría al mostrarla con un orden de canales incorrecto y por qué una máscara de un solo canal no tiene la misma forma que la imagen de color.

## Aplicación en la siguiente práctica

En el [tema 04](04-video-camara-python.md) capturarás fotogramas reales. Relaciona cada imagen de la cámara con los conceptos de esta sección: alto, ancho, canales BGR y coordenadas. Esta relación te ayudará a interpretar las máscaras del tema 05.

[Anterior](01-introduccion-vision-artificial.md) · [Índice](../README.md) · [Siguiente: Instalación](03-instalacion-python-bibliotecas.md)
