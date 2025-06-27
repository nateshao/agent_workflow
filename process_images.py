import os
import requests
import sqlite3
from datetime import datetime
from PIL import Image
from io import BytesIO

REMOVE_BG_API_KEY = "YOUR_REMOVE_BG_KEY"  # 替换为你的 remove.bg API Key
INPUT_DIR = "images/input"
OUTPUT_DIR = "images/output"
BG_PATH = "images/background/bg.jpg"
DB_PATH = "db.sqlite3"
NOTIFY_URL = "http://localhost:8000/api/notify-bg-done"

def remove_bg(image_path):
    with open(image_path, 'rb') as f:
        response = requests.post(
            "https://api.remove.bg/v1.0/removebg",
            files={'image_file': f},
            data={'size': 'auto'},
            headers={'X-Api-Key': REMOVE_BG_API_KEY},
        )
    if response.status_code == 200:
        return response.content
    else:
        print(f"remove.bg error: {response.text}")
        return None

def overlay_bg(fg_bytes, bg_path, out_path):
    fg = Image.open(BytesIO(fg_bytes)).convert("RGBA")
    bg = Image.open(bg_path).convert("RGBA").resize(fg.size)
    bg.paste(fg, (0, 0), fg)
    bg.save(out_path)

def save_to_db(original, newfile):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS processed_images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_filename TEXT,
        new_filename TEXT,
        created_at TEXT
    )''')
    c.execute('INSERT INTO processed_images (original_filename, new_filename, created_at) VALUES (?, ?, ?)',
              (original, newfile, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def notify_project(data):
    try:
        requests.post(NOTIFY_URL, json=data)
    except Exception as e:
        print("Notify error:", e)

if __name__ == "__main__":
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(BG_PATH), exist_ok=True)
    for fname in os.listdir(INPUT_DIR):
        if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        in_path = os.path.join(INPUT_DIR, fname)
        out_path = os.path.join(OUTPUT_DIR, fname)
        fg_bytes = remove_bg(in_path)
        if fg_bytes:
            overlay_bg(fg_bytes, BG_PATH, out_path)
            save_to_db(fname, out_path)
            notify_project({
                "original_filename": fname,
                "new_filename": out_path,
                "created_at": datetime.now().isoformat()
            })
            print(f"Processed: {fname} -> {out_path}") 