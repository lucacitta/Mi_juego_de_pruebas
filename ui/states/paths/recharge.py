import pygame

from elements.fonts import medium_font
from elements.colors import black, gray
from utils import draw_text

def recharge(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    continue_button = session_data['buttons']['continue_button']
    recharge_button = session_data['buttons']['recharge_button']
    hero = session_data['hero']
    hero.restore_potions()

    button_x = screen_width // 2
    button_y = 110

    pygame.draw.rect(
        screen,
        gray,
        (
            button_x - 135,
            button_y - 30,
            270,
            315
        )
    )
    screen.blit(
        recharge_button.image,
        (
            button_x - recharge_button.width // 2,
            button_y - 30
        )
    )

    draw_text(
        text=f'Logras rellenar tus viales\n volviendo a tener {hero.pocionesMaximas}\npociones a dispocision.',
        font=medium_font,
        text_color=black,
        surface=screen,
        x=button_x,
        y=button_y + 165,
    )

    continue_button.move_to(
        screen_width * 0.85 - continue_button.width // 2,
        screen_height * 0.65 - continue_button.height // 2
    )
    screen.blit(
        continue_button.image,
        (continue_button.x, continue_button.y)
    )
    continue_button.action = lambda session_data: session_data.update({
            'actual_state': 'path_selection',
            'road_choices_remaining': session_data['road_choices_remaining'] - 1
        }
    )
    session_data['active_buttons'] = [continue_button]

    return session_data