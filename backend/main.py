from fastapi import FastAPI # type: ignore
from agents.detector import analyze_image
from fastapi import FastAPI, UploadFile, File # type: ignore
import shutil

app = FastAPI(title = "StreetSentinel API")
@app.get("/")
def root():
    return {
        "message": "StreetSentinel API running"
    }

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"
    print("=" * 50)
    print("Received file:", file.filename)
    print("Saved path:", file_path)
    print("=" * 50)

    result = analyze_image(file_path)

    print("Result received")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_image(file_path)

    return {
        "result": result
    }