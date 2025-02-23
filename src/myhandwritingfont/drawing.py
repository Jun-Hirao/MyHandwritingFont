import tkinter as tk
from PIL import Image, ImageDraw
import io
import os

class DrawingCanvas:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)
        
        self.canvas.bind("<B1-Motion>", self.draw)
        self.last_x, self.last_y = None, None
        
        save_btn = tk.Button(master, text="保存", command=self.save_image)
        save_btn.pack()

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=2, fill="black")
        self.last_x, self.last_y = event.x, event.y

    def save_image(self):
        if not os.path.exists("output"):
            os.makedirs("output")
        ps = self.canvas.postscript(colormode="color")
        img = Image.open(io.BytesIO(ps.encode("utf-8")))
        img.save("output/char.png", "PNG")
        print("保存しました！")
