06/01/2025

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


-----------------------------------------------------------------------------------------------------------------------------
08/01/2025

# Mood Classification API

A simple FastAPI backend that classifies user mood based on text input.
Built to practice real backend engineering concepts such as API design,
validation, error handling, logging, and documentation.

---

## Tech Stack
- FastAPI
- Pydantic
- Uvicorn
- Streamlit (optional frontend)

---

## Features
- Health check endpoint
- Text-based mood prediction
- Request validation using Pydantic
- Proper error handling with HTTPException
- Basic logging for API calls
- Auto-generated Swagger documentation

---

## Project Structure
PyProjects/
│
├── backend/
│ ├── main.py # FastAPI app & routes
│ ├── schemas.py # Pydantic request models
│ └── init.py
│
├── docs/ # Swagger & API screenshots
├── app.py # Streamlit frontend (optional)
├── README.md
└── .gitignore

---

## API Endpoints
### GET /health
Checks if the API is