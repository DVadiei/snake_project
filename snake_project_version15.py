import pygame
import time
import random

pygame.init()

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
PURPLE = (128, 0, 128)
LIGHT_BLUE = (173, 216, 230)
DARK_GREEN = (0, 100, 0)
CYAN = (0, 255, 255)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
# Snake colors to choose from
SNAKE_COLORS = [GREEN, RED, PURPLE, YELLOW, DARK_GREEN, LIGHT_BLUE, CYAN, PINK, ORANGE]

# Food images to choose from
SNAKE_FOODS = ["food1.png", "food2.png", "food3.png"]

# Define display dimensions
DIS_WIDTH = 800
DIS_HEIGHT = 600

# Define snake block size and speed
SNAKE_BLOCK = 20
SNAKE_SPEED = 10

# Load background music
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)  # Play the music indefinitely

# Load images
HEAD_IMG = pygame.image.load('red.png')
BODY_IMG = pygame.image.load('black.png')
FOOD_IMGS = [pygame.image.load(food) for food in SNAKE_FOODS]

# Create the display surface
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game')

# Create clock object to control frame rate
CLOCK = pygame.time.Clock()

# Function to read high score from file
def read_high_score():
    try:
        with open('highscore.txt', 'r') as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    return high_score

# Function to write high score to file
def write_high_score(score):
    with open('highscore.txt', 'w') as file:
        file.write(str(score))

def draw_snake(snake_list, snake_color):
    for segment in snake_list:
        if segment == snake_list[0]:
            pygame.draw.rect(DIS, snake_color, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])
            DIS.blit(HEAD_IMG, (segment[0], segment[1]))
        else:
            pygame.draw.rect(DIS, snake_color, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])
            DIS.blit(BODY_IMG, (segment[0], segment[1]))

def draw_food(foodx, foody, food_img):
    DIS.blit(food_img, (foodx, foody))

def game_over_msg(score, high_score):
    font = pygame.font.SysFont(None, 50)
    dis_text = font.render("Game Over! Your Score: " + str(score), True, RED)
    DIS.blit(dis_text, [DIS_WIDTH / 2 - dis_text.get_width() / 2, DIS_HEIGHT / 2 - dis_text.get_height() / 2])
    info_text = font.render("Press 'C' to play again or 'Q' to quit", True, RED)
    DIS.blit(info_text, [DIS_WIDTH / 2 - info_text.get_width() / 2, DIS_HEIGHT / 2 + 50])
    high_score_text = font.render("Highest Score: " + str(high_score), True, RED)
    DIS.blit(high_score_text, [DIS_WIDTH - high_score_text.get_width() - 10, 10])
    reset_text = font.render("Press 'R' to reset high score", True, RED)
    DIS.blit(reset_text, [DIS_WIDTH / 2 - reset_text.get_width() / 2, DIS_HEIGHT / 2 + 100])
    pygame.display.update()
    time.sleep(2)

def draw_menu():
    DIS.fill(WHITE)
    menu_font = pygame.font.SysFont(None, 50)

    # Select Snake Color
    menu_text = menu_font.render("Select Snake Color:", True, BLACK)
    DIS.blit(menu_text, [DIS_WIDTH / 2 - menu_text.get_width() / 2, DIS_HEIGHT / 6])

    color_start_x = (DIS_WIDTH - (120 * 3)) / 2  # Center the color buttons
    color_y = DIS_HEIGHT / 4
    for idx, color in enumerate(SNAKE_COLORS):
        col = idx % 3
        row = idx // 3
        pygame.draw.rect(DIS, color, [color_start_x + col * 120, color_y + row * 60, 100, 50])

    # Select Food Type
    food_text = menu_font.render("Select Food Type:", True, BLACK)
    DIS.blit(food_text, [DIS_WIDTH / 2 - food_text.get_width() / 2, DIS_HEIGHT / 2 + 50])

    food_start_x = (DIS_WIDTH - (120 * len(FOOD_IMGS))) / 2  # Center the food images
    food_y = DIS_HEIGHT / 2 + 100
    for idx, food_img in enumerate(FOOD_IMGS):
        DIS.blit(food_img, (food_start_x + idx * 120, food_y))

    # Instructions
    info_text = menu_font.render("Press 'C' to continue or 'Q' to quit", True, BLACK)
    DIS.blit(info_text, [DIS_WIDTH / 2 - info_text.get_width() / 2, DIS_HEIGHT - 50])

    pygame.display.update()

def draw_color_buttons():
    button_width = 100
    button_height = 50
    for idx, color in enumerate(SNAKE_COLORS):
        pygame.draw.rect(DIS, color, [idx * button_width, 0, button_width, button_height])
        pygame.draw.rect(DIS, BLACK, [idx * button_width, 0, button_width, button_height], 2)
    pygame.display.update()

def generate_food_position():
    while True:
        foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
        foody = round(random.randrange(50, DIS_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0  # Start from y = 50 to avoid buttons
        if not (0 <= foodx < len(SNAKE_COLORS) * 100 and foody < 50):  # Ensure it's not in the button area
            return foodx, foody

def gameLoop(snake_color, food_img):
    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx, foody = generate_food_position()

    score = 0
    high_score = read_high_score()  # Load high score from file

    # Define font for displaying messages
    small_font = pygame.font.SysFont(None, 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    while not game_over:

        while game_close:
            if score > high_score:
                high_score = score
                write_high_score(high_score)  # Save new high score to file
            game_over_msg(score, high_score)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(snake_color, food_img)
                    if event.key == pygame.K_r:  # Reset high score if 'R' key is pressed
                        high_score = 0
                        write_high_score(high_score)
                        gameLoop(snake_color, food_img)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[1] <= 50:
                    snake_color = SNAKE_COLORS[pos[0] // 100]

        # Check if snake hits the walls or the buttons at the top
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 50:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        DIS.fill(BLUE)

        draw_food(foodx, foody, food_img)

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list, snake_color)
        draw_color_buttons()

        value = score_font.render("Your Score: " + str(score), True, YELLOW)
        DIS.blit(value, [0, 50])

        # Display small message in the corner
        small_text = small_font.render("Press 'Q' to quit or 'R' to reset high score", True, WHITE)
        DIS.blit(small_text, [DIS_WIDTH - small_text.get_width() - 10, DIS_HEIGHT - small_text.get_height() - 10])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food_position()
            length_of_snake += 1
            score += 10

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

def main_menu():
    snake_color = GREEN
    selected_food_img = FOOD_IMGS[0]
    show_menu = True
    while show_menu:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    show_menu = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                color_start_x = (DIS_WIDTH - (120 * 3)) / 2  # Center the color buttons
                color_y = DIS_HEIGHT / 4
                food_start_x = (DIS_WIDTH - (120 * len(FOOD_IMGS))) / 2  # Center the food images
                food_y = DIS_HEIGHT / 2 + 100
                for idx, color in enumerate(SNAKE_COLORS):
                    col = idx % 3
                    row = idx // 3
                    if color_start_x + col * 120 <= pos[0] <= color_start_x + col * 120 + 100 and color_y + row * 60 <= pos[1] <= color_y + row * 60 + 50:
                        snake_color = color
                for idx, food_img in enumerate(FOOD_IMGS):
                    if food_start_x + idx * 120 <= pos[0] <= food_start_x + idx * 120 + 100 and food_y <= pos[1] <= food_y + 50:
                        selected_food_img = food_img

    gameLoop(snake_color, selected_food_img)

main_menu()