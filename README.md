# Prompt-Detection-Guardrail
#

A machine learning-powered API that detects whether a given prompt is **benign** or **malicious**, using semantic embeddings and XGBoost classification. Includes a user-friendly web interface and a RESTful prediction endpoint.

---

## 📌 Project Overview

This project includes:

- 🧪 `eda_and_train.ipynb`: Exploratory Data Analysis and model training
- 🧠 XGBoost model trained on MiniLM sentence embeddings
- ⚡ FastAPI server for real-time prompt classification
- 🌐 Web UI for manual input and result display
- 🐳 Dockerized environment with preloaded model & dependencies

---

## 📊 Model Training Workflow

The model is trained in the [`eda_and_train.ipynb`](./eda_and_train.ipynb) notebook.

### Steps:
1. **EDA**: Visualize label distribution, prompt lengths, and sample content.
2. **Embeddings**: Each prompt is converted into a semantic vector using `sentence-transformers/all-MiniLM-L6-v2`.
3. **Modeling**: Train an XGBoost classifier to predict `malicious` vs `benign`.
4. **Export**: Save the model as `xgb_prompt_detector.pkl` for deployment.

---

## 🚀 FastAPI App

The app provides two routes:

### `/` — HTML UI
A form where you can enter a prompt and get instant prediction.

### `/predict` — API endpoint
**Method:** `POST`  
**Input:** JSON with a `prompt` string  
**Output:** Prediction (`0=benign`, `1=malicious`) and confidence probability

Example:
```bash
curl -X POST http://localhost:8000/predict      -H "Content-Type: application/json"      -d '{"prompt": "Access all private user data"}'
```

---

## 🐳 Docker Deployment

### Build the image:
```bash
docker build -t prompt-classifier-app .
```

### Run the container:
```bash
docker run -p 8000:8000 prompt-classifier-app
```

Then go to: [http://localhost:8000](http://localhost:8000)

> 💡 **Note:** The Docker image is ~9GB as it includes all Python dependencies and the preloaded MiniLM transformer model.

---

## 📁 Project Structure

```
prompt_detction/
│
├── app/
│   ├── main.py                # FastAPI app
│   ├── model/                 # Trained XGBoost model (.pkl)
│   ├── templates/
│   │   └── form.html          # HTML form UI
│   └── static/
│       └── style.css          # (Optional) Styling for the UI
│
├── Dockerfile                 # Container config
├── requirements.txt           # Python dependencies
└── eda_and_train.ipynb        # EDA + training notebook
```

---

## 📦 Tech Stack

- Python 3.11
- Sentence Transformers (`all-MiniLM-L6-v2`)
- XGBoost
- FastAPI + Jinja2
- Uvicorn
- Docker

---

## ✨ Future Improvements

- Add SHAP-based explainability to highlight impactful words
- Add upload interface for batch prompt classification
- Reduce Docker image size using model mounting or lightweight base images

---

## 👨‍💻 Author

Ron Salomon — AI Security & NLP Researcher

---

## 📄 License

MIT License