import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3
from datetime import datetime, timedelta
import random
import csv
import json

# データベースに接続
conn = sqlite3.connect('vocabulary.db')
cursor = conn.cursor()

# テーブルの作成
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

def add_word(word, meaning):
    now_str = datetime.now().isoformat()
    cursor.execute('''
    INSERT INTO words (word, meaning, next_review_date)
    VALUES (?, ?, ?)
    ''', (word, meaning, now_str))
    conn.commit()

def import_words_from_csv(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        word_reader = csv.reader(csvfile)
        for row in word_reader:
            if len(row) >= 2:
                word = row[0].strip()
                meaning = row[1].strip()
                cursor.execute('SELECT id FROM words WHERE word = ?', (word,))
                if cursor.fetchone() is None:
                    add_word(word, meaning)

def import_words_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as jsonfile:
        words = json.load(jsonfile)
        for entry in words:
            word = entry.get('word', '').strip()
            meaning = entry.get('meaning', '').strip()
            if word and meaning:
                cursor.execute('SELECT id FROM words WHERE word = ?', (word,))
                if cursor.fetchone() is None:
                    add_word(word, meaning)

def get_question():
    now_str = datetime.now().isoformat()
    cursor.execute('''
    SELECT * FROM words
    WHERE (next_review_date <= ? OR next_review_date IS NULL) AND correct_count < 5
    ''', (now_str,))
    words = cursor.fetchall()
    if not words:
        messagebox.showinfo("お知らせ", "復習する単語はありません。")
        return None
    question_word = random.choice(words)
    cursor.execute('SELECT meaning FROM words WHERE id != ?', (question_word[0],))
    all_meanings = [row[0] for row in cursor.fetchall()]
    choices = random.sample(all_meanings, min(3, len(all_meanings))) + [question_word[2]]
    random.shuffle(choices)
    return question_word, choices

def check_answer(question_word, selected_meaning):
    if question_word[2] == selected_meaning:
        messagebox.showinfo("正解", "おめでとうございます！")
        correct_count = question_word[3] + 1
        if correct_count == 1:
            next_review = datetime.now() + timedelta(days=1)
        elif correct_count == 2:
            next_review = datetime.now() + timedelta(weeks=1)
        elif correct_count == 3:
            next_review = datetime.now() + timedelta(days=30)
        elif correct_count == 4:
            next_review = datetime.now() + timedelta(days=90)
        else:
            next_review = None
        now_str = datetime.now().isoformat()
        next_review_str = next_review.isoformat() if next_review else None
        cursor.execute('''
        UPDATE words
        SET correct_count = ?, next_review_date = ?, last_correct_date = ?
        WHERE id = ?
        ''', (correct_count, next_review_str, now_str, question_word[0]))
        conn.commit()
    else:
        messagebox.showerror("不正解", "残念！もう一度挑戦しましょう。")
        now_str = datetime.now().isoformat()
        cursor.execute('''
        UPDATE words
        SET next_review_date = ?, correct_count = ?
        WHERE id = ?
        ''', (now_str, 0, question_word[0]))
        conn.commit()
    start_quiz()

root = tk.Tk()
root.title("単語帳アプリ")

# 日本語対応フォントの設定
font = tkFont.Font(family='Noto Sans CJK JP', size=12)

def start_quiz():
    result = get_question()
    if result:
        question_word, choices = result
        question_label.config(text=f"次の単語の意味は？: {question_word[1]}", font=font)
        for i in range(len(choices)):
            choice_buttons[i]['text'] = choices[i]
            choice_buttons[i]['command'] = lambda meaning=choices[i]: check_answer(question_word, meaning)
            choice_buttons[i]['font'] = font
            choice_buttons[i]['state'] = 'normal'
        for i in range(len(choices), 4):
            choice_buttons[i]['text'] = ""
            choice_buttons[i]['command'] = None
            choice_buttons[i]['state'] = 'disabled'
    else:
        question_label.config(text="現在、出題する単語はありません。", font=font)
        for btn in choice_buttons:
            btn['text'] = ""
            btn['command'] = None
            btn['state'] = 'disabled'

def open_add_word_window():
    add_window = tk.Toplevel(root)
    add_window.title("新しい単語を追加")

    tk.Label(add_window, text="単語:", font=font).grid(row=0, column=0)
    tk.Label(add_window, text="意味:", font=font).grid(row=1, column=0)

    word_entry = tk.Text(add_window, height=1, width=30, font=font)
    meaning_entry = tk.Text(add_window, height=4, width=30, font=font)
    word_entry.grid(row=0, column=1)
    meaning_entry.grid(row=1, column=1)

 	# フォーカスを設定
    word_entry.focus_set()

    def save_word():
        word = word_entry.get("1.0", "end-1c").strip()
        meaning = meaning_entry.get("1.0", "end-1c").strip()
        
        if word and meaning:
            cursor.execute('SELECT id FROM words WHERE word = ?', (word,))
            if cursor.fetchone() is None:
                add_word(word, meaning)
                messagebox.showinfo("成功", "単語が追加されました。")
                add_window.destroy()
            else:
                messagebox.showwarning("警告", "この単語は既に存在します。")
        else:
            messagebox.showwarning("警告", "単語と意味を入力してください。")

    save_button = tk.Button(add_window, text="保存", command=save_word, font=font)
    save_button.grid(row=2, column=0, columnspan=2)

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

# アプリケーション開始時に語彙をインポート
import_words_from_csv('vocabulary.csv')
# import_words_from_json('vocabulary.json')

root.mainloop()
