import pygame

# Window and Board Settings
WINDOW_SIZE = 600
BOARD_SIZE = 8
CELL_SIZE = WINDOW_SIZE // BOARD_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (220, 0, 0)
DARK_GREEN = (0, 100, 0)

# Initialize Pygame and Fonts
pygame.init()
pygame.font.init()

# Fonts
FONT = pygame.font.SysFont('Arial', 32)
TITLE_FONT = pygame.font.SysFont('Arial', 48)
SUBTITLE_FONT = pygame.font.SysFont('Arial', 24)
SCORE_FONT = pygame.font.SysFont('Arial', 20)

# Screen Setup
SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Othello Game')