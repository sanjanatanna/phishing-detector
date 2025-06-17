from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import joblib
import numpy as np
import os
import zipfile
import requests

# === Setup Model Directory and ZIP Details ===
MODEL_DIR = "models"
ZIP_URL = "https://github.com/sanjanatanna/phishing-detector/releases/download/v1/Archive.zip"
ZIP_PATH = os.path.join(MODEL_DIR, "model_files.zip")

os.makedirs(MODEL_DIR, exist_ok=True)

def download_and_unzip():
    if not os.path.exists(os.path.join(MODEL_DIR, "best_model.joblib")):
        print("📦 Downloading model ZIP...")
        r = requests.get(ZIP_URL)
        r.raise_for_status()  # ensure download was successful
        with open(ZIP_PATH, "wb") as f:
            f.write(r.content)

        print("🧩 Unzipping...")
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(MODEL_DIR)
        print("✅ Done.")

# === Call Once at Startup ===
download_and_unzip()

# === Load Model and Vectorizer ===
model_path = os.path.join(MODEL_DIR, "best_model.joblib")
vectorizer_path = os.path.join(MODEL_DIR, "tfidf_vectorizer.joblib")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# === Initialize FastAPI App ===
app = FastAPI()

# === Optional CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend origin in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Define Input Schema ===
class InputData(BaseModel):
    text: str

# === Inference Route ===
@app.post("/predict")
def predict(input: InputData):
    vect = vectorizer.transform([input.text])
    prediction = model.predict(vect)[0]
    label = "Phishing" if prediction == 1 else "Legitimate"
    return {"prediction": int(prediction), "label": label}

# === Serve Static Frontend ===
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
