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

`approxPolyDP` aproxima una curva por otra con menos vértices, usando una tolerancia llamada epsilon. La idea es conservar la forma global mientras se eliminan variaciones pequeñas del borde.

Es habitual relacionar epsilon con el perímetro para que la tolerancia se adapte parcialmente al tamaño de la figura. El factor exacto debe ajustarse: una tolerancia muy pequeña conserva ruido y demasiados vértices; una muy grande simplifica tanto que elimina esquinas reales.

El resultado depende también de la máscara. Si falta una esquina porque el filtro no la seleccionó, la aproximación no puede reconstruirla con certeza. Antes de modificar epsilon, revisa la imagen binaria.

## 3. Número de vértices

Tres vértices pueden sugerir un triángulo y cuatro un cuadrilátero. Estas son hipótesis útiles para figuras planas, separadas y claramente segmentadas. Deben acompañarse de filtros de área y, cuando la aplicación lo requiera, comprobaciones de convexidad, ángulos o proporciones.

Contar cuatro vértices no basta para afirmar «rectángulo»: un trapecio o un cuadrilátero irregular también tiene cuatro. Del mismo modo, muchos vértices no bastan para afirmar «círculo»: un borde irregular puede producir una aproximación con muchos puntos.

## 4. Cuadrados, rectángulos y perspectiva

La relación ancho / alto del rectángulo envolvente puede ayudar a separar un cuadrado de un rectángulo alargado en una escena bien alineada. Sin embargo, el rectángulo alineado con los ejes cambia cuando la figura rota. Un objeto alargado inclinado puede tener un rectángulo envolvente de proporciones engañosas.

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


[Anterior](08-contornos.md) · [Índice](../README.md) · [Siguiente: Deep Learning](10-introduccion-deep-learning.md)
