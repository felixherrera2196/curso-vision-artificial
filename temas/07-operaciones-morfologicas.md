# 07. Operaciones morfológicas

## Qué aprenderás

Aprenderás a interpretar erosión, dilatación, apertura y cierre sobre una máscara binaria. Comprenderás cómo el tamaño del elemento estructurante cambia el resultado y por qué limpiar una máscara puede mejorar, o perjudicar, la detección de formas.

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

## 5. Apertura

La apertura aplica **erosión seguida de dilatación**, utilizando el elemento estructurante correspondiente. La primera operación elimina regiones pequeñas o detalles que no sobreviven al kernel; la segunda recupera parte del tamaño de las regiones restantes.

No restaura todo lo que borró la erosión. Esa es precisamente su utilidad para quitar puntos aislados. Si un detalle real desaparece en la primera etapa, no se recupera automáticamente en la segunda.

## 6. Cierre

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

En OpenCV, `erode`, `dilate` y `morphologyEx` permiten realizar estas operaciones. `getStructuringElement` ayuda a definir kernels con formas comunes. Se explicarán los argumentos concretos cuando recibamos el ejemplo original.

## Actividad de comprensión

Busca tres defectos distintos: puntos fuera del objeto, huecos dentro del objeto y dos objetos muy cercanos. Propón una operación para los dos primeros y explica por qué debes tener cuidado con el tercero. Compara antes y después, incluyendo objetos pequeños.

## Código original

Pendiente de recibir. Se documentarán la máscara de entrada, el kernel, el orden de operaciones y el efecto de cada parámetro.

[Anterior](06-modelos-color.md) · [Índice](../README.md) · [Siguiente: Contornos](08-contornos.md)
