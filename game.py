import random
from constants import BOARD_SIZE

class OthelloGame:
    def __init__(self, game_mode='ai', difficulty='medium'):
        self.board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = 'B'  # B for Black, W for White
        self.game_mode = game_mode  # 'ai' or 'friend'
        self.difficulty = difficulty  # 'easy', 'medium', or 'hard'
        self.initialize_board()

    def initialize_board(self):
        # Set up the initial four pieces in the center
        center = BOARD_SIZE // 2
        self.board[center-1][center-1] = 'W'
        self.board[center-1][center] = 'B'
        self.board[center][center-1] = 'B'
        self.board[center][center] = 'W'

    def is_valid_move(self, row, col):
        if self.board[row][col] is not None:
            return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                     (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dr, dc in directions:
            if self.would_flip(row, col, dr, dc):
                return True
        return False

    def would_flip(self, row, col, dr, dc):
        r, c = row + dr, col + dc
        if not (0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE):
            return False
        if self.board[r][c] != ('W' if self.current_player == 'B' else 'B'):
            return False

        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
            if self.board[r][c] is None:
                return False
            if self.board[r][c] == self.current_player:
                return True
            r, c = r + dr, c + dc
        return False

    def count_flips(self, row, col):
        if not self.is_valid_move(row, col):
            return 0

        total_flips = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                     (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dr, dc in directions:
            if self.would_flip(row, col, dr, dc):
                r, c = row + dr, col + dc
                flips = 0
                while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] != self.current_player:
                    if self.board[r][c] is None:
                        break
                    flips += 1
                    r, c = r + dr, c + dc
                total_flips += flips

        return total_flips

    def get_valid_moves(self):
        valid_moves = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def evaluate_position(self, row, col):
        score = 0
        # Corner positions are most valuable
        if (row, col) in [(0, 0), (0, 7), (7, 0), (7, 7)]:
            score = 100
        # Edges are also valuable
        elif row in [0, 7] or col in [0, 7]:
            score = 50
        # Positions that flip more pieces are preferred
        else:
            score = self.count_flips(row, col)

        if self.difficulty == 'easy':
            # Add randomness to make it easier
            score += random.randint(-30, 30)
        elif self.difficulty == 'medium':
            # Add small randomness
            score += random.randint(-10, 10)
        # Hard difficulty uses pure strategy (no randomness)
        
        return score

    def ai_move(self):
        valid_moves = self.get_valid_moves()
        if not valid_moves:
            return False

        # Evaluate each move
        move_scores = []
        for row, col in valid_moves:
            score = self.evaluate_position(row, col)
            move_scores.append((score, row, col))

        if self.difficulty == 'easy':
            # Sometimes choose a random move instead of the best one
            if random.random() < 0.3:  # 30% chance of random move
                chosen_move = random.choice(move_scores)
            else:
                chosen_move = max(move_scores)
        elif self.difficulty == 'medium':
            # Sometimes choose a suboptimal move
            if random.random() < 0.2:  # 20% chance of suboptimal move
                move_scores.sort(reverse=True)
                chosen_move = move_scores[min(1, len(move_scores)-1)]  # Second best move
            else:
                chosen_move = max(move_scores)
        else:  # hard
            chosen_move = max(move_scores)

        return self.make_move(chosen_move[1], chosen_move[2])

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                     (1, 1), (-1, -1), (1, -1), (-1, 1)]

        self.board[row][col] = self.current_player
        for dr, dc in directions:
            if self.would_flip(row, col, dr, dc):
                r, c = row + dr, col + dc
                while self.board[r][c] != self.current_player:
                    self.board[r][c] = self.current_player
                    r, c = r + dr, c + dc

        self.current_player = 'W' if self.current_player == 'B' else 'B'
        return True

    def has_valid_moves(self):
        return len(self.get_valid_moves()) > 0

    def count_pieces(self):
        black = sum(row.count('B') for row in self.board)
        white = sum(row.count('W') for row in self.board)
        return black, white