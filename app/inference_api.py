from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize FastAPI app
app = FastAPI()

# Optional: enable CORS for local frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace * with allowed domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and vectorizer
model = joblib.load("models/best_model.joblib")
vectorizer = joblib.load("models/tfidf_vectorizer.joblib")

# Define the input format for the prediction API
class InputData(BaseModel):
    text: str

# Define the POST route for prediction
@app.post("/predict")
def predict(input: InputData):
    text = input.text
    vect = vectorizer.transform([text])
    prediction = model.predict(vect)[0]
    label = "Phishing" if prediction == 1 else "Legitimate"
    return {"prediction": int(prediction), "label": label}

# ✅ Mount frontend static files AFTER defining routes
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
