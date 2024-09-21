import pygame

from elements.fonts import big_font, medium_font
from elements.colors import black
from utils import draw_text

def draw_name_ask(screen, screen_width):
    question_box_rect_x = screen_width // 2 - 200
    question_box_rect_y = 200
    question_box_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/horizontal_message.png'),
        (400, 200)
    )
    screen.blit(question_box_image, (question_box_rect_x, question_box_rect_y))

    draw_text(
        'Cual es tu nombre, viajero?',
        big_font,
        black,
        screen,
        question_box_rect_x + 200,
        question_box_rect_y + 50,
    )

def draw_name_input_box(screen, screen_width, screen_height, player_name, input_box):
    input_box_bg_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/horizontal_message.png'),
        (300, 40)
    )

    input_box_x = screen_width // 2 - 150
    input_box_y = screen_height // 2
    screen.blit(input_box_bg_image, (input_box_x, input_box_y))

    input_box.move_to(input_box_x, input_box_y)
    input_box.action = lambda session_data: session_data.update({'text_input_active': True})

    text_surface = medium_font.render(player_name, True, black)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()

    text_x = input_box.x + (input_box.rect.width - text_width) // 2
    text_y = input_box.y + (input_box.rect.height - text_height) // 2

    screen.blit(text_surface, (text_x, text_y))

def draw_continue_button(screen, screen_width, is_player_name_valid, input_box, session_data):
    continue_button = session_data['buttons']['continue_button']
    continue_button.move_to(screen_width * 0.8 - continue_button.width // 2, 500)
    screen.blit(
        continue_button.image if is_player_name_valid else continue_button.disable_image,
        (continue_button.x, continue_button.y)
    )
    continue_button.action = lambda session_data: session_data.update({'actual_state': 'class_selection'})

    session_data['active_buttons'] = [input_box, continue_button] if is_player_name_valid else [input_box]
    return session_data

def name_selection(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    player_name = session_data['player_name']
    input_box = session_data['buttons']['input_box']

    is_player_name_valid = player_name and len(player_name) >= 3

    draw_name_ask(screen, screen_width)

    draw_name_input_box(screen, screen_width, screen_height, player_name, input_box)

    draw_continue_button(screen, screen_width, is_player_name_valid, input_box, session_data)

    return session_data
