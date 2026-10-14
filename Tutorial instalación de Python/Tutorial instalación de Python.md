# Tutorial instalación de Python 3.12

**Video de apoyo:** [cómo instalar Python en YouTube](https://www.youtube.com/watch?v=cROteyMVtXk).

Esta guía explica cómo instalar **Python 3.12 en Windows 11**, comprobar su instalación e instalar **OpenCV** y **Ultralytics** con pip para el curso de OpenCV y YOLO. No necesitas experiencia en tecnología. Mantén la computadora conectada a Internet durante los pasos.

## 1. Descargar el instalador de Python 3.12

1. Abre tu navegador, por ejemplo Microsoft Edge o Google Chrome.
2. Haz clic en la barra de direcciones, escribe **https://www.python.org/downloads/release/python-31210/** y presiona **Enter**. Esta es la página oficial de **Python 3.12.10**, la versión utilizada en este tutorial.
3. Comprueba que el título de la página indique **Python 3.12.10**. Para el curso se recomienda **Python 3.12**; evita seleccionar otra serie, como 3.13 o 3.14, desde el botón general de descargas.
4. Baja hasta la sección **Files / Archivos**. Haz clic en **Windows installer (64-bit)** para una computadora Intel o AMD. Si tu equipo utiliza un procesador ARM, consulta con el instructor antes de elegir **Windows installer (ARM64)**: esa opción figura como experimental en esta versión. Puedes comprobar la arquitectura en **Inicio → Configuración → Sistema → Información → Tipo de sistema**.
5. El archivo debe ser el **instalador independiente con extensión `.exe`**. No elijas **embeddable package**, archivos de código fuente ni el botón **Download Python install manager**, porque esta guía sigue los pasos del instalador independiente.
6. Espera a que termine la descarga. Para un equipo Intel o AMD de 64 bits, el archivo se llama `python-3.12.10-amd64.exe` y quedará normalmente en **Descargas**.

**Sobre la versión:** Python 3.12.10 es la última publicación de la serie 3.12 que incluye los instaladores independientes tradicionales de Windows. Existen publicaciones 3.12 posteriores con correcciones de seguridad, pero no ofrecen esos mismos instaladores. Si el laboratorio ya dispone de una versión 3.12 más reciente preparada por el instructor, puedes utilizarla sin volver a instalar 3.12.10.

Python es gratuito. Utiliza el sitio oficial indicado arriba.

## 2. Instalar Python haciendo clic en el instalador

1. Abre el **Explorador de archivos**, el icono de carpeta de la barra de tareas. También puedes presionar **Windows + E**.
2. Haz clic en **Descargas** y busca el instalador de Python.
3. Haz doble clic en ese archivo para abrirlo.
4. En la primera pantalla, **marca la casilla `Add python.exe to PATH`**, que suele estar en la parte inferior. Este paso permite que Windows encuentre Python cuando escribas el comando de comprobación.
5. Haz clic en **Install Now**. Significa “Instalar ahora”. Conserva las opciones predeterminadas, incluido el lanzador de Python si aparece; el instalador incluye pip, la herramienta para instalar bibliotecas. El lanzador permite seleccionar Python 3.12 con el comando `py -3.12`.
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
   py -3.12 --version
   ```

5. Debe aparecer **`Python 3.12.10`** si instalaste la versión de esta guía, o **`Python 3.12.x`** si el instructor preparó otra actualización de la misma serie. **Esto confirma que Windows encuentra Python 3.12**. La `x` representa el número de actualización; no se escribe en el comando.

Si dice que `py` no se reconoce, abre una consola nueva. Si sigue igual, abre nuevamente el instalador de Python 3.12.10, selecciona **Modify / Modificar** y comprueba que esté instalado el lanzador de Python, identificado como **Python Launcher** o **py launcher**. Aplica el cambio y vuelve a comprobar la versión. Si el mensaje indica que no se encuentra Python 3.12, revisa que hayas instalado esa serie.

Si también tienes otras versiones de Python, `python --version` puede mostrar una distinta. Por eso en los siguientes pasos utilizaremos **`py -3.12`** para instalar las bibliotecas en Python 3.12. En VS Code, abre **Python: Select Interpreter / Seleccionar intérprete** desde la paleta de comandos y selecciona el intérprete Python 3.12 con el que trabajarás.

## 4. Instalar OpenCV con pip

OpenCV es la biblioteca que se utilizará para trabajar con imágenes y video.

1. En la misma ventana de **Símbolo del sistema**, copia este comando y presiona **Enter**:

   ```bat
   py -3.12 -m pip install opencv-python
   ```

2. Espera a que termine. Verás mensajes de descarga e instalación; no tienes que escribir nada mientras trabaja.
3. Si termina sin errores, normalmente aparecerá **Successfully installed**, seguido de los nombres de los paquetes. Si aparece **Requirement already satisfied**, significa que ya está instalado.

El paquete que debes instalar se llama **`opencv-python`**. La parte `py -3.12 -m pip` utiliza pip desde Python 3.12, aunque haya otras versiones instaladas.

## 5. Instalar Ultralytics con pip

Ultralytics es la biblioteca que se utilizará para trabajar con YOLO.

1. Cuando termine la instalación anterior y vuelva a aparecer la línea donde puedes escribir, copia este comando y presiona **Enter**:

   ```bat
   py -3.12 -m pip install ultralytics
   ```

2. Espera a que termine. Puede tardar más porque descarga otras bibliotecas necesarias automáticamente.
3. Si termina sin errores y muestra **Successfully installed** o **Requirement already satisfied**, la instalación está completa.

**Listo:** Python 3.12 está instalado y verificado con `py -3.12 --version`, y has instalado OpenCV y Ultralytics con pip. Puedes cerrar la consola. Si alguna instalación termina con un mensaje de error, copia el mensaje completo y compártelo con el profesor para que te ayude.
