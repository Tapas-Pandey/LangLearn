import sqlite3

def init_db():
    conn = sqlite3.connect("data/words.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS words
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  term TEXT,
                  translation TEXT,
                  language TEXT)''')
    conn.commit()
    conn.close()

def add_word(term, translation, language):
    conn = sqlite3.connect("data/words.db")
    c = conn.cursor()
    c.execute("INSERT INTO words (term, translation, language) VALUES (?, ?, ?)", (term, translation, language))
    conn.commit()
    conn.close()

def get_all_words():
    conn = sqlite3.connect("data/words.db")
    c = conn.cursor()
    c.execute("SELECT term, translation, language FROM words")
    rows = c.fetchall()
    conn.close()
    return rows
