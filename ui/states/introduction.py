import pygame

from elements.buttons import yes_button, no_button, continue_button
from elements.fonts import big_font, small_font
from elements.colors import black, white
from utils import draw_text

def introduction(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    background_image = session_data['background_image']
    show_introduction = session_data['show_introduction']

    if show_introduction:
        screen.blit(
            background_image,
            (0, 0)
        )
        draw_text('Bienvenido a "Inserte un buen nombre" por Luca Cittá Giordano.\n\n'
        'Este juego es un proyecto para poner en practica mis conocimientos en python, mas adelante se agregara interfaz grafica.\n\n'
        'El objetivo es lograr vencer al jefe de la mazmorra, para eso deberas explorar la misma hasta llegar a el.\n'
        'Todo se genera de manera aleatoria, recomiendo varios intentos.\n'
        'Hay mas de 20 piezas de equipamiento, mas de 20 enemigos (incluidos varios jefes finales) y varios caminos a elegir.\n'
        'Es posible que haya algun fallo, ya sea tipeo o de codigo, de encontrar alguno, se agradece el aviso para solucionarlo.\n'
        'Ahora si, que lo disfrutes :) \n', small_font, black, screen, screen_width // 2, 250, white)

        continue_button.move_to(screen_width * 0.8 - continue_button.width // 2, 500)
        screen.blit(
            continue_button.image,
            (continue_button.x, continue_button.y)
        )
        continue_button.action = lambda session_data: session_data.update({'actual_state': 'name_selection'})
        session_data['active_buttons'] = [continue_button]

    else:
        draw_text('Welcum to the game', big_font, black, screen, screen_width // 2, 100, white)
        draw_text('Saltar introduccion?', big_font, black, screen, screen_width // 2, 250)

        #yes button
        yes_button.move_to(
            (screen_width // 2) - (yes_button.width // 2),
            screen_height - 100
        )
        yes_button.action = lambda session_data: session_data.update({'actual_state': 'name_selection'})
        screen.blit(
            yes_button.image,
            (yes_button.x, yes_button.y)
        )

        #no button
        no_button.move_to(
            (screen_width // 2) - (no_button.width // 2) + 100,
            screen_height - 100
        )
        no_button.action = lambda session_data: session_data.update({'show_introduction': True})
        screen.blit(
            no_button.image,
            (no_button.x, no_button.y)
        )

        session_data['active_buttons'] = [yes_button, no_button]

    return session_data