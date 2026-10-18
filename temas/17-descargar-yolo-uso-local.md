# 17. Descargar el modelo YOLO entrenado para uso local

Ahora descargaremos **el modelo que entrenamos en el capítulo anterior** para utilizarlo en nuestra propia computadora. El archivo que debemos guardar se llama **`best.pt`** y contiene los pesos del modelo seleccionados según su desempeño en validación.

## Cómo descargarlo desde Colab

1. Abre el panel **Archivos**, a la izquierda de Colab.
2. Dentro de `/content/`, abre las carpetas **runs → detect → train → weights**.
3. Localiza el archivo **`best.pt`**. Su ruta habitual es:

   ```text
   /content/runs/detect/train/weights/best.pt
   ```

4. Haz clic en los **tres puntos** a la derecha de `best.pt` y selecciona **Descargar**.
5. Espera a que termine la descarga y guarda el archivo en la carpeta del proyecto de tu computadora. Lo utilizaremos en el siguiente capítulo.

Si ejecutaste varios entrenamientos, la carpeta puede llamarse `train2`, `train3`, etc. Abre la correspondiente al entrenamiento que quieres utilizar y busca su archivo `weights/best.pt`.

Descarga el archivo antes de que termine o se elimine la sesión de Colab, ya que sus archivos temporales pueden perderse.

[Anterior](16-entrenar-yolo-gpu.md) · [Índice](../README.md) · [Siguiente: YOLO y webcam](18-detectar-objeto-webcam-yolo.md)
