import httpx
from gtts import gTTS
import os
from urllib.parse import quote
async def translate_word(text: str, target_lang: str) -> str:
    source_lang = "en"
    encoded_text = quote(text)
    url = f"https://lingva.ml/api/v1/{source_lang}/{target_lang}/{encoded_text}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get("translation", "Translation not found")
    except Exception as e:
        raise ValueError(f"Translation failed: {e}")


def generate_tts(text: str, lang: str, filename: str):
    tts = gTTS(text=text, lang=lang)
    path = f"data/{filename}.mp3"
    os.makedirs("data", exist_ok=True)
    tts.save(path)
    return path