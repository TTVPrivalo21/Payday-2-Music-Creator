import os
import tkinter as tk
from tkinter import messagebox
import yt_dlp

# === CONFIG ===
OUTPUT_FOLDER = "canciones_descargadas"  # Carpeta donde se guardan las canciones descargadas
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# === FUNCIÓN DE DESCARGA ===
def download_song():
    url = url_entry.get().strip()

    if not url:
        messagebox.showwarning("Error", "Por favor, ingresa un enlace de YouTube.")
        return

    try:
        # Opciones de yt-dlp
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(OUTPUT_FOLDER, "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": True,
            "no_warnings": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "Desconocido")

        messagebox.showinfo("✅ Descarga completa", f"'{title}' se guardó en:\n{OUTPUT_FOLDER}")

    except Exception as e:
        messagebox.showerror("❌ Error", f"No se pudo descargar la canción:\n{e}")

# === INTERFAZ GRÁFICA ===
root = tk.Tk()
root.title("🎵 Descargador de Música YouTube → MP3")
root.geometry("450x200")
root.resizable(False, False)
root.configure(bg="#202020")

# Etiqueta
label = tk.Label(root, text="Pega el link de YouTube:", font=("Segoe UI", 11), fg="white", bg="#202020")
label.pack(pady=(20, 5))

# Campo de texto
url_entry = tk.Entry(root, width=50, font=("Segoe UI", 10))
url_entry.pack(pady=5)

# Botón de descarga
download_button = tk.Button(
    root,
    text="⬇️ Descargar MP3",
    command=download_song,
    bg="#3a7bd5",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    padx=10,
    pady=5
)
download_button.pack(pady=15)

# Info
info_label = tk.Label(root, text=f"Los MP3 se guardarán en: {OUTPUT_FOLDER}", fg="gray", bg="#202020", font=("Segoe UI", 8))
info_label.pack(side="bottom", pady=10)

root.mainloop()
