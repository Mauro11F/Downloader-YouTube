# Descargar videos de YOUTUBE
import pafy

print ("                                                                                                            ")
print ("  ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗       ███╗   ██╗ ██████╗ ██╗    ██╗ ")
print ("  ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗      ████╗  ██║██╔═══██╗██║    ██║ ")
print ("  ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗██╔██╗ ██║██║   ██║██║ █╗ ██║ ")
print ("  ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║╚════╝██║╚██╗██║██║   ██║██║███╗██║ ")
print ("  ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝      ██║ ╚████║╚██████╔╝╚███╔███╔╝ ")
print ("  ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝  ")
print ("                                                                                                            ")

url = input("Pegar URL del video: ")

video = pafy.new(url)

streams = video.streams

for i in streams:
    print(i)

best = video.getbest()
print(best.resolution, best.extension)

# .download(filepath="ubicaion")  Donde se descarga(guarda) el Video...
best.download(filepath="C:/Users/User1/Desktop/AppDowload-YouTube/Videos")
print("Descarga finalizada...")
