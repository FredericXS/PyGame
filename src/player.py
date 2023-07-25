import pygame
from src.utils.spritesheet import SpriteSheet

class Player:
    def __init__(self):
        self.is_facing_right = True
        self.iddle_animation_list = []
        self.running_animation_list = []
        self.current_animation = self.iddle_animation_list
        self.animation_cooldown = 100
        self.frame = 0
        self.last_update = pygame.time.get_ticks()

        self.load_animations()

        # default coords where the player starts
        self.x = 320
        self.y = 240
        self.speed = 0.5

    def load_animations(self):
        iddle_spritesheet_image = pygame.image.load('Sprites/spr_player_iddle.png')
        self.iddle_spritesheet = SpriteSheet(iddle_spritesheet_image)

        running_spritesheet_image = pygame.image.load('Sprites/spr_player_running.png')
        self.running_spritesheet = SpriteSheet(running_spritesheet_image)
        
        # width, height, scale, color
        for i in range(11):
            self.iddle_animation_list.append(self.iddle_spritesheet.get_image(i, 32, 32, 2, (0, 0, 0)))
        
        for i in range(12):
            self.running_animation_list.append(self.running_spritesheet.get_image(i, 32, 32, 2, (0, 0, 0)))

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time

            # prevents out of index
            if self.frame >= len(self.current_animation):
                self.frame = 0

    def handle_input(self, event_type, event_key):
        if event_type == pygame.KEYDOWN:
            if event_key == pygame.K_a:
                self.is_facing_right = False
                self.current_animation = self.running_animation_list
                self.frame = 0
            if event_key == pygame.K_d:
                self.is_facing_right = True
                self.current_animation = self.running_animation_list
                self.frame = 0
        if event_type == pygame.KEYUP:
            self.current_animation = self.iddle_animation_list
            self.frame = 0

    def player_movement(self, keys):
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed