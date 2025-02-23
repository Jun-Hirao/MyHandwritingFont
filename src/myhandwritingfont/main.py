import tkinter as tk
from drawing import DrawingCanvas

def main():
    root = tk.Tk()
    root.title("MyHandwritingFont")
    app = DrawingCanvas(root)
    root.mainloop()

if __name__ == "__main__":
    main()