from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import signupPage.signupGui
import db_helper

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def open_signup_page():
    window.destroy()
    signupPage.signupGui.show_signup_window()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def on_login_button_click():
    username = entry_2.get()
    password = entry_1.get()

    if not username:
        messagebox.showerror("Error", "Username is required")
        return

    if not password:
        messagebox.showerror("Error", "Password is required")
        return

    if db_helper.validate_login(username, password):
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")


def show_login_window():
    global window, entry_1, entry_2
    window = Tk()

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
        350.0,
        725.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        351.0,
        635.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        170.0,
        559.9953052699082,
        276.0000228881836,
        561.0,
        fill="#761818",
        outline="")

    canvas.create_rectangle(
        424.0,
        560.0,
        535.0,
        561.0,
        fill="#761818",
        outline="")

    canvas.create_text(
        212.0,
        388.0,
        anchor="nw",
        text="Password",
        fill="#1C1C1C",
        font=("Poppins Regular", 12 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        196.0,
        394.0,
        image=image_image_4
    )

    canvas.create_text(
        212.0,
        296.0,
        anchor="nw",
        text="Username",
        fill="#1C1C1C",
        font=("Poppins Regular", 12 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        195.0,
        297.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        1035.0,
        399.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        350.0,
        227.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        351.0,
        96.0,
        image=image_image_8
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_signup_page,
        relief="flat"
    )
    button_1.place(
        x=276.0,
        y=542.0,
        width=149.0,
        height=38.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=on_login_button_click,
        relief="flat"
    )
    button_2.place(
        x=176.5,
        y=485.5,
        width=364.0,
        height=52.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        359.0,
        436.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFD1D1",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=190.0,
        y=410.0,
        width=338.0,
        height=50.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        353.0,
        345.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFD1D1",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=184.0,
        y=319.0,
        width=338.0,
        height=50.0
    )
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    show_login_window()
