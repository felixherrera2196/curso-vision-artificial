# 07. Operaciones morfológicas

## Qué aprenderás

Practicarás erosión, dilatación y una secuencia de erosión seguida de dilatación sobre una máscara binaria. También conocerás, en el texto, los nombres de otras operaciones. Comprenderás cómo el tamaño del elemento estructurante cambia el resultado y por qué limpiar una máscara puede mejorar, o perjudicar, la detección de formas.

## La idea en palabras sencillas

Mira una máscara como una hoja negra con recortes blancos. Puede tener puntos blancos sueltos que sobran o agujeros negros dentro de una región blanca. Las operaciones de esta sección ayudan a modificar esos defectos pequeños.

La erosión encoge lo blanco y la dilatación lo expande. Combinándolas en diferente orden obtenemos apertura y cierre. El kernel es la pequeña plantilla que determina qué vecinos se examinan. Estas operaciones no saben qué objeto buscas: también pueden borrar una parte importante. Por eso compararás siempre la máscara antes y después.

## 1. El problema que queremos resolver

Una máscara de color puede contener puntos aislados, bordes irregulares o huecos dentro del objeto. Si obtenemos contornos directamente, esos defectos pueden producir muchas regiones pequeñas o dividir un objeto en varias partes.

La **morfología matemática** modifica regiones utilizando su estructura espacial. En el curso trabajaremos principalmente sobre máscaras binarias, aunque OpenCV también permite operaciones morfológicas en imágenes con otros valores.

Siempre identifica qué representa el primer plano. Aquí asumimos que el objeto está marcado en blanco y el fondo en negro. Si la máscara está invertida, las mismas operaciones afectarán a la región opuesta.

## 2. El elemento estructurante o kernel

El **kernel** define el vecindario que se examina alrededor de cada píxel. Puede tener forma rectangular, elíptica o de cruz. Su tamaño determina la escala de los detalles que se eliminarán, expandirán o conectarán.

Un kernel pequeño produce cambios locales; uno grande puede borrar objetos pequeños o unir objetos que deberían permanecer separados. No existe un tamaño correcto independiente de la resolución. Un kernel de cinco píxeles actúa de manera diferente cuando el objeto mide veinte píxeles que cuando mide doscientos.

También influye el número de iteraciones. Repetir una operación aumenta su efecto, pero no convierte cualquier kernel en equivalente a otro de forma distinta. Conviene ajustar con la máscara visible y documentar el motivo de cada valor.

## 3. Erosión

La erosión reduce las regiones del primer plano. De forma intuitiva, un píxel conserva su condición de primer plano cuando el vecindario definido por el kernel cabe dentro de la región, según la operación y sus condiciones de borde.

Esto elimina puntos blancos pequeños y adelgaza objetos. También puede separar regiones unidas por un puente estrecho. Su riesgo es borrar detalles legítimos, como una punta delgada o un objeto pequeño, y modificar el área medida después.

## 4. Dilatación

La dilatación expande el primer plano. Una región puede ocupar píxeles cercanos de acuerdo con la forma del kernel. Ayuda a cerrar discontinuidades pequeñas y a unir partes cercanas.

También agranda ruido y puede fusionar objetos distintos. Si dos figuras se tocan después de dilatar, el análisis de contornos podría interpretarlas como una sola región. Por eso no basta con que la imagen «se vea más sólida»: hay que comprobar que conserva los objetos separados.

## 5. Otras operaciones: apertura

La apertura aplica **erosión seguida de dilatación**, utilizando el elemento estructurante correspondiente. La primera operación elimina regiones pequeñas o detalles que no sobreviven al kernel; la segunda recupera parte del tamaño de las regiones restantes.

No restaura todo lo que borró la erosión. Esa es precisamente su utilidad para quitar puntos aislados. Si un detalle real desaparece en la primera etapa, no se recupera automáticamente en la segunda.

## 6. Otras operaciones: cierre

El cierre aplica **dilatación seguida de erosión**. Se utiliza para cubrir huecos pequeños y discontinuidades del primer plano. Puede mejorar una máscara con vacíos producidos por reflejos o variaciones de color.

El cierre no reconstruye la identidad de un objeto: solo actúa según proximidad espacial. Si el hueco es grande o si el kernel conecta regiones diferentes, el resultado puede ser incorrecto para la tarea.

| Operación | Efecto habitual sobre primer plano blanco | Riesgo principal |
| --- | --- | --- |
| Erosión | Reducir y eliminar detalles pequeños. | Perder objetos o partes delgadas. |
| Dilatación | Expandir y conectar regiones cercanas. | Unir objetos separados. |
| Apertura | Quitar puntos pequeños del primer plano. | Borrar detalles reales. |
| Cierre | Cubrir huecos o pequeñas interrupciones. | Alterar separaciones y geometría. |

## 7. Dónde se utiliza en el curso

El recorrido habitual será fotograma, conversión de color, máscara, morfología y contornos. Mantén visible la máscara original y la procesada mientras ajustas parámetros. Si solo observas el resultado final, será más difícil descubrir qué operación eliminó información.

En OpenCV, `erode`, `dilate` y `morphologyEx` permiten realizar estas operaciones. `getStructuringElement` ayuda a definir kernels con formas comunes. Al aplicarlas, identifica siempre la máscara de entrada, la forma del kernel y el número de iteraciones.

## Actividad de comprensión

Busca tres defectos distintos: puntos fuera del objeto, huecos dentro del objeto y dos objetos muy cercanos. Propón una operación para los dos primeros y explica por qué debes tener cuidado con el tercero. Compara antes y después, incluyendo objetos pequeños.

## Preparación de la práctica

Utiliza como entrada la máscara del [filtro verde HSV del tema 05](05-filtros-color.md), con un único intervalo. Conserva una vista de la máscara sin procesar. Practica primero cada operación por separado y después la secuencia indicada a continuación.

## Ejercicio guiado sin programar

Dibuja un rectángulo blanco grande sobre una hoja negra, varios puntos blancos pequeños fuera y un agujero negro pequeño dentro. Ese dibujo representa una máscara.

1. Imagina que una goma reduce un poco todos los bordes blancos: es la erosión. Los puntos pequeños pueden desaparecer y el agujero crece.
2. Ahora imagina que un marcador engrosa lo blanco: es la dilatación. Los puntos crecen y el agujero puede reducirse.
3. Para quitar puntos, prueba mentalmente erosión seguida de dilatación: apertura. Los puntos eliminados no reaparecen solo por expandir lo que queda.
4. Para cubrir un hueco pequeño, prueba dilatación seguida de erosión: cierre.

Estas son analogías para entender la dirección del cambio. En el programa, el resultado exacto depende de la forma y tamaño del kernel y de cómo estén conectados los píxeles. Cuando observes una máscara real, busca primero el defecto que quieres corregir y después elige la operación.

**Resultado que debes comprobar:** menos puntos o huecos, conservando la figura principal. Si dos objetos pasan a ser una sola mancha, la limpieza alteró información importante y necesitas reducir su efecto.


## Orden de las prácticas del laboratorio

Guarda los tres programas en archivos diferentes: `erosion_verde.py`, `dilatacion_verde.py` y `erosion_dilatacion_verde.py`. Cierra cada ejecución con ESC antes de abrir la siguiente. Utiliza la misma hoja verde y el mismo intervalo HSV del tema 05.

## Práctica 1. Erosión sola

### Qué vas a hacer

Seleccionarás la hoja verde y reducirás las regiones blancas de su máscara. No se modifica la imagen de color ni se reduce el tamaño de toda la imagen: se cambian los píxeles que permanecen blancos.

```python
# Importamos las herramientas para la cámara y los arreglos
import cv2
import numpy as np

# Abrimos la cámara principal
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

# Plantilla cuadrada de cinco filas y cinco columnas
kernel = np.ones((5, 5), np.uint8)

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

    # Reducimos las regiones blancas
    mask_eroded = cv2.erode(mask, kernel, iterations=1)

    # Mostramos el video y la selección sin procesar
    cv2.imshow("Camara web", frame)
    cv2.imshow("Mascara original", mask)
    cv2.imshow("Mascara con erosion", mask_eroded)

    # ESC termina la ejecución
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Dejamos disponible la cámara y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()
```

### Explicación paso a paso

1. Las importaciones y la captura son las mismas que en los temas anteriores. `ret` comprueba cada lectura; `frame` contiene su imagen.
2. Antes del ciclo, `np.ones((5, 5), np.uint8)` crea una plantilla llamada `kernel`: cinco filas y cinco columnas con 25 posiciones activas. Los unos indican dónde examinar vecinos; no son el color del resultado.
3. Dentro del ciclo se convierte a HSV y se crea **una máscara** con el intervalo verde. Si cambias los límites al calibrar, utiliza los mismos valores en los tres programas para comparar.
4. `cv2.erode(mask, kernel, iterations=1)` aplica una pasada de erosión. `mask` es la entrada, `kernel` define el vecindario y `iterations` el número de pasadas.
5. `mask_eroded` guarda el resultado sin reemplazar `mask`. Las ventanas permiten comparar ambas.
6. ESC termina el ciclo. Después se libera la cámara y se cierran las ventanas.

### Por qué se reduce lo blanco

Imagina la plantilla centrada en una posición de la máscara. Con este kernel lleno de unos, el píxel de salida se conserva blanco si todos los vecinos examinados son blancos. Si hay uno negro, la salida será negra. Es equivalente a tomar el mínimo de los valores examinados: en una máscara de 0 y 255, un 0 basta para que el mínimo sea 0.

Cerca del borde del objeto, la plantilla alcanza el fondo negro y esas posiciones dejan de ser blancas. Más adentro, donde la plantilla cabe completamente en blanco, la región permanece. Para observarlo sin complicaciones de borde, mantén la hoja lejos de los extremos de la imagen.

Un cuadrado blanco sólido de 9 × 9 píxeles rodeado de negro, lejos del borde de la imagen, queda en 5 × 5 con este kernel de 5 × 5 centrado y una iteración. Un punto diminuto puede desaparecer. Una parte delgada de la hoja también puede perderse: la operación no distingue un defecto de un detalle importante.

### Qué comprobar y qué cambiar

La máscara procesada conserva su alto y ancho, pero la región de la hoja aparece algo más pequeña. Los puntos blancos pequeños pueden desaparecer y los huecos negros pueden agrandarse.

Prueba un kernel de 3 × 3 manteniendo una iteración: la reducción suele ser menor. Después restaura 5 × 5 y prueba dos iteraciones: la reducción aumenta. Cambia solo un parámetro a la vez. Si la máscara original está negra, corrige primero el filtro: la erosión no puede recuperar una hoja que no se seleccionó.

## Práctica 2. Dilatación sola

### Qué vas a hacer

Volverás a partir de la máscara verde original. Esta vez expandirás las regiones blancas. No tienes que ejecutar ni utilizar el resultado del programa de erosión: es una práctica independiente.

```python
# Importamos las herramientas para la cámara y los arreglos
import cv2
import numpy as np

# Abrimos la cámara principal
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

# Plantilla cuadrada de cinco filas y cinco columnas
kernel = np.ones((5, 5), np.uint8)

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

    # Expandimos las regiones blancas
    mask_dilated = cv2.dilate(mask, kernel, iterations=1)

    # Mostramos el video y la selección sin procesar
    cv2.imshow("Camara web", frame)
    cv2.imshow("Mascara original", mask)
    cv2.imshow("Mascara con dilatacion", mask_dilated)

    # ESC termina la ejecución
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Dejamos disponible la cámara y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()
```

### Explicación de la operación

La captura, el filtro y el kernel permanecen iguales. La diferencia es `cv2.dilate(mask, kernel, iterations=1)`. La entrada sigue siendo `mask`; el resultado nuevo se guarda en `mask_dilated`.

Con este kernel, basta que una de las posiciones examinadas sea blanca para que la posición de salida sea blanca. Es equivalente a tomar el máximo: un 255 entre los vecinos hace que el máximo sea 255. Por eso el blanco se extiende hacia posiciones que antes eran negras.

Un cuadrado blanco sólido de 9 × 9 píxeles, rodeado de negro y lejos del borde de la imagen, pasa a 13 × 13 con este kernel centrado de 5 × 5 y una iteración. Un punto blanco aislado también crece: pasa a una región de 5 × 5. Esto explica por qué dilatar puede reforzar una región, pero también agrandar ruido.

### Qué comprobar y qué cambiar

La hoja debe ocupar más espacio blanco en la máscara procesada. Algunos huecos pequeños pueden reducirse. Dos hojas muy cercanas pueden quedar conectadas, aunque físicamente sean objetos distintos.

Prueba 3 × 3 y luego vuelve a 5 × 5. También puedes probar dos iteraciones por separado. Si se unen objetos que querías mantener separados, el efecto es demasiado fuerte para esa escena. No interpretes «más blanco» como «mejor detección» automáticamente.

## Práctica 3. Erosión seguida de dilatación

### Qué vas a hacer

Ahora sí conectarás dos operaciones: primero quitarás partes blancas pequeñas con erosión y después expandirás lo que sobrevivió. El objetivo es observar si desaparecen puntos sin dejar demasiado reducida la región principal de la hoja.

```python
# Importamos las herramientas para la cámara y los arreglos
import cv2
import numpy as np

# Abrimos la cámara principal
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

# Plantilla cuadrada de cinco filas y cinco columnas
kernel = np.ones((5, 5), np.uint8)

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

    # Primero erosionamos la máscara original
    mask_eroded = cv2.erode(mask, kernel, iterations=1)

    # Después dilatamos EL RESULTADO de la erosión
    mask_clean = cv2.dilate(mask_eroded, kernel, iterations=1)

    # Mostramos el video y la selección sin procesar
    cv2.imshow("Camara web", frame)
    cv2.imshow("Mascara original", mask)
    cv2.imshow("Paso 1: erosion", mask_eroded)
    cv2.imshow("Paso 2: erosion seguida de dilatacion", mask_clean)

    # ESC termina la ejecución
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Dejamos disponible la cámara y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()
```

### La línea que conecta ambos pasos

El primer paso recibe la máscara original y produce `mask_eroded`. El segundo recibe **`mask_eroded`**, no `mask`. Ese cambio de entrada es la clave: la dilatación trabaja sobre el resultado de la erosión.

Si ambas funciones recibieran siempre `mask`, habrías calculado dos resultados independientes. En este programa el recorrido es **máscara original → erosión → dilatación del resultado → máscara final**. `mask_clean` es solo el nombre que le damos a esa salida; no garantiza que la máscara esté limpia en cualquier escena.

Las cuatro ventanas muestran la cámara, la máscara original, el paso erosionado y el resultado final. Observa las imágenes en ese orden. No se calcula ningún otro camino ni otra combinación en este programa.

### Por qué el segundo paso no deshace exactamente el primero

Imagina una región blanca grande y un punto blanco pequeño lejos de ella. La erosión puede borrar el punto por completo mientras conserva el interior de la región grande. La dilatación expande lo que quedó, pero no sabe dónde estaba el punto borrado. Si quedó suficientemente separado, no hay blanco allí desde el cual reconstruirlo.

Por eso la región grande puede recuperar parte de su tamaño mientras el punto pequeño sigue ausente. También pueden perderse detalles legítimos, como una punta delgada. El resultado no tiene por qué ser una copia exacta de la máscara original.

En morfología, esta secuencia con el mismo kernel se conoce como **apertura**. Basta reconocer ese nombre cuando lo encuentres; en la práctica nos centraremos en las dos instrucciones explícitas y en su resultado. El **cierre** invierte el orden y existen otras operaciones, descritas arriba como referencia. No necesitas añadirlas al código para completar esta clase.

### Cómo realizar la prueba con hojas de color

1. Coloca una hoja verde de frente, con el fondo de otro color.
2. Comprueba primero que la máscara original selecciona la hoja. Si no lo hace, corrige luz o límites HSV antes de evaluar morfología.
3. Busca puntos blancos pequeños que no correspondan a la hoja. Si no aparecen naturalmente, puedes colocar pequeños recortes verdes separados de la hoja grande; en esta prueba los consideraremos regiones que queremos eliminar.
4. Observa si esos puntos o recortes desaparecen en la erosión y permanecen ausentes en la imagen final. Su tamaño en píxeles importa: un recorte grande puede sobrevivir al kernel.
5. Comprueba que la hoja principal siga presente. Mira también sus esquinas y detalles.
6. Prueba un kernel de 3 × 3 manteniendo una iteración en cada paso. Compara con 5 × 5 sin cambiar el filtro al mismo tiempo.
7. Termina con ESC y conserva los tres archivos por separado.

Una hoja uniforme puede producir ya una máscara bastante limpia. En ese caso los cambios serán principalmente de borde; no necesitas forzar un resultado espectacular. Explica qué observaste y si la limpieza era necesaria.

## Recordatorios para las tres prácticas

Cada fotograma genera una máscara nueva. Una iteración significa una pasada sobre esa máscara, no una acumulación indefinida entre los fotogramas del video. En el tercer programa se aplica una erosión y una dilatación a la máscara de cada fotograma.

Si el objeto está ausente de la máscara original, ninguna de estas operaciones lo recuperará desde una imagen completamente negra. Si el objeto desaparece solo después de erosionar, prueba una plantilla menor o acerca la hoja para que ocupe más píxeles.

Los programas contemplan salida por ESC y por lectura fallida. Como en las prácticas anteriores, una excepción imprevista requeriría una estructura de limpieza adicional, por ejemplo `try` y `finally`.

## Comprueba que lo entendiste

- ¿Qué cambia entre la máscara original y la erosionada?
- ¿Por qué la dilatación puede agrandar puntos que no querías seleccionar?
- ¿Qué variable recibe la dilatación en el tercer programa?
- ¿Por qué una región borrada por erosión no tiene que reaparecer al dilatar?
- ¿Por qué debes comprobar la selección verde antes de ajustar el kernel?

## Consulta: parámetros de las operaciones morfológicas

### `np.ones`: construir la plantilla

Forma de uso: `np.ones(shape, dtype=np.uint8)`.

| Parámetro | Necesidad | Explicación |
| --- | --- | --- |
| `shape` | Obligatorio. | Dimensiones del arreglo. `(5, 5)` significa cinco filas y cinco columnas. |
| `dtype` | Opcional. | Tipo numérico. Elegimos `np.uint8` para una plantilla sencilla de enteros de ocho bits. |

**Devuelve:** un arreglo lleno de unos. Sin `dtype`, NumPy suele crear números decimales de doble precisión. Los unos no representan la intensidad blanca de la máscara: indican las posiciones activas del kernel.

Para estos ejemplos se usan tamaños cuadrados impares, como 3 × 3 y 5 × 5. Así hay una posición central fácil de identificar. Un tamaño mayor actúa sobre detalles de mayor escala; no es necesariamente mejor.

### `cv2.erode`: reducir las regiones del primer plano

Una forma habitual de la interfaz de Python es:

`cv2.erode(src, kernel, dst=None, anchor=(-1, -1), iterations=1, borderType=cv2.BORDER_CONSTANT, borderValue=valor_predeterminado)`.

Esta línea es una referencia de parámetros, no un bloque para copiar literalmente: `valor_predeterminado` representa el valor especial de borde que OpenCV utiliza si no lo indicas.

| Parámetro | ¿Se indica en la práctica? | Para qué sirve y qué se usa comúnmente |
| --- | --- | --- |
| `src` | Sí: `mask`. | Imagen de entrada. Aquí una máscara de 0 y 255. |
| `kernel` | Sí: `kernel`. | Posiciones vecinas que se examinan; aquí una plantilla de unos de 5 × 5. |
| `dst` | No. | Arreglo de destino compatible. Habitualmente se omite y se asigna el resultado devuelto. |
| `anchor` | No. | Punto del kernel que se coloca sobre la posición evaluada. `(-1, -1)` selecciona el centro. |
| `iterations` | Sí: `1`. | Número de veces que se repite la erosión sobre su resultado. Son habituales una o dos pasadas para explorar, según la escena. |
| `borderType` | No. | Cómo se trata lo que queda fuera de la imagen al examinar vecinos de un borde. El predeterminado es `BORDER_CONSTANT`; otra opción en tareas concretas es `BORDER_REPLICATE`. |
| `borderValue` | No. | Valor usado fuera de la imagen cuando corresponde al modo de borde. El predeterminado de morfología es especial; no debes asumir que equivale a escribir 0. |

En esta forma suministramos imagen y kernel. OpenCV también admite `None` como kernel para utilizar una plantilla rectangular predeterminada de 3 × 3; en el curso lo creamos explícitamente para saber qué forma y tamaño estamos comparando.

**Devuelve:** una imagen erosionada con tamaño y tipo compatibles con la entrada. No devuelve un contorno ni el número de objetos. Con una máscara de un canal, el resultado sigue siendo una máscara de un canal.

**Lo más utilizado en estas prácticas:** `src`, `kernel` e `iterations`. Los demás se dejan predeterminados. Así, `mask_eroded = cv2.erode(mask, kernel, iterations=1)` se puede leer como «erosionar esta máscara con esta plantilla una vez y guardar el resultado».

### Qué significan realmente anclaje y borde

Con un kernel de 5 × 5, el anclaje central corresponde a la posición interna `(2, 2)`, contando desde cero. No es una coordenada del objeto en el video: es una posición dentro de la plantilla. `(-1, -1)` es la señal de OpenCV para elegir ese centro automáticamente.

Cerca del borde exterior de la imagen, parte de la plantilla puede quedar fuera del fotograma. Los parámetros de borde resuelven ese caso. No es lo mismo que el borde entre la hoja y el fondo, donde ambos lados sí están dentro de la imagen y sus valores son conocidos.

Para aprender el efecto básico, mantén la hoja lejos de los extremos del video y deja estos parámetros predeterminados. Cambiar el valor exterior puede afectar objetos que tocan el límite de la imagen; no sirve para calibrar el tono verde.

### `cv2.dilate`: expandir las regiones del primer plano

Utiliza los mismos parámetros generales: `src`, `kernel`, `dst`, `anchor`, `iterations`, `borderType` y `borderValue`. Sus papeles son los de la tabla anterior; cambia la operación sobre los vecinos: se toma el máximo en vez del mínimo.

**Devuelve:** la imagen dilatada. La llamada de la práctica es `cv2.dilate(mask, kernel, iterations=1)`. Para la secuencia, recibe `mask_eroded`, de modo que expande lo que sobrevivió a la erosión.

Las opciones de kernel y anclaje se eligen del mismo modo. No debes reutilizar sin pensar un valor de borde fijado manualmente para erosión: por ser operaciones distintas, un valor constante puede tener efectos diferentes. Mantener el tratamiento predeterminado evita introducir ese problema al empezar.

### Tres cambios habituales y cómo interpretarlos

| Cambio | Qué puedes esperar | Qué necesitas comprobar |
| --- | --- | --- |
| Kernel de 5 × 5 a 3 × 3 | Menor alcance espacial con estos kernels cuadrados. | Si se conserva mejor un detalle sin dejar demasiado ruido. |
| Una iteración a dos | La misma operación se repite sobre el resultado. | Si la hoja se borra al erosionar o se une a otra al dilatar. |
| Una operación aislada a una secuencia | La segunda utiliza la imagen que produjo la primera. | Que la entrada del segundo paso sea el resultado correcto. |

`iterations=2` en una erosión significa erosionar dos veces. No significa «erosión y dilatación». Para esa secuencia necesitas las dos llamadas, en el orden del tercer programa.

### Otra forma de crear el kernel, como referencia

`cv2.getStructuringElement(shape, ksize, anchor=(-1, -1))` devuelve una plantilla morfológica. Los dos primeros parámetros son necesarios en esta forma: `shape` puede ser `MORPH_RECT`, `MORPH_ELLIPSE` o `MORPH_CROSS`; `ksize` indica **ancho y alto**.

Atención al orden: `np.ones` recibe una forma de arreglo, filas y columnas; `getStructuringElement` recibe ancho y alto. En un cuadrado 5 × 5 no se nota la diferencia, pero en una plantilla rectangular sí.

No necesitas añadir esta herramienta al programa. Está aquí para que reconozcas otras formas de kernel si las encuentras. En el laboratorio conservamos `np.ones`, y los únicos programas son erosión, dilatación y erosión seguida de dilatación.


## Para dar el siguiente paso

Ahora tenemos una máscara más limpia, pero el programa todavía trabaja con píxeles blancos y negros. **¿Cómo podemos obtener el borde de cada región para analizarla por separado y medir su tamaño?**

En el siguiente capítulo buscaremos contornos: fronteras que nos permitirán pasar de una selección de píxeles a regiones que podemos medir y dibujar.

[Anterior](06-modelos-color.md) · [Índice](../README.md) · [Siguiente: Contornos](08-contornos.md)
