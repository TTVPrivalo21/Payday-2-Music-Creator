import os
from pydub import AudioSegment

# === CONFIGURACIÓN ===
INPUT_FOLDER = "input_songs"   # Carpeta donde pones los MP3
OUTPUT_FOLDER = "output_mods"  # Donde se crearán los mods
INTRO_DURATION = 10 * 1000     # 10 segundos (en milisegundos)

# === FUNCIONES ===

def create_folder_structure(song_name):
    song_path = os.path.join(OUTPUT_FOLDER, song_name)
    os.makedirs(os.path.join(song_path, "sounds"), exist_ok=True)
    os.makedirs(os.path.join(song_path, "loc"), exist_ok=True)
    return song_path

def convert_audio(song_path, audio, name, intro_audio):
    sounds_folder = os.path.join(song_path, "sounds")
    audio.export(os.path.join(sounds_folder, f"{name}.ogg"), format="ogg")
    intro_audio.export(os.path.join(sounds_folder, f"{name}intro.ogg"), format="ogg")

def create_main_lua(song_name, song_path):
    content = f"""<table name="{song_name.upper()}">
    <Localization directory="loc" default="en.txt"/>
    <HeistMusic id="{song_name.upper()}" directory="sounds">
        <event name="setup" source="stealth.ogg"/>
        <event name="anticipation" start_source="buildupintro.ogg" source="buildup.ogg"/>
        <event name="assault" start_source="assaultintro.ogg" source="assault.ogg"/>
        <event name="control" start_source="controlintro.ogg" source="control.ogg"/>
        <MenuMusic name="menu" start_source="menu.ogg" source="menu.ogg"/>
    </HeistMusic>
</table>
"""
    with open(os.path.join(song_path, "main.xml"), "w", encoding="utf-8") as f:
        f.write(content)

def create_loc_file(song_name, song_path):
    content = f"""{{
    "menu_jukebox_{song_name.upper()}" : "{song_name.upper()}",
    "menu_jukebox_screen_{song_name.upper()}" : "{song_name.upper()}"
}}"""
    with open(os.path.join(song_path, "loc", "en.txt"), "w", encoding="utf-8") as f:
        f.write(content)

def process_song(file_path):
    song_name = os.path.splitext(os.path.basename(file_path))[0]
    print(f"Procesando: {song_name}...")

    # Cargar mp3
    audio = AudioSegment.from_mp3(file_path)
    intro_audio = audio[:INTRO_DURATION]

    # Crear carpetas
    song_path = create_folder_structure(song_name)

    # Crear audios
    for name in ["stealth", "menu", "control", "assault", "buildup"]:
        convert_audio(song_path, audio, name, intro_audio)

    # Crear archivos de texto
    create_main_lua(song_name, song_path)
    create_loc_file(song_name, song_path)

    print(f"✅ {song_name} completado!\n")

# === MAIN ===
def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith(".mp3"):
            process_song(os.path.join(INPUT_FOLDER, file))
    print("🎵 Todos los mods han sido generados correctamente!")

if __name__ == "__main__":
    main()
