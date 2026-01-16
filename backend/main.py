import logging
from fastapi import FastAPI, HTTPException
from backend.schemas import TextInput
from backend.db import get_connection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Mood Classification API")

@app.get("/")
def root():
    return {"message": "Mood Classification API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: TextInput):
    logger.info("Predict endpoint called")
    logger.info(f"Input received: {data.text}")

    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Text input cannot be empty")

    positive_words = ["happy", "great", "good", "excited", "awesome"]
    mood = "POSITIVE" if any(word in data.text.lower() for word in positive_words) else "NEUTRAL"

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO predictions (text, mood) VALUES (%s, %s)",
            (data.text, mood)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Failed to save prediction")

    return {"mood": mood}
