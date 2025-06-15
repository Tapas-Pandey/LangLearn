from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from backend.utils import translate_word,save_pronunciation

app = FastAPI()

db = []  # in-memory storage

class Word(BaseModel):
    term: str
    translation: str = ""
    language: str

