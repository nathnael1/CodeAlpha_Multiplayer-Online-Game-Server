class TicTacToe:
    def __init__(self,room_code):
        self.board = [''] * 9
        self.current_player = 'X'
        self.room_code = room_code
    def make_move(self,position):
        if self.board[position] == '':
            self.board[position] = self.current_player
            winner = self.check_winner()
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return winner
        return None
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)              
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]  
        return None  
    def reset_game(self):
        self.board = [''] * 9
        self.current_player = 'X'
    