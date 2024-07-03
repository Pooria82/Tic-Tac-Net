# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from dotenv import load_dotenv
import jwt
import os
import loginPage.loginGui

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def exit_to_login():
    window.destroy()
    loginPage.loginGui.show_login_window()


def show_menu_window():
    global window
    window = Tk()
    window.title("Menu")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(base_dir, '..', 'images', 'newGameIcon.png')
    window.iconphoto(False, PhotoImage(file=icon_path))

    window.geometry("1400x800")
    window.configure(bg="#FFFFFF")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the center position
    x_cordinate = int((screen_width / 2) - (1400 / 2))
    y_cordinate = int((screen_height / 2) - (800 / 2))

    # Set the geometry of the window to the center of the screen
    window.geometry(f"1400x800+{x_cordinate}+{y_cordinate}")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=800,
        width=1400,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        700.0,
        400.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        582.0,
        119.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        582.0,
        242.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        120.0,
        702.4991077582673,
        266.67311096191406,
        703.50634765625,
        fill="#761818",
        outline="")

    canvas.create_rectangle(
        473.0,
        703.0,
        626.0,
        704.0,
        fill="#761818",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=exit_to_login,
        relief="flat"
    )
    button_1.place(
        x=266.67303466796875,
        y=674.0,
        width=206.71702575683594,
        height=57.99998092651367
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
        x=121.0,
        y=560.67529296875,
        width=505.0,
        height=77.98226928710938
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
        x=121.0,
        y=446.337646484375,
        width=505.0,
        height=77.98226928710938
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
        x=121.0,
        y=332.0,
        width=505.0,
        height=77.98226928710938
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        284.0,
        176.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        1043.0,
        404.0,
        image=image_image_5
    )
    window.resizable(False, False)
    window.mainloop()
