# Tutorial instalación de Python

**Video de apoyo:** [cómo instalar Python en YouTube](https://www.youtube.com/watch?v=cROteyMVtXk).

Esta guía explica cómo instalar **Python en Windows 11**, comprobar su instalación e instalar **OpenCV** y **Ultralytics** con pip para el curso de OpenCV y YOLO. No necesitas experiencia en tecnología. Mantén la computadora conectada a Internet durante los pasos.

## 1. Descargar el instalador de Python

1. Abre tu navegador, por ejemplo Microsoft Edge o Google Chrome.
2. Haz clic en la barra de direcciones de la parte superior, escribe **https://www.python.org/** y presiona **Enter**.
3. En el menú superior, haz clic en **Downloads / Descargas** para abrir **https://www.python.org/downloads/**.
4. Busca el texto **“Or get the standalone installer for Python…”**, que significa “O descarga el instalador independiente de Python…”. Haz clic en el enlace con el número de la **versión estable más reciente**. El número cambia cuando se publica una nueva versión. **No hagas clic en el botón “Download Python install manager”** que aparece arriba de ese enlace.
5. En la página de esa versión, baja hasta la sección **Files / Archivos** y haz clic en **Windows installer (64-bit)** para una computadora Intel o AMD. Si tu equipo utiliza un procesador ARM, elige **Windows installer (ARM64)**. Puedes comprobarlo en **Inicio → Configuración → Sistema → Información → Tipo de sistema**.
6. El archivo debe ser el **instalador independiente con extensión `.exe`**. No elijas **embeddable package**, archivos de código fuente ni versiones de prueba de la sección **Pre-releases**.
7. Espera a que termine la descarga. El archivo tendrá un nombre parecido a `python-3.xx.x-amd64.exe` y quedará normalmente en **Descargas**. Los números dependen de la versión más reciente que descargaste.

Python es gratuito. Utiliza el sitio oficial indicado arriba.

## 2. Instalar Python haciendo clic en el instalador

1. Abre el **Explorador de archivos**, el icono de carpeta de la barra de tareas. También puedes presionar **Windows + E**.
2. Haz clic en **Descargas** y busca el instalador de Python.
3. Haz doble clic en ese archivo para abrirlo.
4. En la primera pantalla, **marca la casilla `Add python.exe to PATH`**, que suele estar en la parte inferior. Este paso permite que Windows encuentre Python cuando escribas el comando de comprobación.
5. Haz clic en **Install Now**. Significa “Instalar ahora”. Deja las demás opciones como están; el instalador incluye pip, la herramienta para instalar bibliotecas.
6. Si Windows pide autorización para realizar cambios, comprueba que sea el instalador oficial de Python y haz clic en **Sí**. Si solicita una contraseña que no tienes, pide ayuda a quien administra la computadora.
7. Espera a que termine la instalación. No cierres la ventana mientras avanza la barra de progreso.
8. Cuando aparezca **Setup was successful**, la instalación terminó correctamente. Haz clic en **Close / Cerrar**.

## 3. Verificar la instalación desde la consola

La consola es una ventana donde escribes instrucciones para la computadora. Usaremos **Símbolo del sistema**, también llamado **cmd**.

1. Haz clic en **Inicio** o presiona la tecla **Windows**.
2. Escribe `cmd` y abre **Símbolo del sistema**. No hace falta ejecutarlo como administrador.
3. Si ya tenías esa ventana abierta antes de instalar Python, ciérrala y abre una nueva.
4. Copia el siguiente comando, pégalo con **Ctrl + V** y presiona **Enter**. Copia solamente la línea dentro del recuadro:

   ```bat
   python --version
   ```

5. Debe aparecer una respuesta como `Python 3.xx.x`. Los números deben corresponder a la versión que instalaste. **Esto confirma que Windows reconoce Python**.

Si dice que `python` no se reconoce o abre Microsoft Store, cierra y vuelve a abrir la consola. Si sigue igual, abre nuevamente el instalador, selecciona **Modify / Modificar**, pulsa **Next / Siguiente** y, en **Advanced Options**, marca **Add Python to environment variables**. Aplica el cambio con **Install**, abre una consola nueva y repite `python --version`.

## 4. Instalar OpenCV con pip

OpenCV es la biblioteca que se utilizará para trabajar con imágenes y video.

1. En la misma ventana de **Símbolo del sistema**, copia este comando y presiona **Enter**:

   ```bat
   python -m pip install opencv-python
   ```

2. Espera a que termine. Verás mensajes de descarga e instalación; no tienes que escribir nada mientras trabaja.
3. Si termina sin errores, normalmente aparecerá **Successfully installed**, seguido de los nombres de los paquetes. Si aparece **Requirement already satisfied**, significa que ya está instalado.

El paquete que debes instalar se llama **`opencv-python`**. La parte `python -m pip` utiliza pip desde el Python que acabas de comprobar.

## 5. Instalar Ultralytics con pip

Ultralytics es la biblioteca que se utilizará para trabajar con YOLO.

1. Cuando termine la instalación anterior y vuelva a aparecer la línea donde puedes escribir, copia este comando y presiona **Enter**:

   ```bat
   python -m pip install ultralytics
   ```

2. Espera a que termine. Puede tardar más porque descarga otras bibliotecas necesarias automáticamente.
3. Si termina sin errores y muestra **Successfully installed** o **Requirement already satisfied**, la instalación está completa.

**Listo:** Python está instalado y verificado con `python --version`, y has instalado OpenCV y Ultralytics con pip. Puedes cerrar la consola. Si alguna instalación termina con un mensaje de error, copia el mensaje completo y compártelo con el profesor para que te ayude.
