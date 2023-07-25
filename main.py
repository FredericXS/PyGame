import pygame
from pygame.locals import *
import sys
from src.player import Player

pygame.init()

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyGame Skeleton')

BLACK = (0, 0, 0)

player = Player()   

keys = {
    pygame.K_UP: False,
    pygame.K_DOWN: False,
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False
}

while True:
    screen.fill(BLACK)

    player.update_animation()

    if player.is_facing_right:
        screen.blit(player.current_animation[player.frame], (player.x, player.y))
    else:
        flipped_image = pygame.transform.flip(player.current_animation[player.frame], True, False)
        screen.blit(flipped_image, (player.x, player.y))

    keys = pygame.key.get_pressed()
    player.player_movement(keys)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            player.handle_input(event.type, event.key)

        if event.type == KEYUP:
            player.handle_input(event.type, event.key)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
