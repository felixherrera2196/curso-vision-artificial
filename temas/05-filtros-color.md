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

## 3. Extra: calibrador BGR

Esta herramienta auxiliar permite ajustar los límites BGR con barras y ver cómo cambia la máscara en tiempo real. Guarda el código como `calibrar_verde_bgr.py` y ejecútalo en el mismo entorno local de las prácticas. Cierra antes cualquier otro programa que use la cámara.

Mueve las barras hasta seleccionar la hoja, pulsa **P** con una ventana de OpenCV seleccionada para imprimir los límites y cópialos al filtro BGR de este capítulo. Pulsa **ESC** para salir. P solo imprime los valores; no modifica el archivo del filtro.

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
cv2.putText(panel, "Mueve las seis barras y observa la mascara.", (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
cv2.putText(panel, "P: imprimir valores en terminal | ESC: salir", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
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

    cv2.putText(preview, f"Min BGR: {lower_green.tolist()}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(preview, f"Max BGR: {upper_green.tolist()}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    if rango_valido:
        mensaje = "P: copiar valores en terminal | ESC: salir"
        color = (255, 255, 255)
    else:
        mensaje = "Rango invalido: cada minimo debe ser <= a su maximo"
        color = (0, 0, 255)

    cv2.putText(preview, mensaje, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

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
- ¿Qué valores debes ajustar para cambiar qué píxeles acepta el filtro?
- ¿Por qué todavía no estamos filtrando directamente por tono?

## Consulta: funciones del filtro BGR


Las funciones de cámara y visualización se describen en el [tema 04](04-video-camara-python.md). Aquí nos centraremos en seleccionar píxeles. Las formas de llamada se muestran simplificadas: no necesitas escribir todos los parámetros opcionales.

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

## Para dar el siguiente paso

Ya seleccionamos la hoja utilizando intensidades BGR. En [Modelos de color](06-modelos-color.md) convertiremos esa misma imagen a HSV, compararemos sus rangos y construiremos otro filtro con su propio calibrador.

[Anterior](04-video-camara-python.md) · [Índice](../README.md) · [Siguiente: Modelos de color](06-modelos-color.md)
