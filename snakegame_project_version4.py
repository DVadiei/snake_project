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

# Snake colors to choose from
SNAKE_COLORS = [GREEN, RED, WHITE, YELLOW]

# Define display dimensions
DIS_WIDTH = 800
DIS_HEIGHT = 600

# Define snake block size and speed
SNAKE_BLOCK = 20
SNAKE_SPEED = 15

# Load background music
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)  # Play the music indefinitely

# Load images
HEAD_IMG = pygame.image.load('head.png.png')
BODY_IMG = pygame.image.load('body.png.png')
FOOD_IMG = pygame.image.load('food.png.png')

# Create the display surface
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game')

# Create clock object to control frame rate
CLOCK = pygame.time.Clock()

def draw_snake(snake_list, snake_color):
    for segment in snake_list:
        if segment == snake_list[0]:
            pygame.draw.rect(DIS, snake_color, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])
            DIS.blit(HEAD_IMG, (segment[0], segment[1]))
        else:
            pygame.draw.rect(DIS, snake_color, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])
            DIS.blit(BODY_IMG, (segment[0], segment[1]))

def draw_food(foodx, foody):
    DIS.blit(FOOD_IMG, (foodx, foody))

def game_over_msg(score):
    font = pygame.font.SysFont(None, 50)
    dis_text = font.render("Game Over! Your Score: " + str(score), True, RED)
    DIS.blit(dis_text, [DIS_WIDTH/4, DIS_HEIGHT/2])
    pygame.display.update()
    time.sleep(2)

def draw_menu():
    menu_font = pygame.font.SysFont(None, 50)
    menu_text = menu_font.render("Select Snake Color:", True, BLACK)
    DIS.blit(menu_text, [DIS_WIDTH/3, DIS_HEIGHT/3])

    color_y = DIS_HEIGHT/2
    for idx, color in enumerate(SNAKE_COLORS):
        pygame.draw.rect(DIS, color, [DIS_WIDTH/3 + idx * 120, color_y, 100, 50])

    pygame.display.update()

def gameLoop():
    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
    foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0

    score = 0

    snake_color = GREEN  # Default snake color

    while not game_over:

        while game_close:
            game_over_msg(score)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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

        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        DIS.fill(BLUE)

        draw_food(foodx, foody)

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

        score_font = pygame.font.SysFont("comicsansms", 35)
        value = score_font.render("Your Score: " + str(score), True, YELLOW)
        DIS.blit(value, [0, 0])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
            foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0
            length_of_snake += 1
            score += 10

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

draw_menu()  # Show menu initially
gameLoop()