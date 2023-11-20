import random
import pygame
from pygame.locals import *


def assign_paddle_colors():
    colors = ['RED', 'BLUE']
    random.shuffle(colors)
    player1_color = colors[0]
    player2_color = colors[1]
    return player1_color, player2_color


pygame.init()
pygame.display.set_caption("Pong")

width, height = 840, 480
screen = pygame.display.set_mode((width, height))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (138, 43, 226)

ball_x = width // 2
ball_y = height // 2
ball_radius = 10
ball_speed_x = 5
ball_speed_y = 6
 
paddle_width = 10
paddle_height = 60
paddle_speed = 5

player_score = 0
computer_score = 0
font = pygame.font.Font(None, 36)

player_paddle = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
computer_paddle = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

player_color, computer_color = assign_paddle_colors()

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_w] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[K_s] and player_paddle.bottom < height:
        player_paddle.y += paddle_speed
    if keys[K_p] and computer_paddle.top > 0:
        computer_paddle.y -= paddle_speed
    if keys[K_l] and computer_paddle.bottom < height:
        computer_paddle.y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if player_paddle.colliderect(pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)):
        ball_speed_x = abs(ball_speed_x)
    if computer_paddle.colliderect(pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)):
        ball_speed_x = -abs(ball_speed_x)

    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y *= -1

    if ball_x - ball_radius < 0:
        computer_score += 1
        player_paddle.y = height // 2 - paddle_height // 2
        computer_paddle.y = height // 2 - paddle_height // 2
        ball_x, ball_y = width // 2, height // 2
    if ball_x + ball_radius > width:
        player_score += 1
        player_paddle.y = height // 2 - paddle_height // 2
        computer_paddle.y = height // 2 - paddle_height // 2
        ball_x, ball_y = width // 2, height // 2

    screen.fill(BLACK)
    pygame.draw.ellipse(screen, GREEN, (ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2))
    pygame.draw.rect(screen, player_color, player_paddle)
    pygame.draw.rect(screen, computer_color, computer_paddle)
    pygame.draw.aaline(screen, WHITE, (width // 2, 0), (width // 2, height))
    screen.blit(font.render(str(player_score), True, WHITE), (50, 10))
    screen.blit(font.render(str(computer_score), True, WHITE), (width - 50 - font.size(str(computer_score))[0], 10))

    pygame.display.update()

pygame.quit()
