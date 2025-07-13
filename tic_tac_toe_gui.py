import tkinter as tk
import math

HUMAN = 'O'
AI = 'X'
EMPTY = ''

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI (Unbeatable)")

        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_buttons()
        self.human_turn = True

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Helvetica', 32), width=5, height=2,
                                   command=lambda row=i, col=j: self.human_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def human_move(self, row, col):
        if self.board[row][col] == EMPTY and self.human_turn:
            self.board[row][col] = HUMAN
            self.buttons[row][col].config(text=HUMAN)
            self.human_turn = False
            if not self.check_game_end():
                self.root.after(500, self.ai_move)

    def ai_move(self):
        best_move = self.find_best_move()
        if best_move:
            row, col = best_move
            self.board[row][col] = AI
            self.buttons[row][col].config(text=AI)
            self.human_turn = True
            self.check_game_end()

    def check_game_end(self):
        result = self.evaluate()
        if result == 10:
            self.show_result("AI Wins!")
            return True
        elif result == -10:
            self.show_result("You Win!")
            return True
        elif not any(EMPTY in row for row in self.board):
            self.show_result("It's a Draw!")
            return True
        return False

    def show_result(self, message):
        result_window = tk.Toplevel(self.root)
        result_window.title("Game Over")
        tk.Label(result_window, text=message, font=('Helvetica', 24)).pack(padx=20, pady=20)
        tk.Button(result_window, text="OK", command=self.root.quit).pack(pady=10)

    def evaluate(self):
        for row in self.board:
            if row.count(AI) == 3:
                return 10
            if row.count(HUMAN) == 3:
                return -10

        for col in range(3):
            if all(self.board[row][col] == AI for row in range(3)):
                return 10
            if all(self.board[row][col] == HUMAN for row in range(3)):
                return -10

        if all(self.board[i][i] == AI for i in range(3)):
            return 10
        if all(self.board[i][i] == HUMAN for i in range(3)):
            return -10

        if all(self.board[i][2 - i] == AI for i in range(3)):
            return 10
        if all(self.board[i][2 - i] == HUMAN for i in range(3)):
            return -10

        return 0

    def minimax(self, board, depth, is_max, alpha, beta):
        score = self.evaluate()

        if score == 10 or score == -10:
            return score
        if not any(EMPTY in row for row in board):
            return 0

        if is_max:
            best = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = AI
                        best = max(best, self.minimax(board, depth + 1, False, alpha, beta))
                        board[i][j] = EMPTY
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            return best
            return best
        else:
            best = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = HUMAN
                        best = min(best, self.minimax(board, depth + 1, True, alpha, beta))
                        board[i][j] = EMPTY
                        beta = min(beta, best)
                        if beta <= alpha:
                            return best
            return best

    def find_best_move(self):
        best_val = -math.inf
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = AI
                    move_val = self.minimax(self.board, 0, False, -math.inf, math.inf)
                    self.board[i][j] = EMPTY
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
