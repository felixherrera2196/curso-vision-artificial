# 05. Filtros de color

## Qué aprenderás

Aprenderás a seleccionar el color de una hoja frente a la cámara. Utilizarás directamente los canales BGR que entrega OpenCV y ajustarás sus límites con un calibrador. En el tema 06 aprenderás a convertir a HSV y compararás ambos métodos.

## La idea en palabras sencillas

Una máscara es una imagen blanca y negra que responde una pregunta en cada posición: «¿este píxel cumple la regla del color?». Blanco significa sí; negro significa no. La máscara no reconoce todavía una hoja como objeto: también puede seleccionar una camisa o un fondo del mismo color.

## 1. Preparar la escena del laboratorio

Utilizaremos una **hoja verde, preferentemente mate y de color intenso**, para que el canal verde destaque frente a azul y rojo. El filtro y su calibrador trabajarán directamente en BGR. En los capítulos siguientes mantendremos la hoja verde como referencia.

1. Coloca la hoja frente a la cámara, sin pegarla al lente, y comprueba que esté enfocada.
2. Busca una iluminación uniforme. Evita reflejos fuertes o una ventana muy brillante detrás.
3. Procura que el fondo no sea verde. Una mesa o pared de otro color facilitará la comparación.
4. Deja visibles los bordes de la hoja: nos servirán para observar las máscaras.
5. Ejecuta un programa a la vez y ciérralo con ESC antes de abrir el siguiente.

La elección de verde simplifica los ejemplos; no garantiza una selección perfecta en cualquier cámara. Los intervalos son puntos de partida para calibrar en el laboratorio.

## 2. Práctica: filtro sencillo en BGR

OpenCV entrega normalmente la imagen en **BGR**: azul, verde y rojo, en ese orden. No necesitamos convertirla a RGB. Para esta primera aproximación pediremos bastante verde y cantidades más bajas de azul y rojo.

Guarda el programa como `filtro_verde_bgr.py`, copia el bloque completo y ejecútalo con Python 3.12 y las bibliotecas del curso.

```python
# Importamos las herramientas para la cámara y los arreglos
import cv2
import numpy as np

# Abrimos la cámara principal
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()


# Repetimos la captura y el procesamiento
while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo leer el video.")
        break

    # Sin conversión: el fotograma ya está en BGR
    # Orden: azul, verde, rojo
    lower_green = np.array([0, 100, 0], dtype=np.uint8)
    upper_green = np.array([120, 255, 120], dtype=np.uint8)

    # Una sola comparación genera una sola máscara
    mask = cv2.inRange(frame, lower_green, upper_green)


    # Mostramos el video y la selección sin procesar
    cv2.imshow("Camara web", frame)
    cv2.imshow("Mascara original", mask)

    # ESC termina la ejecución
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Dejamos disponible la cámara y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()
```

### Cómo leer el programa

```python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()
```

`import cv2` permite utilizar OpenCV y `import numpy as np` permite crear los arreglos de límites. `cap` conserva la conexión con la cámara. Antes del ciclo, `isOpened()` comprueba que la conexión pudo abrirse.

```python
ret, frame = cap.read()
```

`while True` repite la captura. En cada vuelta, `ret` indica si hubo lectura correcta y `frame` contiene el fotograma actual. El bloque `if not ret` evita continuar con una imagen inexistente.

```python
lower_green = np.array([0, 100, 0], dtype=np.uint8)
```

`np.array` crea un arreglo de números. `dtype=np.uint8` indica que sus valores son enteros de ocho bits sin signo, entre 0 y 255. En estos límites se interpreta cada posición así:

| Canal BGR | Mínimo | Máximo | Qué estamos pidiendo |
| --- | --- | --- | --- |
| B: azul | 0 | 120 | No demasiado azul. |
| G: verde | 100 | 255 | Una intensidad verde suficiente. |
| R: rojo | 0 | 120 | No demasiado rojo. |

```python
mask = cv2.inRange(frame, lower_green, upper_green)
```

`cv2.inRange` recibe `frame` y ambos límites. Acepta un píxel solo cuando **los tres canales** están dentro de sus intervalos, incluidos los extremos. Por ejemplo, BGR `[40, 180, 50]` se acepta; `[40, 80, 50]` se rechaza porque G no llega a 100. Son ejemplos numéricos para entender la regla, no medidas de tu hoja.

La salida `mask` tiene el mismo alto y ancho que el fotograma, pero un solo canal. Sus valores son 0 o 255. Por eso la hoja seleccionada aparece blanca en la máscara, aunque en la cámara siga siendo verde.

```python
cv2.imshow("Camara web", frame)
cv2.imshow("Mascara original", mask)
if cv2.waitKey(1) & 0xFF == 27:
    break

# Al salir del ciclo:
cap.release()
cv2.destroyAllWindows()
```

`imshow` abre o actualiza las ventanas. `waitKey` atiende sus eventos y consulta el teclado. Si ESC tiene código 27, `break` termina el ciclo. Al final, `release` libera la cámara y `destroyAllWindows` cierra las ventanas.

### Qué dificultad puedes observar

Haz una sombra suave sobre la hoja. Sus intensidades cambian: una zona verde oscura puede tener G menor que 100 y desaparecer. Un reflejo claro puede elevar B o R por encima de 120. Ampliar esos límites puede recuperar partes de la hoja, pero también aceptar más fondo.

Un filtro BGR puede funcionar bien en condiciones controladas. La dificultad es que estamos ajustando intensidades de tres componentes, no un tono y su brillo por separado.

## 3. Calibrador BGR: ajustar el filtro sin editar números a mano

Este programa aplica el mismo filtro sencillo, pero permite cambiar sus seis límites mientras observas la cámara. Las barras B, G y R controlan **azul, verde y rojo**, en ese orden. Todas recorren valores de **0 a 255**. No convierte el fotograma a otro modelo de color.

Utiliza **Windows 11, Python 3.12.10, `opencv-python` y NumPy** en el equipo local. Las ventanas HighGUI y sus barras no están disponibles en las variantes *headless*. Ejecuta desde VS Code o la consola de Windows, no desde Colab ni WSL para esta práctica. Cierra cualquier otro programa que use la cámara.

Guarda el siguiente programa completo como `calibrar_verde_bgr.py`. Empieza con los mismos límites del filtro: mínimo `[0, 100, 0]` y máximo `[120, 255, 120]`.

```python
import cv2
import numpy as np


# OpenCV llama a esta función cuando se mueve una barra.
# No necesitamos hacer nada aquí: leeremos las barras en el ciclo.
def al_cambiar(valor):
    pass


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()


# Creamos una ventana antes de agregar sus barras.
cv2.namedWindow("Ajustes BGR", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Ajustes BGR", 700, 180)

# Damos contenido a la ventana que alojará las barras en Windows.
panel = np.zeros((100, 700, 3), dtype=np.uint8)
cv2.putText(
    panel, "Mueve las seis barras y observa la mascara.",
    (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1
)
cv2.putText(
    panel, "P: imprimir valores en terminal | ESC: salir",
    (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1
)
cv2.imshow("Ajustes BGR", panel)

# Nombre de la barra, ventana, valor inicial, máximo y función.
# Empezamos con el mismo intervalo BGR verde de este capítulo.
cv2.createTrackbar("B minimo", "Ajustes BGR", 0, 255, al_cambiar)
cv2.createTrackbar("B maximo", "Ajustes BGR", 120, 255, al_cambiar)
cv2.createTrackbar("G minimo", "Ajustes BGR", 100, 255, al_cambiar)
cv2.createTrackbar("G maximo", "Ajustes BGR", 255, 255, al_cambiar)
cv2.createTrackbar("R minimo", "Ajustes BGR", 0, 255, al_cambiar)
cv2.createTrackbar("R maximo", "Ajustes BGR", 120, 255, al_cambiar)


while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo leer el video.")
        break

    # Leemos la posición actual de cada barra.
    b_min = cv2.getTrackbarPos("B minimo", "Ajustes BGR")
    b_max = cv2.getTrackbarPos("B maximo", "Ajustes BGR")
    g_min = cv2.getTrackbarPos("G minimo", "Ajustes BGR")
    g_max = cv2.getTrackbarPos("G maximo", "Ajustes BGR")
    r_min = cv2.getTrackbarPos("R minimo", "Ajustes BGR")
    r_max = cv2.getTrackbarPos("R maximo", "Ajustes BGR")

    lower_green = np.array([b_min, g_min, r_min], dtype=np.uint8)
    upper_green = np.array([b_max, g_max, r_max], dtype=np.uint8)

    # Cada mínimo debe ser menor o igual que su máximo.
    rango_valido = b_min <= b_max and g_min <= g_max and r_min <= r_max

    if rango_valido:
        # Seguimos trabajando con un intervalo y una máscara.
        mask = cv2.inRange(frame, lower_green, upper_green)
    else:
        # Mostramos negro y avisamos si se cruzaron los límites.
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)

    # Copiamos la cámara para escribir los valores sin modificar el fotograma original.
    preview = frame.copy()

    cv2.putText(
        preview, f"Min BGR: {lower_green.tolist()}",
        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2
    )
    cv2.putText(
        preview, f"Max BGR: {upper_green.tolist()}",
        (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2
    )

    if rango_valido:
        mensaje = "P: copiar valores en terminal | ESC: salir"
        color = (255, 255, 255)
    else:
        mensaje = "Rango invalido: cada minimo debe ser <= a su maximo"
        color = (0, 0, 255)

    cv2.putText(
        preview, mensaje, (10, 90),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2
    )

    cv2.imshow("Camara y valores BGR", preview)
    cv2.imshow("Mascara calibrada", mask)

    key = cv2.waitKey(1) & 0xFF

    # P imprime las dos líneas listas para copiar al programa del filtro.
    if key == ord("p") or key == ord("P"):
        if rango_valido:
            print("\nCopia estas líneas en el filtro:")
            print(f"lower_green = np.array({lower_green.tolist()}, dtype=np.uint8)")
            print(f"upper_green = np.array({upper_green.tolist()}, dtype=np.uint8)")
        else:
            print("Corrige los límites: cada mínimo debe ser <= a su máximo.")

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()
```

### Cómo calibrar con la hoja

1. Coloca la hoja verde con iluminación uniforme y comprueba que el fondo no sea verde.
2. Observa «Mascara calibrada»: la hoja debería quedar blanca y el fondo negro.
3. Si se pierde verde oscuro, prueba bajar **G mínimo**. Si aparecen zonas que no buscas, revierte el cambio y observa qué otros canales cumplen el intervalo.
4. Si una parte clara de la hoja desaparece, prueba subir **B máximo** o **R máximo**, de uno en uno. Un reflejo puede aumentar los tres componentes y confundirse con superficies claras del fondo.
5. Cambia distancia y orientación suavemente. No calibres para una única posición de la hoja.
6. Con un intervalo válido, selecciona una ventana de OpenCV y pulsa **P**. Copia las líneas impresas en la terminal en lugar de `lower_green` y `upper_green` del archivo `filtro_verde_bgr.py`.
7. Pulsa ESC para liberar la cámara. Ejecuta el filtro sencillo con esos límites y comprueba el resultado.

P no guarda archivos: solo imprime las dos asignaciones para copiarlas. Al reiniciar, las barras vuelven a sus valores iniciales. Conserva las líneas antes de cerrar la terminal. **Los valores obtenidos aquí son BGR**; no los uses como límites HSV en el siguiente capítulo.

### Qué hace cada parte del calibrador

```python
def al_cambiar(valor):
    pass

cv2.createTrackbar("G minimo", "Ajustes BGR", 100, 255, al_cambiar)
```

`al_cambiar` es la función de aviso que OpenCV recibe al crear la barra. Se entrega su nombre sin paréntesis para que OpenCV pueda llamarla cuando cambie la posición. En este ejemplo no realiza operaciones: `pass` deja su cuerpo vacío, porque las posiciones se leen en cada vuelta del video.

```python
g_min = cv2.getTrackbarPos("G minimo", "Ajustes BGR")
lower_green = np.array([b_min, g_min, r_min], dtype=np.uint8)
upper_green = np.array([b_max, g_max, r_max], dtype=np.uint8)
mask = cv2.inRange(frame, lower_green, upper_green)
```

`getTrackbarPos` obtiene el valor actual de una barra. `np.array` reúne los tres mínimos o máximos en orden B, G y R. `inRange` compara el fotograma BGR directamente: exige que **los tres canales** estén entre sus límites, incluidos los extremos.

```python
rango_valido = b_min <= b_max and g_min <= g_max and r_min <= r_max
mask = np.zeros(frame.shape[:2], dtype=np.uint8)
```

La primera línea comprueba que ningún mínimo supere su máximo. La segunda se utiliza **en la rama de intervalo inválido**: crea una máscara negra de alto y ancho iguales al fotograma. Si aparece un aviso rojo, corrige las barras antes de buscar un problema de iluminación. No se intercambian límites automáticamente.

```python
preview = frame.copy()
cv2.putText(
    preview, f"Min BGR: {lower_green.tolist()}",
    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2
)
print(f"lower_green = np.array({lower_green.tolist()}, dtype=np.uint8)")
```

`copy()` permite escribir en una copia del video. `tolist()` presenta los números del arreglo como una lista, `putText` los dibuja sobre la copia y `print` escribe una asignación en la terminal cuando pulsas P. El prefijo `f` inserta los valores actuales en el texto.

```python
key = cv2.waitKey(1) & 0xFF
if key == ord("p") or key == ord("P"):
```

`waitKey` atiende las ventanas y consulta una tecla. `ord` obtiene el código de cada letra para admitir P mayúscula o minúscula. Esta condición pertenece al ciclo del programa completo; la ventana de OpenCV debe tener el foco. ESC termina el ciclo y después se liberan cámara y ventanas.

### Comprobación en Windows

Comprueba que aparezcan «Ajustes BGR», «Camara y valores BGR» y «Mascara calibrada», con seis barras cuyo máximo sea 255. Mueve una barra y verifica que cambien el número y la máscara cuando corresponda. Cruza un mínimo con su máximo: debe aparecer el aviso y la máscara negra. Corrígelo y pulsa P para verificar las dos líneas en la terminal. Sal con ESC y vuelve a ejecutar para comprobar que la cámara quedó libre.

## 4. Qué dificultad aparece con BGR

Bajar G mínimo puede recuperar una zona verde oscura, pero también ampliar la selección a colores que no deseas. Subir B máximo y R máximo puede recuperar una parte clara de la hoja y, a la vez, aceptar fondo. Las barras ayudan a observarlo, pero no cambian la regla: seguimos comparando tres intensidades independientes.

Esto justifica estudiar otra representación. En el siguiente capítulo separaremos tono, saturación y brillo con HSV para poder ajustar cada aspecto de la selección con un significado más directo. Un filtro BGR puede bastar si la escena y la luz están controladas.

## 5. Resultado esperado y diagnóstico

En el video verás la hoja verde y en la máscara su región mayormente blanca. La máscara marca píxeles seleccionados; no reconoce la hoja como objeto ni mantiene su color original.

| Problema | Qué revisar primero |
| --- | --- |
| No hay video | Cámara, permisos y lectura del tema 04. |
| Máscara negra sin aviso | Iluminación y límites BGR demasiado restrictivos. |
| Máscara negra con aviso rojo | Algún mínimo es mayor que su máximo. |
| Demasiado fondo blanco | Colores del fondo y amplitud de los tres intervalos. |
| P o ESC no responden | Haz clic en una ventana de OpenCV para darle el foco. |

## Comprueba que lo entendiste

- ¿Por qué el orden de los límites es B, G y R aunque normalmente digamos RGB?
- ¿Qué representan los píxeles blancos de la máscara?
- ¿Por qué bajar G mínimo puede recuperar sombra y también aceptar más fondo?
- ¿Qué cambia cuando mueves una barra y qué debes copiar después de pulsar P?
- ¿Por qué todavía no estamos filtrando directamente por tono?

## Consulta: funciones del filtro y del calibrador BGR


Las funciones de cámara y visualización se describen en el [tema 04](04-video-camara-python.md). Aquí nos centraremos en seleccionar píxeles y leer las barras. Las formas de llamada se muestran simplificadas: no necesitas escribir todos los parámetros opcionales.

### `np.array`: construir los límites

```python
lower_green = np.array([0, 100, 0], dtype=np.uint8)
```

Forma habitual en estas prácticas: `np.array(object, dtype=np.uint8)`.

| Parámetro | Necesidad | Qué utiliza el curso |
| --- | --- | --- |
| `object` | Obligatorio. | Lista de tres números, como `[0, 100, 0]`. |
| `dtype` | Opcional en NumPy. | `np.uint8`, enteros sin signo entre 0 y 255, adecuados para estos límites. |

**Devuelve:** un arreglo de NumPy. El orden de sus números depende del modelo de la imagen que filtrarás. La función no sabe que esa lista significa BGR; solo construye números. No convierte grados ni calibra el color automáticamente.

Sin indicar `dtype`, NumPy elige un tipo según los datos. En el curso lo hacemos explícito. No uses números negativos ni mayores que 255 esperando que el tipo los corrija: prepara valores válidos.

### `cv2.inRange`: seleccionar por intervalos

```python
mask = cv2.inRange(frame, lower_green, upper_green)
```

Forma: `cv2.inRange(src, lowerb, upperb, dst=None)`.

| Parámetro | Necesidad | Qué representa |
| --- | --- | --- |
| `src` | Obligatorio. | Imagen a comparar: BGR en este capítulo. |
| `lowerb` | Obligatorio. | Límite inferior de cada canal. |
| `upperb` | Obligatorio. | Límite superior de cada canal. |
| `dst` | Opcional. | Destino de la máscara. En las prácticas se omite. |

**Devuelve:** una máscara de un canal de ocho bits: 255 donde se cumplen todos los intervalos y 0 donde no. Los límites se incluyen: un píxel que coincide con el mínimo puede ser aceptado.

**Uso común:** filtrar colores con límites calibrados, como `lower_green` y `upper_green`. También permite intervalos sobre otros datos, pero no detecta clases ni separa objetos por sí sola. Un mínimo mayor que su máximo no representa un intervalo circular y no se corrige automáticamente.

### `cv2.namedWindow`: preparar una ventana

```python
cv2.namedWindow("Ajustes BGR", cv2.WINDOW_NORMAL)
```

Forma: `cv2.namedWindow(winname, flags=cv2.WINDOW_AUTOSIZE)`.

`winname` es el nombre necesario para identificar la ventana. `flags` es opcional: `WINDOW_AUTOSIZE` ajusta la ventana al contenido; `WINDOW_NORMAL` permite redimensionarla. El calibrador elige `WINDOW_NORMAL` para acomodar los controles. **No devuelve una imagen**.

### `cv2.resizeWindow`: proponer el tamaño

```python
cv2.resizeWindow("Ajustes BGR", 700, 180)
```

En la forma usada recibe `winname`, `width` y `height`: nombre, ancho y alto del área de imagen solicitada, en píxeles. La ventana debe existir y permitir redimensionamiento. El tamaño exterior final también depende de controles, bordes y sistema operativo. Esta función cambia la ventana; **no redimensiona el arreglo de la imagen**.

### `cv2.createTrackbar`: agregar una barra

```python
cv2.createTrackbar("G minimo", "Ajustes BGR", 100, 255, al_cambiar)
```

Forma de Python: `cv2.createTrackbar(trackbarname, winname, value, count, onChange)`.

| Parámetro | Qué debes entregar |
| --- | --- |
| `trackbarname` | Nombre de la barra; debe identificarla dentro de la ventana. |
| `winname` | Nombre de una ventana que ya exista. |
| `value` | Posición inicial, como 0 para B mínimo. |
| `count` | Posición máxima: 255 para B, G y R. |
| `onChange` | Función que recibirá la posición al mover la barra, aquí `al_cambiar`. |

Esta forma necesita esos cinco argumentos. La barra recorre valores enteros desde 0 hasta `count`; no significa que necesites arrastrarla hasta ambos extremos para calibrar. Su posición se lee por separado.

`onChange` es una función de aviso o *callback*: OpenCV la llama cuando corresponde. En el curso contiene `pass` porque consultamos todas las posiciones dentro del ciclo. Entregamos el nombre de la función, sin paréntesis. Crear una barra no cambia por sí solo los límites del filtro: el programa debe leerla y reconstruirlos.

### `cv2.getTrackbarPos`: leer una barra

```python
g_min = cv2.getTrackbarPos("G minimo", "Ajustes BGR")
```

Necesita `trackbarname` y `winname`, con los mismos nombres utilizados al crearla. **Devuelve:** la posición entera actual. La consultamos cada fotograma para que el filtro responda al movimiento. No devuelve los seis límites juntos: cada llamada lee una barra.

### `np.zeros`: crear el panel o una máscara negra

```python
panel = np.zeros((100, 700, 3), dtype=np.uint8)
```

Forma de uso del curso: `np.zeros(shape, dtype=np.uint8)`. `shape` indica las dimensiones necesarias y `dtype` es opcional; si lo omites, NumPy suele utilizar números decimales de doble precisión, no ocho bits.

**Devuelve:** un arreglo lleno de ceros. Con forma `(100, 700, 3)` creamos un panel de color negro de alto 100 y ancho 700. Con `frame.shape[:2]` creamos una imagen negra de un canal con el alto y ancho de la cámara. No confíes en que una imagen negra indique siempre que no hay verde: el calibrador también la utiliza al avisar que los límites son inválidos.

El dibujo de valores utiliza `putText`, cuya ficha completa está en el [tema 09](09-detectar-figuras.md). `.copy()` se detalla en el [tema 08](08-contornos.md). En el calibrador sirven para escribir números sobre una copia del video; no modifican la selección BGR ya calculada.


## Para dar el siguiente paso

Ya seleccionamos la hoja utilizando intensidades BGR. En [Modelos de color](06-modelos-color.md) convertiremos esa misma imagen a HSV, compararemos sus rangos y construiremos otro filtro con su propio calibrador.

[Anterior](04-video-camara-python.md) · [Índice](../README.md) · [Siguiente: Modelos de color](06-modelos-color.md)
