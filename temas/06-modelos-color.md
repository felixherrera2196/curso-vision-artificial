# 06. Modelos de color

## Qué aprenderás

Compararás las representaciones RGB, BGR, escala de grises y HSV. Comprenderás por qué cambiar de modelo puede simplificar una tarea sin agregar información nueva a la imagen.

## 1. Una misma imagen, distintas coordenadas de color

Un modelo de color define cómo expresar numéricamente un color. Cambiar de RGB a HSV se parece a describir la misma posición con otro sistema de coordenadas: cambia la representación y facilita ciertas operaciones, pero no elimina automáticamente los problemas de iluminación o ruido.

La conversión debe corresponder al modelo de origen real. Si el fotograma está en BGR y se interpreta como RGB antes de convertirlo, el tono calculado será incorrecto. Por eso siempre conviene registrar de dónde proviene la imagen y qué transformaciones ya recibió.

## 2. RGB y BGR

RGB describe un color combinando intensidades de rojo, verde y azul. Es una representación aditiva: se relaciona con la combinación de luz. Los valores máximos de los tres canales producen blanco en la representación usual de 8 bits; los mínimos producen negro.

BGR contiene los mismos componentes en orden inverso. OpenCV suele trabajar con BGR al leer imágenes de color. No significa que vea colores distintos; significa que el primer canal debe interpretarse como azul. Herramientas de visualización que esperan RGB necesitan la conversión correspondiente.

RGB o BGR son útiles para mostrar imágenes y para muchas operaciones. Sin embargo, si quieres detectar un color, los tres canales pueden cambiar conjuntamente con la iluminación. Un intervalo construido en una escena puede fallar en otra.

## 3. Escala de grises

La escala de grises resume información de color en una sola intensidad. La conversión convencional utiliza contribuciones distintas de cada canal, relacionadas con la sensibilidad visual; no es simplemente elegir un canal al azar.

Esta representación resulta útil cuando interesan contrastes, bordes o formas y el color no es necesario. También reduce el número de canales que deben procesarse. Su costo es perder información cromática: dos objetos de colores diferentes pueden terminar con intensidades parecidas y ser difíciles de separar.

Es importante distinguir una imagen gris de una máscara binaria. La primera tiene muchos niveles de intensidad; la segunda utiliza dos estados para marcar selección y fondo.

## 4. HSV

HSV representa el color mediante tres componentes:

- **Hue o tono:** indica la familia cromática, como rojo, verde o azul.
- **Saturation o saturación:** expresa cuánta intensidad cromática tiene el color frente a un gris.
- **Value o valor:** corresponde al máximo de los componentes RGB en la definición habitual, y se utiliza como medida de brillo en esta representación.

En imágenes de 8 bits convertidas con la conversión HSV habitual de OpenCV, el tono se representa de 0 a 179. Es una escala reducida del círculo de aproximadamente 360 grados. Saturación y valor se representan de 0 a 255. Otras conversiones o tipos de dato pueden tener rangos distintos; no hay que mezclar sus límites.

## 5. Por qué H no siempre es una señal fiable

Un píxel casi gris tiene muy poca saturación. En esa situación, hablar de su tono es poco informativo: pequeñas variaciones de canales pueden producir grandes variaciones de H. Lo mismo ocurre en zonas muy oscuras, donde la información de color es débil y el ruido puede dominar.

Por eso un filtro de color suele restringir también S y V. Separar componentes facilita ajustar el filtro, pero HSV no vuelve la detección inmune a sombras, luz coloreada, reflejos o cambios de exposición automática.

## 6. Cómo elegir una representación

| Tarea | Representación habitual | Qué debes revisar |
| --- | --- | --- |
| Mostrar un fotograma con OpenCV | BGR | Orden de canales de origen. |
| Mostrarlo con una herramienta que espera RGB | RGB | Conversión desde BGR si corresponde. |
| Segmentar por tono | HSV | Saturación, brillo y continuidad circular del tono. |
| Obtener bordes o umbralizar por intensidad | Grises | Pérdida de separación entre algunos colores. |
| Encontrar contornos sobre una selección | Máscara binaria | Limpieza y significado del primer plano. |

## Actividad de comprensión

Observa una escena con un objeto rojo, uno verde y uno blanco. Explica cuál información se conserva en HSV y cuál se pierde en escala de grises. Después describe por qué sería incorrecto usar un límite H de 300 en la conversión HSV de 8 bits habitual de OpenCV.

## Código del curso

Pendiente de incorporar desde la conversación. Se explicará cada conversión de color, sus rangos y el formato de la imagen que recibe.

[Anterior](05-filtros-color.md) · [Índice](../README.md) · [Siguiente: Morfología](07-operaciones-morfologicas.md)
