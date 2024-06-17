import tkinter as tk
from pynput import mouse

class ClickCoordinatesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Coordinates")
        self.label = tk.Label(root, text="Click anywhere inside this window", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.coord_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.coord_label.pack(pady=20)

        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def on_click(self, x, y, button, pressed):
        if pressed:
            relative_x = x - self.root.winfo_rootx()
            relative_y = y - self.root.winfo_rooty()
            if 0 <= relative_x <= self.root.winfo_width() and 0 <= relative_y <= self.root.winfo_height():
                self.coord_label.config(text=f'Clicked at (X: {relative_x}, Y: {relative_y})')

    def on_close(self):
        self.listener.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCoordinatesApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.geometry("400x300")
    root.mainloop()
