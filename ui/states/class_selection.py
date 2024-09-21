import pygame

from elements.fonts import big_font, medium_font
from elements.colors import black, white
from source.seres import Protagonista
from utils import draw_text

def draw_class_ask(screen, screen_width, screen_height):
    question_box_rect_x = screen_width // 2 - 175
    question_box_rect_y = screen_height // 6
    question_box_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/horizontal_message.png'),
        (400, 40)
    )
    screen.blit(question_box_image, (question_box_rect_x, question_box_rect_y))

    draw_text(
        'Selecciona tu clase',
        big_font,
        black,
        screen,
        question_box_rect_x + 200,
        question_box_rect_y + 20,
    )

def draw_class_selection(screen, screen_width, screen_height, session_data):
    clases = [
        {
            'name': 'Soldado',
            'description': 'Vida inicial: 100\nDaño inicial: 30\nAgilidad inicial: 20\nDefensa inicial: 20\n\n',
            'image': 'soldier.png',
            'text_x': screen_width // 2 + 10,
            'rect_x': screen_width // 2 - 100,
            'button_name': 'soldier_button',
        },
        {
            'name': 'Tanque',
            'description': 'Vida inicial: 150\nDaño inicial: 20\nAgilidad inicial: 10\nDefensa inicial: 40\n\n',
            'image': 'tank.png',
            'text_x': screen_width // 2 + 260,
            'rect_x': screen_width // 2 + 150,
            'button_name': 'tank_button',
        },
        {
            'name': 'Asesino',
            'description': 'Vida inicial: 80\nDaño inicial: 50\nAgilidad inicial: 40\nDefensa inicial: 5\n\n',
            'image': 'assasin.png',
            'text_x': screen_width // 2 - 240,
            'rect_x': screen_width // 2 - 350,
            'button_name': 'assasin_button',
        },
    ]

    session_data['active_buttons'] = []
    for character_class in clases:
        button = session_data['buttons'][character_class['button_name']]
        button.move_to(character_class['rect_x'], screen_height // 2 - 60)
        button.draw(screen)

        draw_text(
            text=character_class['name'],
            font=medium_font,
            text_color=black,
            surface=screen,
            x=character_class['text_x'],
            y=screen_height // 2 - 30,
        )

        image = pygame.image.load(f'ui/assets/classes/{character_class["image"]}')
        image = pygame.transform.scale(image, (100, 165))
        screen.blit(image, (character_class['text_x'] - 50, screen_height // 2 - 10))

        draw_text(
            text=character_class['description'],
            font=medium_font,
            text_color=black,
            surface=screen,
            x=character_class['text_x'],
            y=screen_height // 2 + 170,
        )
    
    #redundant because it was caching the buttons if just define them on the loop
    soldier_button = session_data['buttons']['soldier_button']
    tank_button = session_data['buttons']['tank_button']
    assasin_button = session_data['buttons']['assasin_button']

    soldier_button.action = lambda session_data: initialize_class_selection(session_data, 'soldado')
    tank_button.action = lambda session_data: initialize_class_selection(session_data, 'tanque')
    assasin_button.action = lambda session_data: initialize_class_selection(session_data, 'asesino')

    session_data['active_buttons'] = [soldier_button, tank_button, assasin_button]

def initialize_class_selection(session_data, character_class):
    translation_dict = {
        'soldado': 'soldier',
        'tanque': 'tank',
        'asesino': 'assasin'
    }

    session_data['player_class'] = character_class
    session_data['actual_state'] = 'path_selection'
    session_data['show_status_bar'] = True
    session_data['player_image'] = f'ui/assets/classes/{translation_dict[character_class]}.png'
    hero = Protagonista(
        nombre=session_data['player_name'],
        clase=character_class
    )
    hero.ActualizarStats()
    session_data['hero'] = hero

def class_selection(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    draw_class_ask(screen, screen_width, screen_height)
    draw_class_selection(screen, screen_width, screen_height, session_data)

 

    return session_data
