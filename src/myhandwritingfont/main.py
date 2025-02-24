import tkinter as tk
from drawing import DrawingCanvas
from data import init_database, get_unregistered_chars

def main():
    root = tk.Tk()
    root.title("MyHandwritingFont")

    # データベース初期化
    init_database()

    # フレームワーク表示（Listbox）
    frame = tk.Frame(root)
    frame.pack(pady=10)

    listbox = tk.Listbox(frame, height=10, width=20)
    listbox.pack(side=tk.LEFT, padx=5)

    # 未登録のひらがなを取得してListboxに追加
    unregistered_chars = get_unregistered_chars()
    for char in unregistered_chars:
        listbox.insert(tk.END, char)

    # キャンバス部分
    app = DrawingCanvas(root, initial_char=None)  # 初期文字はNone

    # 文字を選択したらキャンバスに表示
    def on_select(event):
        if listbox.curselection():
            selected_char = listbox.get(listbox.curselection())
            app.clear_canvas()  # キャンバスをクリア
            # ここでは仮に文字をキャンバスに描画（後で手書きに変更）
            app.canvas.create_text(150, 150, text=selected_char, font=("Arial", 50))

    listbox.bind("<<ListboxSelect>>", on_select)

    root.mainloop()

if __name__ == "__main__":
    main()