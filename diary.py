# 📄 File: diary.py — Diary module for PAF

def write_entry(message, filename="diary.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def read_diary(filename="diary.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Diary is empty."
