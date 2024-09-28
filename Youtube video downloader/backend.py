from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import yt_dlp

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"]   # Allows all headers
)

# Current working directory to save the videos
cur_dir = os.getcwd()

# POST endpoint to handle YouTube video download
@app.post("/download")
def download_video(link: str = Form(...)):
    # Set download options for yt-dlp
    youtube_dl_options = {
        "format": "best",  # Selects the best quality available
        "outtmpl": os.path.join(cur_dir, f"Video-{link[-11:]}.mp4")  # Output file name
    }

    # Download the video using yt-dlp
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])

    # Return response
    return {"status": "Download started"}
