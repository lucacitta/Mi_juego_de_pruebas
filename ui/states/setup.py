import pygame

from elements.buttons import yes_button, no_button

def setup():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Inserte un buen nombre")

    background_image = pygame.image.load("ui/assets/backgrounds/dungeon_background.webp")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    return screen, screen_width, screen_height, background_image