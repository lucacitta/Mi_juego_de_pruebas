import pygame

from elements.fonts import big_font, medium_font, small_font
from elements.colors import black, white
from utils import draw_text

def draw_title(screen, screen_width):
    title_box_rect_x = screen_width // 2 - 200
    title_box_rect_y = 20
    title_box_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/horizontal_message.png'),
        (400, 40)
    )
    screen.blit(
        title_box_image,
        (
            title_box_rect_x,
            title_box_rect_y
        )
    )
    draw_text(
        'Inserte un buen nombre',
        big_font,
        black,
        screen,
        title_box_rect_x + 200,
        title_box_rect_y + 20
    )

def draw_skip_intro(screen, screen_width, screen_height, session_data):
    yes_button = session_data['buttons']['yes_button']
    no_button = session_data['buttons']['no_button']
    skip_intro_box_rect_x = screen_width // 2 - 175
    skip_intro_box_rect_y = screen_height // 2 - 50
    skip_intro_box_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/horizontal_message.png'),
        (350, 100)
    )
    screen.blit(
        skip_intro_box_image,
        (
            skip_intro_box_rect_x,
            skip_intro_box_rect_y
        )
    )
    draw_text(
        'Saltar introduccion',
        medium_font,
        black,
        screen,
        skip_intro_box_rect_x + 175,
        skip_intro_box_rect_y + 25
    )
    #yes button
    yes_button.move_to(
        skip_intro_box_rect_x + 100,
        skip_intro_box_rect_y + 50
    )
    yes_button.action = lambda session_data: session_data.update({'actual_state': 'name_selection'})
    screen.blit(
        yes_button.image,
        (yes_button.x, yes_button.y)
    )

    #no button
    no_button.move_to(
        skip_intro_box_rect_x + 200,
        skip_intro_box_rect_y + 50
    )
    no_button.action = lambda session_data: session_data.update({'show_introduction': True})
    screen.blit(
        no_button.image,
        (no_button.x, no_button.y)
    )

    session_data['active_buttons'] = [yes_button, no_button]
    return session_data

def draw_intro_text(screen, screen_width, screen_height, session_data):
    continue_button = session_data['buttons']['continue_button']

    intro_box_x = screen_width // 2 - 300
    intro_box_y = screen_height // 2 - 175
    intro_box_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/horizontal_message.png'),
        (600, 350)
    )
    screen.blit(
        intro_box_image,
        (
            intro_box_x,
            intro_box_y
        )
    )

    draw_text(
        'Bienvenido a "Inserte un buen nombre" por Luca Cittá Giordano.\n\n'
        'Este juego es un proyecto para poner en practica mis \n'
        'conocimientos en python, finalmente, se agrego interfaz grafica.\n\n'
        'El objetivo es lograr vencer al jefe de la mazmorra, \n'
        'para eso deberas explorar la misma hasta llegar a el.\n'
        'Todo se genera de manera aleatoria, recomiendo varios intentos.\n\n'
        'Hay mas de 20 piezas de equipamiento, mas de 20 enemigos \n'
        '(incluidos varios jefes finales) y varios caminos a elegir.\n'
        'Es posible que haya algun bug, se agradece el aviso para solucionarlo.\n'
        'Ahora si, que lo disfrutes :) \n',
        small_font,
        black,
        screen,
        intro_box_x + 300,
        intro_box_y + 40
    )
        

    continue_button.move_to(screen_width * 0.8 - continue_button.width // 2, 500)
    screen.blit(
        continue_button.image,
        (continue_button.x, continue_button.y)
    )
    continue_button.action = lambda session_data: session_data.update({'actual_state': 'name_selection'})
    session_data['active_buttons'] = [continue_button]    
    return session_data    

def introduction(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    show_introduction = session_data['show_introduction']

    draw_title(screen, screen_width)

    session_data = draw_intro_text(screen, screen_width, screen_height, session_data) \
        if show_introduction \
        else draw_skip_intro(screen, screen_width, screen_height, session_data)

    return session_data