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
