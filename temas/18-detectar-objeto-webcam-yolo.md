# 18. Detectar objeto con cámara web usando YOLO

## Qué aprenderás

Integrarás conceptualmente el ciclo de cámara con un modelo entrenado. Comprenderás qué significan las predicciones, cómo influyen los umbrales y qué comprobar para evaluar la aplicación final.

## La idea en palabras sencillas

La aplicación final combina dos cosas que ya conoces: recibir imágenes de la cámara y pedir predicciones al detector. En cada imagen, el modelo intenta localizar objetos y el programa dibuja sus cajas y nombres.

La caja es una propuesta, no una garantía. Necesitarás observar cuándo acierta y cuándo se equivoca. Si no hay detecciones, el video debe seguir funcionando. Si salen muchas cajas para el mismo objeto en distintos momentos, no significa que hayan aparecido muchos objetos nuevos: cada fotograma es otra observación.

## 1. Unir dos componentes ya comprobados

Antes de integrar, verifica que el programa del tema 04 capture video y que el modelo del tema 17 haga predicciones sobre imágenes. La aplicación final combina ambos: captura un fotograma, lo analiza con el detector y muestra el resultado.

Carga el modelo una sola vez antes del ciclo. Cargar pesos en cada fotograma desperdicia tiempo y puede consumir memoria innecesariamente. La cámara también debe abrirse una vez y liberarse al terminar.

## 2. Flujo por fotograma

1. Leer el siguiente fotograma y comprobar el éxito.
2. Enviar la imagen válida al detector.
3. Obtener los resultados de detección.
4. Interpretar cajas, clases y puntuaciones.
5. Dibujar las detecciones aceptadas.
6. Mostrar la imagen y atender la condición de salida.
7. Repetir sin volver a cargar el modelo.

Si no hay objetos detectados, la aplicación debe poder mostrar el fotograma y continuar. Una lista vacía de detecciones es un resultado válido; no equivale a un fallo de captura.

## 3. Qué devuelve el detector

Una predicción de detección suele incluir una caja, un identificador de clase y una puntuación de confianza. La representación exacta depende de la API. En el flujo habitual de Ultralytics existen objetos de resultados que permiten consultar cajas y nombres o generar una imagen anotada.

Para interpretar una caja, confirma su convención de coordenadas. Si trabajas con coordenadas de esquina, debes dibujar esquinas; si recibes centro y tamaño, hay que convertir. También confirma a qué imagen se refieren las coordenadas antes de redimensionar o recortar.

La confianza es una puntuación del modelo asociada a la predicción. No debe presentarse automáticamente como una probabilidad perfectamente calibrada de que el objeto esté allí. Un valor alto no elimina la posibilidad de error.

## 4. Umbral de confianza

Un umbral determina qué predicciones aceptas. Al subirlo, suelen disminuir detecciones débiles y algunas falsas alarmas, pero también puedes perder objetos reales. Al bajarlo, puedes recuperar objetos omitidos a costa de aceptar más resultados incorrectos.

El valor adecuado depende del costo de ambos tipos de error. Para una demostración, observa diferentes escenas y registra cómo cambian los resultados. No elijas el umbral con una sola imagen particularmente favorable.

## 5. Cajas superpuestas e IoU

Los detectores pueden producir varias candidatas relacionadas con una misma instancia. En los flujos que utilizan supresión de detecciones superpuestas, un criterio basado en IoU ayuda a decidir cuáles conservar. Los detalles cambian entre modelos y configuraciones; no hay que asumir que todas las versiones usan el mismo posprocesamiento.

El umbral de confianza y el criterio de superposición no son equivalentes. El primero filtra puntuaciones; el segundo participa en el tratamiento de cajas relacionadas. Antes de ajustar estos parámetros, identifica cuáles admite el modelo que utilizas y qué efecto tiene cada uno sobre las detecciones.

## 6. Coordenadas y color

Si redimensionas antes de inferir y dibujas en otra imagen, asegúrate de que las cajas se transformen correctamente. La API puede encargarse de recuperar coordenadas respecto a la imagen que recibió, pero no adivina transformaciones externas posteriores.

Del mismo modo, respeta el formato de color esperado por la entrada concreta. Algunas interfaces aceptan arreglos de OpenCV y manejan conversiones; otras requieren una representación distinta. Convertir varias veces sin conocer el flujo puede introducir un error de canales.

## 7. Velocidad, latencia y seguimiento

Mide el tiempo del flujo completo, no solamente la inferencia: captura, preparación, predicción, dibujo y visualización también cuentan. Una tasa media alta puede coexistir con retraso si se acumulan fotogramas.

Para mejorar rendimiento puedes evaluar un modelo menor, una entrada menor o un dispositivo más rápido. Cada cambio debe comprobarse también sobre objetos pequeños y escenas difíciles. Si procesas solo algunos fotogramas, el resultado se actualiza con menor frecuencia.

Detectar no equivale a **seguir** identidades. Si una caja aparece en dos fotogramas, el detector por sí solo no garantiza que corresponda al mismo objeto físico. Tampoco debes sumar detecciones de cada fotograma como si fueran objetos diferentes para obtener un conteo acumulado.

## 8. Evaluación final del taller

Prueba presencia y ausencia de objetos, varias instancias, distintos fondos, distancias y luces. Anota falsos positivos, objetos omitidos y clases confundidas. Compara esas condiciones con el dataset para identificar qué ejemplos faltan.

Verifica también la salida: la tecla elegida debe terminar el ciclo, la cámara debe liberarse y las ventanas deben cerrarse. Las excepciones requieren un mecanismo de limpieza si buscas una aplicación más robusta que el ejemplo inicial.

## Actividad integradora

Realiza dos aplicaciones: una selección por color y forma con OpenCV y una detección aprendida con YOLO. Para cada una describe clases o criterios, datos requeridos, condiciones de prueba, aciertos y fallos. Explica en qué escena prefieres cada enfoque usando lo observado.

## Comprobación de la aplicación

Verifica por separado la captura de cámara y la carga del detector. Al integrarlos, comprueba que las predicciones se actualicen, que el programa siga funcionando sin detecciones y que ESC libere la cámara. Registra velocidad, falsas alarmas y objetos omitidos en las condiciones de uso de tu práctica.

## Primera prueba de la aplicación final

Coloca un solo objeto de una clase aprendida frente a la cámara, con buena luz y un fondo sencillo. Abre el programa y comprueba tres resultados por separado: hay video, el detector propone una caja y el nombre corresponde a la clase esperada.

Después retira el objeto. El video debe continuar aunque ya no haya detecciones. Vuelve a colocarlo, cambia la distancia y agrega otra instancia. Observa si ambas se detectan y si aparecen cajas equivocadas en el fondo.

Si no hay video, revisa la captura. Si hay video pero no cajas, revisa pesos, clases, condiciones de la escena y umbral de confianza. Si la imagen va muy lenta, mide el tiempo y revisa el tamaño del modelo y de la entrada. No vuelvas a entrenar antes de identificar cuál de estos problemas estás observando.

Al terminar, pulsa ESC con la ventana seleccionada y vuelve a abrir el programa para confirmar que la cámara quedó libre.


[Anterior](17-descargar-yolo-uso-local.md) · [Índice del curso](../README.md)
