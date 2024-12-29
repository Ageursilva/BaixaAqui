from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
import yt_dlp
import os
import sys

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="static/images"), name="images")
templates = Environment(loader=FileSystemLoader("templates"))

## Ajuste Caminho para o FFmpeg
FFMPEG_PATH = 'C:\\ffmpeg\\bin'
if not os.path.exists(os.path.join(FFMPEG_PATH, 'ffmpeg.exe')):
    raise RuntimeError(f"FFmpeg não encontrado em {FFMPEG_PATH}. Por favor, instale o FFmpeg corretamente.")

if FFMPEG_PATH not in os.environ['PATH']:
    os.environ['PATH'] = FFMPEG_PATH + os.pathsep + os.environ['PATH']

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(playlist_index)s - %(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': FFMPEG_PATH,  
    'ignoreerrors': True,
    'prefer_ffmpeg': True,
    'keepvideo': False,
}


if not os.path.exists("downloads"):
    os.makedirs("downloads")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.get_template("index.html").render({"request": request})

@app.post("/download_playlist/")
async def download_playlist(playlist_url: str = Form(...)):
    try:


        if not os.path.exists(os.path.join(FFMPEG_PATH, 'ffmpeg.exe')):
            raise HTTPException(500, "FFmpeg não encontrado. Verifique a instalação.")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        return {"detail": "Download finalizado com sucesso!"}
    except yt_dlp.utils.DownloadError as e:
        return {"detail": f"Erro ao baixar: {str(e)}"}
    except Exception as e:
        return {"detail": f"Erro inesperado: {str(e)}"}