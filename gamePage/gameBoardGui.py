# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from pathlib import Path
from client import send_message

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def show_game_board_window(opponent, mode):
    global server_socket

    window = Tk()
    window.title("Game Board")

    # Define board and other elements
    board = [['' for _ in range(3)] for _ in range(3)]

    def make_move(row, col):
        import game.NormalMode.game_logic
        if game.NormalMode.game_logic.make_move(board, row, col, "X"):
            send_message(server_socket, f"MOVE:{row}:{col}")

    window.geometry("612x612")
    window.configure(bg="#FFFFFF")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the center position
    x_cordinate = int((screen_width / 2) - (612 / 2))
    y_cordinate = int((screen_height / 2) - (612 / 2))

    # Set the geometry of the window to the center of the screen
    window.geometry(f"612x612+{x_cordinate}+{y_cordinate}")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=612,
        width=612,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        306.0,
        306.0,
        image=image_image_1
    )

    label_opponent = Label(window, text=f"Opponent: {opponent}", font=("Helvetica", 14), bg="#FFFFFF")
    label_opponent.place(x=10, y=10)

    label_mode = Label(window, text=f"Mode: {mode}", font=("Helvetica", 14), bg="#FFFFFF")
    label_mode.place(x=10, y=40)

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=24.0,
        y=538.0,
        width=148.0,
        height=46.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=372.0,
        y=367.0,
        width=121.0,
        height=120.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=234.0,
        y=366.0,
        width=121.0,
        height=120.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=94.0,
        y=366.0,
        width=121.0,
        height=120.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=372.0,
        y=223.0,
        width=121.0,
        height=120.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=235.0,
        y=223.0,
        width=121.0,
        height=120.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=98.0,
        y=226.0,
        width=121.0,
        height=120.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=372.0,
        y=79.0,
        width=121.0,
        height=120.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=242.0,
        y=85.0,
        width=121.0,
        height=120.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    button_10.place(
        x=98.0,
        y=85.0,
        width=121.0,
        height=120.0
    )
    window.resizable(False, False)
    window.mainloop()
