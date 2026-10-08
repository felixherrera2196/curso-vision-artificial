# Tutorial instalación de Python

Esta guía explica cómo instalar **Python en Windows 11** y preparar **OpenCV** para el curso. Está pensada para personas que nunca han programado.

**Python** ejecuta los programas que escribirás. **pip** descarga e instala bibliotecas de Python. **OpenCV** es una de esas bibliotecas y permite trabajar con imágenes y video. **YOLO** se utiliza para detectar objetos; su instalación depende de la versión que se use en el curso.

## 1. Qué necesitas

- Una computadora con Windows 11 y conexión a Internet.
- Permiso para instalar programas en esa computadora.
- Unos minutos para descargar Python e instalar las bibliotecas.

Si el profesor indicó una versión de Python, utiliza esa versión para que los ejercicios coincidan con los del curso. En caso contrario, instala la **versión estable más reciente de Python** disponible en el sitio oficial. Evita las versiones de prueba que indiquen **alpha**, **beta**, **release candidate**, **RC** o **pre-release**.

## 2. Descargar Python desde la página oficial

1. Abre Microsoft Edge, Google Chrome o tu navegador habitual.
2. Haz clic en la barra de direcciones y abre [la página oficial de descargas de Python](https://www.python.org/downloads/).
3. Busca la versión indicada por el profesor o, si no indicó ninguna, la versión estable más reciente. El número cambia con el tiempo.
4. Entra a su página de descarga y busca la sección **Files**.
5. Si ofrece **Windows installer (64-bit)**, descarga esa opción para una computadora Intel o AMD. No elijas **embeddable package**, archivos de código fuente ni una versión de prueba.
6. Si tu computadora usa ARM, busca **Windows installer (ARM64)**. Para comprobar tu equipo, abre **Inicio → Configuración → Sistema → Información → Tipo de sistema**.
7. Espera a que termine la descarga. El nombre del archivo incluirá el número de la versión que elegiste.

Python es gratuito. Descárgalo únicamente desde **python.org**. Si la página te ofrece **Python Install Manager** en lugar del instalador tradicional, sigue la alternativa del apartado siguiente.

## 3. Instalar Python

### Si descargaste el instalador tradicional de Windows

1. Abre el **Explorador de archivos** con **Windows + E**.
2. Entra a **Descargas** y haz doble clic en el instalador de Python que descargaste.
3. En la primera pantalla, **marca la casilla `Add python.exe to PATH`** antes de hacer clic en instalar. PATH ayuda a Windows a encontrar Python cuando escribes comandos.
4. Conserva las demás opciones predeterminadas y haz clic en **Install Now**. Esta instalación normalmente queda disponible para tu usuario.
5. Si Windows solicita autorización, comprueba que se trata del instalador oficial que descargaste y acepta si corresponde. Si tu computadora está administrada y solicita una contraseña que no tienes, pide ayuda al administrador.
6. Espera hasta ver **Setup was successful**: significa que terminó correctamente.
7. Si aparece **Disable path length limit**, puedes usarlo si tienes permisos: ayuda a evitar problemas con rutas muy largas. Es opcional para estos primeros ejercicios; si pide permisos que no tienes, puedes omitirlo.
8. Haz clic en **Close / Cerrar**.

### Si descargaste Python Install Manager

El administrador de instalación es una herramienta oficial que descarga e instala Python.

1. Abre el archivo descargado y haz clic en **Instalar**. Si la página oficial te dirige a Microsoft Store, instala **Python Install Manager** desde ese enlace.
2. Sigue las indicaciones de configuración. Si solicita agregar el directorio de comandos a PATH, acepta.
3. Abre **Símbolo del sistema** siguiendo el apartado 4 y ejecuta:

   ```bat
   py install default
   ```

4. Espera a que termine. Este comando instala la versión estable predeterminada más reciente que ofrece el administrador.
5. Cierra esa ventana y abre una nueva antes de comprobar la instalación.

## 4. Abrir la ventana donde escribirás los comandos

Usaremos **Símbolo del sistema**, también llamado **Command Prompt** o **cmd**. Es una ventana donde das instrucciones escritas a la computadora.

1. Haz clic en **Inicio** o presiona la tecla **Windows**.
2. Escribe `cmd`.
3. Abre **Símbolo del sistema**. No necesitas elegir “Ejecutar como administrador”.
4. Verás una línea parecida a `C:\Users\TuNombre>` y un cursor.

En los siguientes pasos, copia solo el comando del recuadro, pégalo en esa ventana y presiona **Enter**. Puedes pegar con **Ctrl + V**. Ejecuta los comandos de uno en uno. Los textos y números que aparezcan después son la respuesta del programa; no tienes que escribirlos.

Si la ventana estaba abierta antes de instalar Python, ciérrala y abre una nueva.

## 5. Comprobar Python y pip

Escribe:

```bat
python --version
```

Debes ver la palabra `Python` seguida del número de la versión que instalaste. Comprueba que coincida con la versión que elegiste descargar.

Después escribe:

```bat
python -m pip --version
```

Debe aparecer una línea con la versión de pip, su ubicación y la versión de Python.

La parte `-m pip` le indica a Python que ejecute su herramienta de instalación. Si ya tenías otro Python instalado y aparece una versión anterior, revisa las opciones de PATH o pide ayuda para seleccionar la instalación nueva antes de continuar.

Si uno de estos comandos falla, consulta **Problemas frecuentes** al final antes de continuar.

## 6. Crear la carpeta del curso

1. Abre el **Explorador de archivos** y entra a **Documentos**.
2. Crea una carpeta llamada `CursoOpenCV`: haz clic derecho en un espacio vacío y selecciona **Nuevo → Carpeta**. Si ya tienes una carpeta con ese nombre para el curso, usa esa misma carpeta.
3. Abre `CursoOpenCV`.
4. Haz clic en la barra de direcciones del Explorador, donde aparece la ubicación de la carpeta.
5. Escribe `cmd` y presiona **Enter**.

Se abrirá un Símbolo del sistema situado directamente en esa carpeta. Esto funciona incluso si Documentos está dentro de OneDrive o tiene una ubicación diferente. Usa esta nueva ventana para los siguientes pasos.

## 7. Crear un entorno para las bibliotecas del curso

Un **entorno virtual** es una carpeta que guarda las bibliotecas de este proyecto por separado. Así, las instalaciones del curso no se mezclan con las de otros proyectos.

1. En la ventana abierta dentro de `CursoOpenCV`, escribe:

   ```bat
   python -m venv .venv
   ```

2. Espera a que vuelva a aparecer la línea donde puedes escribir. Si no aparece ningún mensaje de error, es normal: el comando creó una carpeta llamada `.venv`.
3. Activa el entorno con este comando, **en Símbolo del sistema**:

   ```bat
   .venv\Scripts\activate.bat
   ```

4. Al inicio de la línea debe aparecer `(.venv)`. Eso indica que estás usando el entorno del curso.
5. Comprueba qué Python está activo:

   ```bat
   python -c "import sys; print(sys.executable)"
   ```

   La ruta debe terminar en `CursoOpenCV\.venv\Scripts\python.exe`.

No borres `.venv` ni guardes tus ejercicios dentro de ella. Los ejercicios se guardan en `CursoOpenCV`, al lado de `.venv`.

## 8. Instalar OpenCV con pip

Con el entorno activo —debe verse `(.venv)`—, actualiza pip:

```bat
python -m pip install --upgrade pip
```

Después instala OpenCV:

```bat
python -m pip install opencv-python
```

Espera a que termine; puede tardar según tu conexión. pip descargará también las dependencias necesarias, como NumPy. Si acaba sin errores, normalmente verás `Successfully installed` seguido de los paquetes instalados. Si ya estaban instalados, puede decir `Requirement already satisfied`.

El paquete se llama **`opencv-python` al instalarlo**, pero en el código se usa el nombre **`cv2`**. No ejecutes `pip install cv2`.

Para este curso en Windows usaremos `opencv-python`, que incluye funciones para mostrar ventanas. No instales a la vez `opencv-python-headless`, `opencv-contrib-python` u otras variantes: comparten el nombre `cv2` y pueden interferir. Si una clase necesita una variante distinta, sigue las indicaciones del profesor.

## 9. Comprobar que OpenCV realmente funciona

Primero consulta la versión:

```bat
python -c "import cv2; print('OpenCV instalado. Versión:', cv2.__version__)"
```

Debes ver `OpenCV instalado. Versión:` y un número. Ahora comprueba una operación real con una imagen de prueba creada en memoria:

```bat
python -c "import cv2; import numpy as np; imagen = np.zeros((100, 100, 3), dtype=np.uint8); gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY); print('Conversión correcta. Tamaño:', gris.shape)"
```

El resultado debe incluir:

```text
Conversión correcta. Tamaño: (100, 100)
```

Este comando crea una imagen negra de 100 × 100 píxeles y la convierte a escala de grises. No abre una ventana ni necesita una cámara o una imagen descargada.

Finalmente, revisa que las dependencias instaladas sean compatibles:

```bat
python -m pip check
```

El resultado esperado es `No broken requirements found.`. Si aparecen conflictos, guarda el mensaje y consulta al profesor antes de cambiar versiones al azar.

## 10. Usar este entorno en VS Code

1. Instala VS Code siguiendo la [guía de instalación de VSCode](../Tutorial%20de%20instalación%20de%20VSCode/Tutorial%20de%20instalación%20de%20VSCode.md).
2. En VS Code, abre **Archivo → Abrir carpeta** y selecciona `CursoOpenCV`.
3. Instala la extensión **Python**, publicada por **Microsoft**.
4. Presiona **Ctrl + Shift + P** y busca **Python: Select Interpreter / Seleccionar intérprete**.
5. Selecciona el Python de `.venv`. Si no aparece, busca manualmente `CursoOpenCV\.venv\Scripts\python.exe` usando **Introducir ruta del intérprete**.

La selección del intérprete indica a VS Code qué Python usar para ejecutar tus archivos. Una terminal que ya estaba abierta puede seguir usando otro entorno: ciérrala y abre una nueva después de seleccionar el intérprete, y comprueba la ruta como en el paso 7.

### Crear y ejecutar tu primer archivo de prueba

1. Con `CursoOpenCV` abierto en VS Code y el intérprete de `.venv` seleccionado, haz clic en **Archivo → Nuevo archivo de texto**.
2. Copia este código completo, conservando sus saltos de línea:

   ```python
   import cv2
   import numpy as np

   imagen = np.zeros((300, 500, 3), dtype=np.uint8)
   cv2.putText(imagen, "OpenCV funciona", (30, 150),
               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

   print("OpenCV instalado. Version:", cv2.__version__)
   cv2.imshow("Prueba de OpenCV", imagen)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

3. Presiona **Ctrl + Shift + S** y guarda el archivo como `prueba_opencv.py` dentro de `CursoOpenCV`, fuera de `.venv`. `.py` indica que es un programa de Python. No lo llames `cv2.py`, `numpy.py` ni `ultralytics.py`, porque esos nombres pueden interferir con las bibliotecas.
4. Abre el Símbolo del sistema dentro de `CursoOpenCV`, como en el apartado 6, y activa el entorno:

   ```bat
   .venv\Scripts\activate.bat
   ```

5. Ejecuta el archivo:

   ```bat
   python prueba_opencv.py
   ```

6. Debe aparecer una ventana negra con el texto verde **OpenCV funciona**. Si queda detrás de VS Code, búscala en la barra de tareas.
7. Haz clic en esa ventana y presiona cualquier tecla para cerrarla. Mientras la ventana esté abierta, es normal que la terminal espere.
8. También puedes ejecutarlo desde VS Code: abre `prueba_opencv.py`, haz clic derecho sobre el código y selecciona **Ejecutar archivo de Python en terminal / Run Python File in Terminal**. La extensión Python debe estar instalada y el intérprete debe ser el de `.venv`.

Esta prueba no requiere cámara, imágenes descargadas ni instalar YOLO.

## 11. Qué hacer cuando regreses otro día

No tienes que reinstalar Python ni OpenCV cada vez.

1. Abre `CursoOpenCV` en el Explorador de archivos.
2. Escribe `cmd` en su barra de direcciones y presiona **Enter**.
3. Activa el entorno:

   ```bat
   .venv\Scripts\activate.bat
   ```

4. Ejecuta tus programas o instala las bibliotecas que indique el profesor usando `python -m pip`.

Para salir del entorno en esa ventana, escribe `deactivate`. También puedes cerrar la ventana. Esto no borra tus archivos ni las bibliotecas.

## 12. Sobre YOLO

OpenCV ya está preparado. **Instalar OpenCV no instala YOLO**. Existen diferentes implementaciones de YOLO y el profesor debe indicar cuál se usará.

Si el curso usa **Ultralytics YOLO**, el siguiente paso, cuando lo indique el profesor, será ejecutar dentro del entorno activo:

```bat
python -m pip install ultralytics
```

Puedes comprobar esa instalación con:

```bat
python -c "import ultralytics; print('Ultralytics instalado. Versión:', ultralytics.__version__)"
```

Esta instalación puede descargar bibliotecas grandes, entre ellas PyTorch. Importar la biblioteca no descarga necesariamente los modelos: los pesos de un modelo suelen descargarse cuando lo cargas por primera vez, y eso requiere Internet. Para comenzar no es indispensable una tarjeta gráfica NVIDIA; los ejemplos pueden ejecutarse con el procesador, aunque más lentamente. La configuración de GPU y CUDA se hará por separado si el curso la requiere.

## 13. Problemas frecuentes

### `python` abre Microsoft Store o no se reconoce

Primero cierra el Símbolo del sistema y abre uno nuevo. Si usaste el instalador tradicional y necesitas corregir PATH, vuelve a abrirlo, elige **Modify / Modificar** y busca en las opciones avanzadas **Add Python to environment variables**. Termina el proceso y abre una terminal nueva. Si usaste Python Install Manager, revisa sus indicaciones de configuración y confirma que ejecutaste `py install default`.

Si el acceso de Microsoft Store sigue interfiriendo, busca **Alias de ejecución de aplicaciones** en Inicio y desactiva únicamente los alias `python.exe` y `python3.exe` que pertenezcan a **App Installer / Instalador de aplicaciones**. No desactives entradas de otra instalación de Python sin comprobarlas.

### Aparece `No module named pip`

Antes de crear el entorno, ejecuta:

```bat
python -m ensurepip --upgrade
```

Si el error aparece dentro del entorno activo, usa `python -m ensurepip --upgrade`. Después vuelve a comprobar pip y repite la instalación de OpenCV.

### Aparece `No module named 'cv2'`

Comprueba que estás dentro de `CursoOpenCV`, activa `.venv` y ejecuta de nuevo `python -m pip install opencv-python`. En VS Code, selecciona el intérprete de ese mismo entorno. La biblioteca puede estar instalada en un Python diferente al que ejecuta tu archivo.

### No se encuentra `activate.bat`

Confirma que la ventana está situada en `CursoOpenCV` y que creaste `.venv` allí. Abre la carpeta en el Explorador y repite el paso de escribir `cmd` en la barra de direcciones. Si `.venv` no existe, vuelve al paso 7.

### PowerShell dice que la ejecución de scripts está deshabilitada

Los comandos de activación de esta guía son para **Símbolo del sistema**. Abre `cmd` y usa `.venv\Scripts\activate.bat`. No necesitas cambiar la política de seguridad de Windows. También puedes omitir la activación y ejecutar directamente:

```bat
.venv\Scripts\python.exe -m pip install opencv-python
```

### pip muestra un error de conexión o certificado

Comprueba tu conexión y si la red de escuela o trabajo permite descargar paquetes. No desactives la comprobación de certificados ni uses páginas desconocidas. Si es una red administrada, pide al responsable que revise el acceso a `pypi.org` y `files.pythonhosted.org`. Guarda el mensaje completo del error para pedir ayuda.

### Aparece `>>>` y los comandos de instalación dan error

Estás dentro de la consola interactiva de Python, no en el Símbolo del sistema. Escribe `exit()` y presiona **Enter** para salir. Ejecuta los comandos de instalación cuando veas una línea parecida a `C:\...>`.

### Aparece `No matching distribution found` o pip intenta compilar y falla

Revisa que el comando esté escrito como `python -m pip install opencv-python` y que pip esté actualizado. Una versión de Python recién publicada o un equipo ARM puede no tener todavía paquetes preparados para alguna biblioteca del curso, especialmente PyTorch para YOLO. Guarda el mensaje completo y consulta al profesor qué versión y arquitectura de Python usar. No descargues paquetes de páginas desconocidas ni instales herramientas de compilación al azar.

Si se necesita otra versión de Python, el entorno `.venv` debe crearse con esa versión; cambiar la instalación principal no actualiza automáticamente un entorno existente. Conserva los ejercicios y pide ayuda para recrear el entorno e instalar sus bibliotecas.

## 14. Comprobación final

- [ ] La versión de Python elegida para el curso está instalada y responde a `python --version`.
- [ ] La carpeta `CursoOpenCV` contiene el entorno `.venv`.
- [ ] Al activar el entorno aparece `(.venv)`.
- [ ] OpenCV se importa con `import cv2` y muestra su versión.
- [ ] La conversión de la imagen de prueba devuelve `(100, 100)`.
- [ ] `python -m pip check` no encuentra dependencias incompatibles.
- [ ] VS Code usa el Python de `.venv` al ejecutar los ejercicios.
- [ ] `prueba_opencv.py` muestra la ventana con el texto verde y se cierra al pulsar una tecla.

Con estas comprobaciones completas, tienes la base preparada para empezar el curso de OpenCV y añadir la implementación de YOLO que indique el profesor.
