from fastapi import FastAPI
from fastapi.responses import FileResponse
import yt_dlp
import zipfile
import os
import uuid
import logging


logging.basicConfig(filename="yt_dlp_errors.log", level=logging.ERROR)


app = FastAPI()


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(playlist_index)s - %(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ignoreerrors': True, 
    'logger': logging.getLogger(), 
}


@app.post("/download_playlist/")
async def download_playlist(playlist_url: str):
    try:

        download_path = "downloads/"

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])


    except Exception as e:
        logging.error(f"Erro ao processar a playlist: {str(e)}")
        return {"detail": f"Erro ao processar a playlist: {str(e)}"}
