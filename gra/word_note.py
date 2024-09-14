import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3
from datetime import datetime, timedelta
import random

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

    
add_word('apple', 'りんご')
add_word('orange', 'オレンジ')
add_word('banana', 'バナナ')

def get_question():
    # 現在の日時をISOフォーマットの文字列で取得
    now_str = datetime.now().isoformat()
    cursor.execute('''
    SELECT * FROM words
    WHERE next_review_date <= ? OR next_review_date IS NULL
    ''', (now_str,))
    words = cursor.fetchall()
    if not words:
        messagebox.showinfo("お知らせ", "復習する単語はありません。")
        return None
    # ランダムに1つの単語を選択
    question_word = random.choice(words)
    # 選択肢を作成
    cursor.execute('SELECT meaning FROM words WHERE id != ?', (question_word[0],))
    all_meanings = [row[0] for row in cursor.fetchall()]
    choices = random.sample(all_meanings, min(3, len(all_meanings))) + [question_word[2]]
    random.shuffle(choices)
    return question_word, choices


def check_answer(question_word, selected_meaning):
    if question_word[2] == selected_meaning:
        # 正解した場合の処理
        correct_count = question_word[3] + 1
        # 次回の出題日時を設定
        if correct_count == 1:
            next_review = datetime.now() + timedelta(days=1)
        elif correct_count == 2:
            next_review = datetime.now() + timedelta(weeks=1)
        elif correct_count == 3:
            next_review = datetime.now() + timedelta(days=30)
        elif correct_count == 4:
            next_review = datetime.now() + timedelta(days=90)
        else:
            next_review = None  # 二度と出題しない

        now_str = datetime.now().isoformat()
        next_review_str = next_review.isoformat() if next_review else None

        cursor.execute('''
        UPDATE words
        SET correct_count = ?, next_review_date = ?, last_correct_date = ?
        WHERE id = ?
        ''', (correct_count, next_review_str, now_str, question_word[0]))
        conn.commit()
    else:
        # 不正解の場合の処理
        now_str = datetime.now().isoformat()
        cursor.execute('''
        UPDATE words
        SET next_review_date = ?
        WHERE id = ?
        ''', (now_str, question_word[0]))
        conn.commit()
    # 次の問題を出題
    start_quiz()


root = tk.Tk()
root.title("単語帳アプリ")

# 日本語対応フォントの設定
font = tkFont.Font(family='Yu Gothic', size=12)

def start_quiz():
    result = get_question()
    if result:
        question_word, choices = result
        question_label.config(text=f"次の単語の意味は？: {question_word[1]}", font=font)
        for i in range(len(choices)):
            choice_buttons[i]['text'] = choices[i]
            choice_buttons[i]['command'] = lambda meaning=choices[i]: check_answer(question_word, meaning)
            choice_buttons[i]['font'] = font
        for i in range(len(choices), 4):
            choice_buttons[i]['text'] = ""
            choice_buttons[i]['command'] = None

question_label = tk.Label(root, text="単語を覚えましょう！", font=font)
question_label.pack()

choice_buttons = []
for _ in range(4):
    btn = tk.Button(root, text="", width=50)
    btn.pack()
    choice_buttons.append(btn)

start_button = tk.Button(root, text="クイズを始める", command=start_quiz)
start_button.pack()

root.mainloop()
