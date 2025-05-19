# Descargar videos de YOUTUBE
import os
import time
from yt_dlp import YoutubeDL
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrarBanner():
    print(Fore.CYAN + Style.BRIGHT + """
     /$$     /$$ /$$$$$$$$       /$$$$$$$   /$$$$$$  /$$      /$$ /$$   /$$
    |  $$   /$$/|__  $$__/      | $$__  $$ /$$__  $$| $$  /$ | $$| $$$ | $$
     \  $$ /$$/    | $$         | $$  \ $$| $$  \ $$| $$ /$$$| $$| $$$$| $$
      \  $$$$/     | $$ /$$$$$$ | $$  | $$| $$  | $$| $$/$$ $$ $$| $$ $$ $$
       \  $$/      | $$|______/ | $$  | $$| $$  | $$| $$$$_  $$$$| $$  $$$$
        | $$       | $$         | $$  | $$| $$  | $$| $$$/ \  $$$| $$\  $$$
        | $$       | $$         | $$$$$$$/|  $$$$$$/| $$/   \  $$| $$ \  $$
        |__/       |__/         |_______/  \______/ |__/     \__/|__/  \__/
""")
    print(Fore.YELLOW + ">>> AppDownload YouTube 0.1 -- Video o Audio\n")

def elegirFormato():
    print(Fore.GREEN + "[1] Descargar Video")
    print(Fore.GREEN + "[2] Descargar Solo Audio (webm)")
    opcion = input(Fore.YELLOW + "Selecciona una opción (1 o 2): ")
    return opcion.strip()

def prepararDirectorios():
    os.makedirs('videos', exist_ok=True)
    os.makedirs('audios', exist_ok=True)

def mostrarBarraProgreso(d):
    if d['status'] == 'downloading':
        porcentaje = d.get('_percent_str', '').strip()
        velocidad = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()
        print(Fore.BLUE + f"\rDescargando... {porcentaje} - {velocidad} - ETA {eta}   ", end='', flush=True)
    elif d['status'] == 'finished':
        print(Fore.GREEN + "\n✔ Descarga completa. Procesando archivo...")

def descargar_video(url):
    print(Fore.MAGENTA + "\nDescargando video con mejor calidad disponible...\n")
    ydl_opts = {
        'format': 'best',  # solo un stream combinado
        'outtmpl': os.path.join('videos', '%(title)s.%(ext)s'),
        'quiet': True,  # suprime la salida de información
        'progress_hooks': [mostrarBarraProgreso],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def descargar_audio(url):
    print(Fore.MAGENTA + "\nDescargando audio en formato original (.webm)...\n")
    ydl_opts = {
        'format': 'bestaudio',  # mejor calidad de audio disponible
        'outtmpl': os.path.join('audios', '%(title)s.%(ext)s'),
        'quiet': True,  # suprime la salida de información
        'progress_hooks': [mostrarBarraProgreso],
        'postprocessors': [],  # sin conversiones
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# ---------- PROGRAMA PRINCIPAL ----------
if __name__ == "__main__":
    limpiarConsola()
    mostrarBanner()

    prepararDirectorios()

    opcion = elegirFormato()
    url = input(Fore.CYAN + "🔗 Pegá la URL del video: ").strip()

    print(Fore.YELLOW + "\n>>🔄 Procesando...")
    try:
        if opcion == "1":
            descargar_video(url)
        elif opcion == "2":
            descargar_audio(url)
        else:
            print(Fore.RED + "❌ Opción no válida.")
            exit()

        print(Fore.GREEN + "✅ Video descargado con éxito.")

    except Exception as e:
        print(Fore.RED + "\n❌ Error al procesar el video:", str(e))

