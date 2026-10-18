# 09. Detectar figuras

## Qué aprenderás

Relacionarás segmentación, contornos y medidas para reconocer figuras geométricas sencillas. Comprenderás qué reglas pueden servir en una práctica controlada y por qué esas reglas tienen límites.

## La idea en palabras sencillas

Para reconocer un triángulo sencillo solemos buscar tres esquinas y tres lados. El programa utilizará pistas parecidas, calculadas a partir del contorno. Primero reduce los pequeños detalles del borde y después examina la forma resultante.

Esta práctica funciona mejor con figuras planas, separadas y de frente. Una figura parcialmente tapada puede perder esquinas; una sombra puede parecer otra figura. No se trata de que el programa comprenda cualquier objeto: aplica reglas geométricas a lo que quedó seleccionado. La respuesta «no determinada» es útil cuando la forma no está clara.

## 1. Del contorno a una hipótesis

Un contorno puede contener muchos puntos. Para identificar una figura necesitamos resumir su geometría: cuántos lados aparenta tener, qué proporciones presenta y qué tan parecida es a un círculo. Esa descripción permite proponer una clase como triángulo, cuadrilátero o círculo.

Este procedimiento reconoce una **silueta geométrica** bajo ciertas condiciones. No identifica automáticamente cualquier objeto con esa forma. Una sombra triangular puede cumplir la regla de triángulo, y una taza vista desde arriba puede generar una región circular.

## 2. Aproximación poligonal

```python
approx = cv2.approxPolyDP(contour, epsilon, True)
```

`approxPolyDP` aproxima una curva por otra con menos vértices, usando una tolerancia llamada epsilon. La idea es conservar la forma global mientras se eliminan variaciones pequeñas del borde.

Es habitual relacionar epsilon con el perímetro para que la tolerancia se adapte parcialmente al tamaño de la figura. El factor exacto debe ajustarse: una tolerancia muy pequeña conserva ruido y demasiados vértices; una muy grande simplifica tanto que elimina esquinas reales.

El resultado depende también de la máscara. Si falta una esquina porque el filtro no la seleccionó, la aproximación no puede reconstruirla con certeza. Antes de modificar epsilon, revisa la imagen binaria.

## 3. Número de vértices

Tres vértices pueden sugerir un triángulo y cuatro un cuadrilátero. Estas son hipótesis útiles para figuras planas, separadas y claramente segmentadas. Deben acompañarse de filtros de área y, cuando la aplicación lo requiera, comprobaciones de convexidad, ángulos o proporciones.

Contar cuatro vértices no basta para afirmar «rectángulo»: un trapecio o un cuadrilátero irregular también tiene cuatro. Del mismo modo, muchos vértices no bastan para afirmar «círculo»: un borde irregular puede producir una aproximación con muchos puntos.

## 4. Cuadrados, rectángulos y perspectiva

La relación ancho / alto del rectángulo envolvente puede ayudar a separar un cuadrado de un rectángulo alargado en una escena bien alineada. Sin embargo, el rectángulo alineado con los ejes cambia cuando la figura rota. Un objeto alargado inclinado puede tener un rectángulo envolvente de proporciones engañosas.

```python
rect = cv2.minAreaRect(contour)
```

Un rectángulo orientado, como el obtenido con `minAreaRect`, reduce ese problema de rotación en el plano, pero no elimina las deformaciones de perspectiva. Un cuadrado inclinado respecto a la cámara puede verse como otro cuadrilátero. Para una práctica inicial, coloca figuras planas de frente y expresa esa condición como parte del método.

## 5. Circularidad

Una medida habitual es **circularidad = 4π × área / perímetro²**. En geometría continua, un círculo ideal tiene circularidad 1. Figuras alargadas o con borde irregular suelen tener valores menores.

En imágenes digitales hay aproximaciones y discretización; no debes esperar un valor exactamente igual a 1. El ruido del borde aumenta el perímetro y puede reducir la circularidad. Antes de calcularla debes comprobar que el perímetro no sea cero.

Un umbral de circularidad necesita calibración y, por sí solo, tampoco prueba la identidad de un objeto. Puede combinarse con área, relación de aspecto y una máscara adecuada.

## 6. Procedimiento completo

1. Capturar un fotograma válido.
2. Seleccionar la región de interés por color o intensidad.
3. Limpiar la máscara conservando las figuras relevantes.
4. Encontrar los contornos.
5. Descartar regiones demasiado pequeñas o degeneradas.
6. Calcular perímetro y aproximación poligonal.
7. Aplicar las reglas geométricas y asignar una hipótesis.
8. Dibujar contorno, etiqueta y, si hace falta, centro o caja.

Mantén una opción «no determinada» cuando las medidas no apoyen una clase clara. Forzar una etiqueta en todos los casos produce resultados aparentemente completos, pero menos confiables.

## Actividad práctica

Usa triángulo, cuadrado, rectángulo y círculo sobre un fondo contrastante. Prueba cada uno de frente, rotado y parcialmente cubierto. Registra la figura real, los vértices calculados y la clase asignada. Busca al menos un caso donde el método falle y explica qué etapa lo causa.

## Preparación de la práctica

Organiza tus reglas antes de programar: escribe qué medidas utilizarás para cada figura y cuándo devolverás una clase no determinada. Usa figuras separadas y de frente para la primera prueba; después cambia orientación, distancia y oclusión para reconocer los límites del método.

## Ejemplo explicado: una figura que deja de parecer triángulo

Coloca un triángulo verde sobre un fondo claro. Si el filtro de color conserva toda su silueta, la aproximación del contorno puede dejar tres esquinas y la regla proponer «triángulo».

Ahora tapa una de sus puntas. El objeto físico sigue siendo un triángulo, pero la parte visible ya no tiene necesariamente la misma silueta. La regla podría proponer otra clase o no determinarla. No significa que el programa haya olvidado la figura: las reglas analizan la información visible de ese momento.

Haz una tabla con tres columnas: figura que colocaste, respuesta del programa y explicación. Incluye una prueba de frente, otra girada y otra parcialmente tapada. No borres los fallos del registro: ayudan a explicar cuándo puedes utilizar el método.


## Práctica: localizar una hoja verde de cuatro esquinas

### Objetivo y preparación

En esta práctica analizaremos una hoja o un recorte verde de cuatro esquinas, bien iluminado, separado de otros objetos y colocado de frente a la cámara. El programa buscará regiones verdes y comprobará si su contorno simplificado tiene cuatro vértices.

Una hoja rectangular debería ser una candidata en esas condiciones, pero la regla también puede aceptar un cuadrado o un trapecio. Por eso la etiqueta del programa será **«Cuadrilatero verde»**. Un cuadrilátero es una figura de cuatro lados; un rectángulo además necesita cuatro ángulos rectos. Este ejemplo no comprueba esos ángulos.

Aunque el texto del capítulo presenta otras figuras y medidas como referencia, el programa se centra en esta regla de cuatro esquinas. No clasifica triángulos ni círculos. Si una región no cumple la regla, simplemente no dibuja su caja ni su nombre.

1. Cierra el programa de contornos con ESC para dejar libre la cámara.
2. Crea `figuras_verdes.py` en la carpeta del curso.
3. Copia el programa completo y guárdalo.
4. Ejecútalo con el mismo Python y las bibliotecas de las prácticas anteriores.
5. Coloca la hoja verde de frente y lejos de los bordes del video, dejando espacio arriba y abajo para los textos.

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
kernel = np.ones((5, 5), np.uint8)


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
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # ==========================================
    # MÁSCARA DE VERDE: UN SOLO INTERVALO
    # ==========================================

    lower_green = np.array([35, 80, 60], dtype=np.uint8)
    upper_green = np.array([85, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_green, upper_green)


    # ==========================================
    # LIMPIEZA
    # ==========================================

    # Erosión
    mask = cv2.erode(mask, kernel, iterations=1)

    # Dilatación del resultado de la erosión
    mask = cv2.dilate(mask, kernel, iterations=1)


    # ==========================================
    # CONTORNOS
    # ==========================================

    # Buscamos los contornos de las regiones blancas
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # ==========================================
    # ANALIZAR CADA CONTORNO
    # ==========================================

    for contour in contours:

        # Calculamos el área e ignoramos regiones pequeñas
        area = cv2.contourArea(contour)

        if area < 500:
            continue

        # Calculamos el perímetro de una curva cerrada
        perimeter = cv2.arcLength(contour, True)

        # Tolerancia para simplificar el borde
        epsilon = 0.04 * perimeter

        # Aproximamos el contorno con un polígono cerrado
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Contamos los vértices del polígono aproximado
        corners = len(approx)

        # Cuatro esquinas indican un cuadrilátero candidato
        # No verificamos aquí que sus ángulos sean rectos
        if corners == 4:

            # Caja alineada con los ejes que contiene el contorno
            x, y, w, h = cv2.boundingRect(contour)

            # Dibujamos la caja en el fotograma
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # Mostramos la clase que permite afirmar esta regla
            cv2.putText(frame, "Cuadrilatero verde", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Mostramos el número de esquinas
            cv2.putText(frame, f"Esquinas: {corners}", (x, y + h + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Mostramos el resultado y la máscara procesada
    cv2.imshow("Deteccion de figuras verdes", frame)
    cv2.imshow("Mascara", mask)


    # ESC para salir
    if cv2.waitKey(1) & 0xFF == 27:
        break


# Liberamos la cámara
cap.release()

# Cerramos las ventanas
cv2.destroyAllWindows()
```

### 1. Repasar el recorrido que ya funciona

Las primeras instrucciones importan las herramientas, abren la cámara y crean el kernel de 5 × 5. Dentro del `while`, cada lectura válida produce un fotograma. El programa convierte a HSV y selecciona verde mediante **un solo intervalo y una sola máscara**, como en los temas 06 a 08.

Después aplica erosión y dilatación en ese orden. Ambas guardan su salida en `mask`, de modo que la segunda recibe el resultado de la primera. El mismo nombre conserva ahora la máscara procesada, no la original sin limpiar.

```python
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

`findContours` busca las fronteras externas de esa máscara. El `for` permite analizar cada una y `continue` salta aquellas cuya área es menor que 500. Ese límite sigue siendo una referencia inicial que debes ajustar a la distancia y resolución de tu escena.

Hasta aquí, el recorrido coincide con el programa de contornos. Ahora añadimos medidas para decidir qué regiones dibujar.

### 2. Medir el perímetro con `arcLength`

El **perímetro** es la longitud del borde. Imagina recorrer la orilla de la hoja con un hilo y después medir el hilo. Aquí se mide sobre la imagen, por lo que el resultado está expresado en unidades de píxel, no en centímetros.

```python
perimeter = cv2.arcLength(contour, True)
```

`cv2.arcLength(contour, True)` recibe la secuencia de puntos y la indicación de que la curva es cerrada. `True` significa que se incluye el segmento desde el último punto de vuelta al primero. La variable `perimeter` conserva la longitud calculada.

No confundas área y perímetro. El área describe el espacio encerrado, mientras el perímetro describe la longitud de su frontera. Una región con borde irregular puede tener un perímetro largo sin ocupar un área muy grande.

### 3. Elegir la tolerancia `epsilon`

Una frontera de una imagen puede tener pequeños escalones, irregularidades o ruido. Si contáramos cada punto de esa frontera como una esquina, obtendríamos demasiados. Antes de contar, necesitamos simplificarla.

`epsilon = 0.04 * perimeter` calcula una tolerancia igual al **4 % del perímetro**. El asterisco significa multiplicación. Si el perímetro calculado fuera 600 píxeles, epsilon sería 24 píxeles. Es un ejemplo numérico, no un tamaño fijo de la hoja.

Esta tolerancia orienta cuánto puede separarse la aproximación de la curva original. No significa que el programa tenga 96 % de precisión ni que borre exactamente 4 % de los puntos.

Relacionarla con el perímetro permite adaptar la escala de la tolerancia al tamaño aparente del contorno. No garantiza estabilidad total ante ruido, distancia u oclusión: sigue siendo un parámetro que debes probar.

### 4. Simplificar el borde con `approxPolyDP`

```python
approx = cv2.approxPolyDP(contour, epsilon, True)
```

`cv2.approxPolyDP(contour, epsilon, True)` recibe el contorno, su tolerancia y la indicación de tratar el resultado como un polígono cerrado. Devuelve una secuencia simplificada de puntos que conservamos en `approx`.

Imagina pasar de un trazo tembloroso alrededor de una hoja a una figura con unos pocos segmentos. La función busca una aproximación geométrica; no sabe que el objeto es papel ni que debería tener cuatro lados.

| Tolerancia | Efecto que puedes observar |
| --- | --- |
| Muy pequeña | Conserva más variaciones del borde y puede dejar demasiados vértices. |
| Muy grande | Simplifica demasiado y puede eliminar esquinas reales. |
| Adecuada para la escena | Conserva la forma general sin seguir todos los detalles pequeños. |

No se debe aumentar epsilon hasta conseguir cuatro esquinas a cualquier costo. Si fuerzas el parámetro, una forma distinta también puede terminar aproximada con cuatro puntos.

### 5. Contar y comparar las esquinas

```python
corners = len(approx)
```

`len(approx)` cuenta cuántos puntos hay en la aproximación. Guardamos ese número en `corners`, que significa esquinas. Estos puntos son los vértices del polígono calculado; su cantidad puede variar si cambia la máscara.

`if corners == 4` pregunta si el número es exactamente cuatro. Recuerda que `=` asigna un valor y `==` compara dos valores. La sangría indica qué instrucciones se ejecutan solamente cuando se cumple esa comparación.

En esta práctica, cuatro puntos permiten tratar la región como **candidata a cuadrilátero**, no certificar que sea un rectángulo. Tampoco se comprueba convexidad, orden de ángulos ni identidad del objeto. Una evaluación geométrica más exigente necesitaría condiciones adicionales.

Si hay tres, cinco o más vértices, el programa no entra en ese bloque y sigue con el siguiente contorno. La imagen continúa mostrándose: no detectar una candidata no es un fallo de la cámara.

### 6. Obtener una caja con `boundingRect`

```python
x, y, w, h = cv2.boundingRect(contour)
```

`x, y, w, h = cv2.boundingRect(contour)` obtiene cuatro resultados y los guarda en cuatro variables:

| Variable | Significado |
| --- | --- |
| `x` | Posición horizontal de la esquina superior izquierda de la caja. |
| `y` | Posición vertical de esa esquina. |
| `w` | Ancho de la caja. |
| `h` | Alto de la caja. |

El rectángulo calculado contiene el contorno y está alineado con los ejes de la imagen. Puede incluir fondo y no sigue necesariamente los lados de una hoja girada. Dibujar esta caja tampoco demuestra que el objeto original sea rectangular: cualquier contorno puede tener una caja envolvente rectangular.

En el programa se calcula la caja del `contour` original, después de comprobar la cantidad de puntos de `approx`. Son datos relacionados, pero no son la misma secuencia de puntos.

### 7. Dibujar el rectángulo y los textos

```python
cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
```

`cv2.rectangle` dibuja sobre `frame` utilizando una esquina en `(x, y)` y la opuesta en `(x + w, y + h)`. Los signos `+` suman ancho y alto a la posición inicial. `(0, 255, 0)` indica verde en BGR y `3` es el grosor de la línea.

A diferencia del tema 08, este ejemplo dibuja directamente sobre `frame`, sin crear `result`. Es adecuado para mostrar el resultado al final de la vuelta, porque la máscara ya se calculó antes de agregar los dibujos. La siguiente lectura entrega otro fotograma: los rectángulos no se van acumulando sobre el video futuro.

```python
cv2.putText(frame, "Cuadrilatero verde", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
```

`cv2.putText` añade texto sobre la imagen. Sus argumentos indican dónde dibujar, qué escribir, la posición, la fuente, la escala, el color y el grosor:

| Elemento | Cómo se utiliza aquí |
| --- | --- |
| `"Cuadrilatero verde"` | Etiqueta acorde con la regla de cuatro vértices. |
| `(x, y - 10)` | Posición del primer texto, un poco arriba de la caja. |
| `cv2.FONT_HERSHEY_SIMPLEX` | Estilo de letra disponible en OpenCV. |
| `0.8` o `0.6` | Escala del texto, no su confianza. |
| `(0, 255, 0)` | Color de la escritura en BGR. |
| `2` | Grosor de los trazos. |

`f"Esquinas: {corners}"` es un texto con un valor insertado. La letra `f` permite reemplazar lo que está entre llaves por su contenido. Cuando la condición se cumple, se muestra «Esquinas: 4». No es un mensaje que debas escribir manualmente en la terminal.

El segundo texto se coloca en `(x, y + h + 25)`, debajo de la caja. Si la hoja está muy cerca del límite superior o inferior del video, algún texto puede quedar cortado; muévela hacia el centro antes de pensar que falló la detección. Las letras se escriben sin acentos en el código porque la fuente básica de OpenCV tiene un repertorio limitado.

### 8. Mostrar las ventanas y terminar

«Deteccion de figuras verdes» contiene el fotograma con las cajas y etiquetas de las regiones aceptadas. «Mascara» muestra la selección limpia. Una región blanca puede aparecer en esa máscara y no tener caja: quizá no supera el área mínima o su aproximación no tiene cuatro vértices.

ESC termina el ciclo; después se libera la cámara y se cierran las ventanas. El ejemplo conserva el manejo de salidas normales de las prácticas anteriores. No asegura limpieza ante cualquier excepción imprevista.

### Pruebas del laboratorio

1. **Hoja rectangular de frente:** observa si aparece una caja y la etiqueta. Antes de ajustar reglas, comprueba que la máscara esté completa.
2. **Cuadrado verde:** también puede aceptarse, porque tiene cuatro vértices. Además, geométricamente un cuadrado es un caso particular de rectángulo.
3. **Trapecio verde:** puede aceptarse como cuadrilátero. Esta prueba muestra por qué cuatro esquinas no bastan para verificar ángulos rectos.
4. **Triángulo o círculo verde:** en una segmentación y aproximación adecuadas no deberían activar esta regla, pero pueden aparecer falsos positivos. El programa no les asignará un nombre alternativo.
5. **Hoja inclinada, doblada o parcialmente tapada:** observa cómo cambia el contorno visible y si deja de cumplir la regla. La hoja física no cambia de identidad, pero su silueta en la imagen sí puede cambiar.
6. **Distancia:** aleja la hoja. Puede perder detalle o quedar por debajo del filtro de área.

```python
print(corners)
```

Registra figura real, si aparece caja y qué muestra la máscara. Para observar el conteo de otras formas, puedes colocar temporalmente un `print(corners)` después de calcular `corners`, fuera del bloque `if corners == 4`. El video repetirá muchas lecturas en la terminal; retíralo después de la observación. Es una ayuda de diagnóstico, no un requisito del programa.

### Ajustar sin perder la explicación

Si necesitas probar otra tolerancia, cambia solo `0.04`, por ejemplo a `0.02`, guarda y vuelve a ejecutar. Compara sobre la misma hoja y distancia. Un valor menor puede conservar más vértices. Después vuelve al valor anterior para comparar, sin modificar al mismo tiempo área mínima, color y kernel.

Si una hoja no se detecta, revisa en este orden: captura, máscara verde, efecto de la limpieza, tamaño de la región y aproximación. Cambiar epsilon no recupera una hoja que nunca quedó seleccionada.

### Qué debes poder explicar al terminar

- ¿Qué diferencia hay entre área y perímetro?
- ¿Qué significa el valor 0.04 en el cálculo de epsilon?
- ¿Por qué no contamos directamente todos los puntos del contorno?
- ¿Qué comprueba realmente `corners == 4`?
- ¿Por qué una caja rectangular alrededor de una región no prueba que la región sea rectangular?
- ¿Por qué una región blanca de la máscara puede quedar sin etiqueta?

Con esta práctica completas el recorrido de reglas de OpenCV: **capturar → seleccionar color → limpiar → encontrar fronteras → medir → decidir → dibujar**.

## Consulta: funciones nuevas para describir y marcar figuras

Las herramientas de captura, filtro, limpieza y búsqueda de contornos ya están explicadas en los capítulos anteriores. Estas fichas se centran en los pasos que añadimos para analizar una figura. Las formas mostradas son las de uso frecuente en Python con OpenCV 4.

### `cv2.arcLength`: calcular longitud de una curva

Forma: `cv2.arcLength(curve, closed)`.

| Parámetro | Necesidad | Qué significa |
| --- | --- | --- |
| `curve` | Obligatorio. | Secuencia de puntos, como `contour`. No recibe la máscara completa. |
| `closed` | Obligatorio. | `True` incluye la unión del último punto con el primero; `False` trata el recorrido como abierto. |

**Devuelve:** una longitud numérica en unidades de píxel. Para el perímetro de la silueta utilizamos `True`. Para una línea abierta, como un recorrido que no quieres cerrar, utilizarías `False`.

No determina por sí sola si una figura es un rectángulo. Tampoco mide la longitud física de los lados de la hoja sin una relación de escala o calibración adicional. El resultado depende del contorno que recibió; un borde ruidoso puede aumentar la longitud.

### `cv2.approxPolyDP`: simplificar una curva con menos vértices

Forma habitual: `cv2.approxPolyDP(curve, epsilon, closed)`; la interfaz también permite un destino opcional.

| Parámetro | Necesidad | Uso en la práctica y significado |
| --- | --- | --- |
| `curve` | Obligatorio. | Contorno que vamos a aproximar. |
| `epsilon` | Obligatorio. | Tolerancia de distancia entre la curva y su aproximación, expresada en las mismas unidades que sus coordenadas. |
| `closed` | Obligatorio. | `True` para una aproximación cerrada; `False` para una curva abierta. |

**Devuelve:** una nueva secuencia de puntos. En este programa representa un polígono aproximado y se guarda en `approx`. No devuelve el nombre de una figura ni altera automáticamente la máscara o el fotograma.

**Cómo suele elegirse epsilon:** como una fracción del perímetro, por ejemplo `0.02 * perimeter` o `0.04 * perimeter`, ajustada según el ruido y la tarea. Son valores para probar, no constantes universales. El programa parte de 0.04 para mantener la regla de la práctica.

Un valor menor tiende a conservar más detalles. Uno mayor permite una simplificación más fuerte. No se interpreta como porcentaje de aciertos ni como porcentaje exacto de puntos eliminados. Una tolerancia negativa no es válida.

Si la máscara está incompleta, no aumentes epsilon esperando que invente la parte oculta. La función aproxima la curva recibida. Para una figura pequeña, un cambio de pocos píxeles puede cambiar el número de vértices de forma notable.

### `len`: contar los elementos de la aproximación

`len(objeto)` es una función de Python, no de OpenCV. Necesita un objeto que tenga longitud y **devuelve un entero**. En `len(approx)` cuenta los elementos de la secuencia de vértices; no calcula el área ni los lados físicos del papel.

No necesita otros parámetros para este uso. Escribe `len(approx)`, no `approx.len()`. El nombre `corners` es una variable elegida para guardar ese resultado y no una función que descubra esquinas por su cuenta.

### `cv2.boundingRect`: obtener una caja alineada con los ejes

Forma: `cv2.boundingRect(array)`.

`array` es el único parámetro necesario en esta forma. Puede representar puntos como los de un contorno; la función también admite una imagen de un canal de ocho bits para obtener la caja de sus píxeles no nulos. En el programa entregamos el contorno individual.

**Devuelve cuatro enteros:** `x`, `y`, `w` y `h`. La esquina superior izquierda es `(x, y)` y el tamaño es ancho `w` y alto `h`. Si necesitas extraer una región mediante cortes del arreglo, la forma habitual sería usar filas de `y` a `y + h` y columnas de `x` a `x + w`, recordando que el extremo final de un corte de Python queda excluido.

El punto `(x + w, y + h)` se utiliza en el dibujo de la práctica como extremo de referencia de la caja. No confundas ancho y alto con las coordenadas máximas ni con una lista de vértices del objeto. Esta caja siempre está alineada con la imagen, aunque la hoja esté girada.

### `cv2.rectangle`: dibujar una caja

Forma habitual: `cv2.rectangle(img, pt1, pt2, color, thickness=1, lineType=cv2.LINE_8, shift=0)`.

| Parámetro | Necesidad | Opciones comunes y uso del taller |
| --- | --- | --- |
| `img` | Obligatorio. | Imagen que recibirá el dibujo; aquí `frame`. |
| `pt1` | Obligatorio. | Primera esquina de la caja, `(x, y)`. |
| `pt2` | Obligatorio. | Esquina opuesta, basada en `(x + w, y + h)`. |
| `color` | Obligatorio. | Color BGR de la línea. No es un intervalo de detección. |
| `thickness` | Opcional; `1`. | Grosor positivo. La práctica usa 3. Un valor negativo como `FILLED` rellena el rectángulo. |
| `lineType` | Opcional; `LINE_8`. | Tipo de línea; `LINE_AA` suaviza el dibujo en imágenes compatibles. |
| `shift` | Opcional; `0`. | Número de bits fraccionarios en las coordenadas para representar posiciones subpíxel. En el taller lo dejamos en 0. |

**Modifica `img` y la devuelve.** Por eso no hace falta escribir una nueva asignación para ver el dibujo en `frame`. Solo dibuja la caja que le indicas: no busca rectángulos ni comprueba ángulos.

El relleno es útil en otras tareas, pero aquí taparía el interior de la hoja y dificultaría observarla. Conserva un grosor positivo para estudiar el contorno y la caja.

### `cv2.putText`: escribir información sobre la imagen

Forma de referencia: `cv2.putText(img, text, org, fontFace, fontScale, color, thickness=1, lineType=cv2.LINE_8, bottomLeftOrigin=False)`.

| Parámetro | Necesidad | Significado y opciones habituales |
| --- | --- | --- |
| `img` | Obligatorio. | Imagen donde aparecerá el texto. |
| `text` | Obligatorio. | Texto, por ejemplo `"Cuadrilatero verde"` o un texto con valores insertados. |
| `org` | Obligatorio. | Posición de referencia de la línea base del texto, en coordenadas `(x, y)`. No es la esquina superior izquierda de las letras. |
| `fontFace` | Obligatorio. | Tipo de letra. Se utiliza habitualmente `FONT_HERSHEY_SIMPLEX` para mensajes sencillos. |
| `fontScale` | Obligatorio. | Factor de escala respecto al tamaño base de esa fuente. Se prueban valores como 0.5, 0.6 u 0.8 según la resolución. |
| `color` | Obligatorio. | Color BGR del texto. Conviene que contraste con la imagen. |
| `thickness` | Opcional; `1`. | Grosor de los trazos; en la práctica se usa 2. |
| `lineType` | Opcional; `LINE_8`. | `LINE_AA` es frecuente si quieres suavizar las letras en una imagen de ocho bits. |
| `bottomLeftOrigin` | Opcional; `False`. | Convención de origen para colocar el texto. El taller conserva la habitual de las imágenes. |

**Modifica la imagen y la devuelve.** No imprime en la terminal: para eso se utiliza `print`. Cambiar el texto no cambia la decisión geométrica; escribir «Rectángulo» no verifica que lo sea.

`fontScale` no es un tamaño en píxeles, una probabilidad ni una puntuación del detector. La posición `org` se interpreta respecto a la imagen completa. Si queda fuera o muy cerca de un borde, las letras pueden cortarse. Para esta práctica basta centrar la hoja y dejar espacio alrededor.

Las fuentes básicas de OpenCV tienen un repertorio limitado: utilizamos rótulos sin acentos en los programas. Para sistemas de escritura o tipografías más completas se necesita otra solución de dibujo, que no es necesaria para el taller.

### Cómo elegir qué parámetro modificar

| Si observas esto | Revisa antes | Evita confundirlo con |
| --- | --- | --- |
| No se selecciona la hoja | Intervalo HSV e iluminación. | Grosor o color de la caja. |
| Región pequeña descartada | Umbral de área y distancia. | Escala de la fuente. |
| Demasiados o pocos vértices | Máscara, kernel y epsilon. | Tamaño de letra de la etiqueta. |
| Caja o texto poco visible | Color, grosor, escala y posición del dibujo. | Parámetros del filtro de color. |

Esta separación es útil para depurar: algunas funciones **calculan información** y otras solo **la muestran**. Cambia un parámetro del paso donde se origina el problema, no todos al mismo tiempo.


## Para dar el siguiente paso

Las reglas de color y número de esquinas nos sirven para esta práctica con hojas. **¿Qué haríamos si quisiéramos reconocer una taza o una mochila con distintos colores, posiciones y fondos, sin escribir una regla para cada apariencia?**

En el siguiente capítulo conoceremos Deep Learning: una forma de ajustar modelos a partir de ejemplos etiquetados para aprender patrones útiles. Esto abrirá el camino al detector de objetos con YOLO.

[Anterior](08-contornos.md) · [Índice](../README.md) · [Siguiente: Deep Learning](10-introduccion-deep-learning.md)
