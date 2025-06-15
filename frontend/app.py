import streamlit as st
import httpx
import os
import random

API_URL = "http://localhost:8000"
AUDIO_DIR = "D:\\2025-Vacation\\project\\langlearn\\data"

st.title("🧠 Language Learning App")

# ----------------------------
# 📥 Add Word Section
# ----------------------------
st.subheader("Add a New Word")
term = st.text_input("Word (in English):")
lang = st.selectbox("Translate to:", ["es", "fr", "de", "it", "ja", "hi"])

if st.button("Translate & Add"):
    if term.strip():
        with st.spinner("Translating and generating audio..."):
            try:
                response = httpx.post(f"{API_URL}/add", json={
                    "term": term.strip(),
                    "translation": "",
                    "language": lang
                })
                response.raise_for_status()
                data = response.json()

                st.success(f"Translated: {data['term']} → {data['translation']}")

                # Play English TTS
                audio_file_en = os.path.join(AUDIO_DIR, f"{term}.mp3")
                if os.path.exists(audio_file_en):
                    st.audio(open(audio_file_en, "rb").read(), format="audio/mp3")

                # Play translated TTS
                audio_file_trans = os.path.join(AUDIO_DIR, f"{term}_{lang}.mp3")
                if os.path.exists(audio_file_trans):
                    st.audio(open(audio_file_trans, "rb").read(), format="audio/mp3")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a word.")

# ----------------------------
# 📋 Vocabulary Table
# ----------------------------
st.subheader("📋 Vocabulary List")
if st.button("Show All Words"):
    try:
        r = httpx.get(f"{API_URL}/list")
        r.raise_for_status()
        data = r.json()
        if data:
            st.table(data)
        else:
            st.info("No words added yet.")
    except Exception as e:
        st.error(f"Failed to fetch word list: {e}")

# ----------------------------
# 🧹 Reset
# ----------------------------
if st.button("Reset All"):
    try:
        r = httpx.post(f"{API_URL}/reset")
        r.raise_for_status()
        st.success("All words cleared!")
    except Exception as e:
        st.error(f"Failed to reset: {e}")

# ----------------------------
# 📝 Quiz Mode
# ----------------------------
st.subheader("📝 Quiz Mode")

if st.button("Start Quiz"):
    try:
        r = httpx.get(f"{API_URL}/list")
        r.raise_for_status()
        words = r.json()

        if not words:
            st.info("Add some words first.")
        else:
            q_word = random.choice(words)
            with st.form(key="quiz_form"):
                user_input = st.text_input(f"What is '{q_word['term']}' in {q_word['language']}?")
                submit = st.form_submit_button("Submit")

                if submit:
                    correct = q_word['translation'].strip().lower()
                    if user_input.strip().lower() == correct:
                        st.success("Correct! 🎉")
                    else:
                        st.error(f"Wrong. Correct answer: {q_word['translation']}")
    except Exception as e:
        st.error(f"Quiz error: {e}")
