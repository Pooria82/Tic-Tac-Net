# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, Toplevel, Label, Frame, Listbox
from pathlib import Path
import dotenv
import jwt
import os
import client

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")
dotenv.load_dotenv(Path(OUTPUT_PATH, '..', 'SECRETKEY', 'SECRET_KEY.env'))
SECRET_KEY = os.getenv("SECRET_KEY")

online_users_listbox = None


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def validate_token():
    try:
        with open('token.txt', 'r') as f:
            token = f.read()
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except Exception as e:
        messagebox.showerror("Error", "Invalid or expired token")
        exit_to_login()


def exit_to_login():
    try:
        os.remove('token.txt')
    except FileNotFoundError:
        pass
    window.destroy()
    import loginPage.loginGui
    loginPage.loginGui.show_login_window()


def on_closing():
    exit_to_login()


def open_game_mode_popup():
    popup = Toplevel(window)
    popup.title("Select Game Mode")
    popup.geometry("300x150")
    popup.configure(bg="#333333")

    label = Label(popup, text="SELECT GAME MODE", font=("Helvetica", 14, "bold"), bg="#333333", fg="#FFFFFF")
    label.pack(pady=10)

    normal_mode_button = Button(popup, text="NormalMode", font=("Helvetica", 12), bg="#4CAF50", fg="#FFFFFF",
                                relief="flat", command=lambda: select_mode("Normal", popup))
    normal_mode_button.pack(pady=5)

    hard_mode_button = Button(popup, text="HardMode", font=("Helvetica", 12), bg="#F44336", fg="#FFFFFF",
                              relief="flat", command=lambda: select_mode("Hard", popup))
    hard_mode_button.pack(pady=5)

    # Center the popup window
    popup.update_idletasks()
    window_width = popup.winfo_width()
    window_height = popup.winfo_height()
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    position_right = int(screen_width / 2 - window_width / 2)
    position_down = int(screen_height / 2 - window_height / 2)
    popup.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")


def select_mode(mode, popup):
    popup.destroy()
    show_user_list_popup(mode)


def get_available_users():  # TODO : Handle clients
    # return ["user1", "user2", "user3", "user4"]
    client.fetch_users()


def show_user_list_popup(mode):
    popup = Toplevel(window)
    popup.title("Select Opponent")
    popup.geometry("300x400")
    popup.configure(bg="#333333")

    label = Label(popup, text="SELECT OPPONENT", font=("Helvetica", 14, "bold"), bg="#333333", fg="#FFFFFF")
    label.pack(pady=10)

    global online_users_listbox
    online_users_listbox = Listbox(popup, font=("Helvetica", 12), bg="#761818", fg="#FFFFFF", relief="flat")
    online_users_listbox.pack(pady=5, fill='x')

    get_available_users()

    # Center the popup window
    popup.update_idletasks()
    window_width = popup.winfo_width()
    window_height = popup.winfo_height()
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    position_right = int(screen_width / 2 - window_width / 2)
    position_down = int(screen_height / 2 - window_height / 2)
    popup.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

    online_users_listbox.bind("<Double-1>", lambda event: start_game(online_users_listbox.get(online_users_listbox.curselection()), mode, popup))


def update_online_users(users):
    global online_users_listbox
    if online_users_listbox:
        online_users_listbox.delete(0, 'end')
        for user in users:
            online_users_listbox.insert('end', user)


def start_game(opponent, mode, popup):
    popup.destroy()
    window.destroy()
    import gamePage.gameBoardGui
    gamePage.gameBoardGui.show_game_board_window(opponent, mode)


def show_menu_window():
    global window
    window = Tk()
    window.title("Menu")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(base_dir, '..', 'Images', 'newGameIcon.png')
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

    window.protocol("WM_DELETE_WINDOW", on_closing)

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
        command=open_game_mode_popup,
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
    validate_token()
    client.start_receiving_thread()
    window.mainloop()
