from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import subprocess
import os

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    input_path = "15sec_input_720p.mp4"
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run your tracking pipeline (this should generate output_tracking.mp4)
    subprocess.run(["python", "main.py"])

    output_path = "output_tracking.mp4"
    if os.path.exists(output_path):
        return FileResponse(output_path, media_type='video/mp4', filename="output_tracking.mp4")
    else:
        return {"error": "Tracking failed"}
