# 08. Contornos

## Qué aprenderás

Comprenderás qué representa un contorno, cómo se obtiene a partir de una máscara y qué medidas permiten describir una región. Estas herramientas son la base de la detección de figuras del siguiente tema.

## La idea en palabras sencillas

Si dibujas una figura y recorres su borde con un lápiz, estás siguiendo su contorno. El programa hace algo parecido sobre las regiones de una máscara y obtiene puntos que describen su frontera.

Con esa frontera puede medir cuánto espacio encierra, cuánto mide el borde o dónde dibujar una caja. Antes de medir, necesitas una máscara razonable: si dos objetos aparecen unidos en blanco, el programa puede tratarlos como una sola región. El primer objetivo es observar que el borde dibujado coincide con la región que quieres estudiar.

## 1. De píxeles seleccionados a regiones

Una máscara responde si cada posición pertenece al primer plano. Un **contorno** describe una frontera como una secuencia de puntos. Al encontrar contornos podemos pasar de miles de píxeles individuales a regiones que admiten medidas geométricas.

Un contorno no equivale necesariamente a un objeto real. Una máscara fragmentada puede producir varios contornos para el mismo objeto; dos objetos conectados pueden generar un contorno compartido. La calidad de la segmentación determina qué regiones analizaremos.

## 2. Entrada de la búsqueda

```python
contours, _ = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

La práctica habitual utiliza una imagen binaria de un canal. Puede ser una máscara de color limpia o el resultado de un umbral. `findContours` interpreta las regiones del primer plano según el modo elegido.

No conviene enviar directamente un fotograma BGR esperando que la función reconozca objetos. Primero hay que definir qué píxeles pertenecen a la región de interés. Encontrar bordes con otro algoritmo también puede generar una entrada útil, pero su interpretación requiere atención: bordes rotos o dobles no describen necesariamente una región cerrada limpia.

## 3. Modos de recuperación y jerarquía

Los contornos pueden estar unos dentro de otros. Una figura con un agujero tiene una frontera externa y otra asociada al hueco. La **jerarquía** describe relaciones de anidamiento o vecindad entre los contornos encontrados.

Un modo como `RETR_EXTERNAL` recupera las fronteras externas y es útil cuando solo interesa la silueta exterior. Un modo como `RETR_TREE` permite conservar relaciones más completas entre fronteras anidadas. Elegir el modo cambia qué información queda disponible: si ignoras los huecos, no podrás analizarlos después a partir de contornos que nunca recuperaste.

La aproximación de almacenamiento de puntos también es diferente de la recuperación. Por ejemplo, `CHAIN_APPROX_SIMPLE` reduce puntos redundantes de ciertos segmentos. No sustituye la aproximación poligonal que usaremos para clasificar figuras.

## 4. Área y perímetro

```python
area = cv2.contourArea(contour)
```

`contourArea` estima el área encerrada por el contorno mediante su geometría. Se expresa en unidades de píxel al cuadrado. No debe confundirse siempre con contar exactamente los píxeles blancos de una máscara: son procedimientos diferentes y pueden dar valores distintos, especialmente en regiones pequeñas o complejas.

```python
perimeter = cv2.arcLength(contour, True)
```

`arcLength` calcula la longitud de la secuencia, indicando si se trata como cerrada. El perímetro se expresa en unidades de píxel. Un borde ruidoso puede tener una longitud mayor que una frontera suave, aunque ambos correspondan al mismo objeto.

Un filtro de área mínima ayuda a descartar ruido. El umbral depende de la resolución y de la distancia del objeto. Si alejas la figura de la cámara, su área aparente disminuye y puede quedar descartada sin haber cambiado físicamente.

## 5. Rectángulo y centro

```python
x, y, w, h = cv2.boundingRect(contour)
```

`boundingRect` proporciona un rectángulo alineado con los ejes que contiene el contorno. Es útil para dibujar la posición de una región o extraer una zona. El rectángulo puede contener fondo; no equivale a la máscara de la figura.

Los **momentos** describen propiedades de distribución de una región. A partir de ellos puede calcularse un centroide: x del centro se obtiene como m10 / m00 y y como m01 / m00. Antes de dividir debes comprobar que m00 no sea cero. Los contornos degenerados o demasiado pequeños pueden no ofrecer un área útil.

Un centroide geométrico no siempre coincide con el centro visual de un objeto complejo, y en formas cóncavas puede incluso quedar fuera de parte de la región.

## 6. Seleccionar un contorno

Puedes analizar todos los contornos que superen el filtro de área o seleccionar el mayor. La segunda opción simplifica una práctica con un único objeto, pero no permite detectar varios objetos por sí sola. Si no hay contornos, la selección del mayor debe manejar esa lista vacía.

Mientras desarrollas, dibuja los contornos sobre una copia del fotograma. Así comparas la región calculada con la escena original y evitas mezclar dibujos con la información que procesarás después.

## Actividad de comprensión

Coloca una figura sólida, una figura con agujero y dos figuras que se toquen. Predice los contornos con recuperación externa y con jerarquía completa. Después explica cómo el ruido del borde afectaría al perímetro y a la detección de vértices.

## Preparación de la práctica

Antes de buscar contornos, verifica que tienes una máscara de un canal con el objeto en blanco. Identifica qué fronteras necesitas recuperar, cómo descartarás ruido por área y qué medidas utilizarás. Dibuja los resultados sobre el fotograma para comprobar que las regiones calculadas corresponden a lo que quieres analizar.

## Cómo leer el resultado de una práctica de contornos

Imagina una máscara con tres círculos blancos separados: uno grande y dos puntos pequeños. El programa puede encontrar tres fronteras, aunque tú solo quieras el círculo grande.

1. Observa la máscara antes de mirar los contornos. ¿Hay tres regiones separadas?
2. Busca el borde dibujado sobre cada región en el fotograma.
3. Comprueba qué regiones descarta el filtro de área mínima.
4. Aleja el círculo grande: su imagen ocupará menos píxeles y podría dejar de superar ese mínimo.
5. Acércalo a otro objeto seleccionado hasta que las manchas se toquen. Comprueba si ahora aparece una frontera conjunta.

**Resultado que debes comprobar:** los contornos describen las regiones de la máscara, no una lista infalible de objetos reales. Si una frontera no corresponde al objeto que buscas, revisa primero la máscara y después las medidas.


## Recorrido de la práctica con hojas verdes

Usaremos la misma selección verde HSV del tema 06 y la erosión seguida de dilatación del tema 07. No necesitas aprender otro color ni agregar un segundo intervalo.

| Etapa | Qué recibe | Qué produce |
| --- | --- | --- |
| Captura | La cámara. | Un fotograma BGR. |
| Conversión de color | El fotograma. | Su representación HSV. |
| Selección del verde | HSV y un intervalo de color. | Una máscara blanca y negra. |
| Erosión seguida de dilatación | La máscara. | La selección procesada. |
| Búsqueda de contornos | La selección procesada. | Secuencias de puntos que describen fronteras. |
| Dibujo | Los contornos y una imagen para mostrar. | El video con fronteras visibles. |

La búsqueda no devuelve una fotografía nueva por sí sola: devuelve datos que describen las fronteras. Después utilizamos esos datos para dibujar sobre el fotograma. Dibujar una línea no cambia qué seleccionó la máscara; solo permite ver el resultado.

### Preparar el material

Coloca una hoja o recorte verde sobre un fondo de otro color. Empieza con una sola figura, completamente visible y sin tocar los bordes del video. Comprueba primero la máscara: si la hoja no aparece bien seleccionada, corrige el filtro antes de buscar contornos.

Después prueba dos recortes separados. Finalmente acércalos hasta que se toquen. Este cambio permite observar por qué una frontera no equivale necesariamente a un objeto físico: dos recortes pueden formar una sola región en la máscara.

### Cómo entender el filtro de área

Imagina que la búsqueda encuentra tres regiones cuyas áreas calculadas son 40, 120 y 4 000 píxeles cuadrados. Si la regla acepta solo áreas mayores que 500, conservará únicamente la tercera. Es un ejemplo numérico para entender la decisión, no un valor obligatorio para la práctica.

El programa no está diciendo que la región de 120 sea falsa. Solo aplica el límite elegido. Un recorte válido puede quedar fuera al alejarlo de la cámara, porque ocupa menos píxeles. Por eso debes probar distintas distancias antes de fijar el umbral.

### Encontrar, filtrar y dibujar son pasos diferentes

Encontrar contornos identifica fronteras en la selección. Filtrar decide cuáles vas a utilizar, por ejemplo según su área. Dibujar muestra las que decidiste conservar. Si no aparece una línea, revisa esos pasos en ese orden: puede que la región nunca se seleccionara, que no se recuperara como esperabas o que se descartara por el filtro.

Si no hay regiones seleccionadas, el resultado puede ser una colección vacía. La aplicación debe seguir mostrando el video sin intentar elegir un contorno que no existe. Una colección vacía no implica necesariamente que la cámara falló: puede que no haya nada verde frente a ella.

### Qué debes poder explicar antes de detectar figuras

Al terminar esta etapa, identifica la máscara que recibe la búsqueda, la regla que descarta regiones y la imagen sobre la que se dibuja. Explica también por qué dos recortes juntos pueden producir una frontera compartida. Con eso estarás preparado para estudiar cómo aproximar esa frontera y contar sus esquinas en el tema 09.

## Práctica: dibujar los contornos de hojas verdes

### Preparar y ejecutar

Crea un archivo llamado `contornos_verde.py` y guarda el programa completo que aparece abajo. Cierra las prácticas anteriores para dejar disponible la cámara. Utiliza OpenCV 4, instalado mediante el paquete `opencv-python` del tutorial.

El programa continúa el trabajo de los temas 05 y 07: selecciona verde con un único intervalo, aplica erosión seguida de dilatación y busca las fronteras de las regiones resultantes. Empezarás con una hoja o recorte verde, bien iluminado, sobre un fondo de otro color.

### Código completo

```python
# Importamos OpenCV
import cv2

# Importamos NumPy
import numpy as np


# Abrimos la cámara
cap = cv2.VideoCapture(0)


# Comprobamos la cámara
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()


# Creamos el kernel
kernel = np.ones(
    (5, 5),
    np.uint8
)


# Ciclo principal
while True:

    # Capturamos un fotograma
    ret, frame = cap.read()

    # Comprobamos la captura
    if not ret:
        break


    # ==========================================
    # HSV
    # ==========================================

    # Convertimos BGR a HSV
    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )


    # ==========================================
    # MÁSCARA DE VERDE: UN SOLO INTERVALO
    # ==========================================

    lower_green = np.array([35, 80, 60], dtype=np.uint8)
    upper_green = np.array([85, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(
        hsv,
        lower_green,
        upper_green
    )


    # ==========================================
    # LIMPIEZA
    # ==========================================

    # Erosión
    mask = cv2.erode(
        mask,
        kernel,
        iterations=1
    )

    # Dilatación del resultado de la erosión
    mask = cv2.dilate(
        mask,
        kernel,
        iterations=1
    )


    # ==========================================
    # CONTORNOS
    # ==========================================

    # Buscamos los contornos de las regiones blancas
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )


    # Creamos una copia del frame
    result = frame.copy()


    # ==========================================
    # DIBUJAR CONTORNOS
    # ==========================================

    # Recorremos todos los contornos encontrados
    for contour in contours:

        # Calculamos el área del contorno
        area = cv2.contourArea(contour)

        # Ignoramos objetos pequeños
        if area < 500:
            continue

        # Dibujamos el contorno sobre el video
        cv2.drawContours(
            result,
            [contour],
            -1,
            (0, 255, 0),
            3
        )


    # Mostramos la cámara
    cv2.imshow(
        "Contornos detectados",
        result
    )


    # También podemos mostrar la máscara
    cv2.imshow(
        "Mascara",
        mask
    )


    # ESC para salir
    if cv2.waitKey(1) & 0xFF == 27:
        break


# Liberamos la cámara
cap.release()

# Cerramos las ventanas
cv2.destroyAllWindows()
```

### 1. Lo que ya conoces: captura, color y limpieza

`cv2` proporciona las herramientas de cámara e imagen. `np` es el nombre corto de NumPy, que utilizamos para construir los límites y la plantilla de 5 × 5.

```python
ret, frame = cap.read()
```

La cámara se abre una vez, antes de `while True`. En cada vuelta, `cap.read()` entrega el indicador `ret` y la imagen `frame`. Si la lectura falla, `break` sale del ciclo y el programa libera los recursos al final. En este ejemplo, ese fallo de lectura no imprime un mensaje adicional.

```python
mask = cv2.inRange(
    hsv,
    lower_green,
    upper_green
)
```

Después se convierte a HSV y se crea una máscara con el mismo intervalo verde del tema 06. Si calibraste otros límites para tus hojas, utiliza aquí esos valores. Solo hay una llamada a `inRange`: no se combinan dos máscaras.

La limpieza aplica primero erosión y después dilatación. Observa que ambas instrucciones guardan su resultado en `mask`. Eso significa que el nombre pasa a referirse a la imagen procesada: cuando empieza la dilatación, `mask` ya contiene el resultado erosionado. Cuando empieza la búsqueda de contornos, contiene el resultado final de ambos pasos.

Es el mismo orden del tercer programa del tema 07, pero allí conservábamos nombres diferentes para comparar las imágenes intermedias. Aquí reutilizamos el nombre porque solo mostraremos la máscara final. El fotograma `frame` permanece disponible en color.

### 2. Buscar las fronteras con `findContours`

La llamada recibe tres argumentos que conviene leer de izquierda a derecha:

| Argumento | Qué significa en esta práctica |
| --- | --- |
| `mask` | Buscar regiones en la máscara ya procesada, no en el video de color. |
| `cv2.RETR_EXTERNAL` | Recuperar las fronteras externas. No analizar aquí los contornos interiores de los huecos. |
| `cv2.CHAIN_APPROX_SIMPLE` | Guardar menos puntos redundantes en ciertos segmentos del borde. |

`CHAIN_APPROX_SIMPLE` no clasifica figuras ni cuenta automáticamente sus esquinas. Permite almacenar el contorno de forma más compacta. La aproximación para identificar figuras será un paso posterior.

En OpenCV 4, esta llamada devuelve dos resultados. `contours` conserva la colección de contornos encontrados. `_` recibe la información de jerarquía, que no utilizaremos en esta práctica. El guion bajo es un nombre de variable válido: se usa por convención para señalar un resultado que no necesitamos consultar.

Un **contorno** es una secuencia de puntos de una frontera; **`contours`** es la colección que puede contener varias de esas secuencias. No son imágenes independientes de cada objeto. Si no hay regiones blancas, la colección puede estar vacía y el programa debe continuar normalmente.

### 3. Crear una imagen donde dibujar

```python
result = frame.copy()
```

`result = frame.copy()` crea una copia de los datos del fotograma. Dibujaremos sobre `result`, dejando `frame` disponible sin esas líneas añadidas.

Es como fotocopiar una fotografía para marcar sobre la copia. Si solo escribiéramos `result = frame`, ambos nombres se referirían al mismo arreglo y dibujar sobre uno también afectaría al otro. `.copy()` evita compartir esos mismos datos para el dibujo.

La copia no necesita otra conversión de color: sigue siendo BGR y se mostrará con OpenCV.

### 4. Revisar los contornos uno por uno con `for`

`for contour in contours` significa «para cada contorno de la colección, realiza las instrucciones que siguen». Durante una vuelta, `contour` es una frontera; en la siguiente será otra.

La sangría muestra qué instrucciones se repiten para cada contorno. Este ciclo está dentro del ciclo de video: `while` recorre fotogramas y `for` recorre los contornos encontrados en el fotograma actual. No necesitas crear un ciclo distinto para cada hoja.

Si hay tres contornos, el cuerpo del `for` se evalúa tres veces. Si no hay ninguno, se omite ese cuerpo y el programa continúa mostrando el video y consultando ESC.

### 5. Medir el área y saltar regiones pequeñas

```python
area = cv2.contourArea(contour)
```

`area = cv2.contourArea(contour)` calcula el área encerrada por esa frontera. El valor se expresa en píxeles cuadrados, no en centímetros cuadrados ni en número de hojas. La cámara no conoce la escala física de la escena con este programa.

`if area < 500` pregunta si esa área es menor que 500. Si la respuesta es verdadera, `continue` salta el resto de esa vuelta del `for`: no dibuja el contorno pequeño y pasa al siguiente. No cierra la cámara ni termina el ciclo de video.

Compara las dos instrucciones de control:

| Instrucción | Efecto en su ubicación dentro del programa |
| --- | --- |
| `continue` bajo el filtro de área | Pasar al siguiente contorno del `for`. |
| `break` al detectar ESC | Salir del `while` de video. |

El umbral 500 es una referencia inicial, no un valor universal. Con esta comparación, un área exactamente igual a 500 **sí se conserva**, porque no es menor que 500. Un área de 100 se descarta y una de 2 000 se conserva.

El filtro no borra las regiones de `mask`. Solo decide cuáles se dibujan. Por eso puedes ver puntos blancos pequeños en la ventana de máscara sin una línea correspondiente en el video. Tampoco elimina necesariamente todo el ruido: una región incorrecta grande puede superar el límite.

### 6. Dibujar con `drawContours`

Esta función recibe varios datos. Los paréntesis se escriben en varias líneas para facilitar la lectura, pero forman una sola llamada.

| Valor | Para qué sirve |
| --- | --- |
| `result` | Imagen sobre la que se dibuja. |
| `[contour]` | Lista que contiene únicamente el contorno que estamos revisando. |
| `-1` | Dibujar todos los contornos de esa lista; aquí solo contiene uno. |
| `(0, 255, 0)` | Color de la línea en BGR: verde. |
| `3` | Grosor solicitado para la línea, en píxeles. |

Los corchetes de `[contour]` crean una lista de un elemento porque la función espera una colección de contornos. No agregan una caja ni generan una máscara adicional.

El color de dibujo es independiente del intervalo HSV de selección. Podrías dibujar una línea azul sin que cambie qué hojas detecta el filtro. En este programa la línea es verde, como en el ejemplo de la clase. Si no se distingue bien sobre la hoja, puedes probar un color contrastante como BGR `(255, 0, 0)`, que corresponde a azul, sin tocar los límites del filtro.

### 7. Mostrar el resultado y terminar

«Contornos detectados» muestra `result`, la copia del fotograma con los bordes de las regiones aceptadas. «Mascara» muestra la selección después de la erosión y la dilatación, antes de cualquier decisión sobre dibujar por área.

```python
cap.release()
cv2.destroyAllWindows()
```

Pulsa ESC con una ventana seleccionada para salir. `release()` deja libre la cámara y `destroyAllWindows()` cierra las ventanas. Una excepción imprevista no está cubierta por una estructura `try` y `finally` en este ejemplo; su limpieza es la de las salidas normales ya estudiadas.

### Pruebas con las hojas del laboratorio

1. Coloca un recorte verde grande y separado del fondo. Comprueba que la máscara lo seleccione y que aparezca una línea siguiendo su borde.
2. Coloca dos recortes separados. Si ambos superan el área mínima, deberían dibujarse ambas fronteras externas.
3. Retira las hojas. El video debe continuar aunque no se dibujen contornos. Si aparecen líneas en el fondo, revisa qué regiones quedaron blancas.
4. Aleja un recorte hasta que ocupe pocos píxeles. Puede dejar de dibujarse por el área mínima, aunque aún lo veas en la máscara.
5. Acerca los dos recortes hasta que sus selecciones se toquen. Puede aparecer una sola frontera para la región conjunta.
6. Cambia solamente el umbral 500, guarda y vuelve a ejecutar. Un umbral menor puede recuperar recortes pequeños, pero también dibujar más ruido. Un umbral mayor puede excluir objetos válidos.

### Diagnóstico: mira cada etapa en orden

| Qué observas | Qué revisar primero |
| --- | --- |
| No aparece video | Cámara, permisos y apertura del dispositivo. |
| Hay video, pero la máscara está negra | Hoja, luz e intervalo verde HSV. |
| La hoja desaparece con la limpieza | Tamaño del objeto en píxeles y fuerza de la erosión. |
| La hoja está en la máscara, pero no tiene línea | Área mínima y tamaño del contorno. |
| Dos hojas tienen un solo contorno | Si las regiones se tocan o quedaron conectadas. |
| Hay líneas en objetos no deseados | Qué zonas del fondo selecciona el filtro. |

Todavía no aparecen nombres como «triángulo» o «cuadrado». Este programa encuentra y dibuja fronteras, pero no clasifica figuras. El siguiente capítulo añadirá medidas y reglas sobre esos contornos.

### Comprueba que lo entendiste

- ¿Por qué la búsqueda recibe `mask` y no `frame`?
- ¿Qué diferencia hay entre el `while` y el `for` de este programa?
- ¿Qué hace `continue` si un área es menor que 500?
- ¿Por qué puede haber un punto blanco en la máscara sin un contorno dibujado en el video?
- ¿Para qué utilizamos `.copy()` antes de dibujar?
- ¿Por qué encontrar tres contornos no prueba por sí solo que haya tres objetos físicos?

## Consulta: funciones nuevas para analizar contornos

La captura, `inRange`, `erode` y `dilate` se detallan en los temas anteriores. Aquí empezamos a trabajar con fronteras como conjuntos de puntos, no solamente con imágenes.

### `cv2.findContours`: obtener las fronteras

Forma habitual en OpenCV 4: `cv2.findContours(image, mode, method, offset=(0, 0))`. La interfaz también permite destinos opcionales; en el curso utilizamos los resultados devueltos directamente.

| Parámetro | Necesidad | Significado y opciones habituales |
| --- | --- | --- |
| `image` | Obligatorio. | Imagen de entrada. Para el modo utilizado, una máscara de un canal de ocho bits. Los valores distintos de cero se tratan como primer plano. |
| `mode` | Obligatorio. | Qué contornos recuperar: `RETR_EXTERNAL` para fronteras externas, `RETR_LIST` para recuperarlos sin jerarquía anidada completa o `RETR_TREE` para relaciones de anidamiento. |
| `method` | Obligatorio. | Cómo guardar puntos: `CHAIN_APPROX_SIMPLE` reduce redundancias; `CHAIN_APPROX_NONE` conserva todos los puntos de la cadena. |
| `offset` | Opcional; `(0, 0)`. | Desplazamiento que se suma a los puntos. Es útil al analizar un recorte y necesitar coordenadas respecto a una imagen mayor. |

**Devuelve dos resultados:** colección de contornos y jerarquía. Por eso escribimos `contours, _ = ...`: conservamos las fronteras y no consultamos la jerarquía en esta práctica.

Para cada contorno, la jerarquía puede describir el siguiente, el anterior, el primer hijo y el padre; un valor `-1` indica que esa relación no existe. No significa que cada contorno corresponda a un objeto independiente.

**Combinación habitual del taller:** `RETR_EXTERNAL` y `CHAIN_APPROX_SIMPLE`. La primera opción evita estudiar agujeros interiores al empezar; la segunda evita guardar puntos redundantes. Son decisiones diferentes. Cambiar a `CHAIN_APPROX_NONE` no hace que el programa reconozca mejor una figura automáticamente.

En OpenCV 4, esta función no modifica la imagen de entrada. Eso no significa que cualquier otra operación posterior conserve todas sus variables: las asignaciones de `erode` y `dilate` del programa sí sustituyen a qué imagen se refiere `mask`.

### `.copy()`: conservar un fotograma sin dibujos

`frame` es un arreglo de NumPy. Su método `frame.copy()` se utiliza sin argumentos en el curso y **devuelve otro arreglo con una copia de los datos**. La operación no pertenece a `cv2`, aunque la imagen provenga de OpenCV.

Su opción adicional habitual es `order`, que controla la organización de datos en memoria; no necesitamos cambiarla para el dibujo. `result = frame` no copia los píxeles: solo crea otro nombre para el mismo arreglo. Usa `.copy()` cuando quieras separar el original de la imagen donde escribirás o dibujarás.

### `cv2.contourArea`: medir el área geométrica

Forma: `cv2.contourArea(contour, oriented=False)`.

| Parámetro | Necesidad | Uso común |
| --- | --- | --- |
| `contour` | Obligatorio. | Secuencia de puntos del contorno que vas a medir. |
| `oriented` | Opcional; `False`. | Con `False`, área no negativa. Con `True`, área con signo según la orientación del recorrido de los puntos. |

**Devuelve:** un número de área en unidades de píxel al cuadrado. Para filtrar regiones pequeñas se utiliza habitualmente el valor sin signo, como en la práctica.

No entrega centímetros cuadrados ni cuenta exactamente todos los píxeles blancos. En contornos degenerados o con cruces, su interpretación puede ser problemática. El filtro de área es una regla de selección, no una certificación de que una frontera sea válida ni de que el objeto sea real.

### `cv2.drawContours`: dibujar fronteras

Forma de referencia de Python:

`cv2.drawContours(image, contours, contourIdx, color, thickness=1, lineType=cv2.LINE_8, hierarchy=None, maxLevel=..., offset=(0, 0))`.

Los puntos suspensivos indican que omitimos aquí el valor numérico grande predeterminado de `maxLevel`; esta es una referencia de lectura, no una llamada para copiar.

| Parámetro | Necesidad | Qué significa y qué se utiliza comúnmente |
| --- | --- | --- |
| `image` | Obligatorio. | Imagen sobre la que dibujar: `result` en el curso. |
| `contours` | Obligatorio. | Colección de contornos, por ejemplo `[contour]`. |
| `contourIdx` | Obligatorio. | Índice del contorno a dibujar; `-1` pide todos los de la colección. |
| `color` | Obligatorio. | Color o intensidad del dibujo. En imagen BGR, `(0, 255, 0)` es verde. |
| `thickness` | Opcional; `1`. | Grosor positivo en píxeles. La práctica usa 3. Un valor negativo, como `FILLED`, rellena las regiones en lugar de dibujar solo el borde. |
| `lineType` | Opcional; `LINE_8`. | Tipo de línea. `LINE_AA` permite suavizado en imágenes adecuadas, como las de ocho bits. |
| `hierarchy` | Opcional. | Relaciones entre contornos para controlar niveles de dibujo. Se omite en esta práctica. |
| `maxLevel` | Opcional. | Profundidad de niveles que se dibuja al utilizar jerarquía. No es el número máximo de objetos que puede detectar. |
| `offset` | Opcional; `(0, 0)`. | Desplazamiento aplicado al dibujar los puntos. |

**Modifica la imagen entregada** y también la devuelve en la interfaz Python. El programa no necesita reasignar esa salida: el dibujo ya está en `result`. Esta diferencia importa al comparar con funciones como `cvtColor`, cuya salida guardamos por separado.

La llamada del curso utiliza los cuatro argumentos obligatorios y el grosor: imagen, colección, índice, color y grosor. `[contour]` contiene una sola frontera y `-1` solicita todas las de esa lista. Si cambiaras la colección por `contours`, `-1` dibujaría todas sus fronteras, incluso aquellas que no pasaron el filtro individual de área si las incluyeras sin filtrar.

**Error frecuente:** entregar una sola secuencia de puntos sin envolverla como espera el argumento de colección. Otro error es usar un color RGB suponiendo que el fotograma está en RGB. Conserva BGR para los dibujos de OpenCV.


## Para dar el siguiente paso

Ya podemos localizar y dibujar los contornos de las regiones verdes. **¿Cómo podemos hacer que el programa sepa si uno de esos contornos podría corresponder a un rectángulo? ¿Qué características tendríamos que revisar?**

En el siguiente capítulo simplificaremos los bordes y contaremos sus esquinas para empezar a distinguir figuras. También veremos por qué tener cuatro esquinas es una primera pista, pero no basta para garantizar que una figura sea un rectángulo.

[Anterior](07-operaciones-morfologicas.md) · [Índice](../README.md) · [Siguiente: Detectar figuras](09-detectar-figuras.md)
