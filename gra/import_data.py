import sqlite3
import csv
from nltk.corpus import wordnet as wn
from datetime import datetime

def add_words_from_wordnet(filename, limit=100):
	conn = sqlite3.connect('vocabulary.db')
	cursor = conn.cursor()
	for synset in wn.all_synsets():
		for lemma in synset.lemmas():
			word = lemma.name()
			cursor.execute('SELECT id FROM words WHERE word = ?', (word,))
			if cursor.fetchone() is None:
				meaning = synset.definition()
				add_word(word, meaning)
				limit -= 1
				if limit <= 0:
					break
		if limit <= 0:
			break
	conn.commit()
	conn.close()

def add_word(word, meaning):
	conn = sqlite3.connect('vocabulary.db')
	cursor = conn.cursor()
	now_str = datetime.now().isoformat()
	cursor.execute('''
	INSERT INTO words (word, meaning, next_review_date)
	VALUES (?, ?, ?)
	''', (word, meaning, now_str))
	conn.commit()
	conn.close()

def import_words_from_csv(filename):
    conn = sqlite3.connect('vocabulary.db')
    cursor = conn.cursor()
    with open(filename, newline='', encoding='utf-8') as csvfile:
        word_reader = csv.reader(csvfile)
        for row in word_reader:
            if len(row) >= 2:
                word = row[0].strip()
                meaning = row[1].strip()
                cursor.execute('SELECT id FROM words WHERE word = ?', (word,))
                if cursor.fetchone() is None:
                    add_word(word, meaning)
    conn.commit()
    conn.close()


# データベースの初期化
conn = sqlite3.connect('vocabulary.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT NOT NULL,
    meaning TEXT NOT NULL,
    correct_count INTEGER DEFAULT 0,
    next_review_date TEXT,
    last_correct_date TEXT
)
''')
conn.commit()
conn.close()

# データのインポート
add_words_from_wordnet('vocabulary.csv')
import_words_from_csv('vocabulary.csv')
