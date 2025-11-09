# 🎧 Payday 2 Music Tool By PV21

Este proyecto contiene **dos programas** escritos en Python que te permiten:

1. **Descargar canciones desde YouTube** en formato `.mp3`.  
2. **Crear automáticamente un mod de música para Payday 2**, con todos los archivos y estructuras necesarias.

---

## 🧩 Estructura del proyecto


Payday2MusicTool/
│
├── 📁 Payday2 Music Creator/ # Proyecto 1: Descargador de música
│ ├── desmusic.py
│ ├── setup_desmusic.bat
│ └── start_desmusic.bat
│
├── 📁 MISMA CARPETA / # Proyecto 2: Creador de mods para Payday 2
│ ├── payday.py
│ ├── setup_payday.bat
│ └── start_payday.bat
│
└── README.md

---

## ⚙️ Requisitos

Antes de usar los scripts asegúrate de tener:

- **Windows 10/11**
- **Python 3.10 o superior**  
  👉 Descarga desde: [https://www.python.org/downloads](https://www.python.org/downloads)

> 🔧 Durante la instalación de Python, **marca la opción “Add Python to PATH”**.

---

## 🚀 Instalación

Cada herramienta tiene su propio instalador `.bat` que configurará todo automáticamente.

### 🧩 1. Descargador de música (`desmusic.py`)

1. Ejecuta `setup_desmusic.bat`.
2. Se instalarán los paquetes necesarios (`yt-dlp`).
3. Una vez completado, ejecuta `start_desmusic.bat` para iniciar el programa.

El script descargará canciones desde **YouTube** usando el enlace que introduzcas y las guardará en una carpeta (por ejemplo `input_songs/`).

---

### 🎵 2. Creador de mods de música (`payday.py`)

1. Ejecuta `setup_payday.bat`.
2. Se instalarán los paquetes necesarios (`pydub`).
3. Si no tienes **FFmpeg**, instálalo ejecutando (como administrador en PowerShell):

   ```choco install ffmpeg```

4. Coloca tus archivos .mp3 en la carpeta input_songs/.
5. Ejecuta start_payday.bat para generar los mods.







## 🛠️ Cómo funciona


# 🔹 Descargador de música (desmusic.py)

Descarga cualquier canción de YouTube con su link.

Convierte automáticamente el video a .mp3.

Guarda el archivo en la carpeta especificada (canciones_descargadas/ o similar).

Ejemplo:

Ingrese el link de YouTube:
https://www.youtube.com/watch?v=dQw4w9WgXcQ

Descargando...
✅ Canción guardada en canciones_descargadas/Rick Astley - Never Gonna Give You Up.mp3


# 🔹 Creador de mods (payday.py)

Toma los .mp3 que pongas en input_songs/ y crea una estructura como esta:

# CALABRIA/
# ├── main.xml
# ├── loc/
# │   └── en.txt
# └── sounds/
#     ├── assault.ogg
#    ├── assaultintro.ogg
#    ├── buildup.ogg
#    ├── buildupintro.ogg
#    ├── control.ogg
#    ├── controlintro.ogg
#    ├── menu.ogg
#    ├── menuintro.ogg
#    ├── stealth.ogg
#    └── stealthintro.ogg




# 📂 El script:

Toma los primeros 10 segundos de la canción para los archivos “intro”.
Convierte todo a formato .ogg.

Genera automáticamente:
El archivo main.xml con la estructura del mod.
El archivo loc/en.txt con el nombre de la canción.



# 📂 Salida final

Los mods se guardan dentro de:

output_mods/
└── NOMBRE_CANCION/
    ├── main.xml
    ├── loc/en.txt
    └── sounds/*.ogg


Cada subcarpeta dentro de output_mods es un mod completo listo para colocar en tu carpeta de mod_overrides de Payday 2.




### Consejos y notas

Los nombres de las canciones se limpian automáticamente (quita caracteres especiales o paréntesis).
Si una canción tiene un nombre largo, el script lo acorta para evitar errores.
Puedes colocar varias canciones a la vez en input_songs/ y todas serán procesadas.
Si modificas los archivos .bat, asegúrate de mantener las rutas correctas.

# 💡 Créditos

Desarrollado por: PV21 / Privalo21 🧠

Librerías usadas:
> yt-dlp
 — para descargar videos de YouTube.
> pydub
 — para cortar y convertir audio.
> Compatibilidad: Windows 10/11 (Python 3.10+)



