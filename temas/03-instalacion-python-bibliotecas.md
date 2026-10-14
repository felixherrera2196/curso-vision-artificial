# 03. Instalación de Python y bibliotecas a utilizar (OpenCV y Roboflow)

## Qué aprenderás

Prepararás el entorno local y distinguirás entre el lenguaje, el editor, los paquetes y los servicios que se usarán durante el curso. Al terminar la preparación, el editor debe ejecutar el mismo Python en el que instalaste las bibliotecas.

## 1. Para qué sirve cada componente

| Componente | Función en el curso |
| --- | --- |
| Python | Ejecutar los programas y coordinar las bibliotecas. |
| VS Code | Editar archivos y trabajar con una terminal. |
| OpenCV | Capturar video, transformar imágenes, crear máscaras y analizar contornos. |
| NumPy | Representar arreglos y realizar operaciones numéricas usadas en imágenes. |
| Roboflow | Organizar y etiquetar datos; su SDK permite acceder a proyectos y descargas compatibles. |
| Ultralytics | Entrenar y utilizar modelos YOLO compatibles con la versión instalada. |
| Google Colab | Ejecutar notebooks remotos, con posibilidad de acceder a una GPU. |

Instalar VS Code no instala necesariamente Python. Del mismo modo, crear una cuenta de Roboflow no instala su paquete en el equipo. Son componentes relacionados, pero independientes.

## 2. Preparación de Python y VS Code

El repositorio ya incluye un [tutorial de instalación de Python](../Tutorial%20instalaci%C3%B3n%20de%20Python/Tutorial%20instalaci%C3%B3n%20de%20Python.md) y un [tutorial de instalación de VS Code](../Tutorial%20de%20instalaci%C3%B3n%20de%20VSCode/Tutorial%20de%20instalaci%C3%B3n%20de%20VSCode.md). Sigue ambos tutoriales para preparar tu equipo antes de comenzar las prácticas de cámara.

Utiliza una versión de Python compatible con los paquetes que vas a instalar. Elegir una versión recién publicada sin revisar compatibilidad puede causar fallos porque algunas bibliotecas todavía no ofrecen archivos preparados para ella. En computadoras del laboratorio conviene conservar la configuración que haya validado el instructor.

Después de instalar Python, abre una terminal nueva y verifica que el sistema encuentre el intérprete. Las terminales que estaban abiertas antes de la instalación pueden conservar una configuración anterior.

## 3. Por qué conviene un entorno virtual

Un **entorno virtual** es una carpeta que contiene un entorno de Python separado para un proyecto. Permite que este curso use sus versiones de paquetes sin modificar las de otros proyectos. No es una máquina virtual ni un sistema operativo nuevo.

El flujo consiste en crear el entorno, activarlo en la terminal, instalar ahí las bibliotecas y seleccionar ese intérprete en VS Code. La activación afecta a esa sesión de terminal; abrir otra terminal puede requerir activarlo nuevamente. En VS Code, la selección del intérprete debe apuntar al Python del entorno.

Para ejecutar pip, es preferible hacerlo a través del intérprete elegido. Así se reduce el riesgo de instalar en un Python y ejecutar desde otro. Tener varios Python en un equipo es una causa común de «paquete instalado, pero módulo no encontrado».

## 4. Nombres de instalación y nombres de importación

El paquete habitual de OpenCV para escritorio se llama `opencv-python`, mientras que su módulo se llama `cv2`. El SDK de Roboflow se distribuye como `roboflow`. La biblioteca de Ultralytics se distribuye como `ultralytics`. El nombre del paquete y el del módulo no siempre coinciden.

Para las prácticas con ventanas y cámara local, necesitas una distribución de OpenCV que incluya funciones de interfaz gráfica. Una variante **headless** está pensada para entornos sin ventanas y puede fallar al intentar mostrar una imagen con las funciones del curso. Evita instalar varias variantes de OpenCV en el mismo entorno: comparten el módulo `cv2` y pueden interferir.

## 5. Qué significa verificar la instalación

No basta con que termine una descarga. La comprobación debe avanzar por niveles:

1. El sistema encuentra Python y muestra su versión.
2. El intérprete puede cargar las bibliotecas requeridas.
3. VS Code utiliza ese mismo intérprete.
4. Un programa local logra abrir la cámara y recibir un fotograma.
5. La ventana de visualización aparece y puede cerrarse correctamente.

El último nivel depende de permisos del sistema y de hardware disponible. Un equipo sin cámara puede superar las primeras comprobaciones y fallar en la práctica de video; no significa que OpenCV esté mal instalado.

## 6. Local y Colab son entornos distintos

Lo instalado en tu computadora no aparece automáticamente en Colab. Colab utiliza un sistema remoto, con paquetes y archivos propios. Más adelante instalaremos allí lo necesario para entrenar y trasladaremos el archivo de pesos al equipo local.

La cámara web del equipo se utilizará en el programa local. Abrir el dispositivo número 0 en una sesión remota no equivale a acceder a la cámara del navegador.

## Problemas frecuentes

- **Módulo no encontrado:** revisa el intérprete seleccionado y dónde se instaló el paquete.
- **Instalación incompatible:** comprueba versión de Python, arquitectura y mensaje completo de pip.
- **Ventana no disponible:** comprueba la variante de OpenCV y si estás en un escritorio local.
- **Cámara ocupada:** cierra aplicaciones que estén usando el dispositivo y revisa permisos.

## Antes de continuar

Completa los tutoriales de instalación y selecciona el intérprete correcto en VS Code. Después ejecuta la [práctica de cámara del tema 04](04-video-camara-python.md): abrir una ventana con video y cerrarla con ESC será tu comprobación del entorno local.

[Anterior](02-que-es-una-imagen.md) · [Índice](../README.md) · [Siguiente: Cámara](04-video-camara-python.md)
