import pygame

from elements.fonts import big_font, medium_font
from elements.colors import black, white, gray

from utils import draw_text, road_choices_generator

road_choices_translations = {
    'strong_fight': 'En este camino hay\n un enemigo bastante\nfuerte.',
    'weak_fight': 'En este camino hay\nun enemigo el cual no\nparece muy poderoso',
    'event': 'En este camino hay\nno sabes que te espera.',
    'chest': 'Ves un cofre dorado\nen la lejanía.',
    'rest': 'Encuentras un lugar\nseguro para descansar.',
    'recharge': 'Encuentras un caldero\ncon el cual recargar\ntus pociones',
    'store': 'Ves lo que podria\nser un mercader errante',
}

def path_selection(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    buttons = session_data['buttons']
    road_choices = session_data.get('road_choices', [])

    if not road_choices:
        session_data = road_choices_generator(2, session_data)
        # road_choices = ['chest', 'rest']
        session_data['active_buttons'] = []

    button_x = screen_width // 2 - 150
    button_y = 110
    active_buttons = []
    path_choice_image = pygame.transform.scale(
        pygame.image.load(f'ui/assets/backgrounds/path_choice.png'),
        (260, 300)
    )

    for road_choice in road_choices:

        button_rect = pygame.draw.rect(
            screen,
            gray,
            (
                button_x - 130,
                button_y - 30,
                259,
                300
            )
        )

        screen.blit(path_choice_image, (button_x - 130, button_y - 30))

        draw_text(
            text=road_choices_translations[road_choice],
            font=medium_font,
            text_color=black,
            surface=screen,
            x=button_x,
            y=button_y + 165,
        )

        button = buttons[f'{road_choice}_button']
        button.move_to(
            button_x - button.width // 2,
            button_y
        )
        button.rect = button_rect
        button_x += 300

        button.draw(screen)

        active_buttons.append(button)

    session_data['active_buttons'] = active_buttons

    return session_data