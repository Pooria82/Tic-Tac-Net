from tkinter import messagebox
from client import Client
from Database.db_helper import save_game_to_db


class InviteHandler:
    def __init__(self, client):
        self.client = client
        self.client.set_invite_callback(self.on_invite_received)
        self.client.set_response_callback(self.on_response_received)

    def send_invite(self, opponent_username):
        invite_data = {
            "type": "invite",
            "to": opponent_username,
            "from": self.client.username
        }
        self.client.send_message(invite_data)
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
        response_data = {
            "type": "response",
            "to": opponent_username,
            "from": self.client.username,
            "response": "accept"
        }
        self.client.send_message(response_data)

        from gamePage.gameBoardGui import show_game_board_window
        show_game_board_window(self.client.username, opponent_username, "TicTacToe")

    def reject_invite(self, opponent_username):
        response_data = {
            "type": "response",
            "to": opponent_username,
            "from": self.client.username,
            "response": "reject"
        }
        self.client.send_message(response_data)

    def on_response_received(self, response_data):
        if response_data["response"] == "accept":
            opponent_username = response_data["from"]
            messagebox.showinfo("Invite Accepted", f"{opponent_username} has accepted your invite. Starting game...")

            from gamePage.gameBoardGui import show_game_board_window
            show_game_board_window(self.client.username, opponent_username, "TicTacToe")
        else:
            opponent_username = response_data["from"]
            messagebox.showinfo("Invite Rejected", f"{opponent_username} has rejected your invite.")


if __name__ == "__main__":
    client = Client("username", "secret_key")
    invite_handler = InviteHandler(client)
    invite_handler.send_invite("opponent_username")
