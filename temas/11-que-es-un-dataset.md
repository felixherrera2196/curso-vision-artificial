# 11. ¿Qué es un dataset?

## Qué aprenderás

Comprenderás cómo organizar un conjunto de imágenes para detección, por qué separarlo en entrenamiento, validación y prueba, y qué características hacen que los ejemplos sean útiles para el uso final.

## La idea en palabras sencillas

Un dataset es la colección organizada de ejemplos del proyecto. Para detectar objetos, no basta con reunir fotografías: también hay que indicar qué objetos aparecen y dónde están.

Si enseñas siempre el mismo vaso sobre la misma mesa, el modelo puede funcionar solo en situaciones muy parecidas. Necesitas diferentes vistas, fondos y condiciones reales. Separaremos imágenes para aprender y otras para comprobar lo aprendido. La idea central es sencilla: evaluar con imágenes nuevas ayuda a saber si el modelo puede funcionar fuera de sus ejemplos conocidos.

## 1. Dataset de detección

Un **dataset** es un conjunto organizado de datos para una tarea. En detección de objetos incluye imágenes, anotaciones de clases y posiciones, y una organización que permite relacionar cada imagen con sus etiquetas.

No es solamente una carpeta de fotografías. Si faltan anotaciones o si los identificadores de clase cambian entre archivos, el entrenamiento recibirá información incompleta o contradictoria. El formato y la coherencia son parte de la calidad de los datos.

## 2. Definir la tarea antes de reunir imágenes

Decide qué clases debe detectar el modelo y cómo distinguirlas. Por ejemplo, «botella» y «vaso» son clases; cada botella o vaso visible es una **instancia**. Una imagen puede contener varias instancias de una misma clase y de clases diferentes.

Define también las condiciones de uso: cámara web, distancia, tamaño de objetos, luz y fondos. Un dataset de fotos tomadas muy cerca sobre un fondo blanco puede ser insuficiente para detectar objetos pequeños en una mesa desordenada.

Si las clases son ambiguas, redacta criterios antes de anotar. Un objeto no debe recibir una clase un día y otra al siguiente porque cambió la persona que etiqueta.

## 3. Diversidad que importa

Busca variaciones reales: orientación, distancia, escala, iluminación, fondo, modelos del mismo objeto y presencia de obstáculos. Necesitas ejemplos que permitan distinguir el objeto de pistas accidentales.

Si todos los vasos están sobre una mesa azul y todas las botellas sobre una mesa roja, el modelo puede aprender el fondo como una pista. Para evitarlo, varía los contextos y procura que las clases compartan escenarios cuando sea razonable.

Muchos fotogramas consecutivos de un mismo video pueden ser casi idénticos. Aumentan el número de archivos sin aportar la misma diversidad que imágenes tomadas en sesiones distintas. La cantidad importa, pero no sustituye la cobertura de condiciones.

## 4. Entrenamiento, validación y prueba

- **Entrenamiento:** imágenes utilizadas para ajustar los pesos.
- **Validación:** imágenes separadas para evaluar decisiones durante el desarrollo.
- **Prueba:** imágenes reservadas para estimar el desempeño final, después de elegir el modelo y los ajustes.

No hay una proporción universal que funcione para cualquier proyecto. Cada división debe contener suficientes ejemplos relevantes de las clases y condiciones. Un conjunto diminuto de prueba puede dar una medida muy inestable.

La separación debe evitar **fuga de datos**. Si imágenes prácticamente iguales de la misma grabación quedan en entrenamiento y prueba, el resultado puede parecer mejor de lo que será en otra escena. Cuando sea posible, separa por sesión, video, ubicación u objeto físico, según lo que quieras evaluar.

## 5. Datos negativos y etiquetas completas

Una imagen sin objetos de las clases de interés puede servir como ejemplo negativo. Ayuda a evaluar y aprender situaciones donde no debería aparecer una detección. Pero una imagen con objetos objetivo visibles y sin etiquetar no es un negativo correcto: contiene supervisión incompleta.

Revisa que estén anotadas todas las instancias que cumplen la política de etiquetado. Si algunas se omiten, el sistema puede recibir mensajes contradictorios sobre regiones que sí contienen objetos.

## 6. Balance y dificultad

Si una clase aparece en cientos de imágenes y otra en muy pocas, las métricas generales pueden ocultar el problema de la clase escasa. Revisa cantidades por clase y resultados por clase, incluyendo objetos pequeños o parcialmente cubiertos.

No elimines todos los ejemplos difíciles para lograr una evaluación más alta. Si esos casos ocurrirán en la cámara real, deben formar parte de una evaluación representativa. También distingue entre un ejemplo difícil y una etiqueta incorrecta: el segundo sí requiere corrección.

## 7. Versiones y transformaciones

Una versión del dataset debe identificar imágenes, etiquetas, divisiones y transformaciones aplicadas. Si vuelves a entrenar después de cambiar datos, registra la versión para poder explicar qué se modificó.

El **aumento de datos** crea variaciones de entrenamiento, como ciertos cambios de brillo o de orientación. Debe preservar las etiquetas de forma coherente y no crear escenas absurdas para la tarea. Primero realiza una separación que evite fugas y después aplica aumentos de entrenamiento; las variantes de la misma imagen no deben contaminar la prueba.

## Actividad de comprensión

Diseña un dataset de dos clases para una cámara web. Describe las variaciones necesarias, cómo separarías las sesiones y qué escenas sin objetos incluirías. Explica por qué cien fotografías casi iguales no equivalen a cien situaciones distintas.

## Preparar tu primera colección, paso a paso

Como ejercicio, considera dos clases: «vaso» y «botella». Los nombres son un ejemplo; utiliza las clases indicadas para la práctica del taller.

1. Escribe qué entra en cada clase y qué casos serían confusos.
2. Toma fotografías de distintos objetos de cada clase, no solo del mismo objeto repetido.
3. Cambia fondo, luz, orientación y distancia. Incluye algunas escenas con varios objetos.
4. Descarta archivos dañados y revisa si hay muchas imágenes casi idénticas.
5. Anota qué fotografías pertenecen a la misma sesión o grabación.
6. Separa sesiones para entrenamiento, validación y prueba, evitando repartir fotografías prácticamente iguales entre ellas.
7. Dibuja las cajas de todas las instancias que cumplen la política de anotación.
8. Revisa que cada división permita evaluar las clases que necesitas.

No hay una cantidad de imágenes que garantice el éxito. Antes de reunir cientos de fotografías parecidas, revisa qué condiciones de uso faltan. Si una clase no tiene suficientes ejemplos, regístralo en lugar de asumir que el entrenamiento lo resolverá.


[Anterior](10-introduccion-deep-learning.md) · [Índice](../README.md) · [Siguiente: Etiquetado](12-etiquetado-bounding-boxes.md)
