import tkinter as tk
from PIL import Image, ImageDraw
import os
import io

class DrawingCanvas:
    def __init__(self, master, initial_char=None):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)
        
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
        self.last_x, self.last_y = None, None
        
        save_btn = tk.Button(master, text="保存", command=self.save_image)
        save_btn.pack()
        clear_btn = tk.Button(master, text="クリア", command=self.clear_canvas)
        clear_btn.pack()

        # 初期文字があれば表示
        if initial_char:
            self.canvas.create_text(150, 150, text=initial_char, font=("Arial", 50))

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=2, fill="black")
        self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.last_x, self.last_y = None, None

    def save_image(self):
        if not os.path.exists("output"):
            os.makedirs("output")
        count = 1
        while os.path.exists(f"output/char_{count}.png"):
            count += 1
        ps = self.canvas.postscript(colormode="color")
        img = Image.open(io.BytesIO(ps.encode("utf-8")))
        img.save(f"output/char_{count}.png", "PNG")
        # 登録状況を更新（後で実装）
        print(f"保存したよ！（output/char_{count}.png）")