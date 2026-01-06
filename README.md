# Mood Classification API

## Tech Stack
- FastAPI
- Pydantic
- Uvicorn
- Streamlit (optional frontend)

## Features
- Health check endpoint
- Text-based mood prediction API

## API Endpoints

### GET /health
Returns service status.

### POST /predict
Input:
{
  "text": "I feel happy today"
}

Output:
{
  "mood": "POSITIVE"
}

## Screenshots
See /docs folder for Swagger UI responses.