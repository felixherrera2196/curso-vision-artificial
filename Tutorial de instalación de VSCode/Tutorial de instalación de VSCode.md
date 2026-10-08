# Tutorial de instalación de VSCode

Esta guía te ayudará a instalar **Visual Studio Code**, también llamado **VS Code**, en una computadora con **Windows 11**. No necesitas experiencia en programación.

VS Code es el programa en el que escribirás y ejecutarás los ejercicios del curso de OpenCV y YOLO. **Python se instala por separado**: tener VS Code no significa que ya tengas Python.

## 1. Antes de empezar

Necesitas una conexión a Internet y espacio disponible en tu computadora. Si es una computadora de escuela o trabajo y no te permite instalar programas, pide ayuda a la persona que la administra.

En esta guía, “hacer clic” significa presionar una vez el botón izquierdo del ratón. Cuando aparezca un comando, copia únicamente el texto dentro del recuadro; no copies los símbolos que delimitan el recuadro.

## 2. Descargar VS Code desde su página oficial

1. Abre tu navegador, por ejemplo Microsoft Edge o Google Chrome.
2. Haz clic en la barra de direcciones de la parte superior.
3. Escribe **https://code.visualstudio.com/** y presiona **Enter**.
4. Busca el botón de descarga para **Windows**. Si no aparece, entra a [la página oficial de descargas](https://code.visualstudio.com/Download).
5. Elige **User Installer** para Windows. Esta opción instala el programa para tu usuario y normalmente no necesita permisos de administrador.
6. Selecciona **x64** si tu computadora tiene un procesador Intel o AMD, que es lo más habitual. Si tu equipo usa un procesador ARM, selecciona **Arm64**.
   - Para comprobarlo, abre **Inicio → Configuración → Sistema → Información** y busca **Tipo de sistema**.
7. Espera a que termine la descarga. El archivo tendrá un nombre parecido a `VSCodeUserSetup-x64-...exe`.

Descarga el programa desde el sitio oficial. No necesitas pagar ni usar una página de descargas de terceros.

## 3. Ejecutar el instalador

1. Abre el **Explorador de archivos**, que tiene un icono de carpeta. También puedes presionar **Windows + E**.
2. Entra a **Descargas**.
3. Haz doble clic en el archivo que descargaste.
4. Si Windows pregunta si permites cambios en el equipo, revisa que el archivo sea el instalador descargado del sitio oficial de VS Code. Acepta si corresponde. Si aparece una advertencia de seguridad inesperada, no desactives la protección: verifica el origen del archivo o pide ayuda.
5. Lee el acuerdo de licencia y selecciona **Acepto el acuerdo** si estás de acuerdo; después haz clic en **Siguiente**.
6. Conserva la carpeta de instalación propuesta y haz clic en **Siguiente**.
7. Conserva el nombre del acceso en el menú Inicio y continúa.
8. En **Tareas adicionales**, marca estas opciones si aparecen; los nombres pueden variar un poco según el idioma:
   - **Crear un icono en el escritorio**, para encontrar el programa fácilmente.
   - **Agregar la acción “Abrir con Code” al menú contextual de directorio**, para poder abrir carpetas desde el Explorador.
   - **Agregar a PATH**, para poder abrir VS Code mediante el comando `code`.
9. Haz clic en **Instalar** y espera a que termine.
10. Marca **Ejecutar Visual Studio Code** y haz clic en **Finalizar**.

Si tenías una terminal abierta durante la instalación, ciérrala y vuelve a abrirla para que reconozca los cambios.

## 4. Poner el programa en español

Este paso es opcional, pero puede facilitarte el uso del programa.

1. Con VS Code abierto, haz clic en **Extensiones**: es el icono de bloques en el lado izquierdo. También puedes presionar **Ctrl + Shift + X**.
2. En el buscador de extensiones escribe `Spanish Language Pack`.
3. Selecciona **Spanish Language Pack for Visual Studio Code**, publicado por **Microsoft**.
4. Haz clic en **Install / Instalar**.
5. Si aparece el botón **Change Language and Restart / Cambiar idioma y reiniciar**, haz clic en él.
6. Si no aparece, presiona **Ctrl + Shift + P**, escribe `Configure Display Language`, selecciona esa opción y elige `es` o **Español**. Acepta reiniciar VS Code.

## 5. Comprobar que VS Code está instalado

1. Cierra VS Code si está abierto.
2. Abre **Inicio** y escribe `Visual Studio Code`.
3. Haz clic en el resultado para abrirlo.
4. Si aparece la pantalla de bienvenida o la ventana principal, la instalación está completa. No necesitas escribir código ni ejecutar Python para comprobarlo.

## 6. Preparar VS Code para escribir en Python

1. Abre **Extensiones** con **Ctrl + Shift + X**. La tecla **Shift** también se llama **Mayús**.
2. Escribe `Python` en el buscador.
3. Busca la extensión llamada **Python**, publicada por **Microsoft**, y haz clic en **Instalar / Install**. Puede instalar otras extensiones necesarias automáticamente.
4. Esta extensión ayuda a VS Code a trabajar con Python, pero **no instala Python ni OpenCV**. Completa la guía de Python enlazada al final.
5. Cuando esa guía te indique crear `CursoOpenCV`, abre esa carpeta desde **Archivo → Abrir carpeta / File → Open Folder**. Selecciona la carpeta y pulsa **Seleccionar carpeta**.
6. Si aparece una pregunta sobre confiar en los autores, puedes confiar si es la carpeta que tú creaste para los ejercicios. Con carpetas descargadas, comprueba primero su origen.
7. Presiona **Ctrl + Shift + P** para abrir la lista de acciones. Escribe `Python: Select Interpreter` y selecciona **Python: Seleccionar intérprete** o su equivalente en inglés.
8. Elige el Python de `.venv`, el entorno que crearás siguiendo la otra guía. Si todavía no existe, completa primero la instalación de Python.

Para ver una guía `.md` con un formato más cómodo, ábrela en VS Code y presiona **Ctrl + Shift + V**. `.md` significa que el archivo contiene texto con formato Markdown.

## 7. Problemas frecuentes

### No encuentro VS Code después de instalarlo

Abre **Inicio**, escribe `Visual Studio Code` y haz clic en el resultado. Puedes hacer clic derecho en su icono y elegir **Anclar a la barra de tareas**. Si no aparece, revisa si el instalador terminó correctamente.

### La computadora no me permite instalarlo

Si es una computadora de escuela o trabajo, pide ayuda a la persona que la administra. Puedes intentar la opción **User Installer** del sitio oficial, que normalmente no requiere permisos de administrador.

### No encuentro exactamente el mismo texto en un botón

Los nombres pueden cambiar entre versiones o idiomas. Busca la opción equivalente usando los nombres en español o inglés que aparecen en esta guía.

## 8. Comprobación final

- [ ] La instalación terminó sin errores.
- [ ] VS Code aparece en el menú Inicio.
- [ ] VS Code abre y muestra su ventana principal.
- [ ] Si elegiste el idioma español, los menús aparecen en español.

Con esto, VS Code está instalado. La instalación de Python y OpenCV se explica por separado en la [guía de instalación de Python](../Tutorial%20instalación%20de%20Python/Tutorial%20instalación%20de%20Python.md).
