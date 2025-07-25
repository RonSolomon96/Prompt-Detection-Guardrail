from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sentence_transformers import SentenceTransformer
from importlib.resources import files
from pydantic import BaseModel
import joblib
import os
from fastapi.staticfiles import StaticFiles




app = FastAPI()

# Load model
model_path = files("app.model").joinpath("xgb_prompt_detector.pkl")
model = joblib.load(model_path)

# Load embedder
e_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Setup templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# API Input Schema
class PromptRequest(BaseModel):
    prompt: str

# HTML UI
@app.get("/", response_class=HTMLResponse)
def ui_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Prediction API
@app.post("/predict")
def predict_prompt(data: PromptRequest):
    emb = e_model.encode(data.prompt)
    y_pred = int(model.predict([emb])[0])
    y_proba = float(model.predict_proba([emb])[0, 1])
    return {
        "prediction": y_pred,
        "label": "Malicious" if y_pred == 1 else "Benign",
        "probability": round(y_proba, 4)
    }