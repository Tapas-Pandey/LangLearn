# 🧠 Language Learning App

A simple language learning tool built with **FastAPI** and **Streamlit**. Users can add vocabulary words, get translations, and hear audio pronunciations via Text-to-Speech (TTS).

---

## ✨ Features

- 🔤 Add English words and get translations in other languages
- 🌍 Supports multiple target languages (Spanish, French, German, Italian, Japanese, Hindi)
- 🔊 Generates audio using TTS for both original and translated words
- 📋 View all added words
- ♻️ Reset vocabulary list

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **TTS:** gTTS (Google Text-to-Speech)
- **Translation:** LibreTranslate (or other free API)

---

## 🧪 How to Run Locally

## ⚙️ Installation

1️⃣ **Clone the Repository**
```sh
git clone https://github.com/SoyalIslam/Cosmic_classifier.git
cd Cosmic_classifier
```
2️⃣ Create a Virtual Environment (Optional but recommended)
```sh
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```
3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
4️⃣ Start the Backend
```sh
cd backend
uvicorn main:app --reload
```
5️⃣ Start the Frontend (in a new terminal)
```sh
cd frontend
streamlit run app.py
```
---
## 🔮 Future Enhancements

✅ Authentication System
Allow users to create accounts and save personal vocabulary lists securely.

🌐 Cloud Translation APIs
Integrate with services like Microsoft Translator or DeepL for higher accuracy and reliability.

🧠 Spaced Repetition Learning
Implement Anki-style review algorithms to optimize vocabulary retention.

🔊 Text-to-Speech for Translations
Add pronunciation support for translated words in target languages.

📈 Progress Tracking Dashboard
Show stats such as total words learned, quiz performance, and learning streaks.

🎮 Gamification Features
Include daily challenges, streaks, badges, and leaderboards to increase motivation.

📱 Mobile App Support
Build cross-platform mobile apps using React Native or Flutter for on-the-go learning.

🧩 Multi-language UI
Localize the app interface to support multiple languages for global accessibility.

🗃️ Export/Import Vocabulary Lists
Allow users to back up or share their vocabulary lists in CSV or PDF formats.


---
