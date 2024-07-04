import tkinter as tk
from PIL import Image, ImageTk

background_image_path = "../Images/istockphoto-1214544890-612x612.jpg"
x_image_path = "../Images/X_prev_ui.png"
o_image_path = "../Images/O_prev_ui.png"

BOARD_SIZE = 3


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # بارگذاری تصاویر
        self.background_image = ImageTk.PhotoImage(Image.open(background_image_path))
        self.x_image = ImageTk.PhotoImage(Image.open(x_image_path).resize((100, 100)))
        self.o_image = ImageTk.PhotoImage(Image.open(o_image_path).resize((100, 100)))

        # ساخت بورد بازی
        self.canvas = tk.Canvas(root, width=self.background_image.width(), height=self.background_image.height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # ذخیره وضعیت بازی
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

        # مختصات گوشه‌های مربع‌ها
        self.coordinates = [
            [(0, 0), (200, 0), (400, 0)],
            [(0, 200), (200, 200), (400, 200)],
            [(0, 400), (200, 400), (400, 400)]
        ]

        # اضافه کردن دکمه‌های نامرئی
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', command=lambda i=i, j=j: self.on_button_click(i, j))
                button.place(x=self.coordinates[i][j][0], y=self.coordinates[i][j][1], width=200, height=200)
                button.config(bg='light gray', highlightthickness=0, bd=0)
                button.lift()
                self.buttons[i][j] = button

    def on_button_click(self, i, j):
        if self.board[i][j] is None:
            x, y = self.coordinates[i][j]
            if self.current_player == 'X':
                self.board[i][j] = self.canvas.create_image(x + 100, y + 100, image=self.x_image)
                self.current_player = 'O'
            else:
                self.board[i][j] = self.canvas.create_image(x + 100, y + 100, image=self.o_image)
                self.current_player = 'X'


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
