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

## Código auxiliar: calibrar HSV con barras

### Para qué sirve

Los valores iniciales del filtro pueden no ajustarse exactamente a la hoja y a la iluminación del laboratorio. En lugar de editar el archivo y volver a ejecutarlo por cada cambio, esta herramienta permite mover **seis barras** y observar la máscara en el momento.

Tendrás una barra para el mínimo y otra para el máximo de H, S y V. Los números aparecen sobre el video. Cuando el resultado sea adecuado, pulsarás **P** para obtener en la terminal las dos líneas que debes copiar al filtro.

La herramienta sigue usando **un intervalo y una máscara**. No aplica erosión ni dilatación: aquí interesa calibrar primero la selección de color, antes de limpiar sus imperfecciones.

### Entorno de la práctica: Windows 11 y Python 3.12.10

Las barras utilizan **HighGUI**, la interfaz de ventanas de OpenCV, disponible en la distribución de escritorio `opencv-python` para Windows. No necesitas instalar Qt ni crear una aplicación con otro editor visual. `namedWindow`, `createTrackbar`, `getTrackbarPos`, `imshow` y `waitKey` forman parte de este mismo conjunto de herramientas.

Utiliza **Windows 11, Python 3.12.10 y `opencv-python`** en el equipo local. Las variantes *headless* no incluyen estas ventanas. Evita mezclar varias variantes de OpenCV en el mismo entorno. Ejecuta el archivo `.py` desde VS Code o la consola de Windows, no desde Colab ni WSL para esta práctica.

### Preparación

1. Cierra los demás programas de cámara con ESC.
2. Crea un archivo llamado `calibrar_verde_hsv.py` y copia el programa completo.
3. Ejecútalo desde VS Code con el mismo Python, OpenCV y NumPy de las prácticas anteriores.
4. Coloca la hoja verde frente a la cámara, con la luz y distancia que utilizarás en clase.
5. Organiza las ventanas para ver simultáneamente las barras, la cámara y la máscara.

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
cv2.namedWindow("Ajustes HSV", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Ajustes HSV", 700, 180)

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
cv2.imshow("Ajustes HSV", panel)

# Nombre de la barra, ventana, valor inicial, máximo y función.
# Empezamos con el mismo intervalo verde de la clase.
cv2.createTrackbar("H minimo", "Ajustes HSV", 35, 179, al_cambiar)
cv2.createTrackbar("H maximo", "Ajustes HSV", 85, 179, al_cambiar)
cv2.createTrackbar("S minimo", "Ajustes HSV", 80, 255, al_cambiar)
cv2.createTrackbar("S maximo", "Ajustes HSV", 255, 255, al_cambiar)
cv2.createTrackbar("V minimo", "Ajustes HSV", 60, 255, al_cambiar)
cv2.createTrackbar("V maximo", "Ajustes HSV", 255, 255, al_cambiar)


while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo leer el video.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Leemos la posición actual de cada barra.
    h_min = cv2.getTrackbarPos("H minimo", "Ajustes HSV")
    h_max = cv2.getTrackbarPos("H maximo", "Ajustes HSV")
    s_min = cv2.getTrackbarPos("S minimo", "Ajustes HSV")
    s_max = cv2.getTrackbarPos("S maximo", "Ajustes HSV")
    v_min = cv2.getTrackbarPos("V minimo", "Ajustes HSV")
    v_max = cv2.getTrackbarPos("V maximo", "Ajustes HSV")

    lower_green = np.array([h_min, s_min, v_min], dtype=np.uint8)
    upper_green = np.array([h_max, s_max, v_max], dtype=np.uint8)

    # Cada mínimo debe ser menor o igual que su máximo.
    rango_valido = h_min <= h_max and s_min <= s_max and v_min <= v_max

    if rango_valido:
        # Seguimos trabajando con un intervalo y una máscara.
        mask = cv2.inRange(hsv, lower_green, upper_green)
    else:
        # Mostramos negro y avisamos si se cruzaron los límites.
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)

    # Copiamos la cámara para escribir los valores sin modificar el HSV.
    preview = frame.copy()

    cv2.putText(
        preview, f"Min HSV: {lower_green.tolist()}",
        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2
    )
    cv2.putText(
        preview, f"Max HSV: {upper_green.tolist()}",
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

    cv2.imshow("Camara y valores HSV", preview)
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

### Cómo usar las barras paso a paso

1. Empieza con los valores predeterminados: mínimo `[35, 80, 60]` y máximo `[85, 255, 255]`, en orden **H, S, V**.
2. Mira la máscara: intenta que la hoja quede mayormente blanca y el fondo mayormente negro.
3. Ajusta primero **H mínimo y H máximo** para limitar el tono verde. Si seleccionas otros colores, estrecha el intervalo con cuidado.
4. Ajusta **S mínimo** si aparecen regiones grises o poco coloreadas. Subirlo puede excluirlas, pero también puede quitar reflejos o zonas poco saturadas de la hoja.
5. Ajusta **V mínimo** para permitir o excluir regiones oscuras. Bajarlo puede recuperar una sombra de la hoja, pero también aceptar fondo oscuro que cumpla los otros límites.
6. Normalmente puedes dejar **S máximo y V máximo en 255**. También están disponibles por si necesitas restringirlos; reducirlos puede excluir partes muy saturadas o brillantes del objeto.
7. Mueve suavemente la hoja y comprueba que no desaparezca con pequeñas variaciones de orientación o distancia. Evita calibrar solo para una posición inmóvil.
8. Cuando la selección sea adecuada, haz clic en una ventana de OpenCV y pulsa **P**. Mira la terminal de VS Code: aparecerán `lower_green` y `upper_green` con los números elegidos.
9. Copia esas dos líneas. Pulsa ESC para cerrar el calibrador y pégalas en lugar de los límites del programa HSV del capítulo. No las agregues como una segunda pareja de límites.
10. Guarda y ejecuta el filtro normal para comprobar el resultado. Utiliza también esos valores en las prácticas posteriores que seleccionan la misma hoja.

La tecla P **no escribe ni modifica archivos automáticamente**. Solo imprime el texto para que lo copies. Si vuelves a abrir el calibrador, empezará otra vez con sus valores iniciales; conserva las líneas obtenidas antes de cerrar la terminal.

### Qué hace cada parte nueva del código

**`def al_cambiar(valor)` y `pass`.** `def` define una función. OpenCV necesita una función para notificar el movimiento de cada barra y le entrega su nueva posición como argumento. En este ejemplo la función no realiza ninguna operación: `pass` significa «no hacer nada». Las posiciones se consultan dentro del ciclo de video. No escribas `al_cambiar()` al crear las barras: se entrega el nombre de la función para que OpenCV pueda llamarla después.

**`namedWindow`.** Crea la ventana antes de colocar controles dentro. `WINDOW_NORMAL` permite cambiar su tamaño. `resizeWindow` propone un tamaño inicial. Mostramos además un panel negro con instrucciones mediante `imshow` antes de crear las barras, para que la ventana tenga contenido visible desde el principio. Ese panel no es otra máscara de color; solo sirve de fondo para la interfaz. Puedes ampliar la ventana si las barras no se ven cómodamente.

**`createTrackbar`.** Cada llamada indica nombre de la barra, ventana donde aparece, valor inicial, valor máximo y función de aviso. El mínimo de recorrido es 0. H termina en 179 porque esa es la escala de esta conversión HSV de ocho bits; S y V terminan en 255. Los nombres con «mínimo» y «máximo» indican qué límite del filtro controla cada barra, no escalas diferentes.

**`getTrackbarPos`.** Lee la posición actual de una barra. Se ejecuta en cada fotograma, de modo que al moverla cambia el arreglo de límites y se recalcula la máscara. Los nombres de barra y ventana deben coincidir con los utilizados al crearlas.

**`rango_valido` y `and`.** Comprobamos las tres parejas de límites. `and` exige que todas las comparaciones sean verdaderas. No tiene sentido pedir simultáneamente H mayor o igual que 80 y menor o igual que 40. Si cruzas una pareja, el programa muestra un aviso y una máscara negra hasta que la corrijas. No intercambia números automáticamente: así ves qué valor necesitas ajustar.

**`np.zeros(frame.shape[:2], dtype=np.uint8)`.** Se utiliza únicamente para mostrar una máscara negra cuando el intervalo es inválido. `frame.shape[:2]` toma alto y ancho del fotograma; `zeros` crea una imagen llena de ceros de esas dimensiones. No se combina con otra máscara de color.

**`tolist()`, textos y `print`.** `tolist()` permite presentar los valores del arreglo como una lista legible. `putText` los muestra en la cámara y `print` escribe las líneas de Python en la terminal. Los textos que empiezan por `f` insertan los valores actuales dentro del mensaje.

**`ord("p")`.** Permite comparar la tecla recibida con la letra P. Se aceptan tanto minúscula como mayúscula. Si la terminal tiene el foco, la pulsación puede no llegar a OpenCV: selecciona una ventana de la herramienta antes de pulsarla.

### Comprobación en el equipo Windows del laboratorio

1. En una consola nueva, ejecuta `python --version` y confirma **Python 3.12.10**. Selecciona ese mismo intérprete en VS Code.
2. Ejecuta el calibrador. Deben aparecer «Ajustes HSV», con sus seis barras, «Camara y valores HSV» y «Mascara calibrada».
3. Arrastra una barra con el ratón. Comprueba que cambie su número, que el valor sobre el video se actualice y que la máscara responda cuando el cambio afecta a los píxeles de la escena.
4. Prueba un mínimo mayor que su máximo: debe aparecer el aviso de intervalo inválido. Corrígelo antes de continuar.
5. Con el intervalo válido, selecciona una ventana de OpenCV y pulsa P. Comprueba que las dos líneas aparezcan en la terminal, sin tener que escribir los números manualmente.
6. Pulsa ESC con una ventana seleccionada y verifica que las ventanas se cierren. Vuelve a ejecutar para comprobar que la cámara quedó libre.

Si no aparecen ventanas y el mensaje dice que la función no está implementada, revisa si instalaste una variante *headless* o si ejecutas desde otro entorno. Si las ventanas aparecen pero no hay cámara, revisa conexión, otras aplicaciones y los permisos de **Configuración → Privacidad y seguridad → Cámara** de Windows 11, incluido el acceso de aplicaciones de escritorio.

Si las barras no se ven completas, amplía la ventana de ajustes y separa las ventanas en la pantalla. Si P o ESC no responden, haz clic en una ventana de OpenCV antes de pulsarlas; la terminal no debe tener el foco. La atención a estas ventanas se mantiene mediante `waitKey` dentro del ciclo, así que no elimines esa llamada.

Referencia de las funciones utilizadas: [documentación oficial de HighGUI](https://docs.opencv.org/4.x/d7/dfc/group__highgui.html). Para la diferencia entre distribución de escritorio y *headless*, consulta [la página del paquete opencv-python](https://pypi.org/project/opencv-python/).

### Cómo comprobar que copiaste lo correcto

Los tres valores del mínimo deben aparecer juntos en `lower_green`, y los tres del máximo, en `upper_green`. Conserva el orden H, S y V y la indicación `dtype=np.uint8`. No copies los códigos como instrucciones de la terminal: reemplaza las líneas correspondientes **dentro del archivo Python del filtro**.

El programa normal no muestra barras; utiliza los límites que pegaste. Si su selección no coincide con la del calibrador, comprueba que guardaste los cambios, ejecutaste el archivo correcto y mantuviste las condiciones de luz.

Si la máscara queda negra incluso con un intervalo válido, revisa qué canal está excluyendo la hoja. Si queda casi toda blanca, el intervalo acepta demasiados píxeles o el fondo tiene colores similares. No busques una calibración perfecta a costa de perder toda la hoja cuando se mueve ligeramente.

El calibrador permite explorar otros tonos cambiando las barras, pero la práctica sigue centrada en verde. Un solo intervalo numérico no representa una región que cruza el final y el inicio de H, como puede suceder con el rojo.


## Consulta: funciones nuevas del filtro y del calibrador

Las funciones de cámara y visualización se describen en el [tema 04](04-video-camara-python.md). Aquí nos centraremos en convertir el color, seleccionar píxeles y leer las barras. Las formas de llamada se muestran simplificadas: no necesitas escribir todos los parámetros opcionales.

### `np.array`: construir los límites

Forma habitual en estas prácticas: `np.array(object, dtype=np.uint8)`.

| Parámetro | Necesidad | Qué utiliza el curso |
| --- | --- | --- |
| `object` | Obligatorio. | Lista de tres números, como `[35, 80, 60]`. |
| `dtype` | Opcional en NumPy. | `np.uint8`, enteros sin signo entre 0 y 255, adecuados para estos límites. |

**Devuelve:** un arreglo de NumPy. El orden de sus números depende del modelo de la imagen que filtrarás. La función no sabe que esa lista significa HSV; solo construye números. No convierte grados ni calibra el color automáticamente.

Sin indicar `dtype`, NumPy elige un tipo según los datos. En el curso lo hacemos explícito. No uses números negativos ni mayores que 255 esperando que el tipo los corrija: prepara valores válidos y, para H, respeta además su máximo 179 en esta conversión.

### `cv2.cvtColor`: cambiar la representación del color

Forma frecuente en Python: `cv2.cvtColor(src, code, dst=None, dstCn=0)`. El resultado se asigna a una variable, como `hsv`.

| Parámetro | Necesidad | Significado y opciones comunes |
| --- | --- | --- |
| `src` | Obligatorio. | Imagen de entrada, por ejemplo `frame`. |
| `code` | Obligatorio. | Conversión que corresponde al origen: `COLOR_BGR2HSV`, `COLOR_BGR2GRAY` o `COLOR_BGR2RGB`, según la tarea. |
| `dst` | Opcional. | Arreglo de destino compatible. Lo omitimos y utilizamos el resultado devuelto. |
| `dstCn` | Opcional; `0` por defecto. | Número de canales de salida. Con 0 se determina a partir de la conversión. |

**Devuelve:** la imagen convertida. No modifica `frame` cuando guardamos la salida en otra variable sin indicar un destino compartido. Para el filtro elegimos `COLOR_BGR2HSV`; cambiar a `COLOR_RGB2HSV` sería incorrecto si la cámara entregó BGR.

El rango de H de 0 a 179 corresponde a esta conversión de imágenes de ocho bits. Otras variantes, como HSV de rango completo, o imágenes decimales pueden usar escalas distintas. No mezcles sus límites con los del curso.

### `cv2.inRange`: seleccionar por intervalos

Forma: `cv2.inRange(src, lowerb, upperb, dst=None)`.

| Parámetro | Necesidad | Qué representa |
| --- | --- | --- |
| `src` | Obligatorio. | Imagen a comparar: BGR en el primer programa o HSV en el segundo. |
| `lowerb` | Obligatorio. | Límite inferior de cada canal. |
| `upperb` | Obligatorio. | Límite superior de cada canal. |
| `dst` | Opcional. | Destino de la máscara. En las prácticas se omite. |

**Devuelve:** una máscara de un canal de ocho bits: 255 donde se cumplen todos los intervalos y 0 donde no. Los límites se incluyen: un píxel que coincide con el mínimo puede ser aceptado.

**Uso común:** filtrar colores con límites calibrados, como `lower_green` y `upper_green`. También permite intervalos sobre otros datos, pero no detecta clases ni separa objetos por sí sola. Un mínimo mayor que su máximo no representa un intervalo circular y no se corrige automáticamente.

### `cv2.namedWindow`: preparar una ventana

Forma: `cv2.namedWindow(winname, flags=cv2.WINDOW_AUTOSIZE)`.

`winname` es el nombre necesario para identificar la ventana. `flags` es opcional: `WINDOW_AUTOSIZE` ajusta la ventana al contenido; `WINDOW_NORMAL` permite redimensionarla. El calibrador elige `WINDOW_NORMAL` para acomodar los controles. **No devuelve una imagen**.

### `cv2.resizeWindow`: proponer el tamaño

En la forma usada recibe `winname`, `width` y `height`: nombre, ancho y alto del área de imagen solicitada, en píxeles. La ventana debe existir y permitir redimensionamiento. El tamaño exterior final también depende de controles, bordes y sistema operativo. Esta función cambia la ventana; **no redimensiona el arreglo de la imagen**.

### `cv2.createTrackbar`: agregar una barra

Forma de Python: `cv2.createTrackbar(trackbarname, winname, value, count, onChange)`.

| Parámetro | Qué debes entregar |
| --- | --- |
| `trackbarname` | Nombre de la barra; debe identificarla dentro de la ventana. |
| `winname` | Nombre de una ventana que ya exista. |
| `value` | Posición inicial, como 35 para H mínimo. |
| `count` | Posición máxima: 179 para H o 255 para S y V. |
| `onChange` | Función que recibirá la posición al mover la barra, aquí `al_cambiar`. |

Esta forma necesita esos cinco argumentos. La barra recorre valores enteros desde 0 hasta `count`; no significa que necesites arrastrarla hasta ambos extremos para calibrar. Su posición se lee por separado.

`onChange` es una función de aviso o *callback*: OpenCV la llama cuando corresponde. En el curso contiene `pass` porque consultamos todas las posiciones dentro del ciclo. Entregamos el nombre de la función, sin paréntesis. Crear una barra no cambia por sí solo los límites del filtro: el programa debe leerla y reconstruirlos.

### `cv2.getTrackbarPos`: leer una barra

Necesita `trackbarname` y `winname`, con los mismos nombres utilizados al crearla. **Devuelve:** la posición entera actual. La consultamos cada fotograma para que el filtro responda al movimiento. No devuelve los seis límites juntos: cada llamada lee una barra.

### `np.zeros`: crear el panel o una máscara negra

Forma de uso del curso: `np.zeros(shape, dtype=np.uint8)`. `shape` indica las dimensiones necesarias y `dtype` es opcional; si lo omites, NumPy suele utilizar números decimales de doble precisión, no ocho bits.

**Devuelve:** un arreglo lleno de ceros. Con forma `(100, 700, 3)` creamos un panel de color negro de alto 100 y ancho 700. Con `frame.shape[:2]` creamos una imagen negra de un canal con el alto y ancho de la cámara. No confíes en que una imagen negra indique siempre que no hay verde: el calibrador también la utiliza al avisar que los límites son inválidos.

El dibujo de valores utiliza `putText`, cuya ficha completa está en el [tema 09](09-detectar-figuras.md). `.copy()` se detalla en el [tema 08](08-contornos.md). En el calibrador sirven para escribir números sobre una copia del video; no modifican la selección HSV ya calculada.


## Para dar el siguiente paso

Conseguimos seleccionar la hoja, pero los límites cambian de significado cuando usamos BGR o HSV. **¿Por qué una misma imagen se puede representar de distintas maneras y cómo elegimos la más útil para encontrar un color?**

En el siguiente capítulo entenderemos mejor los modelos de color. Así podrás ajustar los filtros sabiendo qué representa cada número, en lugar de cambiarlos por ensayo y error.

[Anterior](04-video-camara-python.md) · [Índice](../README.md) · [Siguiente: Modelos de color](06-modelos-color.md)
