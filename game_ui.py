import pygame
import random

window_quotes = [
    "Hitchhiker's Tic-Tac-Toe",
    "Brain the size of a planet, and I'm a window title.",
    "Don't panic. Or do. I don't care. I'm a title",
    "42: The answer to how to win the game.",
    "I've calculated your chances of winning. They're 42.",
    "Life, loathe it or ignore it, you can't like it.",
    "Everything is quite remarkably pointless. Especially Tic-Tac-Toe"
]

background_files = [
    'babel-fish.png',
    'hitchikers.png',
    'arthur_dent.png',
    'restaurant.png'
]

#initialising the game=
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font("Harlow Solid Regular.ttf", 100)
button_font = pygame.font.Font("Harlow Solid Regular.ttf", 40)
RESET_BUTTON_RECT = pygame.Rect(950, 620, 300, 60)
chosen_bg = random.choice(background_files)
bg_image = pygame.image.load(chosen_bg).convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

#setting the background
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
pygame.display.set_caption(random.choice(window_quotes))

#setting the icons
icon_size = (180, 180)
#vorgon is 'X'
vorgon_img = pygame.image.load('vorgon.png').convert_alpha()
vorgon_img = pygame.transform.scale(vorgon_img, icon_size)
#don't panic is 'O'
dontpanic_img = pygame.image.load('dont_panic.png').convert_alpha()
dontpanic_img = pygame.transform.scale(dontpanic_img, icon_size)

#creating a reset button
def draw_reset_button():
    #crating the button
    pygame.draw.rect(screen, (50, 50, 50), RESET_BUTTON_RECT)  # Dark Grey
    pygame.draw.rect(screen, (255, 255, 255), RESET_BUTTON_RECT, 3)
    btn_text = button_font.render("Abandon Hope", True, (255, 255, 255))

    #telling the board what to do
    text_rect = btn_text.get_rect(center=RESET_BUTTON_RECT.center)
    screen.blit(btn_text, text_rect)

def randomize_background():
    global bg_image
    chosen_bg = random.choice(background_files)
    new_bg = pygame.image.load(chosen_bg).convert_alpha()
    bg_image = pygame.transform.scale(new_bg, (WIDTH, HEIGHT))

def draw_game_window(board):
    #Rendering the display and icons

    # Draw the background and grid
    screen.blit(bg_image, (0, 0))
    #
    """
    Creating the board, and printing it.
    This is instead of the print_board function in the game file.
    """
    # Draw the Grid Lines
    line_color = (255, 255, 255)
    # Vertical
    pygame.draw.line(screen, line_color, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), 5)
    pygame.draw.line(screen, line_color, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), 5)
    # Horizontal
    pygame.draw.line(screen, line_color, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), 5)
    pygame.draw.line(screen, line_color, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), 5)

    # Draw the X's and O's
    for i, cell in enumerate(board):
        if cell in ["❌", "⭕"]:
            row = i // 3
            col = i % 3

            # Center coordinates for the icons
            x_pos = (col * (WIDTH // 3)) + (WIDTH // 6) - (icon_size[0] // 2)
            y_pos = (row * (HEIGHT // 3)) + (HEIGHT // 6) - (icon_size[1] // 2)

            if cell == "❌":
                screen.blit(vorgon_img, (x_pos, y_pos))
            elif cell == "⭕":
                screen.blit(dontpanic_img, (x_pos, y_pos))
    draw_reset_button()
    pygame.display.flip()

if __name__ == "__main__":
    test_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        draw_game_window(test_board)
        clock.tick(60)