# 🎬 Downloader-YouTube
Este script permite descargar videos o extraer audio desde YouTube
de forma sencilla utilizando [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

___

## ✅ Requisitos

1. **Python 3.7 o superior**

Verifica que esté instalado:
```bash
python --version
```

2. **Instalar dependencias**

Ejecutar:
```bash
pip install -r requirements.txt
```

Si no quieres instalar con el archivo requirements.txt, instala manualmente:
```bash
pip install yt-dlp colorama
```

## ▶️ Modo de uso

Ejecuta el script con el enlace del video de YouTube que desees descargar.

Ejemplo:
```bash
python DescargarVideo.py
```

Sigue las instrucciones en pantalla para elegir entre:

- Descargar video
- Extraer audio (webm)

## 📂 Archivos descargados

- Los videos se guardan en la carpeta: **videos/**
- Los audios se guardan en la carpeta: **audios/**

## 🌐 Notas

- Se necesita conexión a internet.
- No funciona con videos privados o con restricciones de edad/geográficas.
- Si YouTube cambia su estructura, actualiza `yt-dlp` con:
```bash
pip install -U yt-dlp
```

## ⚠️ Importante
Este programa es solo para uso personal y educativo. Verifica que el contenido que descargues no infrinja derechos de autor.

