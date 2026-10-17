# 11. ¿Qué es un dataset?

## Qué es y para qué sirve

Un **dataset** es una colección organizada de ejemplos que utilizamos para enseñar y evaluar un modelo de inteligencia artificial. En este curso trabajaremos con fotografías de los objetos que queremos detectar.

Por ejemplo, para detectar **vasos y botellas**, necesitamos imágenes donde aparezcan esos objetos en diferentes posiciones, distancias, fondos e iluminaciones. El modelo utiliza esos ejemplos para aprender patrones que después le permitan reconocerlos en imágenes nuevas.

Para entrenar un detector, las fotografías también necesitan **etiquetas**: el nombre de cada objeto y una caja que indique dónde está. Primero reuniremos las imágenes; en el siguiente capítulo aprenderemos a etiquetarlas.

**Más fotos no siempre significa un mejor dataset.** Cien fotografías casi iguales aportan menos variedad que imágenes de distintos objetos y situaciones. Busca ejemplos parecidos a las condiciones donde utilizarás tu detector.

## Práctica: recolectar tus propias imágenes

El siguiente programa abre la cámara y guarda fotografías JPG automáticamente cada **0.5 segundos**. También puedes tomar una foto adicional con **espacio** y salir con **ESC**.

Las fotos se guardan en la carpeta `mi_dataset_imagenes`, con nombres como `objeto_0.jpg`, `objeto_1.jpg`, etc. Al volver a ejecutarlo, continúa la numeración de las imágenes existentes que siguen ese formato. Los textos de la ventana no aparecen en las fotografías guardadas.

### Cómo utilizarlo

1. Cierra otros programas que usen la cámara. En tu equipo Windows, utiliza el mismo Python y OpenCV de las prácticas anteriores. Las otras bibliotecas del código vienen con Python.
2. Guarda el código completo como `recolectar_imagenes.py`.
3. Si lo necesitas, cambia las opciones al inicio:

| Opción | Para qué sirve |
| --- | --- |
| `OUTPUT_DIR` | Carpeta donde se guardan las imágenes. Se crea si no existe; una ruta relativa depende de la carpeta desde donde ejecutas el programa. |
| `IMAGE_PREFIX` | Inicio del nombre de las fotos, por ejemplo `"objeto"` o `"vaso_sesion01"`. No asigna etiquetas de entrenamiento. |
| `INTERVALO_SEGUNDOS` | Tiempo entre fotos automáticas. Usa un valor positivo; por ejemplo, `2.0` deja aproximadamente dos segundos entre capturas. |

4. Ejecútalo desde VS Code o con `python recolectar_imagenes.py` en la terminal. La captura automática comienza al abrir el programa.
5. Cambia la posición, distancia y fondo entre tomas. Haz clic en la ventana «Captura Roboflow» para usar **espacio** o **ESC**.
6. Al terminar, abre la carpeta y revisa las imágenes. Elimina las borrosas y evita conservar muchas casi idénticas. Puedes usar una carpeta diferente para cada sesión.

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

## Qué debes obtener

Una carpeta con imágenes claras y variadas de las clases que quieres detectar. Incluye distintos ejemplares de cada clase y algunas escenas sin los objetos objetivo. **No necesitan ser verdes**: esta práctica prepara imágenes para entrenar un detector.

Este programa solo captura fotografías: no etiqueta objetos ni sube archivos a Roboflow. El siguiente paso será dibujar las cajas y asignar las clases de los objetos presentes.

[Anterior](10-introduccion-deep-learning.md) · [Índice](../README.md) · [Siguiente: Etiquetado](12-etiquetado-bounding-boxes.md)
