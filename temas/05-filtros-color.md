# 05. Filtros de color

## Qué aprenderás

Aprenderás a seleccionar el color de una hoja frente a la cámara. Primero utilizarás el fotograma sin convertir su modelo de color; después lo convertirás a HSV para comparar cómo se definen los límites.

## La idea en palabras sencillas

Una máscara es una imagen blanca y negra que responde una pregunta en cada posición: «¿este píxel cumple la regla del color?». Blanco significa sí; negro significa no. La máscara no reconoce todavía una hoja como objeto: también puede seleccionar una camisa o un fondo del mismo color.

## 1. Preparar la escena del laboratorio

Utilizaremos una **hoja verde, preferentemente mate y de color intenso**, porque su tono se puede seleccionar con un único intervalo HSV. Los dos programas de esta clase y las prácticas de morfología utilizarán el mismo color.

1. Coloca la hoja frente a la cámara, sin pegarla al lente, y comprueba que esté enfocada.
2. Busca una iluminación uniforme. Evita reflejos fuertes o una ventana muy brillante detrás.
3. Procura que el fondo no sea verde. Una mesa o pared de otro color facilitará la comparación.
4. Deja visibles los bordes de la hoja: nos servirán para observar las máscaras.
5. Ejecuta un programa a la vez y ciérralo con ESC antes de abrir el siguiente.

La elección de verde simplifica los ejemplos; no garantiza una selección perfecta en cualquier cámara. Los intervalos son puntos de partida para calibrar en el laboratorio.

## 2. Primera práctica: filtro directo en BGR

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

`import cv2` permite utilizar OpenCV y `import numpy as np` permite crear los arreglos de límites. `cap` conserva la conexión con la cámara. Antes del ciclo, `isOpened()` comprueba que la conexión pudo abrirse.

`while True` repite la captura. En cada vuelta, `ret` indica si hubo lectura correcta y `frame` contiene el fotograma actual. El bloque `if not ret` evita continuar con una imagen inexistente.

`np.array` crea un arreglo de números. `dtype=np.uint8` indica que sus valores son enteros de ocho bits sin signo, entre 0 y 255. En estos límites se interpreta cada posición así:

| Canal BGR | Mínimo | Máximo | Qué estamos pidiendo |
| --- | --- | --- | --- |
| B: azul | 0 | 120 | No demasiado azul. |
| G: verde | 100 | 255 | Una intensidad verde suficiente. |
| R: rojo | 0 | 120 | No demasiado rojo. |

`cv2.inRange` recibe `frame` y ambos límites. Acepta un píxel solo cuando **los tres canales** están dentro de sus intervalos, incluidos los extremos. Por ejemplo, BGR `[40, 180, 50]` se acepta; `[40, 80, 50]` se rechaza porque G no llega a 100. Son ejemplos numéricos para entender la regla, no medidas de tu hoja.

La salida `mask` tiene el mismo alto y ancho que el fotograma, pero un solo canal. Sus valores son 0 o 255. Por eso la hoja seleccionada aparece blanca en la máscara, aunque en la cámara siga siendo verde.

`imshow` abre o actualiza las ventanas. `waitKey` atiende sus eventos y consulta el teclado. Si ESC tiene código 27, `break` termina el ciclo. Al final, `release` libera la cámara y `destroyAllWindows` cierra las ventanas.

### Qué dificultad puedes observar

Haz una sombra suave sobre la hoja. Sus intensidades cambian: una zona verde oscura puede tener G menor que 100 y desaparecer. Un reflejo claro puede elevar B o R por encima de 120. Ampliar esos límites puede recuperar partes de la hoja, pero también aceptar más fondo.

Un filtro BGR puede funcionar bien en condiciones controladas. La dificultad es que estamos ajustando intensidades de tres componentes, no un tono y su brillo por separado.

## 3. Segunda práctica: un solo intervalo HSV

HSV organiza el color mediante H, tono; S, saturación o qué tan alejado está de un gris; y V, valor o brillo. En la conversión de ocho bits usada aquí, H va de 0 a 179 y S y V de 0 a 255.

Guarda este segundo programa como `filtro_verde_hsv.py`. Utiliza la misma hoja y escena. Cierra el programa BGR antes de ejecutarlo.

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

    # Convertimos el fotograma de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Un único intervalo para el verde: H, S y V
    lower_green = np.array([35, 80, 60], dtype=np.uint8)
    upper_green = np.array([85, 255, 255], dtype=np.uint8)

    # Seleccionamos el verde en una sola máscara
    mask = cv2.inRange(hsv, lower_green, upper_green)


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

### Qué cambió respecto al primer programa

La captura, las ventanas y la salida son iguales. El cambio empieza en `cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)`, que guarda en `hsv` una representación HSV del fotograma. `frame` sigue disponible en BGR para mostrar el video original.

Ahora `inRange` recibe **`hsv`**, no `frame`. Los límites ya no significan azul, verde y rojo:

| Canal HSV | Mínimo | Máximo | Función del intervalo |
| --- | --- | --- | --- |
| H: tono | 35 | 85 | Seleccionar una zona amplia alrededor del verde. |
| S: saturación | 80 | 255 | Excluir colores demasiado cercanos al gris. |
| V: valor | 60 | 255 | Excluir zonas muy oscuras. |

Un píxel HSV `[60, 180, 150]` cumple las tres condiciones. `[60, 30, 150]` no cumple S y `[60, 180, 40]` no cumple V. Ajustar H no arreglaría esos dos rechazos.

Los valores 35 y 85 no son porcentajes ni grados escritos directamente: pertenecen a la escala de H de OpenCV. No compares una imagen BGR con estos límites HSV; los números tendrían significados distintos.

### Por qué usamos verde y un solo intervalo

El tono es circular, como los números de una carátula de reloj. En HSV el rojo está cerca de la unión entre el comienzo y el final de la escala, por lo que una selección amplia de rojos puede necesitar dos intervalos. El verde que seleccionamos está en una zona continua, lejos de esa unión. Por eso basta **una llamada a `inRange` y una máscara**.

En esta práctica no hay que unir máscaras ni aprender una operación extra para resolver el color. Nos centraremos en observar la selección. El mismo filtro HSV se reutilizará en las operaciones morfológicas.

## 4. Comparar ambos programas

| Aspecto | BGR directo | HSV |
| --- | --- | --- |
| Entrada al filtro | `frame`, sin conversión. | `hsv`, después de convertir. |
| Significado de los límites | Azul, verde y rojo. | Tono, saturación y brillo. |
| Número de máscaras | Una. | Una. |
| Ajuste de iluminación | Puede necesitar cambios en varios componentes. | Puede ajustarse V conservando inicialmente el intervalo H. |

La ventaja de HSV es facilitar la descripción del color. No hace que el programa sea inmune a sombras, reflejos, luz coloreada o exposición automática. Los dos filtros necesitan calibración. Además, sus intervalos no seleccionan exactamente los mismos colores: una diferencia puede deberse tanto a la representación como a los valores elegidos.

## 5. Calibración guiada con la hoja

1. Ejecuta un programa y observa la hoja con la luz normal del laboratorio.
2. Comprueba si la máscara incluye la hoja y excluye el fondo.
3. Cambia suavemente la orientación para observar reflejos y sombras.
4. En HSV, si aceptas otros tonos, ajusta H; si seleccionas grises, revisa S; si pierdes partes oscuras, revisa V.
5. Cambia un límite a la vez, guarda el archivo y vuelve a ejecutar. No cambies los tres canales simultáneamente.
6. Registra qué valor cambiaste, qué parte recuperaste y si apareció fondo no deseado.

Si necesitas editar el programa, ciérralo primero con ESC. No aumentes el máximo de H por encima de 179 en esta conversión. Mantén cada mínimo menor o igual que su máximo.

## 6. Resultado esperado y problemas frecuentes

En el video verás la hoja verde; en la máscara, su región será mayormente blanca y el fondo mayormente negro. Puede haber pequeñas imperfecciones: la siguiente parte del curso permitirá estudiar su limpieza.

**Máscara negra:** revisa luz, hoja, límites y modelo de color. **Demasiado fondo blanco:** busca regiones verdes del entorno y revisa el intervalo. **Hoja fragmentada:** examina sombras, reflejos y límites muy estrictos. **No hay video:** vuelve al diagnóstico de captura del tema 04 antes de cambiar el filtro.

Ambos programas muestran una máscara, no una imagen en la que solo la hoja conserve su color. Seleccionar píxeles, limpiar la selección y reconocer figuras son etapas distintas.

## Comprueba que lo entendiste

- ¿Por qué usamos BGR directamente en el primer programa?
- ¿Qué representa un píxel blanco en la máscara?
- ¿Qué recibe `inRange` en cada programa?
- ¿Por qué el verde permite trabajar con un solo intervalo HSV?
- ¿Cómo comprobarías si un fallo corresponde al filtro o a la cámara?

[Anterior](04-video-camara-python.md) · [Índice](../README.md) · [Siguiente: Modelos de color](06-modelos-color.md)
