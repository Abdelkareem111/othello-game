import pygame
from constants import (
    WINDOW_SIZE, BOARD_SIZE, CELL_SIZE, BLACK, WHITE, GREEN, GRAY,
    SCREEN, FONT, TITLE_FONT, SUBTITLE_FONT, SCORE_FONT
)
from button import Button

def draw_score_box():
    # Draw score box background
    score_box = pygame.Rect(10, WINDOW_SIZE - 60, 200, 50)
    pygame.draw.rect(SCREEN, WHITE, score_box)
    pygame.draw.rect(SCREEN, BLACK, score_box, 2)

def draw_winner_screen(winner, black_score, white_score):
    # Semi-transparent overlay
    overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
    overlay.fill(WHITE)
    overlay.set_alpha(200)
    SCREEN.blit(overlay, (0, 0))

    # Draw winner announcement
    if winner == "Tie":
        title_text = "It's a Tie!"
        title_color = (0, 0, 255)  # Blue
    else:
        title_text = f"{winner} Wins!"
        title_color = BLACK if winner == "Black" or winner == "Player" else WHITE

    title = TITLE_FONT.render(title_text, True, title_color)
    title_rect = title.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 - 50))
    
    # Draw score
    if winner == "Tie":
        score_text = f"Final Score: {black_score} - {white_score}"
    else:
        winner_score = black_score if winner in ["Black", "Player"] else white_score
        loser_score = white_score if winner in ["Black", "Player"] else black_score
        score_text = f"Score: {winner_score} - {loser_score}"
    
    score = FONT.render(score_text, True, BLACK)
    score_rect = score.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 + 20))

    # Draw background for winner announcement
    bg_rect = pygame.Rect(0, 0, 400, 200)
    bg_rect.center = (WINDOW_SIZE//2, WINDOW_SIZE//2)
    pygame.draw.rect(SCREEN, GREEN, bg_rect)
    pygame.draw.rect(SCREEN, BLACK, bg_rect, 3)

    # Draw texts
    SCREEN.blit(title, title_rect)
    SCREEN.blit(score, score_rect)

    # Draw "Click to continue" message
    continue_text = SUBTITLE_FONT.render("Click anywhere to continue", True, BLACK)
    continue_rect = continue_text.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 + 70))
    SCREEN.blit(continue_text, continue_rect)

def draw_board(game):
    SCREEN.fill(GREEN)
    
    # Draw grid lines
    for i in range(BOARD_SIZE + 1):
        pygame.draw.line(SCREEN, BLACK, (i * CELL_SIZE, 0), 
                        (i * CELL_SIZE, WINDOW_SIZE))
        pygame.draw.line(SCREEN, BLACK, (0, i * CELL_SIZE), 
                        (WINDOW_SIZE, i * CELL_SIZE))

    # Draw pieces
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if game.board[row][col]:
                color = BLACK if game.board[row][col] == 'B' else WHITE
                center = (col * CELL_SIZE + CELL_SIZE // 2,
                         row * CELL_SIZE + CELL_SIZE // 2)
                pygame.draw.circle(SCREEN, color, center, CELL_SIZE // 2 - 4)

    # Draw current player indicator and label
    color = BLACK if game.current_player == 'B' else WHITE
    pygame.draw.circle(SCREEN, color, (WINDOW_SIZE - 20, 20), 10)
    
    # Draw player labels and scores
    black_score, white_score = game.count_pieces()
    
    if game.game_mode == 'ai':
        player_text = "Your Turn" if game.current_player == 'B' else f"AI's Turn ({game.difficulty})"
        score_text = f"Player: {black_score} - AI: {white_score}"
    else:
        player_text = "Black's Turn" if game.current_player == 'B' else "White's Turn"
        score_text = f"Black: {black_score} - White: {white_score}"
    
    # Draw score box
    draw_score_box()
    
    # Draw texts
    text_surface = FONT.render(player_text, True, BLACK)
    score_surface = SCORE_FONT.render(score_text, True, BLACK)
    SCREEN.blit(text_surface, (10, 10))
    SCREEN.blit(score_surface, (20, WINDOW_SIZE - 45))
    
    # Draw valid moves
    if game.game_mode == 'friend' or (game.game_mode == 'ai' and game.current_player == 'B'):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if game.is_valid_move(row, col):
                    center = (col * CELL_SIZE + CELL_SIZE // 2,
                            row * CELL_SIZE + CELL_SIZE // 2)
                    pygame.draw.circle(SCREEN, GRAY, center, 5)

def draw_menu():
    SCREEN.fill(WHITE)
    
    # Draw title
    title = TITLE_FONT.render('OTHELLO', True, BLACK)
    title_rect = title.get_rect(center=(WINDOW_SIZE//2, 100))
    SCREEN.blit(title, title_rect)
    
    # Create buttons
    vs_ai_button = Button(WINDOW_SIZE//4, 250, WINDOW_SIZE//2, 60, 'vs Computer', GREEN)
    vs_friend_button = Button(WINDOW_SIZE//4, 350, WINDOW_SIZE//2, 60, 'vs Friend', (0, 0, 255))
    
    # Draw buttons
    vs_ai_button.draw()
    vs_friend_button.draw()
    
    pygame.display.flip()
    
    # Handle menu events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if vs_ai_button.handle_event(event):
                return 'ai'
            if vs_friend_button.handle_event(event):
                return 'friend'
            
            vs_ai_button.handle_event(event)
            vs_friend_button.handle_event(event)
        
        vs_ai_button.draw()
        vs_friend_button.draw()
        pygame.display.flip()

def draw_difficulty_menu():
    SCREEN.fill(WHITE)
    
    # Draw title
    title = TITLE_FONT.render('SELECT DIFFICULTY', True, BLACK)
    title_rect = title.get_rect(center=(WINDOW_SIZE//2, 100))
    SCREEN.blit(title, title_rect)
    
    # Create difficulty buttons
    easy_button = Button(WINDOW_SIZE//4, 200, WINDOW_SIZE//2, 60, 'Easy', GREEN)
    medium_button = Button(WINDOW_SIZE//4, 300, WINDOW_SIZE//2, 60, 'Medium', (0, 0, 255))
    hard_button = Button(WINDOW_SIZE//4, 400, WINDOW_SIZE//2, 60, 'Hard', (220, 0, 0))
    
    # Add difficulty descriptions
    easy_desc = SUBTITLE_FONT.render('(Random moves, good for beginners)', True, GRAY)
    medium_desc = SUBTITLE_FONT.render('(Balanced AI, occasional mistakes)', True, GRAY)
    hard_desc = SUBTITLE_FONT.render('(Strategic AI, challenging)', True, GRAY)
    
    SCREEN.blit(easy_desc, (WINDOW_SIZE//4, 270))
    SCREEN.blit(medium_desc, (WINDOW_SIZE//4, 370))
    SCREEN.blit(hard_desc, (WINDOW_SIZE//4, 470))
    
    # Draw buttons
    easy_button.draw()
    medium_button.draw()
    hard_button.draw()
    
    pygame.display.flip()
    
    # Handle menu events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if easy_button.handle_event(event):
                return 'easy'
            if medium_button.handle_event(event):
                return 'medium'
            if hard_button.handle_event(event):
                return 'hard'
            
            easy_button.handle_event(event)
            medium_button.handle_event(event)
            hard_button.handle_event(event)
        
        easy_button.draw()
        medium_button.draw()
        hard_button.draw()
        pygame.display.flip()