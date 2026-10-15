# Tutorial instalación de Python 3.12.10 en Windows 11

**Video de apoyo:** [cómo instalar una versión anterior de Python con el instalador tradicional](https://youtu.be/TLe0yty_Mpw?si=iVMCgtdYCqa5I97T).

**Importante:** el video utiliza **Python 3.11** como ejemplo. Para este curso sigue el mismo procedimiento con **Python 3.12.10**, utilizando el instalador enlazado abajo. No necesitas instalar 3.11 para seguir el video.

Esta guía explica cómo instalar **Python 3.12.10 en Windows 11**, comprobar su instalación e instalar **OpenCV** y **Ultralytics** con pip para el curso de OpenCV y YOLO. No necesitas experiencia en tecnología. Mantén la computadora conectada a Internet durante los pasos.

## 1. Descargar el instalador de Python 3.12.10

1. Abre tu navegador, por ejemplo Microsoft Edge o Google Chrome.
2. Haz clic en la barra de direcciones, escribe **https://www.python.org/downloads/release/python-31210/** y presiona **Enter**. Esta es la página oficial de **Python 3.12.10**, la versión utilizada en este tutorial.
3. Comprueba que el título de la página indique **Python 3.12.10**. La versión que usaremos en el curso es **Python 3.12.10**; evita seleccionar otra serie, como 3.13 o 3.14, desde el botón general de descargas.
4. Baja hasta la sección **Files / Archivos**. Haz clic en **Windows installer (64-bit)** para una computadora Intel o AMD. Si tu equipo utiliza un procesador ARM, consulta con el instructor antes de elegir **Windows installer (ARM64)**: esa opción figura como experimental en esta versión. Puedes comprobar la arquitectura en **Inicio → Configuración → Sistema → Información → Tipo de sistema**.
5. El archivo debe ser el **instalador independiente con extensión `.exe`**. No elijas **embeddable package**, archivos de código fuente ni el botón **Download Python install manager**, porque esta guía sigue los pasos del instalador independiente.
6. Espera a que termine la descarga. Para un equipo Intel o AMD de 64 bits, el archivo se llama `python-3.12.10-amd64.exe` y quedará normalmente en **Descargas**.

**Sobre la versión:** Python 3.12.10 es la última publicación de la serie 3.12 que incluye los instaladores independientes tradicionales de Windows. Existen publicaciones 3.12 posteriores con correcciones de seguridad, pero no ofrecen esos mismos instaladores. Para mantener el mismo entorno durante las prácticas, sigue las indicaciones del instructor antes de cambiar la versión instalada en el laboratorio.

Python es gratuito. Utiliza el sitio oficial indicado arriba.

## 2. Instalar Python con Customize installation

Seguiremos la instalación tradicional: abrir el archivo `.exe`, elegir **Customize installation / Personalizar instalación** y revisar sus opciones. No utilizaremos el nuevo Python Install Manager.

1. Abre el **Explorador de archivos**, el icono de carpeta de la barra de tareas. También puedes presionar **Windows + E**.
2. Entra a **Descargas** y busca `python-3.12.10-amd64.exe` si tu equipo es Intel o AMD de 64 bits.
3. Haz doble clic en el archivo. Comprueba que la ventana corresponda a **Python 3.12.10**. Si aparecen opciones como **Modify**, **Repair** y **Uninstall**, esa versión ya está instalada: puedes pasar a la comprobación del apartado 3 o usar **Modify** para revisar sus componentes.
4. En la primera pantalla de una instalación nueva, **marca `Add python.exe to PATH`**, normalmente en la parte inferior. Esto permite utilizar el comando `python` desde la consola.
5. Haz clic en **Customize installation / Personalizar instalación**. Esta opción permite revisar los componentes y la configuración antes de instalar.
6. En **Optional Features / Características opcionales**, mantén marcada **pip**. Es la herramienta que utilizarás para instalar OpenCV y Ultralytics. Puedes conservar las demás opciones predeterminadas, como la documentación, Tcl/Tk e IDLE y el lanzador si aparecen; no hace falta cambiar todo para seguir el curso.
7. Pulsa **Next / Siguiente** para llegar a **Advanced Options / Opciones avanzadas**.
8. Comprueba que esté marcada **Add Python to environment variables**. Es la opción que configura las variables de entorno para que Windows pueda encontrar Python. Si ya marcaste la casilla de PATH en la primera pantalla, verifica que aquí se conserve la configuración.
9. Para tu computadora personal, puedes dejar **Install for all users / Instalar para todos los usuarios** sin marcar y conservar la ubicación propuesta. No necesitas instalar para todos los usuarios para realizar las prácticas. En una computadora del laboratorio, utiliza la configuración indicada por el instructor o la persona que administra el equipo.
10. Conserva la carpeta de instalación propuesta, salvo que el instructor indique otra. No necesitas activar las opciones de descarga de símbolos o binarios de depuración para este curso.
11. Haz clic en **Install / Instalar**. Si Windows solicita autorización, comprueba que sea el instalador oficial. Si pide una contraseña que no tienes, solicita ayuda a quien administra el equipo.
12. Espera hasta que aparezca **Setup was successful**. No cierres la ventana mientras se realiza la instalación.
13. Haz clic en **Close / Cerrar**. Abre una consola nueva para que pueda reconocer los cambios del PATH.

**Qué debes recordar:** usa el `.exe` de Python 3.12.10, elige **Customize installation**, conserva **pip** y activa la opción que permite encontrar Python desde la consola. Aunque el video muestre 3.11, en tus ventanas y archivos debe aparecer **3.12.10**.

## 3. Verificar la instalación desde la consola

La consola es una ventana donde escribes instrucciones para la computadora. Usaremos **Símbolo del sistema**, también llamado **cmd**.

1. Haz clic en **Inicio** o presiona la tecla **Windows**.
2. Escribe `cmd` y abre **Símbolo del sistema**. No hace falta ejecutarlo como administrador.
3. Si ya tenías esa ventana abierta antes de instalar Python, ciérrala y abre una nueva.
4. Copia el siguiente comando, pégalo con **Ctrl + V** y presiona **Enter**. Copia solamente la línea dentro del recuadro:

   ```bat
   python --version
   ```

5. Debe aparecer exactamente **`Python 3.12.10`**. Esa es la versión que usaremos en el curso. Si aparece otro número, revisa qué instalación está seleccionando el comando antes de instalar las bibliotecas.

Si dice que `python` no se reconoce o abre Microsoft Store, cierra y vuelve a abrir la consola. Si sigue igual, abre nuevamente el instalador de Python 3.12.10, selecciona **Modify / Modificar**, pulsa **Next / Siguiente** y, en **Advanced Options**, marca **Add Python to environment variables**. Aplica el cambio, abre una consola nueva y repite `python --version`.

Si aparece una versión distinta de **3.12.10**, no instales todavía las bibliotecas: el comando `python` está seleccionando otra instalación. En **Inicio**, busca **Editar las variables de entorno de esta cuenta**, abre **Path → Editar** y coloca las entradas de Python 3.12 y su carpeta **Scripts** antes de las de otras versiones. No elimines las otras entradas. Si no identificas las rutas, pide ayuda al instructor. Abre una consola nueva y comprueba de nuevo `python --version`; debe indicar **3.12.10** antes de continuar. Si tienes otra actualización de la serie 3.12 y no aparece 3.12.10 entre tus instalaciones, consulta al instructor para preparar la versión del curso.

En VS Code, abre la paleta de comandos con **Ctrl + Shift + P**, busca **Python: Select Interpreter / Seleccionar intérprete** y selecciona Python 3.12.10. Esta selección configura el editor; comprueba también la versión en la terminal donde instalarás las bibliotecas.

## 4. Instalar OpenCV con pip

OpenCV es la biblioteca que se utilizará para trabajar con imágenes y video.

1. En la misma ventana de **Símbolo del sistema**, copia este comando y presiona **Enter**:

   ```bat
   python -m pip install opencv-python
   ```

2. Espera a que termine. Verás mensajes de descarga e instalación; no tienes que escribir nada mientras trabaja.
3. Si termina sin errores, normalmente aparecerá **Successfully installed**, seguido de los nombres de los paquetes. Si aparece **Requirement already satisfied**, significa que ya está instalado.

El paquete que debes instalar se llama **`opencv-python`**. La parte `python -m pip` utiliza pip desde el mismo intérprete que acabas de comprobar con `python --version`. Por eso es importante verificar que indique Python 3.12.10 antes de instalar.

**Para las ventanas y barras de Windows 11:** utiliza **`opencv-python`**, que incluye la interfaz gráfica de escritorio. Las variantes `opencv-python-headless` y `opencv-contrib-python-headless` están pensadas para entornos sin ventanas y no sirven para las prácticas de barras con `imshow`. Evita instalar varias variantes de OpenCV en el mismo entorno, porque comparten el módulo `cv2`.

Ejecuta los archivos `.py` localmente desde VS Code o la consola de Windows, en la sesión gráfica de tu equipo. No ejecutes el calibrador en Colab ni dentro de WSL siguiendo este tutorial. Si la cámara no abre, revisa **Configuración → Privacidad y seguridad → Cámara**, incluyendo el permiso de acceso para aplicaciones de escritorio.

## 5. Instalar Ultralytics con pip

Ultralytics es la biblioteca que se utilizará para trabajar con YOLO.

1. Cuando termine la instalación anterior y vuelva a aparecer la línea donde puedes escribir, copia este comando y presiona **Enter**:

   ```bat
   python -m pip install ultralytics
   ```

2. Espera a que termine. Puede tardar más porque descarga otras bibliotecas necesarias automáticamente.
3. Si termina sin errores y muestra **Successfully installed** o **Requirement already satisfied**, la instalación está completa.

**Listo:** Python 3.12.10 está instalado y verificado con `python --version`, y has instalado OpenCV y Ultralytics con pip. Puedes cerrar la consola. Si alguna instalación termina con un mensaje de error, copia el mensaje completo y compártelo con el profesor para que te ayude.
