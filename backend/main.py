from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from backend.utils import translate_word, generate_tts

app = FastAPI()

db = []  # In-memory storage

class Word(BaseModel):
    term: str
    translation: str = ""
    language: str

@app.post("/add")
async def add(word: Word):
    word.translation = await translate_word(word.term, word.language)
    
    # Save TTS for the English word
    generate_tts(word.term, "en", word.term)
    
    # Save TTS for the translated word
    generate_tts(word.translation, word.language, f"{word.term}_{word.language}")
    
    db.append(word.dict())
    return word

@app.get("/list", response_model=List[Word])
async def list_words():
    return db

@app.post("/reset")
async def reset():
    db.clear()
    return {"status": "cleared"}
