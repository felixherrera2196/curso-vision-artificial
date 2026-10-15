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

La práctica habitual utiliza una imagen binaria de un canal. Puede ser una máscara de color limpia o el resultado de un umbral. `findContours` interpreta las regiones del primer plano según el modo elegido.

No conviene enviar directamente un fotograma BGR esperando que la función reconozca objetos. Primero hay que definir qué píxeles pertenecen a la región de interés. Encontrar bordes con otro algoritmo también puede generar una entrada útil, pero su interpretación requiere atención: bordes rotos o dobles no describen necesariamente una región cerrada limpia.

## 3. Modos de recuperación y jerarquía

Los contornos pueden estar unos dentro de otros. Una figura con un agujero tiene una frontera externa y otra asociada al hueco. La **jerarquía** describe relaciones de anidamiento o vecindad entre los contornos encontrados.

Un modo como `RETR_EXTERNAL` recupera las fronteras externas y es útil cuando solo interesa la silueta exterior. Un modo como `RETR_TREE` permite conservar relaciones más completas entre fronteras anidadas. Elegir el modo cambia qué información queda disponible: si ignoras los huecos, no podrás analizarlos después a partir de contornos que nunca recuperaste.

La aproximación de almacenamiento de puntos también es diferente de la recuperación. Por ejemplo, `CHAIN_APPROX_SIMPLE` reduce puntos redundantes de ciertos segmentos. No sustituye la aproximación poligonal que usaremos para clasificar figuras.

## 4. Área y perímetro

`contourArea` estima el área encerrada por el contorno mediante su geometría. Se expresa en unidades de píxel al cuadrado. No debe confundirse siempre con contar exactamente los píxeles blancos de una máscara: son procedimientos diferentes y pueden dar valores distintos, especialmente en regiones pequeñas o complejas.

`arcLength` calcula la longitud de la secuencia, indicando si se trata como cerrada. El perímetro se expresa en unidades de píxel. Un borde ruidoso puede tener una longitud mayor que una frontera suave, aunque ambos correspondan al mismo objeto.

Un filtro de área mínima ayuda a descartar ruido. El umbral depende de la resolución y de la distancia del objeto. Si alejas la figura de la cámara, su área aparente disminuye y puede quedar descartada sin haber cambiado físicamente.

## 5. Rectángulo y centro

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


[Anterior](07-operaciones-morfologicas.md) · [Índice](../README.md) · [Siguiente: Detectar figuras](09-detectar-figuras.md)
