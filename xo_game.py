import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


def _ensure_utf8_console_output():
    """Prevent UnicodeEncodeError on Windows consoles when printing emoji."""
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if not stream or not hasattr(stream, "reconfigure"):
            continue
        try:
            stream.reconfigure(encoding="utf-8")
        except OSError:
            # Some IDE provided streams (e.g. debug consoles) do not allow reconfigure.
            pass


_ensure_utf8_console_output()

class TicTacToeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.board = [['' for _ in range(3)] for _ in range(3)]  # 3x3 board
        self.current_player = 'X'  # Human is X, Bot is O
        self.game_over = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('XO Game - Tic Tac Toe')
        self.setGeometry(300, 300, 500, 600)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(25)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Title label
        title_label = QLabel('Tic Tac Toe')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Segoe UI', 28, QFont.Weight.Bold))
        main_layout.addWidget(title_label)

        # Status label
        self.status_label = QLabel('Your turn (❌)')
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFont(QFont('Segoe UI', 20))
        main_layout.addWidget(self.status_label)

        # Grid layout for the board
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(15)
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton('')
                button.setFont(QFont('Segoe UI', 36))
                button.setFixedSize(130, 130)
                button.clicked.connect(lambda checked, r=i, c=j: self.on_button_click(r, c))
                self.grid_layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

        main_layout.addLayout(self.grid_layout)

        # New Game button
        self.new_game_button = QPushButton('🔄 New Game')
        self.new_game_button.setFont(QFont('Segoe UI', 18))
        self.new_game_button.clicked.connect(self.new_game)
        main_layout.addWidget(self.new_game_button)

        self.setLayout(main_layout)

        # Apply QSS styling
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                background-color: #ffffff;
                border: 4px solid #000000;
                border-radius: 20px;
                color: #000000;
                padding: 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
                border-color: #333333;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
                border-color: #666666;
            }
        """)

    def on_button_click(self, row, col):
        if self.game_over or self.board[row][col] != '':
            return

        # Human move
        self.board[row][col] = 'X'
        self.buttons[row][col].setText('❌')
        self.buttons[row][col].setStyleSheet("color: #ff0000; font-size: 36px;")

        if self.check_winner('X'):
            self.status_label.setText('You win!')
            self.highlight_winner('X')
            self.game_over = True
            return
        elif self.is_draw():
            self.status_label.setText('Draw!')
            self.game_over = True
            return

        # Bot move
        self.status_label.setText("Bot's turn (⭕)")
        self.bot_move()

    def bot_move(self):
        # Use Minimax to find best move
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            self.buttons[row][col].setText('⭕')
            self.buttons[row][col].setStyleSheet("color: #0000ff; font-size: 36px;")

            if self.check_winner('O'):
                self.status_label.setText('Bot wins!')
                self.highlight_winner('O')
                self.game_over = True
            elif self.is_draw():
                self.status_label.setText('Draw!')
                self.game_over = True
            else:
                self.status_label.setText('Your turn (❌)')

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner_minimax(board, 'O'):
            return 1
        elif self.check_winner_minimax(board, 'X'):
            return -1
        elif self.is_draw_minimax(board):
            return 0

        if is_maximizing:
            max_eval = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'O'
                        eval = self.minimax(board, depth + 1, False)
                        board[i][j] = ''
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'X'
                        eval = self.minimax(board, depth + 1, True)
                        board[i][j] = ''
                        min_eval = min(min_eval, eval)
            return min_eval

    def check_winner_minimax(self, board, player):
        # Check rows, columns, diagonals
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_draw_minimax(self, board):
        return all(board[i][j] != '' for i in range(3) for j in range(3))

    def check_winner(self, player):
        # Same as check_winner_minimax but for actual board
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                self.winning_line = [(i, j) for j in range(3)]
                return True
            if all(self.board[j][i] == player for j in range(3)):
                self.winning_line = [(j, i) for j in range(3)]
                return True
        if all(self.board[i][i] == player for i in range(3)):
            self.winning_line = [(i, i) for i in range(3)]
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            self.winning_line = [(i, 2-i) for i in range(3)]
            return True
        return False

    def is_draw(self):
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))

    def highlight_winner(self, player):
        color = "#ff0000" if player == 'X' else "#0000ff"
        for row, col in self.winning_line:
            self.buttons[row][col].setStyleSheet(f"background-color: #ffff00; color: {color}; font-size: 36px;")

    def new_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.status_label.setText('Your turn (❌)')
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText('')
                self.buttons[i][j].setStyleSheet("")
        # Reapply general button style
        self.setStyleSheet(self.styleSheet())  # To reset

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToeGame()
    game.show()
    sys.exit(app.exec())