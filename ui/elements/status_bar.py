import pygame

from elements.fonts import big_font, small_medium_font
from elements.colors import black
from utils import draw_text, convert_to_grayscale


def draw_status_bar(session_data):
    screen = session_data['screen']
    hero = session_data['hero']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    status_bar_x = 0
    status_bar_y = screen_height - 200

    status_bar_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/status_bar.png'),
        (screen_width, 200)
    )
    screen.blit(status_bar_image, (status_bar_x, status_bar_y))


    hero_image = pygame.transform.scale(
        pygame.image.load(session_data['player_image']),
        (100, 165)
    )

    if hero.vida <= 0:
        hero_image = convert_to_grayscale(hero_image)

    screen.blit(hero_image, (status_bar_x + 20, status_bar_y + 20))

    draw_text(
        text=f'{session_data["player_name"]}',
        font=big_font,
        text_color=black,
        surface=screen,
        x=status_bar_x + 200,
        y=status_bar_y + 25,
    )

    draw_text(
        text=f'HP: {hero.vida}/{hero.vidaMaxima}\nDaño: {hero.danio}\nArmadura: {hero.armadura}\nAgilidad: {hero.agilidad}\nPociones: {hero.pociones}/{hero.pocionesMaximas}\nMonedas: {hero.oro}',
        font=small_medium_font,
        text_color=black,
        surface=screen,
        x=status_bar_x + 200,
        y=status_bar_y + 55,
    )

    equipment = [
        {
            'equipment_type': 'weapon',
            'x': status_bar_x + 360,
            'image': 'weapons/sword.png',
        },
        {
            'equipment_type': 'armor',
            'x': status_bar_x + 520,
            'image': 'armors/armor.png',
        },
        {
            'equipment_type': 'ring',
            'x': status_bar_x + 680,
            'image': 'rings/ring.png',
        },
    ]

    for item in equipment:
        item_attributes = hero.get_equipment(item['equipment_type'])

        draw_text(
            text=f'{item["equipment_type"]}',
            font=big_font,
            text_color=black,
            surface=screen,
            x=item['x'],
            y=status_bar_y + 25,
        )

        item_image = pygame.transform.scale(
            pygame.image.load(f'ui/assets/equipment/{item["image"]}'),
            (40, 40)
        )

        screen.blit(item_image, (item['x'] - 20, status_bar_y + 40))

        for key, value in item_attributes.items():
            if key == 'Nombre':
                text = f'Testing name'
            else:
                text += f'\n{key}: {value}'

        draw_text(
            text=text,
            font=small_medium_font,
            text_color=black,
            surface=screen,
            x=item['x'],
            y=status_bar_y + 90,
        )

    return session_data