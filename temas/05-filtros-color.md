# 05. Filtros de color

## Qué aprenderás

Aprenderás a seleccionar píxeles por color y a interpretar una máscara binaria. Primero aplicarás un filtro directamente al fotograma de la cámara, **sin convertir su modelo de color**. Después ejecutarás el ejemplo en HSV con un intervalo y, finalmente, el de dos intervalos proporcionados por Felix. Compararás las tres prácticas para entender qué aporta cada cambio.

OpenCV entrega normalmente el fotograma en **BGR**, no en RGB. Por eso el primer ejemplo trabaja directamente en BGR. El segundo convierte de **BGR a HSV**; ninguno necesita una conversión intermedia a RGB.

## 1. Qué significa filtrar por color

En esta práctica, filtrar significa seleccionar los píxeles cuyos valores están dentro de unos límites. La selección se representa mediante una **máscara**: una imagen de un canal donde 255, mostrado como blanco, significa «seleccionado» y 0, mostrado como negro, significa «no seleccionado».

Imagina una pelota roja sobre una mesa. El filtro puede seleccionar la pelota, pero también una etiqueta roja o parte de una camisa. La máscara dice qué píxeles cumplen el criterio; todavía no reconoce la identidad de la pelota ni cuenta objetos.

La función `cv2.inRange` compara cada canal con su límite inferior y superior, incluidos los extremos. Un píxel se selecciona solamente si **todos sus canales** cumplen los intervalos correspondientes. La máscara tiene el mismo alto y ancho que el fotograma, pero un solo canal.

## 2. Primera práctica: filtrar directamente en BGR

### 2.1. Cómo pensar el intervalo

En BGR, cada píxel tiene tres intensidades en este orden: **azul, verde y rojo**. En la imagen de 8 bits habitual, cada intensidad está entre 0 y 255. Para un primer filtro de rojo intenso podemos pedir poco azul, poco verde y bastante rojo.

Utilizaremos como punto de partida el límite inferior `[0, 0, 150]` y el superior `[100, 100, 255]`. Su interpretación es:

| Canal | Mínimo | Máximo | Condición |
| --- | --- | --- | --- |
| B: azul | 0 | 100 | Componente azul relativamente baja. |
| G: verde | 0 | 100 | Componente verde relativamente baja. |
| R: rojo | 150 | 255 | Componente roja relativamente alta. |

Estos valores son **didácticos y necesitan calibración**. No representan todos los rojos posibles. Una superficie roja con poca luz puede tener R menor que 150; una con un reflejo claro puede tener B o G mayor que 100.

### 2.2. Código completo sin conversión de color

Este ejemplo es una **adaptación didáctica creada a petición de Felix** a partir de la estructura de su código HSV. No es un código recuperado del enlace compartido. Puedes guardarlo como `filtro_rojo_bgr.py` y ejecutarlo localmente con OpenCV y NumPy instalados.

```python
# Importamos OpenCV
import cv2

# Importamos NumPy para crear los rangos de color
import numpy as np


# Abrimos la cámara web
cap = cv2.VideoCapture(0)


# Comprobamos si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()


# Ciclo principal del programa
while True:

    # Capturamos un fotograma de la cámara
    ret, frame = cap.read()

    # Comprobamos que el fotograma se haya capturado correctamente
    if not ret:
        print("No se pudo leer el video.")
        break


    # Trabajamos directamente con frame, que está en BGR
    # El orden de los valores es: azul, verde, rojo
    lower_red = np.array([0, 0, 150], dtype=np.uint8)
    upper_red = np.array([100, 100, 255], dtype=np.uint8)


    # Creamos la máscara SIN convertir el modelo de color
    mask = cv2.inRange(
        frame,
        lower_red,
        upper_red
    )


    # Mostramos el video original
    cv2.imshow(
        "Camara web",
        frame
    )


    # Mostramos la selección de rojo realizada en BGR
    cv2.imshow(
        "Mascara roja BGR",
        mask
    )


    # ESC termina el programa
    if cv2.waitKey(1) & 0xFF == 27:
        break


# Liberamos la cámara
cap.release()

# Cerramos las ventanas
cv2.destroyAllWindows()
```

### 2.3. Explicación por bloques

**Importaciones.** `cv2` proporciona captura, comparación y ventanas. `numpy`, abreviado como `np`, permite construir los arreglos con los límites. `np.array` convierte la lista de tres valores en un arreglo. En esta adaptación, `dtype=np.uint8` hace explícito el tipo de entero de 8 bits sin signo utilizado para los límites de 0 a 255.

**Captura.** La apertura, `isOpened`, la lectura con `ret` y `frame`, y la salida con ESC funcionan como en el [capítulo 04](04-video-camara-python.md). `frame` contiene el fotograma actual; aquí lo usamos sin llamar a `cvtColor`.

**Límites.** `lower_red` y `upper_red` no son colores para dibujar en pantalla. Definen el intervalo aceptado en cada canal. El tercer valor corresponde a rojo porque el arreglo de entrada está en BGR. Si interpretaras el primer valor como rojo, seleccionarías colores diferentes de los esperados.

**Comparación.** `cv2.inRange(frame, lower_red, upper_red)` examina el fotograma BGR. Por ejemplo, el píxel `[30, 40, 200]` se acepta: B y G no superan 100 y R está entre 150 y 255. El píxel `[30, 40, 120]` se rechaza porque su componente roja es demasiado baja para este intervalo, aunque podría pertenecer a una superficie roja en sombra.

**Ventanas.** La primera muestra el video original y la segunda muestra la máscara. Los píxeles seleccionados aparecen blancos, no rojos: es una selección binaria, no una imagen coloreada del objeto.

**Salida y limpieza.** Selecciona una ventana de OpenCV y pulsa ESC. El ciclo termina, se libera la cámara y se cierran las ventanas. Ejecuta un ejemplo a la vez para evitar que dos programas intenten usar la misma cámara.

Los límites se construyen dentro del ciclo para mantener la estructura del ejemplo recibido. Como son constantes, podrían definirse antes del ciclo en otra versión; eso no cambia el criterio de selección.

### 2.4. Qué dificultad queremos observar

Coloca un objeto rojo bajo una luz estable y observa su máscara. Después proyecta una sombra o cambia suavemente la iluminación. El objeto sigue siendo rojo para una persona, pero sus intensidades B, G y R pueden variar y salir de los límites.

Bajar el mínimo de R puede recuperar zonas oscuras, pero también aceptar otras regiones. Subir los máximos de B y G puede recuperar reflejos o rojos más claros, pero ampliar demasiado la selección. En BGR, estamos delimitando **intensidades absolutas de tres componentes**, lo que puede hacer incómoda la separación entre color y brillo.

Esta práctica no busca demostrar que BGR siempre falla. Un filtro BGR calibrado puede funcionar bien en una escena controlada. Queremos reconocer qué describen sus límites antes de cambiar de representación.

## 3. Segunda práctica: convertir a HSV antes de filtrar

### 3.1. Por qué hacer la transformación

HSV organiza la información mediante **H: tono**, **S: saturación** y **V: valor o brillo**. Esto permite expresar el filtro como «un intervalo de tono rojo, con suficiente saturación y brillo», en lugar de ajustar tres intensidades BGR por separado.

En la conversión habitual de OpenCV para imágenes de 8 bits, H está entre **0 y 179**, y S y V están entre **0 y 255**. No uses límites de tono de 0 a 360 en este ejemplo. El [capítulo 06](06-modelos-color.md) explica esos componentes con más detalle.

### 3.2. Código original proporcionado por Felix

El siguiente código se conserva tal como fue enviado. Puedes guardarlo como `filtro_rojo_hsv.py`. Cierra primero el programa BGR con ESC y después ejecuta este.

```python
# Importamos OpenCV
import cv2

# Importamos NumPy para crear los rangos de color
import numpy as np


# Abrimos la cámara web
cap = cv2.VideoCapture(0)


# Comprobamos si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()


# Ciclo principal del programa
while True:

    # Capturamos un fotograma de la cámara
    ret, frame = cap.read()

    # Comprobamos que el fotograma se haya capturado correctamente
    if not ret:
        print("No se pudo leer el video.")
        break


    # Convertimos el fotograma de BGR a HSV
    # HSV permite trabajar de manera más sencilla con los colores
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # Definimos el límite inferior del color rojo
    lower_red = np.array([0, 100, 100])

    # Definimos el límite superior del color rojo
    upper_red = np.array([10, 255, 255])


    # Creamos una máscara utilizando el rango de rojo
    # Los píxeles que cumplen la condición serán blancos
    # Los demás píxeles serán negros
    mask = cv2.inRange(
        hsv,
        lower_red,
        upper_red
    )


    # Mostramos el video original
    cv2.imshow(
        "Camara web",
        frame
    )


    # Mostramos la máscara
    cv2.imshow(
        "Mascara roja",
        mask
    )


    # Esperamos una tecla
    # ESC termina el programa
    if cv2.waitKey(1) & 0xFF == 27:
        break


# Liberamos la cámara
cap.release()

# Cerramos las ventanas
cv2.destroyAllWindows()
```

### 3.3. Explicación de la conversión

`cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)` transforma la representación del fotograma de BGR a HSV. El resultado se almacena en `hsv`. `frame` conserva la imagen original, que se sigue utilizando para la ventana «Camara web».

La conversión no reconoce objetos ni mejora por sí misma la iluminación: reorganiza la información para facilitar la comparación. Cada fotograma nuevo necesita su propia conversión antes de aplicar el filtro.

No se debe usar `COLOR_RGB2HSV` si el arreglo que entrega la cámara está en BGR. Tampoco hay que comparar una imagen BGR con límites pensados para HSV: los números representarían componentes distintos.

### 3.4. Explicación de los límites HSV

En esta segunda práctica, los mismos nombres de variables tienen una interpretación diferente porque la imagen de entrada cambió de modelo:

| Canal | Mínimo | Máximo | Significado en el ejemplo |
| --- | --- | --- | --- |
| H: tono | 0 | 10 | Seleccionar una zona del tono rojo cerca del inicio de la escala. |
| S: saturación | 100 | 255 | Excluir colores demasiado poco saturados, cercanos al gris. |
| V: valor | 100 | 255 | Excluir zonas demasiado oscuras para este filtro. |

`np.array([0, 100, 100])` y `np.array([10, 255, 255])` crean los límites. El ejemplo original no indica un `dtype` explícito; NumPy utiliza su tipo entero predeterminado para estas listas. Se mantiene ese detalle sin modificar la fuente. Lo importante para la comparación es que los valores correspondan a los canales y rangos de esta conversión.

El mínimo de S ayuda a evitar zonas poco coloreadas cuyo tono no es una pista fiable. El mínimo de V elimina regiones oscuras, pero también puede excluir partes reales del objeto en sombra. Estos valores necesitan calibración igual que los de BGR.

### 3.5. Explicación de la máscara

La diferencia central está en el primer argumento: ahora `cv2.inRange` recibe **`hsv`**, no `frame`. La función sigue realizando el mismo tipo de comparación, pero sobre tono, saturación y brillo.

Un píxel HSV `[5, 180, 200]` se acepta porque cumple los tres intervalos. `[5, 180, 80]` se rechaza por brillo insuficiente. `[5, 50, 200]` se rechaza por poca saturación. Estos valores son ejemplos numéricos explicativos, independientes de los píxeles concretos de tu cámara.

Mostrar, consultar ESC y liberar recursos mantiene el mismo comportamiento que en el primer programa. Eso permite centrar la comparación en la representación y los límites, sin cambiar el ciclo de captura.

## 4. Comparación: qué ventaja aporta HSV

| Aspecto | Filtro directo en BGR | Filtro después de convertir a HSV |
| --- | --- | --- |
| Imagen que recibe `inRange` | `frame`. | `hsv`. |
| Significado de los límites | Intensidades azul, verde y roja. | Tono, saturación y valor. |
| Cómo se describe el rojo | Poco B y G, bastante R, en esta adaptación. | Tono cercano al rojo y mínimos de S y V. |
| Conversión previa | No requiere. | Usa `COLOR_BGR2HSV`. |
| Ajuste del brillo | Puede exigir cambios en varios límites de componentes. | Se puede ajustar V manteniendo el intervalo de H. |
| Limitaciones | Sensible a intensidades y condiciones de la escena. | También requiere calibración y falla en condiciones difíciles. |

La ventaja principal de HSV es **hacer más interpretable la selección de color**. Bajo ciertos cambios moderados de iluminación, el tono puede mantenerse aproximadamente mientras varía V. Esto suele facilitar un filtro de color más manejable, pero no garantiza que la máscara HSV sea mejor en toda escena.

La exposición automática, la luz de otro color, los reflejos, la baja saturación y las sombras intensas pueden cambiar el resultado. El ejemplo HSV todavía exige V de al menos 100: si el objeto queda por debajo de ese valor, también desaparecerá de la máscara.

Además, los intervalos BGR y HSV de estas prácticas no seleccionan exactamente el mismo conjunto de colores. Una diferencia de resultados puede deberse tanto a la representación como a los umbrales. Calibra ambos en la misma condición inicial antes de sacar conclusiones sobre cambios de iluminación.

## 5. Tercera práctica: detectar rojo con dos intervalos HSV

### 5.1. Por qué el tono es circular

H representa una posición en un **círculo de tonos**. Al recorrerlo encontramos rojo, amarillo, verde, cian, azul, magenta y finalmente rojo otra vez. El inicio y el final se encuentran: no son colores alejados, aunque sus valores numéricos parezcan muy diferentes.

Puedes imaginar la carátula de un reloj: una posición justo antes de las doce y otra justo después están próximas, aunque al escribir sus horas aparezcan en extremos distintos de una lista. Con el tono sucede algo semejante. Para guardarlo en un arreglo necesitamos una escala lineal, pero el fenómeno representado sigue siendo circular.

En la conversión `COLOR_BGR2HSV` de imágenes de 8 bits, OpenCV representa H con enteros de **0 a 179**, aproximadamente la mitad del ángulo en grados. Por ejemplo, H = 10 corresponde aproximadamente a 20°, y H = 170 a 340°. H = 179 está cerca de 358°, próximo a 0° al completar la vuelta. **179 no es un rojo más intenso que 0**: indica otra posición cercana al rojo en el círculo. La saturación y el valor, no un H mayor, describen otros aspectos de la apariencia.

El rojo puro ideal suele quedar en H = 0. Los rojos reales pueden desplazarse a un lado u otro de ese punto por su composición cromática, iluminación, reflejos, balance de blancos y pequeñas variaciones de la captura. Un rojo algo más próximo al amarillo puede quedar cerca del extremo bajo, y uno algo más próximo al magenta, cerca del extremo alto. Incluso diferentes píxeles de un mismo objeto pueden quedar en ambos extremos.

### 5.2. Por qué un solo intervalo pierde parte del rojo

El programa anterior seleccionaba H entre **0 y 10**. Eso cubre una vecindad del rojo a un lado del inicio, pero no cubre la zona **170 a 179**, que también está próxima al rojo al otro lado del círculo.

`cv2.inRange` compara números mediante intervalos ordinarios. **No interpreta automáticamente que H es circular**. Pedir un límite inferior de H = 170 y uno superior de H = 10 no significa «pasar por el final y volver al comienzo»: exige simultáneamente H ≥ 170 y H ≤ 10, una condición imposible.

Tampoco conviene usar simplemente H de 0 a 179. Eso incluiría todos los tonos que cumplan S y V, como amarillos, verdes o azules saturados y suficientemente brillantes. No sería una selección específica de rojo.

La solución es representar esa región circular como la unión de **dos intervalos lineales**:

| Máscara | Intervalo H | Intervalo S | Intervalo V | Región seleccionada |
| --- | --- | --- | --- | --- |
| `mask1` | 0 a 10 | 100 a 255 | 100 a 255 | Rojo cerca del inicio de la escala. |
| `mask2` | 170 a 179 | 100 a 255 | 100 a 255 | Rojo cerca del final de la escala. |

Los dos rangos usan los mismos mínimos de saturación y valor para mantener el mismo criterio de color suficientemente saturado y visible. Los números son puntos de partida: cubrir ambos extremos **no garantiza detectar todo objeto que una persona considere rojo**. Un objeto oscuro todavía puede quedar fuera por V y un reflejo poco saturado por S.

### 5.3. Código original de dos intervalos proporcionado por Felix

Este tercer ejemplo se conserva tal como fue enviado. Puedes guardarlo como `filtro_rojo_hsv_dos_intervalos.py`. Cierra el programa anterior con ESC antes de ejecutarlo, para que la cámara quede disponible.

```python
# Importamos OpenCV
import cv2

# Importamos NumPy
import numpy as np


# Abrimos la cámara web
cap = cv2.VideoCapture(0)


# Comprobamos si la cámara está disponible
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()


# Ciclo principal
while True:

    # Capturamos un fotograma
    ret, frame = cap.read()

    # Comprobamos que la captura haya funcionado
    if not ret:
        print("No se pudo leer el video.")
        break


    # Convertimos la imagen de BGR a HSV
    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )


    # ==========================================
    # PRIMER RANGO DE ROJO
    # ==========================================

    # Límite inferior del primer rango
    lower_red1 = np.array([0, 100, 100])

    # Límite superior del primer rango
    upper_red1 = np.array([10, 255, 255])

    # Creamos la primera máscara
    mask1 = cv2.inRange(
        hsv,
        lower_red1,
        upper_red1
    )


    # ==========================================
    # SEGUNDO RANGO DE ROJO
    # ==========================================

    # Límite inferior del segundo rango
    lower_red2 = np.array([170, 100, 100])

    # Límite superior del segundo rango
    upper_red2 = np.array([179, 255, 255])

    # Creamos la segunda máscara
    mask2 = cv2.inRange(
        hsv,
        lower_red2,
        upper_red2
    )


    # ==========================================
    # UNIR LAS DOS MÁSCARAS
    # ==========================================

    # Unimos ambas máscaras mediante OR
    # Un píxel será blanco si pertenece
    # a cualquiera de los dos rangos
    mask = cv2.bitwise_or(
        mask1,
        mask2
    )


    # Mostramos la cámara original
    cv2.imshow(
        "Camara web",
        frame
    )


    # Mostramos la primera máscara
    cv2.imshow(
        "Mascara 1",
        mask1
    )


    # Mostramos la segunda máscara
    cv2.imshow(
        "Mascara 2",
        mask2
    )


    # Mostramos la máscara final
    cv2.imshow(
        "Mascara roja",
        mask
    )


    # ESC para salir
    if cv2.waitKey(1) & 0xFF == 27:
        break


# Liberamos la cámara
cap.release()

# Cerramos todas las ventanas
cv2.destroyAllWindows()
```

### 5.4. Explicación del recorrido del programa

**Capturar y convertir una vez por fotograma.** Las importaciones, la apertura de cámara, la comprobación de `ret` y la conversión funcionan como en la segunda práctica. La variable `hsv` contiene el fotograma convertido. Ambas máscaras se calculan sobre **esa misma imagen**, de modo que cada posición corresponde al mismo píxel capturado en el mismo momento.

**Crear `mask1`.** `lower_red1` y `upper_red1` definen H entre 0 y 10, S entre 100 y 255 y V entre 100 y 255. `cv2.inRange` produce una imagen de un canal, con 255 en las posiciones que cumplen las tres condiciones y 0 en las demás. Esta selección coincide con el criterio del ejemplo HSV anterior.

**Crear `mask2`.** `lower_red2` y `upper_red2` conservan los intervalos S y V, pero cambian H a 170–179. La segunda máscara recupera los píxeles próximos al rojo que quedaron al otro lado del límite numérico. No convierte de nuevo la imagen ni modifica `mask1`.

**Unir con `cv2.bitwise_or`.** La operación compara las dos máscaras posición por posición y guarda el resultado en `mask`. Para máscaras binarias de 0 y 255, equivale a decir: «seleccionar este píxel si lo selecciona la primera máscara **o** la segunda».

**Mostrar cuatro ventanas.** «Camara web» contiene el fotograma BGR original. «Mascara 1» permite ver lo seleccionado por el intervalo bajo; «Mascara 2», por el alto; y «Mascara roja», la unión. Las ventanas intermedias ayudan a entender el aporte de cada intervalo, aunque una aplicación posterior podría mostrar únicamente el resultado final.

**Terminar y liberar.** ESC interrumpe el ciclo. Después se ejecutan `release` y `destroyAllWindows`, como en los ejemplos anteriores. Las cuatro ventanas se cierran al finalizar normalmente.

### 5.5. Por qué OR y no AND

OR conserva la **unión** de las selecciones. Para entenderlo, revisa los valores en una misma posición:

| `mask1` | `mask2` | OR: `mask` | Interpretación |
| --- | --- | --- | --- |
| 0 | 0 | 0 | No cumple ninguno de los intervalos. |
| 255 | 0 | 255 | Cumple solamente el intervalo bajo. |
| 0 | 255 | 255 | Cumple solamente el intervalo alto. |
| 255 | 255 | 255 | Si ambas seleccionaran, seguiría seleccionado. |

La última fila describe el comportamiento general de OR; **no ocurre con estos dos intervalos H**, porque un píxel no puede tener H entre 0 y 10 y entre 170 y 179 a la vez.

AND exigiría pertenecer a ambos rangos simultáneamente. Como son disjuntos, su intersección es vacía y el resultado quedaría negro. Necesitamos aceptar una de las dos regiones del círculo, no las dos al mismo tiempo.

`bitwise_or` trabaja sobre bits. En estas máscaras, 0 tiene todos los bits apagados y 255 tiene los ocho bits encendidos. Por eso OR coincide con la unión lógica esperada. No significa que cualquier OR sobre imágenes de color produzca una unión de objetos con ese mismo significado.

### 5.6. Ejemplos numéricos de la selección

Estos valores HSV son ejemplos didácticos para seguir las condiciones; no son mediciones de una cámara concreta.

| Píxel HSV | `mask1` | `mask2` | Máscara final | Motivo |
| --- | --- | --- | --- | --- |
| `[5, 180, 200]` | 255 | 0 | 255 | Tono dentro del primer rango y S, V suficientes. |
| `[175, 180, 200]` | 0 | 255 | 255 | Tono dentro del segundo rango y S, V suficientes. |
| `[60, 180, 200]` | 0 | 0 | 0 | Tono verde, fuera de ambos rangos de rojo. |
| `[175, 50, 200]` | 0 | 0 | 0 | Tono aceptable para el segundo rango, pero S menor que 100. |
| `[5, 180, 80]` | 0 | 0 | 0 | Tono aceptable para el primer rango, pero V menor que 100. |

El segundo píxel muestra exactamente la mejora respecto al ejemplo anterior: antes se perdía por H; ahora queda incluido mediante `mask2`. Los dos últimos muestran límites que la unión no resuelve: añadir el extremo alto no elimina los requisitos de saturación y brillo.

### 5.7. Qué debes observar durante la práctica

Prueba diferentes superficies rojas y observa las tres máscaras. Algunas pueden aparecer casi enteras en «Mascara 1», otras en «Mascara 2», y otras repartirse entre las dos. La unión debe conservar las regiones seleccionadas en cualquiera de ellas.

Si «Mascara 2» está vacía, puede que todos los píxeles rojos visibles estén en el extremo bajo o que los del extremo alto no cumplan S y V. No demuestra por sí solo un error: la distribución depende del objeto y de la captura. No fuerces un resultado cambiando números sin observar sus efectos.

Compara la segunda práctica con esta tercera manteniendo **los mismos límites del primer intervalo y las mismas condiciones**. Aquí el cambio está bien identificado: añadimos el segundo rango y su unión. Esto permite explicar mejor qué píxeles se recuperaron que comparar dos filtros calibrados de manera totalmente diferente.

Si aún faltan zonas, revisa sus canales: ampliar H no resuelve un rechazo por V, y bajar S puede aceptar fondos poco saturados. Ajusta una condición a la vez y verifica que no introduzca demasiadas selecciones falsas. La máscara final es la que utilizaremos como entrada a morfología y contornos cuando avancemos en el curso.


## 6. Práctica comparativa guiada

1. Usa el mismo objeto rojo, cámara, fondo y distancia para ambos programas.
2. Ejecuta BGR y calibra sus límites hasta obtener una selección razonable con luz estable. Anota los valores.
3. Introduce una sombra suave y observa qué partes desaparecen. No cambies los límites durante esta observación.
4. Cierra BGR con ESC y ejecuta HSV. Calibra H, S y V en la misma condición de luz inicial, comprobando la precaución del rojo circular.
5. Repite el cambio de iluminación y observa la máscara HSV sin modificar sus límites.
6. Prueba un objeto blanco, uno oscuro y otro rojo distinto. Busca regiones aceptadas que no sean tu objeto objetivo.
7. Registra qué cambios ayudarían a recuperar el objeto y qué selecciones indeseadas producirían.

| Condición de prueba | Máscara BGR | Máscara HSV | Explicación posible |
| --- | --- | --- | --- |
| Luz inicial | Completar durante la práctica. | Completar durante la práctica. | Ajuste inicial de cada filtro. |
| Sombra suave | Completar durante la práctica. | Completar durante la práctica. | Cambios de intensidades y de V. |
| Reflejo claro | Completar durante la práctica. | Completar durante la práctica. | Incremento de componentes o reducción de S. |
| Otro objeto rojo | Completar durante la práctica. | Completar durante la práctica. | Se selecciona color, no identidad. |

No hay un resultado predeterminado que debas forzar. Si ambos funcionan, explica qué condiciones lo permitieron. Si uno falla, identifica qué límite dejó fuera los píxeles y comprueba si ampliar ese límite introduce falsas selecciones.

## 7. Máscara e imagen filtrada no son lo mismo

Los tres programas muestran el video original y máscaras blancas y negras. No crean una tercera imagen con el objeto rojo visible y el resto del fondo negro. Para esa visualización se podría aplicar la máscara sobre el fotograma, por ejemplo mediante `bitwise_and`, pero sería una ampliación diferente de los ejemplos de esta clase.

La máscara es útil para las siguientes etapas: limpiar ruido con operaciones morfológicas y encontrar contornos. Conviene observarla directamente, porque puntos aislados o agujeros pueden dificultar la detección de figuras aunque el video original se vea bien.

## 8. Problemas frecuentes

**La máscara BGR queda negra:** revisa el orden B, G, R, el mínimo de R y las intensidades reales del objeto. **HSV no selecciona un rojo visible:** revisa el extremo alto de H y los mínimos de S y V. **Se selecciona demasiado fondo:** estrecha los intervalos después de observar qué valores producen el problema. **El objeto sale fragmentado:** puede haber sombras, reflejos o límites demasiado estrechos. **Hay puntos dispersos:** algunas regiones del fondo cumplen los rangos; el siguiente tema práctico explicará cómo limpiar la máscara.

La comprobación de lectura y la limpieza del programa mantienen las limitaciones del ejemplo de cámara: están previstas las salidas por ESC y por lectura fallida, pero no se garantiza la limpieza ante toda excepción. Esa mejora puede documentarse aparte sin alterar los códigos originales.

## 9. Comprobación y preguntas de repaso

Se verificó la sintaxis de los tres bloques Python. La captura y las máscaras deben probarse localmente: este entorno de documentación no dispone de OpenCV ni de una webcam con interfaz gráfica para ejecutarlas.

- ¿Por qué el primer intervalo está escrito en BGR y no en RGB?
- ¿Qué significa el tercer valor del límite inferior en cada programa?
- ¿Por qué el color rojo se muestra blanco en la máscara?
- ¿Qué ventaja ofrece ajustar V sin cambiar el intervalo de H?
- ¿Por qué el ejemplo HSV de un intervalo pierde rojos próximos al extremo alto de H?
- ¿Por qué `inRange` no puede representar el paso de H = 179 a H = 0 con un límite inferior de 170 y uno superior de 10?
- ¿Qué diferencia producirían OR y AND al combinar estos dos intervalos?
- ¿Por qué un objeto oscuro puede seguir sin detectarse después de añadir el segundo rango?
- ¿Cómo comprobarías si una mejora proviene de la representación o de haber elegido límites distintos?

[Anterior](04-video-camara-python.md) · [Índice](../README.md) · [Siguiente: Modelos de color](06-modelos-color.md)
