from tkinter import messagebox
from client import send_invite, send_invite_response
from gamePage.gameBoardGui import show_game_board_window
from menuPage.menuGui import update_online_users


class InviteHandler:
    def __init__(self, client):
        self.client = client
        self.client.set_invite_callback(self.on_invite_received)
        self.client.set_response_callback(self.on_response_received)

    def send_invite(self, opponent_username):
        send_invite(opponent_username)
        messagebox.showinfo("Invite Sent", f"Invite sent to {opponent_username}")

    def on_invite_received(self, invite_data):
        opponent_username = invite_data["from"]
        response = messagebox.askyesno("Game Invite",
                                       f"{opponent_username} has invited you to play Tic-Tac-Toe. Do you accept?")
        if response:
            self.accept_invite(opponent_username)
        else:
            self.reject_invite(opponent_username)

    def accept_invite(self, opponent_username):
        send_invite_response(opponent_username, "ACCEPT")
        show_game_board_window(self.client.username, opponent_username, "TicTacToe")

    def reject_invite(self, opponent_username):
        send_invite_response(opponent_username, "REJECT")

    def on_response_received(self, response_data):
        if response_data["response"] == "accept":
            opponent_username = response_data["from"]
            messagebox.showinfo("Invite Accepted", f"{opponent_username} has accepted your invite. Starting game...")
            show_game_board_window(self.client.username, opponent_username, "TicTacToe")
        else:
            opponent_username = response_data["from"]
            messagebox.showinfo("Invite Rejected", f"{opponent_username} has rejected your invite.")


if __name__ == "__main__":
    client = Client("username", "secret_key")
    invite_handler = InviteHandler(client)
    invite_handler.send_invite("opponent_username")
