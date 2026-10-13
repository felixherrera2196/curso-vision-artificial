# 08. Contornos

## Qué aprenderás

Comprenderás qué representa un contorno, cómo se obtiene a partir de una máscara y qué medidas permiten describir una región. Estas herramientas son la base de la detección de figuras del siguiente tema.

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

Un filtro de área mínima ayuda a descartar ruido. El umbral depende de la resolución y de la distancia del objeto. Si el usuario aleja la figura, su área aparente disminuye y puede quedar descartada sin haber cambiado físicamente.

## 5. Rectángulo y centro

`boundingRect` proporciona un rectángulo alineado con los ejes que contiene el contorno. Es útil para dibujar la posición de una región o extraer una zona. El rectángulo puede contener fondo; no equivale a la máscara de la figura.

Los **momentos** describen propiedades de distribución de una región. A partir de ellos puede calcularse un centroide: x del centro se obtiene como m10 / m00 y y como m01 / m00. Antes de dividir debes comprobar que m00 no sea cero. Los contornos degenerados o demasiado pequeños pueden no ofrecer un área útil.

Un centroide geométrico no siempre coincide con el centro visual de un objeto complejo, y en formas cóncavas puede incluso quedar fuera de parte de la región.

## 6. Seleccionar un contorno

Puedes analizar todos los contornos que superen el filtro de área o seleccionar el mayor. La segunda opción simplifica una práctica con un único objeto, pero no permite detectar varios objetos por sí sola. Si no hay contornos, la selección del mayor debe manejar esa lista vacía.

Mientras desarrollas, dibuja los contornos sobre una copia del fotograma. Así comparas la región calculada con la escena original y evitas mezclar dibujos con la información que procesarás después.

## Actividad de comprensión

Coloca una figura sólida, una figura con agujero y dos figuras que se toquen. Predice los contornos con recuperación externa y con jerarquía completa. Después explica cómo el ruido del borde afectaría al perímetro y a la detección de vértices.

## Código original

Pendiente de recibir. Se explicarán modo de recuperación, almacenamiento de puntos, filtros, medidas y dibujo, según lo que utilice el ejemplo.

[Anterior](07-operaciones-morfologicas.md) · [Índice](../README.md) · [Siguiente: Detectar figuras](09-detectar-figuras.md)
