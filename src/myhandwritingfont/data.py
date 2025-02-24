import sqlite3

def init_database():
    conn = sqlite3.connect("characters.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS chars (
            char TEXT PRIMARY KEY,
            registered BOOLEAN DEFAULT 0,
            image_path TEXT
        )
    """)
    # ひらがな46文字を初期登録（未登録状態）
    hiragana = [chr(i) for i in range(0x3041, 0x3097) if 0x3041 <= i <= 0x3096]  # 「あ」〜「ん」
    for char in hiragana:
        c.execute("INSERT OR IGNORE INTO chars (char, registered, image_path) VALUES (?, 0, ?)", (char, None))
    conn.commit()
    conn.close()

def get_unregistered_chars():
    conn = sqlite3.connect("characters.db")
    c = conn.cursor()
    c.execute("SELECT char FROM chars WHERE registered = 0")
    chars = [row[0] for row in c.fetchall()]
    conn.close()
    return chars

if __name__ == "__main__":
    init_database()