import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Car Image
car_img = pygame.image.load('car.png')  # You need to provide the path to your car image

# Car dimensions
car_width = 73
car_height = 82

# Font
font = pygame.font.SysFont(None, 25)


def car(x, y):
    game_display.blit(car_img, (x, y))


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [display_width / 3, display_height / 2])


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    obstacle_startx = random.randrange(0, display_width)
    obstacle_starty = -600
    obstacle_speed = 7
    obstacle_width = 100
    obstacle_height = 100

    game_exit = False
    crashed = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        game_display.fill(white)

        # Drawing obstacle
        pygame.draw.rect(game_display, red, [obstacle_startx, obstacle_starty, obstacle_width, obstacle_height])
        obstacle_starty += obstacle_speed

        # Drawing car
        car(x, y)

        # Check if the car is hitting the obstacle
        if x > obstacle_startx and x < obstacle_startx + obstacle_width or x + car_width > obstacle_startx and x + car_width < obstacle_startx + obstacle_width:
            if y < obstacle_starty + obstacle_height:
                crashed = True

        if crashed:
            message_to_screen("You crashed!", red)
            pygame.display.update()
            time.sleep(2)
            game_loop()

        if x > display_width - car_width or x < 0:
            crashed = True
            message_to_screen("You crashed!", red)
            pygame.display.update()
            time.sleep(2)
            game_loop()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


game_loop()
