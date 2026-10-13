# 12. Etiquetado y bounding boxes

## Qué aprenderás

Aprenderás a describir objetos mediante clases y cajas delimitadoras, a interpretar coordenadas y a revisar que las anotaciones proporcionen una supervisión consistente.

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

[Anterior](11-que-es-un-dataset.md) · [Índice](../README.md) · [Siguiente: Roboflow](13-que-es-roboflow.md)
