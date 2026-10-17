# 12. Etiquetado y bounding boxes

## Qué aprenderás

Aprenderás a describir objetos mediante clases y cajas delimitadoras, a interpretar coordenadas y a revisar que las anotaciones proporcionen una supervisión consistente.

## La idea en palabras sencillas

Etiquetar significa dar al modelo la respuesta que esperamos que aprenda. En una fotografía con dos vasos, dibujas una caja alrededor de cada vaso y asignas a ambas la clase «vaso». Cada objeto visible que etiquetas es una instancia.

La caja dice dónde está; el nombre de clase dice qué es. Si una caja está desplazada o tiene el nombre incorrecto, el ejemplo enseña una respuesta equivocada. Comenzaremos revisando visualmente las cajas. Después veremos cómo se guardan como números para que el programa pueda leerlas.

## 1. Qué es una bounding box

Una **bounding box**, o caja delimitadora, es un rectángulo que localiza una instancia. En la detección convencional está alineado con los ejes de la imagen. La caja contiene el objeto, pero también puede incluir fondo, especialmente si el objeto tiene forma irregular.

Etiquetar una caja implica dos decisiones: qué clase corresponde y qué región debe abarcar. Una clase correcta con una caja muy desplazada sigue siendo una anotación incorrecta para entrenamiento.

## 2. Convenciones de coordenadas

Una caja puede representarse de distintas maneras:

- Esquina superior izquierda y esquina inferior derecha: xmin, ymin, xmax, ymax.
- Esquina superior izquierda, ancho y alto: x, y, w, h.
- Centro, ancho y alto: xc, yc, w, h.

Son representaciones convertibles si conocemos su significado. No puedes intercambiarlas directamente. Un valor que representa el centro no debe interpretarse como la esquina superior izquierda.

En la convención geométrica usual, x crece hacia la derecha y y hacia abajo. Los límites deben ser coherentes con el ancho y alto de la imagen y con la convención del formato sobre el borde final.

## 3. Formato YOLO normalizado

En el formato de etiquetas habitual para detección con YOLO, cada instancia se describe en una línea con identificador de clase, centro x, centro y, ancho y alto. Las coordenadas se normalizan respecto al ancho o alto de la imagen, según corresponda.

Esto permite expresar la posición en una escala relativa. Para convertir desde esquinas, calcula primero el centro como el promedio de los extremos y el tamaño como su diferencia. Después divide las magnitudes horizontales entre el ancho de la imagen y las verticales entre el alto.

No se debe dividir todo entre el ancho ni intercambiar las dimensiones. Las imágenes rectangulares hacen esos errores más visibles.

## 4. Ejemplo numérico explicado

Considera una imagen de 800 píxeles de ancho y 600 de alto. Una caja va desde x = 200 hasta x = 400, y desde y = 150 hasta y = 450.

- Su centro horizontal es 300 y su centro vertical es 300.
- Su ancho es 200 y su alto es 300.
- El centro x normalizado es 300 / 800 = 0,375.
- El centro y normalizado es 300 / 600 = 0,5.
- El ancho normalizado es 200 / 800 = 0,25.
- El alto normalizado es 300 / 600 = 0,5.

Utiliza este ejemplo numérico para comprobar que entiendes la normalización antes de revisar las anotaciones de tu dataset. El identificador de clase depende del mapa de clases del proyecto.

## 5. Identificadores de clase

En el formato habitual, los identificadores comienzan en 0 y corresponden al orden de los nombres en la configuración del dataset. Si 0 significa «vaso» y 1 significa «botella», debes mantener esa relación en todas las imágenes y en la configuración utilizada para entrenar.

Una imagen con tres objetos necesita tres anotaciones, aunque los tres pertenezcan a la misma clase. El archivo de etiquetas asociado debe corresponder a la imagen correcta; suele conservar el mismo nombre base y cambiar la extensión.

## 6. Política de anotación

Para una práctica básica, procura que la caja ajuste la extensión visible del objeto con poco margen innecesario. Si el objeto está parcialmente oculto, define una política consistente sobre lo visible. No mezcles cajas de la parte visible con cajas que estiman todo el objeto oculto sin documentar ese cambio.

Si una instancia está truncada por el borde, la caja debe respetar los límites de la imagen de acuerdo con el formato. También define qué hacer con objetos demasiado pequeños o imposibles de identificar. La consistencia entre anotadores es más útil que improvisar cada caso.

## 7. Revisión visual

Visualiza las cajas sobre las imágenes exportadas. Revisa nombres de clases, cajas desplazadas, instancias omitidas y archivos sin pareja. Si se redimensiona o recorta una imagen, sus cajas deben transformarse junto con ella.

Una anotación mal convertida puede tener números dentro de 0 y 1 y aun así señalar una región equivocada. La revisión visual complementa la validación del formato.

## Actividad de comprensión

Convierte una caja de esquinas a centro y tamaño, primero en píxeles y después normalizada. Explica qué cambiaría al reducir la imagen a la mitad conservando proporciones: los valores en píxeles cambian, pero los valores relativos permanecen iguales si la transformación es uniforme y coherente.

## Antes de exportar las etiquetas

Visualiza las cajas sobre varias imágenes y comprueba que sus clases coincidan con el mapa del proyecto. Repite la conversión numérica de esta sección con una caja de tu dataset. No avances al entrenamiento si las posiciones o las clases son incoherentes.

## Tu primera anotación, paso a paso

1. Abre una imagen en la herramienta de etiquetado y localiza un objeto de una clase del proyecto.
2. Selecciona la herramienta para dibujar una caja rectangular.
3. Arrastra desde una esquina hasta la opuesta, procurando encerrar la parte del objeto definida por la política de anotación.
4. Asigna el nombre de clase correcto. No escribas un nombre distinto para cada objeto físico: dos vasos pertenecen a la misma clase si esa es la definición del proyecto.
5. Repite con los demás objetos de interés de la fotografía.
6. Guarda y vuelve a revisar las cajas. Ajusta las que dejen fuera partes relevantes o incluyan demasiado espacio innecesario.

Imagina que aparecen dos vasos y una botella: necesitas tres cajas, no una sola caja gigante para los tres. Si solo anotas un vaso, el ejemplo queda incompleto para la tarea. Antes de continuar con muchas imágenes, revisa unas pocas con el instructor para confirmar que todos aplican el mismo criterio.

## Cómo se guarda la caja del ejemplo

Retoma la imagen de 800 × 600 y la caja ya calculada en esta sección. Si su clase es 0, una línea de etiqueta de detección YOLO sería:

```text
0 0.375 0.5 0.25 0.5
```

No es un programa que debas ejecutar. Es un registro de datos: clase, centro horizontal, centro vertical, ancho y alto. Los archivos utilizan **punto decimal**, aunque al explicar los cálculos en español aparezca coma decimal.

| Campo | Valor | Qué describe |
| --- | --- | --- |
| Clase | 0 | Primer nombre del mapa de clases, por ejemplo vaso. |
| Centro x | 0.375 | Posición horizontal relativa al ancho. |
| Centro y | 0.5 | Posición vertical relativa al alto. |
| Ancho | 0.25 | Caja que ocupa un cuarto del ancho de la imagen. |
| Alto | 0.5 | Caja que ocupa la mitad del alto de la imagen. |

Si la imagen se llama `foto_01.jpg`, su archivo de etiquetas suele llamarse `foto_01.txt` en la carpeta de etiquetas de la misma división. Dos objetos requieren dos líneas. El orden de las líneas no representa un seguimiento de identidades entre imágenes.

## Revisión en parejas

Una persona etiqueta y otra revisa una muestra con las cajas superpuestas. Comprueben tres cosas: no faltan instancias que deban anotarse, el nombre corresponde a la clase correcta y las cajas siguen la misma política.

Busquen especialmente un caso parcialmente oculto y otro pegado al borde. Si las dos personas dibujarían cajas muy diferentes, primero acuerden el criterio. Repetir un desacuerdo en cien fotos no lo corrige.

También revisen imágenes negativas. No deben contener objetos de las clases de interés sin anotar, salvo los casos que una política explícita de la tarea trate de otra forma. Para el taller utilizaremos una política sencilla y consistente definida con el instructor.

**Resultado esperado:** una colección de imágenes acompañadas por etiquetas que se puedan interpretar y verificar visualmente. No necesitas escribir a mano todos los archivos si la plataforma los exporta, pero entender el formato te permite reconocer errores.

## Para dar el siguiente paso

Ya entendemos qué información necesita una etiqueta. **¿Dónde podemos organizar muchas imágenes, revisar sus cajas y preparar una versión que después podamos descargar?** Conoceremos Roboflow y el papel que tiene en el proyecto.

[Anterior](11-que-es-un-dataset.md) · [Índice](../README.md) · [Siguiente: Roboflow](13-que-es-roboflow.md)
