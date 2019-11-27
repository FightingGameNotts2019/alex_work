import pygame
import sys
import os

pygame.init()
fps = 60
animation = 4
display_width = 1280
display_height = 630
ground_height = 500
clock = pygame.time.Clock()

x = 640
y = 435
width = 40
height = 60
vel = 5
plat_pos_x = 500
plat_pos_y = 300
plat_w = 300
plat_h = 20


'''
Classes
'''
# TODO Implement the level class so that it changes the background depending on the level.
# TODO Generate and changes the platform so that it changes with the level.
# TODO Set the spawn points for each character in the level.


class Platform:
    def __init__(self, size_x, size_y, pos_x, pos_y, colour):
        self.surf = pygame.Surface((size_x, size_y))
        self.rect = self.surf.get_rect(midbottom=(pos_x, pos_y))
        self.surf.fill(colour)

    def draw(self):
        screen.blit(self.surf, self.rect)


'''
Setup
'''
# This changes the window caption, loads the background image for the game and grey is used for ALPHA function

pygame.display.set_caption("Fighting Game")
screen = pygame.display.set_mode([display_width, display_height])
background = pygame.image.load(os.path.join('images', 'background1.png')).convert()
background_box = screen.get_rect()
sky = (102, 178, 255)
grey = (38, 38, 38)


'''
Main Loop
'''
# Maintains the game until it is quit
has_quit = True

while has_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < display_width - width:
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel

    if keys[pygame.K_DOWN] and y < ground_height - height - vel and (x != (plat_pos_x + height)):
        y += vel

    screen.blit(background, background_box)
    platform = pygame.draw.rect(screen, (0, 255, 0), (plat_pos_x, plat_pos_y, plat_w, plat_h))
    player = pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    clock.tick(fps)
