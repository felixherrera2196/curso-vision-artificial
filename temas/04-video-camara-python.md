# 04. Obtener video de una cámara con Python

## Qué aprenderás

Comprenderás el ciclo de captura de video y la responsabilidad de cada parte: abrir un dispositivo, leer imágenes, procesarlas, mostrarlas y liberar los recursos. Esta estructura se reutilizará tanto para los filtros de color como para YOLO.

## La idea en palabras sencillas

El video que ves en pantalla es una sucesión de fotografías. El programa pide una fotografía a la cámara, la muestra y vuelve a pedir otra. Esa repetición produce el movimiento.

En esta primera práctica no intentaremos reconocer nada. Solo comprobaremos que la computadora recibe imágenes y puede mostrarlas. Cuando esto funcione, conservaremos la misma estructura y añadiremos el análisis de color. Si no tienes experiencia, ejecuta primero el ejemplo completo; después utiliza los comentarios para localizar dónde abre la cámara, dónde repite y dónde termina.

## 1. Práctica: mostrar el video de la cámara

En esta práctica abrirás la cámara, mostrarás los fotogramas y terminarás la ejecución con ESC. Guarda el siguiente código en un archivo con extensión `.py`, por ejemplo `camara_web.py`, y ejecútalo localmente desde el entorno preparado en el tema 03. No nombres el archivo `cv2.py`, porque ese nombre puede interferir con la importación de OpenCV.

```python
# Importamos OpenCV
import cv2

# Creamos el objeto que controla la cámara web
# El número 0 representa normalmente la cámara principal
cap = cv2.VideoCapture(0)

# Comprobamos si la cámara pudo abrirse correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

# Creamos un ciclo infinito para leer continuamente el video
while True:

    # Leemos un fotograma de la cámara
    # ret indica si el fotograma se obtuvo correctamente
    # frame contiene la imagen capturada
    ret, frame = cap.read()

    # Comprobamos si hubo algún problema al leer el fotograma
    if not ret:
        print("No se pudo leer el video.")
        break

    # Mostramos el fotograma en una ventana
    cv2.imshow("Camara web", frame)

    # Esperamos 1 milisegundo por una tecla
    # Si la tecla ESC (27) es presionada, salimos del ciclo
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Liberamos la cámara
cap.release()

# Cerramos todas las ventanas de OpenCV
cv2.destroyAllWindows()
```

## 2. Explicación de cada bloque

### Importar la biblioteca

`import cv2` hace disponible el módulo de OpenCV. Después, el prefijo `cv2.` permite acceder a sus funciones y clases. Si falla aquí con un error de módulo no encontrado, todavía no se ha intentado abrir la cámara: revisa la instalación y el intérprete del tema 03.

### Crear el objeto de captura

```python
cap = cv2.VideoCapture(0)
```

`cap = cv2.VideoCapture(0)` construye un objeto y solicita la apertura del dispositivo de índice 0. `cap` es una variable que conserva ese objeto para las lecturas posteriores. No almacena todo el video; administra la fuente desde la cual iremos obteniendo imágenes.

La línea se ejecuta una sola vez. Si hay varias cámaras, puede ser necesario cambiar el índice después de identificar los dispositivos disponibles. La cámara que el sistema considera primero puede no ser la externa que quieras utilizar.

### Comprobar la apertura

```python
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()
```

`cap.isOpened()` produce una respuesta de verdadero o falso sobre la apertura. `not` invierte esa respuesta, de modo que el bloque del `if` se ejecuta cuando la fuente **no** se pudo abrir. El programa imprime un mensaje y termina mediante `exit()`.

El ejemplo usa `exit()` como salida sencilla. Es un auxiliar habitualmente disponible en Python; en un programa de producción suele preferirse una salida explícita con `sys.exit()` o una estructura de función. Durante esta práctica, concéntrate en comprender la comprobación de apertura y el flujo de salida.

### Repetir la lectura

`while True` inicia un ciclo cuya condición permanece verdadera. El programa continuará hasta encontrar una instrucción que interrumpa el ciclo o hasta terminar por otra causa. Aquí existen dos salidas previstas: fallo de lectura y pulsación de ESC.

La sangría indica qué instrucciones pertenecen al ciclo. Las últimas dos instrucciones del programa están fuera de él y se ejecutan después de salir por `break`.

### Separar éxito e imagen

```python
ret, frame = cap.read()
```

`ret, frame = cap.read()` recibe dos resultados. `ret` indica si se obtuvo el fotograma y `frame` contiene los datos de esa imagen cuando la lectura fue válida. La coma permite asignar cada resultado a una variable diferente.

`ret` no representa la frecuencia de video ni la resolución. `frame` tampoco es el archivo completo del video: es la imagen de la lectura actual. En la siguiente vuelta se reemplaza por otra imagen.

El bloque `if not ret` evita intentar mostrar una captura fallida. El mensaje informa que el dispositivo se abrió, pero una lectura no tuvo éxito. `break` sale del `while`; no termina inmediatamente todo el programa. Por eso después se ejecuta la limpieza.

### Mostrar el fotograma

```python
cv2.imshow("Camara web", frame)
```

`cv2.imshow("Camara web", frame)` presenta la imagen en una ventana identificada por ese título. Usar el mismo título en cada vuelta actualiza la misma ventana. La imagen habitual de la cámara es un arreglo BGR, como se explicó en el tema 02.

En este punto todavía no se ha aplicado un filtro ni un detector: se muestra lo que entrega la cámara. Esta es una base útil para comprobar captura y visualización antes de agregar procesamiento.

### Consultar ESC

```python
if cv2.waitKey(1) & 0xFF == 27:
    break
```

`cv2.waitKey(1)` atiende eventos de la ventana y espera brevemente una entrada de teclado. La espera solicitada es de un milisegundo; el tiempo real puede ser mayor por la planificación del sistema y por el trabajo del ciclo. No significa que el programa alcance mil fotogramas por segundo.

`& 0xFF` es una operación AND de bits con una máscara de ocho bits. Conserva la parte baja del código devuelto, una práctica común en estos ejemplos de OpenCV para comparar teclas simples. No modifica la imagen ni el color.

`== 27` compara el código con el de ESC. Si coincide, `break` termina el ciclo. La ventana de OpenCV debe tener el foco para recibir esa tecla. Cerrar la ventana con su botón no es la condición de salida que implementa este ejemplo; utiliza ESC durante la práctica.

### Liberar y cerrar

```python
cap.release()
cv2.destroyAllWindows()
```

`cap.release()` deja disponible la cámara y `cv2.destroyAllWindows()` cierra las ventanas creadas por OpenCV. Ambas se ejecutan después de las salidas normales del ciclo.

Si una excepción ocurre antes de llegar a esas líneas, el código no asegura que la limpieza se ejecute. Como ejercicio de mejora, puedes utilizar `try` y `finally` para asegurar la liberación de recursos también cuando se produce una excepción.

## 3. Resultado esperado y comprobación

Al ejecutar el archivo, aparece la ventana «Camara web» con video que cambia continuamente. Mueve un objeto frente a la cámara para verificar que no sea una imagen fija. Presiona ESC con la ventana seleccionada: debe cerrarse y la ejecución debe terminar.

Después vuelve a ejecutar el programa. Si la cámara abre nuevamente, la liberación funcionó en la salida normal. Si aparece alguno de los mensajes de fallo, consulta «Errores frecuentes» y distingue si falló la apertura o la lectura.

Realiza esta comprobación en tu computadora con cámara y escritorio gráfico. Si la ventana no aparece o el dispositivo no se abre, revisa los permisos, la conexión y el entorno de Python antes de continuar.

## Errores frecuentes

- **No se abre el dispositivo:** revisa índice, conexión, permisos y otras aplicaciones.
- **Se abre pero no entrega imágenes:** comprueba cada lectura y prueba el dispositivo fuera del programa.
- **Ventana congelada:** revisa la atención de eventos y si alguna operación bloquea el ciclo.
- **Video con retraso:** evalúa costo por fotograma y posible acumulación de imágenes.
- **Fallo en Colab:** recuerda que el kernel remoto no tiene acceso directo a la cámara local.

## Consulta: herramientas nuevas de este capítulo

### Cómo leer los parámetros de una función

Un **parámetro** es el nombre de un dato que una herramienta puede recibir. Un **argumento** es el valor que entregas al utilizarla. Por ejemplo, en `cv2.waitKey(1)`, `delay` es el parámetro y `1` es el argumento que elegimos.

Un argumento puede escribirse por posición, respetando el orden, o por nombre cuando la interfaz lo permite, como `iterations=1`. Un parámetro opcional utiliza su valor predeterminado si no lo escribes. Las formas mostradas aquí están simplificadas para la práctica: algunas herramientas tienen más variantes.

### `cv2.VideoCapture`: abrir una fuente de video

Es un constructor: crea un objeto de captura. Una forma habitual para cámara es `cv2.VideoCapture(index, apiPreference=cv2.CAP_ANY)`.

| Parámetro | ¿Lo necesitas indicar? | Qué significa y qué suele utilizarse |
| --- | --- | --- |
| `index` | Sí, en esta forma de apertura. | Número del dispositivo. Se suele comenzar con `0`; otra cámara puede estar en `1` u otro índice. |
| `apiPreference` | No. | Interfaz de captura preferida. `CAP_ANY` deja elegir a OpenCV. En Windows existen opciones como `CAP_DSHOW` y `CAP_MSMF`. |

**Devuelve:** un objeto que guardamos en `cap`. Crear el objeto no garantiza que la cámara se haya abierto; por eso comprobamos `isOpened()`.

El primer argumento también puede ser el nombre de un archivo de video en otra forma de uso. Abrir un archivo y abrir un dispositivo son situaciones distintas. Para el laboratorio conservamos el índice de cámara.

**Opciones comunes:** prueba primero `VideoCapture(0)` como en el programa. Si en Windows hay problemas concretos de captura, el instructor puede probar una interfaz explícita. Cambiar la interfaz no corrige por sí solo permisos denegados, una cámara desconectada o un índice equivocado.

### `cap.isOpened()`: comprobar la apertura

Se llama sobre el objeto `cap`, sin argumentos adicionales. **Devuelve** `True` si la captura está abierta y `False` si no. Solo comprueba el estado de apertura: aún necesitamos verificar cada lectura.

### `cap.read()`: pedir la siguiente imagen

En la forma utilizada en el curso no necesita argumentos. **Devuelve dos resultados:** la señal de éxito y la imagen. Los guardamos en `ret, frame`.

Si la lectura falla, no utilices el supuesto fotograma para convertir color ni mostrarlo. En un archivo de video puede fallar al terminar el contenido; en una cámara puede indicar una interrupción de captura. La función no devuelve toda la grabación ni guarda imágenes automáticamente.

### `cv2.imshow`: mostrar o actualizar una imagen

Forma de uso: `cv2.imshow(winname, mat)`.

| Parámetro | Qué recibe | Uso habitual |
| --- | --- | --- |
| `winname` | Texto que identifica la ventana. | Mantener el mismo nombre para actualizar la misma ventana. |
| `mat` | Imagen que se mostrará. | `frame` para la cámara o una máscara de un canal. |

Ambos argumentos son necesarios en esta forma. **No devuelve una imagen procesada**: su propósito es mostrarla. Para una imagen de color de OpenCV se utiliza BGR. La atención de eventos requiere `waitKey` u otra función de eventos compatible; llamar repetidamente a `imshow` sin atenderlos puede dejar la ventana sin respuesta.

### `cv2.waitKey`: atender ventanas y consultar una tecla

Forma: `cv2.waitKey(delay=0)`.

| Valor de `delay` | Comportamiento |
| --- | --- |
| `0`, predeterminado | Espera una tecla sin un límite temporal. Es común al mostrar una fotografía fija. |
| Positivo, como `1` | Solicita una espera breve en milisegundos. Se utiliza habitualmente dentro del ciclo de video. |

**Devuelve:** un código de tecla, o `-1` si no se recibió ninguna en el intervalo. La espera real puede superar el tiempo solicitado según el sistema. `1` no significa «procesar mil imágenes por segundo».

`& 0xFF` conserva los ocho bits inferiores para la comparación usada en el ejemplo; `27` corresponde a ESC. La ventana debe tener el foco para recibir la tecla. No elimines `waitKey` pensando que solo retrasa el video: también participa en la respuesta de las ventanas.

### `cap.release()` y `cv2.destroyAllWindows()`: terminar

En estas formas no necesitan argumentos y no producen una imagen de salida. `release()` libera la captura del objeto; `destroyAllWindows()` cierra las ventanas creadas por OpenCV. Cumplen tareas diferentes y por eso utilizamos ambas.

No liberan automáticamente los recursos si el programa falla antes de llegar a ellas. Una estructura de limpieza ante excepciones sería una mejora posterior. Para esta práctica utiliza ESC cuando el video responda.


## Para dar el siguiente paso

Ya conseguimos que la cámara muestre lo que tiene enfrente. **¿Cómo podemos hacer que el programa seleccione únicamente la hoja verde, en lugar de tratar toda la imagen por igual?**

En el siguiente capítulo utilizaremos filtros de color para construir una máscara que señale las partes que nos interesan.

[Anterior](03-instalacion-python-bibliotecas.md) · [Índice](../README.md) · [Siguiente: Filtros de color](05-filtros-color.md)
