import pygame

from elements.fonts import big_font, medium_font
from elements.colors import black, white, gray
from elements.buttons import continue_button
from elements.buttons import input_box
from utils import draw_text

def name_selection(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    text_input_active = session_data['text_input_active']
    player_name = session_data['player_name']

    draw_text(
        text='Cual es tu nombre, viajero?',
        font=big_font,
        text_color=black,
        surface=screen,
        x=screen_width // 2, 
        y=160,
        bg_color=white
    )

    input_box.move_to(
        x=screen_width // 2 - 140,
        y=screen_height // 2
    )
    input_box.action = lambda session_data: session_data.update({'text_input_active': True})

    input_box_rect_color = gray if text_input_active else white
    input_box.rect = pygame.draw.rect(
        surface=screen,
        color=input_box_rect_color,
        rect = input_box.rect,
    )

    text_surface = medium_font.render(player_name, True, black)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()

    text_x = input_box.x + (input_box.rect.width - text_width) // 2
    text_y = input_box.y + (input_box.rect.height - text_height) // 2

    screen.blit(text_surface, (text_x, text_y))

    continue_button.move_to(screen_width * 0.8 - continue_button.width // 2, 500)
    screen.blit(
        continue_button.image if player_name else continue_button.disable_image,
        (continue_button.x, continue_button.y)
    )
    continue_button.action = lambda session_data: session_data.update({'actual_state': 'class_selection'})

    session_data['active_buttons'] = [input_box, continue_button] if player_name else [input_box]

    return session_data