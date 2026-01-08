import logging

from fastapi import FastAPI, HTTPException
from backend.schemas import TextInput

# --------------------
# Logging setup
# --------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --------------------
# App initialization
# --------------------
app = FastAPI(title="Mood Classification API")

# --------------------
# Routes
# --------------------
@app.get("/")
def root():
    return {"message": "Mood Classification API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: TextInput):
    logger.info("Predict endpoint called")
    logger.info(f"Input received length: {len(data.text)}")

    # Extra safety check
    if not data.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text input cannot be empty"
        )

    positive_words = ["happy", "great", "good", "excited", "awesome"]

    if any(word in data.text.lower() for word in positive_words):
        mood = "POSITIVE"
    else:
        mood = "NEUTRAL"

    return {"mood": mood}