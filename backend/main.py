from fastapi import FastAPI
from backend.schemas import TextInput

app = FastAPI(title="Mood Classification API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: TextInput):
    positive_words = ["happy", "great", "good", "excited", "awesome"]

    if any(word in data.text.lower() for word in positive_words):
        mood = "POSITIVE"
    else:
        mood = "NEUTRAL"

    return {"mood": mood}