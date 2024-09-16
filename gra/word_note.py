import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3
from datetime import datetime, timedelta
import random

root = tk.Tk()
root.title("単語帳アプリ")

# 日本語対応フォントの設定
font = tkFont.Font(family='Noto Sans CJK JP', size=12)

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

def get_question():
	conn = sqlite3.connect('vocabulary.db')
	cursor = conn.cursor()
	cursor.execute('''
	SELECT id, word, meaning
	FROM words
	WHERE next_review_date <= ?
	ORDER BY RANDOM()
	LIMIT 1
	''', (datetime.now().isoformat(),))
	row = cursor.fetchone()
	conn.close()
	if row is None:
		return None
	return {'id': row[0], 'word': row[1], 'meaning': row[2]}

def check_answer(question_word, selected_meaning):
	conn = sqlite3.connect('vocabulary.db')
	cursor = conn.cursor()
	cursor.execute('''
	SELECT meaning
	FROM words
	WHERE word = ?
	''', (question_word,))
	correct_meaning = cursor.fetchone()[0]
	conn.close()
	return selected_meaning == correct_meaning

def start_quiz():
	question = get_question()
	if question is None:
		messagebox.showinfo('お知らせ', '復習すべき単語がありません')
		return
	question_label['text'] = question['word']
	meanings = [question['meaning']]
	conn = sqlite3.connect('vocabulary.db')
	cursor = conn.cursor()
	cursor.execute('''
	SELECT meaning
	FROM words
	WHERE word != ?
	ORDER BY RANDOM()
	LIMIT 3
	''', (question['word'],))
	for row in cursor.fetchall():
		meanings.append(row[0])
	conn.close()
	random.shuffle(meanings)
	for btn, meaning in zip(choice_buttons, meanings):
		btn['text'] = meaning
		btn['state'] = 'normal'

def open_add_word_window():
	add_word_window = tk.Toplevel(root)
	add_word_window.title("新しい単語の追加")
	add_word_window.geometry("400x200")
	add_word_window.resizable(False, False)

	word_label = tk.Label(add_word_window, text="単語", font=font)
	word_label.pack()

	word_entry = tk.Entry(add_word_window, font=font)
	word_entry.pack()

	meaning_label = tk.Label(add_word_window, text="意味", font=font)
	meaning_label.pack()

	meaning_entry = tk.Entry(add_word_window, font=font)
	meaning_entry.pack()

	def add_word_and_close_window():
		word = word_entry.get()
		meaning = meaning_entry.get()
		add_word(word, meaning)
		add_word_window.destroy()

	add_button = tk.Button(add_word_window, text="追加", command=add_word_and_close_window, font=font)
	add_button.pack()

question_label = tk.Label(root, text="単語を覚えましょう！", font=font)
question_label.pack()

choice_buttons = []
for _ in range(4):
    btn = tk.Button(root, text="", width=50, font=font, state='disabled')
    btn.pack(pady=5)
    choice_buttons.append(btn)

start_button = tk.Button(root, text="クイズを始める", command=start_quiz, font=font)
start_button.pack(pady=5)

add_word_button = tk.Button(root, text="新しい単語を追加", command=open_add_word_window, font=font)
add_word_button.pack(pady=5)

root.mainloop()
