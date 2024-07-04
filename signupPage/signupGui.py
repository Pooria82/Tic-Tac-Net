# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, Toplevel, Label
from pathlib import Path
import os
import re
import jwt
import dotenv
import hashlib
from Database import db_helper
from signupPage import captcha_helper

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")
dotenv.load_dotenv(Path(OUTPUT_PATH, '..', 'SECRETKEY', 'SECRET_KEY.env'))
SECRET_KEY = os.getenv("SECRET_KEY")


def open_login_page():
    window.destroy()
    import loginPage.loginGui
    loginPage.loginGui.show_login_window()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def show_signup_window():
    global window, entry_1, entry_2, entry_3, entry_4  # *** changed ***
    window = Tk()
    window.title("Sign Up")

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
        76.0,
        101.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        676.0,
        101.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        189.0,
        724.9953052699082,
        295.0000228881836,
        726.0,
        fill="#761818",
        outline="")

    canvas.create_rectangle(
        443.0,
        725.0,
        554.0,
        726.0,
        fill="#761818",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_login_page,
        relief="flat"
    )
    button_1.place(
        x=295.0,
        y=707.0,
        width=149.0,
        height=38.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=on_signup_button_click,
        relief="flat"
    )
    button_2.place(
        x=190.0,
        y=642.0,
        width=364.0,
        height=52.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        372.0,
        596.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFD1D1",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=203.0,
        y=570.0,
        width=338.0,
        height=50.0
    )

    canvas.create_text(
        225.0,
        548.0,
        anchor="nw",
        text="Repeat password",
        fill="#1C1C1C",
        font=("Poppins Regular", 12 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        209.0,
        555.0,
        image=image_image_4
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        372.0,
        506.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFD1D1",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=203.0,
        y=480.0,
        width=338.0,
        height=50.0
    )

    canvas.create_text(
        225.0,
        458.0,
        anchor="nw",
        text="Create Password",
        fill="#1C1C1C",
        font=("Poppins Regular", 12 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        208.0,
        464.0,
        image=image_image_5
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        372.0,
        419.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFD1D1",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=203.0,
        y=393.0,
        width=338.0,
        height=50.0
    )

    canvas.create_text(
        225.0,
        372.0,
        anchor="nw",
        text="Email address",
        fill="#1C1C1C",
        font=("Poppins Regular", 12 * -1)
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        208.0,
        378.0,
        image=image_image_6
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        372.0,
        332.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFD1D1",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=203.0,
        y=306.0,
        width=338.0,
        height=50.0
    )

    canvas.create_text(
        225.0,
        288.0,
        anchor="nw",
        text="Username",
        fill="#1C1C1C",
        font=("Poppins Regular", 12 * -1)
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        208.0,
        289.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        371.0,
        221.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        372.0,
        101.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        1110.0,
        425.0,
        image=image_image_10
    )
    window.resizable(False, False)
    window.mainloop()


def on_signup_button_click():
    global window
    global entry_1, entry_2, entry_3, entry_4

    # Validate input fields
    username = entry_4.get()
    email = entry_3.get()
    password = entry_2.get()
    repeat_password = entry_1.get()

    # username is 4-20 characters long
    # no _ or . at the beginning
    # no __ or _. or ._ or .. inside
    # [a-zA-Z0-9._] =>  allowed characters
    # no _ or . at the end
    username_regex = r"^(?=[a-zA-Z0-9._]{4,20}$)(?!.*[_.]{2})[^_.].*[^_.]$"
    # General Email Regex (RFC 5322 Official Standard)
    email_regex = r"^(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$"
    # Minimum eight characters
    # at least one uppercase letter, one lowercase letter, one number and one special character
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if not username:
        messagebox.showerror("Error", "Username is required")
        return

    if not re.match(username_regex, username):
        messagebox.showerror("Error", "Invalid username format")
        return

    if not email:
        messagebox.showerror("Error", "Email address is required")
        return

    if not re.match(email_regex, email):
        messagebox.showerror("Error", "Invalid email format")
        return

    if not password:
        messagebox.showerror("Error", "Password is required")
        return

    if not re.match(password_regex, password):
        messagebox.showerror("Error",
                             "The password must contain at least 8 characters:\nAt least one UPPERCASE Letter, one lowercase letter, one Number and one Special character.")
        return

    if not repeat_password:
        messagebox.showerror("Error", "Repeat password is required")
        return

    if password != repeat_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    if not db_helper.is_unique_username(username):
        messagebox.showerror("Error", "Username already exists")
        return

    if not db_helper.is_unique_email(email):
        messagebox.showerror("Error", "This Email has already been registered.")
        return

    def generate_and_show_captcha():
        global captcha_text, captcha_image_path
        captcha_text, captcha_image_path = captcha_helper.generate_captcha()

        popup = Toplevel(window)
        popup.title("CAPTCHA Verification")
        popup.geometry("400x250")

        # Center the popup window
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        popup_width = 400
        popup_height = 250
        position_right = int(window.winfo_x() + (window_width / 2) - (popup_width / 2))
        position_down = int(window.winfo_y() + (window_height / 2) - (popup_height / 2))
        popup.geometry(f"{popup_width}x{popup_height}+{position_right}+{position_down}")

        captcha_image = PhotoImage(file=captcha_image_path)
        captcha_image_label = Label(popup, image=captcha_image)
        captcha_image_label.image = captcha_image
        captcha_image_label.pack(pady=10)

        entry_captcha = Entry(popup, font=("Helvetica", 14))
        entry_captcha.pack(pady=10)

        def on_verify():
            user_captcha_input = entry_captcha.get()
            if captcha_helper.validate_captcha(user_captcha_input, captcha_text):
                # Proceed with sign-up logic
                try:
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    db_helper.save_user_to_db(username, email, hashed_password)
                    token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
                    with open('token.txt', 'w') as f:
                        f.write(token)
                    messagebox.showinfo("Success", "Signup successful!")
                    os.remove(captcha_image_path)
                    popup.destroy()
                    open_login_page()
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")
            else:
                messagebox.showerror("Error", "Invalid CAPTCHA")
                os.remove(captcha_image_path)
                popup.destroy()
                generate_and_show_captcha()

        verify_button = Button(popup, text="Verify", font=("Helvetica", 14), command=on_verify)
        verify_button.pack(pady=20)

    generate_and_show_captcha()


if __name__ == "__main__":
    show_signup_window()
