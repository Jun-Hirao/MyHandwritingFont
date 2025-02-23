import tkinter as tk
from PIL import Image, ImageDraw
import io
import os

class DrawingCanvas:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)
        
        # 描画イベントをバインド
        self.canvas.bind("<Button-1>", self.start_draw)  # マウス押したとき
        self.canvas.bind("<B1-Motion>", self.draw)       # マウス動かしたとき
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)  # マウス離したとき
        self.last_x, self.last_y = None, None
        
        save_btn = tk.Button(master, text="保存", command=self.save_image)
        save_btn.pack()

        clear_btn = tk.Button(master, text="クリア", command=self.clear_canvas)
        clear_btn.pack()

    def clear_canvas(self):
        self.canvas.delete("all")
        self.last_x, self.last_y = None, None

    def start_draw(self, event):
        # 描画開始時の位置を記録（新しい線を開始）
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        # 線を描く（前の位置から現在の位置へ）
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=2, fill="black")
        self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        # 線を終了して次の線が繋がらないように位置をリセット
        self.last_x, self.last_y = None, None

    def save_image(self):
# 連番付きファイル名
        count = 1
        while os.path.exists(f"output/char_{count}.png"):
            count += 1
        ps = self.canvas.postscript(colormode="color")
        img = Image.open(io.BytesIO(ps.encode("utf-8")))
        img.save(f"output/char_{count}.png", "PNG")
        print(f"保存しました！（output/char_{count}.png）")