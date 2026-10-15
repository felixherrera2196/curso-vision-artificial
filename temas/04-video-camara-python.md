# 04. Obtener video de una cámara con Python

## Qué aprenderás

Comprenderás el ciclo de captura de video y la responsabilidad de cada parte: abrir un dispositivo, leer imágenes, procesarlas, mostrarlas y liberar los recursos. Esta estructura se reutilizará tanto para los filtros de color como para YOLO.

## La idea en palabras sencillas

El video que ves en pantalla es una sucesión de fotografías. El programa pide una fotografía a la cámara, la muestra y vuelve a pedir otra. Esa repetición produce el movimiento.

En esta primera práctica no intentaremos reconocer nada. Solo comprobaremos que la computadora recibe imágenes y puede mostrarlas. Cuando esto funcione, conservaremos la misma estructura y añadiremos el análisis de color. Si no tienes experiencia, ejecuta primero el ejemplo completo; después utiliza los comentarios para localizar dónde abre la cámara, dónde repite y dónde termina.

## 1. La cámara como fuente de fotogramas

OpenCV ofrece `VideoCapture` para trabajar con una cámara o una fuente de video. Al abrir una cámara local, se suele indicar un índice de dispositivo. El índice 0 es un primer intento habitual, pero no garantiza que corresponda a la cámara deseada: un equipo puede tener una integrada, una externa y dispositivos virtuales.

Abrir una fuente y recibir imágenes son comprobaciones diferentes. `isOpened` permite saber si se abrió la captura. La lectura con `read` devuelve una señal de éxito y el fotograma obtenido. Debes revisar ambas cosas; procesar un fotograma inexistente provoca errores en etapas posteriores.

## 2. Estructura del ciclo

1. Crear la captura una vez, antes de entrar al ciclo.
2. Comprobar que se abrió correctamente.
3. Pedir un nuevo fotograma.
4. Si la lectura falla, manejar el caso o terminar.
5. Procesar el fotograma válido.
6. Mostrar la imagen y consultar una condición de salida.
7. Repetir hasta terminar.
8. Liberar la cámara y cerrar las ventanas.

La captura no debe abrirse nuevamente en cada iteración. Hacerlo añade trabajo y puede impedir una secuencia fluida. Del mismo modo, cerrar la cámara dentro del ciclo antes de la siguiente lectura corta la fuente de video.

## 3. Visualización y respuesta del teclado

En un programa local, `imshow` permite mostrar un fotograma en una ventana. Las funciones de espera de teclado, como `waitKey`, también permiten que OpenCV procese eventos de esa ventana. Si el programa no atiende los eventos, la interfaz puede aparentar que se bloqueó.

La espera debe ser breve para seguir avanzando por el video. Su valor no establece por sí solo los fotogramas por segundo: también cuenta el tiempo de lectura, el procesamiento y la visualización. Al crear tu aplicación, indica qué tecla permite salir y comprueba su pulsación dentro del ciclo.

Conviene que el programa pueda liberar recursos aunque haya una excepción. La lógica de limpieza suele organizarse de forma que se ejecute al terminar normalmente o al producirse un fallo. El ejemplo de esta guía libera los recursos al salir por ESC o por un fallo de lectura; para asegurar la limpieza también ante excepciones, puedes utilizar una estructura `try` y `finally`.

## 4. Liberar los recursos

`release` libera la fuente de captura. Cerrar las ventanas elimina la interfaz de visualización. Son acciones relacionadas, pero no equivalentes: cerrar una ventana no debe sustituir el cierre del dispositivo.

Si el programa termina dejando la cámara ocupada, otro proceso puede no abrirla inmediatamente. En un notebook también es posible que una captura permanezca activa entre ejecuciones de celdas. Para estas prácticas, un archivo ejecutado localmente suele ofrecer un ciclo de vida más fácil de controlar.

## 5. Resolución y rendimiento

Una cámara puede admitir distintas resoluciones. Solicitar un tamaño no garantiza que el dispositivo lo acepte; revisa el tamaño real del fotograma recibido. Aumentar la resolución incrementa la cantidad de datos y el costo de las transformaciones posteriores.

Para diagnosticar lentitud, primero prueba la captura sin procesamiento. Después agrega una operación a la vez. Así sabrás si el límite está en el dispositivo, en el algoritmo o en la visualización. Si tienes que reducir resolución, verifica que los objetos pequeños sigan siendo visibles.

## 6. Prueba guiada

Coloca la cámara frente a una escena iluminada y establece una tecla de salida. Comprueba que el video cambia al mover un objeto y que el programa termina sin dejar ventanas abiertas. Ejecuta nuevamente para verificar que la cámara quedó disponible.

Después prueba con la cámara desconectada o con un índice incorrecto. La aplicación debe informar el problema de captura en lugar de intentar convertir o dibujar sobre un fotograma inválido.

## Errores frecuentes

- **No se abre el dispositivo:** revisa índice, conexión, permisos y otras aplicaciones.
- **Se abre pero no entrega imágenes:** comprueba cada lectura y prueba el dispositivo fuera del programa.
- **Ventana congelada:** revisa la atención de eventos y si alguna operación bloquea el ciclo.
- **Video con retraso:** evalúa costo por fotograma y posible acumulación de imágenes.
- **Fallo en Colab:** recuerda que el kernel remoto no tiene acceso directo a la cámara local.

## 7. Práctica: mostrar el video de la cámara

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

## 8. Explicación de cada bloque

### Importar la biblioteca

`import cv2` hace disponible el módulo de OpenCV. Después, el prefijo `cv2.` permite acceder a sus funciones y clases. Si falla aquí con un error de módulo no encontrado, todavía no se ha intentado abrir la cámara: revisa la instalación y el intérprete del tema 03.

### Crear el objeto de captura

`cap = cv2.VideoCapture(0)` construye un objeto y solicita la apertura del dispositivo de índice 0. `cap` es una variable que conserva ese objeto para las lecturas posteriores. No almacena todo el video; administra la fuente desde la cual iremos obteniendo imágenes.

La línea se ejecuta una sola vez. Si hay varias cámaras, puede ser necesario cambiar el índice después de identificar los dispositivos disponibles. La cámara que el sistema considera primero puede no ser la externa que quieras utilizar.

### Comprobar la apertura

`cap.isOpened()` produce una respuesta de verdadero o falso sobre la apertura. `not` invierte esa respuesta, de modo que el bloque del `if` se ejecuta cuando la fuente **no** se pudo abrir. El programa imprime un mensaje y termina mediante `exit()`.

El ejemplo usa `exit()` como salida sencilla. Es un auxiliar habitualmente disponible en Python; en un programa de producción suele preferirse una salida explícita con `sys.exit()` o una estructura de función. Durante esta práctica, concéntrate en comprender la comprobación de apertura y el flujo de salida.

### Repetir la lectura

`while True` inicia un ciclo cuya condición permanece verdadera. El programa continuará hasta encontrar una instrucción que interrumpa el ciclo o hasta terminar por otra causa. Aquí existen dos salidas previstas: fallo de lectura y pulsación de ESC.

La sangría indica qué instrucciones pertenecen al ciclo. Las últimas dos instrucciones del programa están fuera de él y se ejecutan después de salir por `break`.

### Separar éxito e imagen

`ret, frame = cap.read()` recibe dos resultados. `ret` indica si se obtuvo el fotograma y `frame` contiene los datos de esa imagen cuando la lectura fue válida. La coma permite asignar cada resultado a una variable diferente.

`ret` no representa la frecuencia de video ni la resolución. `frame` tampoco es el archivo completo del video: es la imagen de la lectura actual. En la siguiente vuelta se reemplaza por otra imagen.

El bloque `if not ret` evita intentar mostrar una captura fallida. El mensaje informa que el dispositivo se abrió, pero una lectura no tuvo éxito. `break` sale del `while`; no termina inmediatamente todo el programa. Por eso después se ejecuta la limpieza.

### Mostrar el fotograma

`cv2.imshow("Camara web", frame)` presenta la imagen en una ventana identificada por ese título. Usar el mismo título en cada vuelta actualiza la misma ventana. La imagen habitual de la cámara es un arreglo BGR, como se explicó en el tema 02.

En este punto todavía no se ha aplicado un filtro ni un detector: se muestra lo que entrega la cámara. Esta es una base útil para comprobar captura y visualización antes de agregar procesamiento.

### Consultar ESC

`cv2.waitKey(1)` atiende eventos de la ventana y espera brevemente una entrada de teclado. La espera solicitada es de un milisegundo; el tiempo real puede ser mayor por la planificación del sistema y por el trabajo del ciclo. No significa que el programa alcance mil fotogramas por segundo.

`& 0xFF` es una operación AND de bits con una máscara de ocho bits. Conserva la parte baja del código devuelto, una práctica común en estos ejemplos de OpenCV para comparar teclas simples. No modifica la imagen ni el color.

`== 27` compara el código con el de ESC. Si coincide, `break` termina el ciclo. La ventana de OpenCV debe tener el foco para recibir esa tecla. Cerrar la ventana con su botón no es la condición de salida que implementa este ejemplo; utiliza ESC durante la práctica.

### Liberar y cerrar

`cap.release()` deja disponible la cámara y `cv2.destroyAllWindows()` cierra las ventanas creadas por OpenCV. Ambas se ejecutan después de las salidas normales del ciclo.

Si una excepción ocurre antes de llegar a esas líneas, el código no asegura que la limpieza se ejecute. Como ejercicio de mejora, puedes utilizar `try` y `finally` para asegurar la liberación de recursos también cuando se produce una excepción.

## 9. Resultado esperado y comprobación

Al ejecutar el archivo, aparece la ventana «Camara web» con video que cambia continuamente. Mueve un objeto frente a la cámara para verificar que no sea una imagen fija. Presiona ESC con la ventana seleccionada: debe cerrarse y la ejecución debe terminar.

Después vuelve a ejecutar el programa. Si la cámara abre nuevamente, la liberación funcionó en la salida normal. Si aparece alguno de los mensajes de fallo, utiliza el diagnóstico de la sección anterior y distingue si falló la apertura o la lectura.

Realiza esta comprobación en tu computadora con cámara y escritorio gráfico. Si la ventana no aparece o el dispositivo no se abre, revisa los permisos, la conexión y el entorno de Python antes de continuar.

[Anterior](03-instalacion-python-bibliotecas.md) · [Índice](../README.md) · [Siguiente: Filtros de color](05-filtros-color.md)
