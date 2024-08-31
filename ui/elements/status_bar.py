import pygame

from elements.fonts import medium_font, big_font, small_medium_font
from utils import draw_text


def draw_status_bar(session_data):
    screen = session_data['screen']
    hero = session_data['hero']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    status_bar_x = 0
    status_bar_y = screen_height - 180

    pygame.draw.rect(
        screen, (0, 0, 0),
        (
            status_bar_x,
            status_bar_y,
            screen_width,
            180
        )
    )

    hero_image = pygame.transform.scale(
        pygame.image.load(session_data['player_image']),
        (100, 165)
    )
    screen.blit(hero_image, (status_bar_x + 10, status_bar_y + 10))

    draw_text(
        text=f'{session_data["player_name"]}',
        font=big_font,
        text_color=(255, 255, 255),
        surface=screen,
        x=status_bar_x + 200,
        y=status_bar_y + 20,
    )

    draw_text(
        text=f'HP: {hero.vida}/{hero.vidaMaxima}\nDaño: {hero.danio}\nArmadura: {hero.armadura}\nAgilidad: {hero.agilidad}\nPociones: {hero.pociones}/{hero.pocionesMaximas}\Monedas: {hero.oro}',
        font=small_medium_font,
        text_color=(255, 255, 255),
        surface=screen,
        x=status_bar_x + 200,
        y=status_bar_y + 50,
    )

    equipment = [
        {
            'type': 'Arma',
            'x': status_bar_x + 360,
            'image': 'weapons/sword.png',
        },
        {
            'type': 'Armadura',
            'x': status_bar_x + 520,
            'image': 'armors/armor.png',
        },
        {
            'type': 'Anillo',
            'x': status_bar_x + 680,
            'image': 'rings/ring.png',
        },
    ]

    for item in equipment:
        item_attributes = hero.get_equipment(item['type'])

        item_image = pygame.transform.scale(
            pygame.image.load(f'ui/assets/equipment/{item["image"]}'),
            (40, 40)
        )

        screen.blit(item_image, (item['x'] - 20, status_bar_y + 20 + 10))

        for key, value in item_attributes.items():
            if key == 'Nombre':
                text = f'{value}'
            else:
                text += f'\n{key}: {value}'

        draw_text(
            text=f'{item["type"]}',
            font=big_font,
            text_color=(255, 255, 255),
            surface=screen,
            x=item['x'],
            y=status_bar_y + 20,
        )

        draw_text(
            text=text,
            font=small_medium_font,
            text_color=(255, 255, 255),
            surface=screen,
            x=item['x'],
            y=status_bar_y + 80,
        )

    return session_data