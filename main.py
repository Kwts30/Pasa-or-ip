import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
FPS = 60
GRID_SIZE = 3
LINE_WIDTH = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Load images
logo_img = pygame.image.load('mmcm.png')
background1_img = pygame.transform.scale(pygame.image.load('Tic Tac Toe.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
background2_img = pygame.transform.scale(pygame.image.load('HELP.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
background3_img = pygame.transform.scale(pygame.image.load('bg3.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
player1_img = pygame.image.load('dev1.png')
player2_img = pygame.image.load('Player2.jpeg')
emmy_img = pygame.image.load('MAAMEMMY.png')
player2_emmy_img = pygame.image.load('Player2.jpeg')  # New image for Player 2 vs Emmy

# Resize player images
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
player1_img = pygame.transform.scale(player1_img, (250, 250))
player2_img = pygame.transform.scale(player2_img, (250, 250))
emmy_img = pygame.transform.scale(emmy_img, (250, 250))
player2_emmy_img = pygame.transform.scale(player2_emmy_img, (250, 250))  # Resizing new image

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TIC TAC TOE (Tres or IP)")

# Fonts
font = pygame.font.SysFont(None, 40)
popup_font = pygame.font.SysFont(None, 60)

# Functions to draw text and buttons
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def draw_button(text, font, color, surface, x, y, w, h):
    button_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, color, button_rect, border_radius=15)
    draw_text(text, font, WHITE, surface, x + w // 2, y + h // 2)

def draw_popup(text, font, surface, x, y, w, h):
    popup_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, WHITE, popup_rect, border_radius=15)
    draw_text(text, font, BLACK, surface, x + w // 2, y + h // 2)

# Main Menu
def main_menu():
    click = False
    while True:
        screen.fill(GREEN)
        screen.blit(background1_img, (0, 0))
        
        
       
        
        mx, my = pygame.mouse.get_pos()
        
        button_width = 200
        button_height = 50
        button_gap = 20
        button_x1 = (SCREEN_WIDTH // 2) - button_width - (button_gap // 2)
        button_x2 = (SCREEN_WIDTH // 2) + (button_gap // 2)
        button_y1 = 650
        button_y2 = button_y1 + button_height + button_gap
        
        button_1 = pygame.Rect(button_x1, button_y1, button_width, button_height)
        button_2 = pygame.Rect(button_x2, button_y1, button_width, button_height)
        button_3 = pygame.Rect(button_x1, button_y2, button_width, button_height)
        button_4 = pygame.Rect(button_x2, button_y2, button_width, button_height)
        
        if button_1.collidepoint((mx, my)):
            if click:
                player_selection()
        if button_2.collidepoint((mx, my)):
            if click:
                help_menu()
        if button_3.collidepoint((mx, my)):
            if click:
                credits()
        if button_4.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        
        draw_button('Start Game', font, BLUE, screen, button_x1, button_y1, button_width, button_height)
        draw_button('Help', font, BLUE, screen, button_x2, button_y1, button_width, button_height)
        draw_button('Credits', font, BLUE, screen, button_x1, button_y2, button_width, button_height)
        draw_button('Quit', font, BLUE, screen, button_x2, button_y2, button_width, button_height)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

# Help Menu
def help_menu():
    running = True
    while running:
        screen.fill(GREEN)
        screen.blit(background2_img, (0, 0))
        
        draw_text('The game tic tac toe tres or ip is played on a grid', font, GREEN, screen, SCREEN_WIDTH // 2, 400)
        draw_text('that is 3 squares by 3 squares. The mechanics of the game', font, GREEN, screen, SCREEN_WIDTH // 2, 450)
        draw_text('is to be the first player to align three of your chosen Game Modes    ', font, GREEN, screen, SCREEN_WIDTH // 2, 500)
        draw_text('either horizontally, vertically, or diagonally in the 3x3 squares. ', font, GREEN, screen, SCREEN_WIDTH // 2, 550)
        
        back_button = pygame.Rect(SCREEN_WIDTH // 2 - 300, 750, 100, 50)
        if back_button.collidepoint((pygame.mouse.get_pos())):
            if pygame.mouse.get_pressed()[0]:
                running = False
        
        draw_button('Back', font, BLUE, screen, SCREEN_WIDTH // 2 - 300, 750, 100, 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

# Credits Menu
def credits():
    running = True
    dev1_img = pygame.transform.scale(pygame.image.load('dev1.png'), (300, 350))
    dev2_img = pygame.transform.scale(pygame.image.load('Player2.jpeg'), (300, 350))
    fontcredit = pygame.font.SysFont(None, 35)
    
    while running:
        screen.fill(GREEN)
        screen.blit(background3_img, (0, 0))

        # Display developer images
        screen.blit(dev1_img, (SCREEN_WIDTH // 2 - 400, 150))
        screen.blit(dev2_img, (SCREEN_WIDTH // 2 + 100, 150))
        
        # Display developer details
        draw_text('Jaryl Kurt Benedicto', font, BLACK, screen, SCREEN_WIDTH // 2 - 250, 530)
        draw_text('1st Year Student', font, BLACK, screen, SCREEN_WIDTH // 2 - 250, 560)
        draw_text('BS in Computer Engineering', font, BLACK, screen, SCREEN_WIDTH // 2 - 250, 590)
        
        draw_text('Hannah Kyla Barol', font, BLACK, screen, SCREEN_WIDTH // 2 + 250, 530)
        draw_text('1st Year Student', font, BLACK, screen, SCREEN_WIDTH // 2 + 250, 560)
        draw_text('BS in Computer Engineering', font, BLACK, screen, SCREEN_WIDTH // 2 + 250, 590)

        draw_text('Mapua Malayan Colleges Mindanao', font, RED, screen, SCREEN_WIDTH // 2, 710)
        draw_text('Davao City', fontcredit, WHITE, screen, SCREEN_WIDTH // 2, 740)
        
        back_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, 780, 200, 50)
        if back_button.collidepoint((pygame.mouse.get_pos())):
            if pygame.mouse.get_pressed()[0]:
                running = False
        
        draw_button('Back', font, BLUE, screen, SCREEN_WIDTH // 2 - 100, 780, 200, 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        pygame.time.Clock().tick(FPS)


# Draw Tic Tac Toe Grid
def draw_grid():
    for x in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, SCREEN_HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, x * CELL_SIZE), (SCREEN_WIDTH, x * CELL_SIZE), LINE_WIDTH)

# Check for winner
def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(GRID_SIZE):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(GRID_SIZE)):
        return True
    if all(board[i][GRID_SIZE - 1 - i] == player for i in range(GRID_SIZE)):
        return True
    return False

# Check for draw
def check_draw(board):
    for row in board:
        if None in row:
            return False
    return True

# Player Selection
def player_selection():
    click = False
    while True:
        screen.fill(GREEN)
        screen.blit(background1_img, (0, 0))
        
        
        
        mx, my = pygame.mouse.get_pos()
        
        button_1 = pygame.Rect(320, 300, 200, 50)
        button_2 = pygame.Rect(320, 400, 200, 50)
        button_3 = pygame.Rect(320, 500, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            if click:
                game_loop("player1", "emmy")

        if button_2.collidepoint((mx, my)):
            if click:
                game_loop("player2_emmy", "emmy")

        if button_3.collidepoint((mx, my)):
            if click:
                game_loop("player1", "player2_emmy")
        
        draw_button('Jaryl vs Mam Ems', font, BLUE, screen, 320, 300, 270, 50)
        draw_button('Kyla vs Mam Ems', font, BLUE, screen, 320, 400, 270, 50)
        draw_button('Jaryl vs Kyla', font, BLUE, screen, 315, 500, 280, 50)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

# Main Game Loop
def game_loop(player1, player2):
    board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
    current_player = player1
    game_over = False
    winner = None

    while True:
        screen.fill(WHITE)
        screen.blit(background3_img, (0, 0))
        draw_grid()

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if board[y][x] == "player1":
                    screen.blit(player1_img, (x * CELL_SIZE + (CELL_SIZE - player1_img.get_width()) // 2,
                                              y * CELL_SIZE + (CELL_SIZE - player1_img.get_height()) // 2))
                elif board[y][x] == "emmy":
                    screen.blit(emmy_img, (x * CELL_SIZE + (CELL_SIZE - emmy_img.get_width()) // 2,
                                           y * CELL_SIZE + (CELL_SIZE - emmy_img.get_height()) // 2))
                elif board[y][x] == "player2":
                    screen.blit(player2_img, (x * CELL_SIZE + (CELL_SIZE - player2_img.get_width()) // 2,
                                              y * CELL_SIZE + (CELL_SIZE - player2_img.get_height()) // 2))
                elif board[y][x] == "player2_emmy":
                    screen.blit(player2_emmy_img, (x * CELL_SIZE + (CELL_SIZE - player2_emmy_img.get_width()) // 2,
                                                   y * CELL_SIZE + (CELL_SIZE - player2_emmy_img.get_height()) // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // CELL_SIZE
                clicked_col = mouseX // CELL_SIZE
                if board[clicked_row][clicked_col] is None:
                    if current_player == "player2" and player2 == "emmy":
                        board[clicked_row][clicked_col] = "player2_emmy"
                    else:
                        board[clicked_row][clicked_col] = current_player
                    if check_winner(board, current_player):
                        game_over = True
                        winner = current_player
                    elif check_draw(board):
                        game_over = True
                    current_player = player2 if current_player == player1 else player1

        if game_over:
            if winner:
                if winner == "player1" and player2 == "emmy":
                    win_text = "Pasado ka na par!"

                elif winner == "player2_emmy" and player2 == "emmy":
                    win_text = "Pasado ka na par!"

                elif winner == "emmy":
                    win_text = "See you next sem!"
                else:
                    if winner == "player1":
                        win_text = "Jaryl wins!"

                    else:
                        win_text = "Hannah wins!"

            else:
                win_text = "It's a draw!"
            draw_popup(win_text, popup_font, screen, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200, 400, 100)
            
            mx, my = pygame.mouse.get_pos()
            button_restart = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)
            button_main_menu = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150, 200, 50)
            
            if button_restart.collidepoint((mx, my)) and pygame.mouse.get_pressed()[0]:
                player_selection()
            if button_main_menu.collidepoint((mx, my)) and pygame.mouse.get_pressed()[0]:
                main_menu()

            draw_button('Restart', font, GREEN, screen, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)
            draw_button('Main Menu', font, RED, screen, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150, 200, 50)

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main_menu()
