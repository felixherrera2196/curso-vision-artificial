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

## Ejemplo guiado: organizar una colección pequeña

Supongamos, solo para practicar la organización, que reuniste 100 imágenes variadas de vasos y botellas, tomadas en distintas sesiones. Una división ilustrativa sería 70 para entrenamiento, 20 para validación y 10 para prueba. Estos números explican la idea; no son una recomendación de cantidad suficiente para obtener un detector confiable.

Antes de repartirlas, agrupa imágenes de la misma escena o grabación. Si el mismo objeto y fondo aparecen casi idénticos en varios archivos, evita repartirlos entre entrenamiento y evaluación. Revisa que ambas clases y las condiciones importantes queden representadas de manera útil.

| Grupo | Para qué utilizarías sus imágenes | Qué evitar |
| --- | --- | --- |
| Entrenamiento | Ajustar los parámetros del detector. | Omitir etiquetas o tener una sola apariencia por clase. |
| Validación | Comparar ejecuciones y orientar ajustes. | Confundir una mejora de validación con una garantía de uso real. |
| Prueba | Estimar el desempeño final tras elegir el modelo. | Cambiar repetidamente parámetros para mejorar ese mismo resultado. |

## Fotografías que ayudan y fotografías que repiten

Diez fotos del mismo vaso casi sin mover la cámara aportan menos diversidad que diez vistas con cambios de orientación, fondo y distancia. Eso no vuelve inútil toda repetición, pero explica por qué debes mirar qué situaciones cubres además de contar archivos.

Incluye ejemplos parecidos al laboratorio: objetos sobre mesas, luz del salón y distancias reales de la webcam. También son útiles escenas sin las clases objetivo. No conviertas una escena con un vaso visible sin anotar en un ejemplo negativo por descuido.

## Revisión de datos antes de etiquetar

Abre algunas imágenes de cada sesión. Comprueba que se ven los objetos, que las clases se distinguen y que no hay archivos dañados. Si el objeto es casi imposible de reconocer para una persona, define con el instructor cómo se tratará antes de dibujar cajas.

Al terminar, escribe una frase que describa tu objetivo: «detectar estas clases, con esta cámara y bajo estas condiciones». Esa frase ayuda a decidir qué ejemplos faltan y qué pruebas harán falta después.

## Práctica: recolectar imágenes con la cámara web

Este programa abre la cámara principal y guarda fotografías JPG automáticamente, con un intervalo inicial de **0.5 segundos**. También permite tomar una fotografía adicional con la **barra espaciadora** y terminar con **ESC**. Guarda el fotograma original; los textos de ayuda solo aparecen en la ventana de vista previa.

Las imágenes se guardan en una carpeta local con nombres como `objeto_0.jpg`, `objeto_1.jpg` y `objeto_2.jpg`. Al iniciar, busca las imágenes que coinciden con el prefijo y continúa después del número mayor cuando los nombres tienen el formato esperado. Conserva ese formato si deseas continuar una colección.

### Preparar y ejecutar

1. En tu equipo Windows, utiliza el Python y OpenCV preparados para las prácticas de cámara. `os`, `time` y `glob` forman parte de Python y no requieren instalación adicional.
2. Cierra otros programas que estén usando la cámara. Guarda el código completo como `recolectar_imagenes.py` en la carpeta de tu proyecto.
3. Ajusta las tres opciones de configuración antes de ejecutarlo:

| Opción | Valor inicial | Para qué cambiarla |
| --- | --- | --- |
| `OUTPUT_DIR` | `"mi_dataset_imagenes"` | Elegir la carpeta de esta colección o sesión. Si no existe, se crea. Una ruta relativa se resuelve desde el directorio de trabajo al ejecutar el programa. |
| `IMAGE_PREFIX` | `"objeto"` | Elegir el comienzo del nombre de los archivos, por ejemplo `"vaso_sesion01"`. Es un nombre de archivo, no una etiqueta de entrenamiento. |
| `INTERVALO_SEGUNDOS` | `0.5` | Cambiar el tiempo entre capturas automáticas. Utiliza un número positivo; por ejemplo, `2.0` para dejar aproximadamente dos segundos entre fotos. |

4. Ejecútalo localmente desde VS Code o la terminal:

```bash
python recolectar_imagenes.py
```

5. Selecciona la ventana «Captura Roboflow» para que reciba las teclas. La captura automática comienza al ejecutar el programa; no necesitas pulsar espacio para iniciarla.
6. Mueve el objeto y cambia las condiciones de la escena entre fotografías. Pulsa **espacio** cuando quieras una toma manual adicional; esto no pausa la captura automática.
7. Pulsa **ESC** para terminar, liberar la cámara y cerrar la ventana. Abre la carpeta de salida para comprobar que los JPG se guardaron y se ven correctamente.

### Código completo

```python
import cv2
import os
import time
import glob

# --- CONFIGURACIÓN ---
OUTPUT_DIR = "mi_dataset_imagenes"
IMAGE_PREFIX = "objeto"
INTERVALO_SEGUNDOS = 0.5  # <--- Modifica este número para cambiar el tiempo de captura automática
# ---------------------

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Buscar qué imágenes ya existen para saber en qué número continuar
existing_files = glob.glob(os.path.join(OUTPUT_DIR, f"{IMAGE_PREFIX}_*.jpg"))
if existing_files:
    try:
        # Extrae el número del final del archivo (quitando la extensión)
        numbers = [int(os.path.splitext(os.path.basename(f))[0].split('_')[-1]) for f in existing_files]
        img_counter = max(numbers) + 1
    except ValueError:
        img_counter = len(existing_files)
else:
    img_counter = 0

print(f"[INFO] Continuando desde la imagen número: {img_counter}")
print(f"[INFO] Captura automática configurada cada {INTERVALO_SEGUNDOS} segundos.")

cap = cv2.VideoCapture(0)
last_capture_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Guardar una foto automáticamente según el intervalo configurado
    current_time = time.time()
    if current_time - last_capture_time >= INTERVALO_SEGUNDOS:
        img_name = os.path.join(OUTPUT_DIR, f"{IMAGE_PREFIX}_{img_counter}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"[AUTO] Guardada: {img_name}")
        img_counter += 1
        last_capture_time = current_time

    # Mostrar info en pantalla
    display_frame = frame.copy()
    cv2.putText(display_frame, f"Siguiente ID: {img_counter}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(display_frame, f"[ESPACIO] Manual | [ESC] Salir | Auto: {INTERVALO_SEGUNDOS}s", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Captura Roboflow", display_frame)

    key = cv2.waitKey(1) & 0xFF

    # Salir con la tecla ESC
    if key == 27:
        print("[INFO] Cerrando capturador...")
        break

    # Captura manual con la barra ESPACIADORA
    elif key == ord(' '):
        img_name = os.path.join(OUTPUT_DIR, f"{IMAGE_PREFIX}_{img_counter}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"[MANUAL] Guardada: {img_name}")
        img_counter += 1

cap.release()
cv2.destroyAllWindows()
print(f"[FIN] Proceso terminado. Siguiente ID libre en carpeta: {img_counter}")
```

### Cómo utilizar las fotos para tu dataset

El programa facilita reunir imágenes, pero la diversidad depende de cómo prepares las escenas. Cambia orientación, distancia, fondo e iluminación; incluye distintos ejemplares de cada clase y algunas escenas sin los objetos objetivo. No necesitas que los objetos sean verdes: esta recolección servirá para el detector que entrenarás después.

Con un intervalo corto puedes reunir muchas fotografías casi idénticas. Si no tienes tiempo de cambiar la escena, aumenta el intervalo o termina y prepara otra sesión. Usa carpetas distintas para identificar sesiones y conserva esa información al separar entrenamiento, validación y prueba. Evita repartir fotos casi iguales de la misma secuencia entre esas divisiones.

Después revisa las imágenes, descarta las desenfocadas o dañadas y reduce repeticiones innecesarias. **Este código solo recolecta fotografías:** no dibuja cajas, no asigna clases, no divide el dataset y no sube archivos a Roboflow, aunque la ventana tenga ese nombre. En los capítulos siguientes organizarás las fotos y anotarás todas las instancias correspondientes.

## Para dar el siguiente paso

Ya tenemos fotografías, pero el modelo no sabe qué queremos que encuentre. **¿Cómo le indicamos qué objeto hay y dónde está dentro de cada imagen?** En el siguiente capítulo dibujaremos cajas y asignaremos clases para construir las etiquetas.

[Anterior](10-introduccion-deep-learning.md) · [Índice](../README.md) · [Siguiente: Etiquetado](12-etiquetado-bounding-boxes.md)
