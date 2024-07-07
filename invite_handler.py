from tkinter import messagebox
import client

class InviteHandler:
    def __init__(self, client):
        self.client = client
        self.client.set_invite_callback(self.on_invite_received)
        self.client.set_response_callback(self.on_response_received)

    def send_invite(self, opponent_username, mode):
        client.send_invite(opponent_username, mode)
        messagebox.showinfo("Invite Sent", f"Invite sent to {opponent_username}")

    def on_invite_received(self, invite_data):
        opponent_username = invite_data["from"]
        mode = invite_data["mode"]
        response = messagebox.askyesno("Game Invite",
                                       f"{opponent_username} has invited you to play {mode}. Do you accept?")
        if response:
            self.accept_invite(opponent_username, mode)
        else:
            self.reject_invite(opponent_username)

    def accept_invite(self, opponent_username, mode):
        client.send_invite_response(opponent_username, "ACCEPT", mode)
        import gamePage.gameBoardGui
        gamePage.gameBoardGui.show_game_board_window(self.client.username, opponent_username, mode)

    def reject_invite(self, opponent_username):
        client.send_invite_response(opponent_username, "REJECT", "")

    def on_response_received(self, response_data):
        if response_data["response"] == "ACCEPT":
            opponent_username = response_data["from"]
            mode = response_data["mode"]
            messagebox.showinfo("Invite Accepted", f"{opponent_username} has accepted your invite. Starting game...")
            import gamePage.gameBoardGui
            gamePage.gameBoardGui.show_game_board_window(self.client.username, opponent_username, mode)
        else:
            opponent_username = response_data["from"]
            messagebox.showinfo("Invite Rejected", f"{opponent_username} has rejected your invite.")


# Example client setup
if __name__ == "__main__":
    client = client.Client("username", "secret_key")
    invite_handler = InviteHandler(client)
    invite_handler.send_invite("opponent_username", "TicTacToe")
