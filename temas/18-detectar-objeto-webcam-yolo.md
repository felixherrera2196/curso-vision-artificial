# 18. Detectar objetos con tu modelo YOLO y la cámara web

## Preparar el modelo en tu computadora

Utilizaremos el archivo **`best.pt` que descargaste de Colab** en el capítulo anterior. Este contiene el modelo entrenado con tus imágenes y tus clases; ahora lo probaremos con la cámara de tu propia PC.

1. Abre **Descargas** y localiza `best.pt`.
2. Muévelo a **tu carpeta de usuario de Windows**, donde guardamos los códigos del curso. Por ejemplo:

   ```text
   C:\Users\TuUsuario\best.pt
   ```

   Puedes abrir esa carpeta escribiendo **`%USERPROFILE%`** en la barra de direcciones del Explorador y pulsando Enter.
3. Comprueba que el archivo se llame exactamente **`best.pt`**, sin números añadidos por la descarga.

El programa obtiene automáticamente tu carpeta de usuario y busca ahí `best.pt`. Así no tendrás que escribir una ruta con tu nombre de usuario. **Lo busca directamente en esa carpeta**, no dentro de Descargas ni en subcarpetas, aunque guardes el código en otro lugar.

## Crear y ejecutar el programa

Crea un archivo nuevo en esa carpeta, con un nombre diferente al de las prácticas anteriores, por ejemplo **`probar_mi_yolo.py`**. Copia el código completo de abajo.

Utiliza el Python local y OpenCV de las prácticas anteriores. También necesitas Ultralytics en ese mismo entorno de Windows; instalarlo en Colab no lo instala en tu PC. Si aún no lo tienes, ejecuta en la terminal de ese entorno:

```bash
python -m pip install ultralytics
```

Cierra otros programas que utilicen la cámara y ejecuta `probar_mi_yolo.py` desde VS Code o con:

```bash
python probar_mi_yolo.py
```

## Código completo

```python
import os
import cv2
from ultralytics import YOLO

# 1. Buscar el archivo 'best.pt' en tu carpeta de usuario de Windows
ruta_usuario = os.path.expanduser("~")
ruta_modelo = os.path.join(ruta_usuario, "best.pt")

# 2. Cargar tu modelo de YOLOv11
model = YOLO(ruta_modelo)

# 3. Abrir la cámara web de tu PC
cap = cv2.VideoCapture(0)
print("Presiona la tecla 'q' en el teclado para cerrar la ventana.")

# 4. Bucle para procesar la cámara en vivo
while True:
    success, frame = cap.read()
    if not success:
        break

    # Filtramos por confianza alta y reducimos cuadros duplicados
    results = model(frame, conf=0.8, iou=0.1, max_det=1)

    # Dibujar los resultados en la imagen
    annotated_frame = results[0].plot()

    # Mostrar la imagen en pantalla
    cv2.imshow("Prueba YOLOv11", annotated_frame)

    # Si presionas la 'q', se cierra todo
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Apagar cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
```

## Cómo funciona y qué debes observar

El programa carga `best.pt` una sola vez, abre la cámara y analiza cada fotograma. Después dibuja las cajas y etiquetas del modelo sobre el video. Acerca uno de los objetos de tus clases y comprueba si lo detecta.

Esta línea controla las detecciones que se muestran:

```python
results = model(frame, conf=0.8, iou=0.1, max_det=1)
```

- **`conf=0.8`**: filtra las predicciones con puntuación de confianza inferior a 0.8. Puede reducir falsas detecciones, pero también dejar fuera objetos que el modelo detecta con menor puntuación.
- **`iou=0.1`**: establece un umbral bajo de solapamiento para suprimir cajas repetidas de una misma clase. También puede eliminar cajas de objetos cercanos; no garantiza quitar todos los duplicados.
- **`max_det=1`**: permite mostrar **como máximo una detección por fotograma**, aunque haya varios objetos presentes.

Para terminar, haz clic en la ventana del video y pulsa **q**. El programa libera la cámara y cierra las ventanas.

Si no aparece ninguna caja, comprueba que usas el `best.pt` correcto y muestra un objeto de las clases que entrenaste, con buena iluminación. Si aparece un error al cargar el modelo, revisa que el archivo esté directamente en tu carpeta de usuario.

[Anterior](17-descargar-yolo-uso-local.md) · [Índice del curso](../README.md)
