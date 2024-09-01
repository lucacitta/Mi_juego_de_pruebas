import pygame

from elements.fonts import big_font, medium_font, small_medium_font, small_font
from elements.colors import black, white, gray
from utils import draw_text, equip_and_go_back_to_path_selection, discard_and_go_back_to_path_selection

from source.acciones import generate_equipment

def chest(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    discard_button = session_data['buttons']['discard_button']
    equip_button = session_data['buttons']['equip_button']
    equipment = session_data['tmp'].get('equipment')

    if not equipment:
        equipment =  generate_equipment()
        session_data['tmp'] = {'equipment': equipment}

    draw_text(
        f'Al abrir el cofre te encuentras con un objeto',
        big_font,
        black,
        screen,
        screen_width // 2,
        screen_height // 6,
        white
    )

    pygame.draw.rect(
        screen,
        gray,
        (
            screen_width // 2 - 150,
            screen_height // 4.5,
            300,
            200
        )
    )

    item_image = pygame.transform.scale(
        pygame.image.load(f'ui/assets/equipment/{equipment.image}'),
        (70, 70)
    )

    screen.blit(
        item_image,
        (
            screen_width // 2 - item_image.get_width() // 2,
            screen_height // 4.5
        )
    )

    text = ''
    for key, value in equipment.get_attributes_to_user().items():
        if key == 'Nombre':
            pass
        else:
            text += f'\n{key}: {value}'

    draw_text(
        text=f'{equipment.get_attributes_to_user()["Nombre"]}',
        font=big_font,
        text_color=black,
        surface=screen,
        x=screen_width // 2,
        y=screen_height // 4.5 + 80,
    )

    draw_text(
        text=text,
        font=small_medium_font,
        text_color=black,
        surface=screen,
        x=screen_width // 2,
        y=screen_height // 4.5 + 90,
    )

    equip_button.move_to(
        screen_width * 0.85 - equip_button.width // 2,
        screen_height * 0.65 - equip_button.height // 2
    )
    screen.blit(
        equip_button.image,
        (equip_button.x, equip_button.y)
    )
    equip_button.action = lambda session_data: equip_and_go_back_to_path_selection(session_data)
    session_data['active_buttons'] = [equip_button]

    if session_data['hero'].has_equipment_by_type(equipment.equipment_type):
        draw_text(
            text='Si deseas equiparlo, perderás el objeto que ya tienes equipado.',
            font=small_font,
            text_color=black,
            surface=screen,
            x=screen_width * 0.60,
            y=screen_height * 0.6 - 10,
            bg_color=white
        )

        discard_button.move_to(
            screen_width * 0.65 - discard_button.width // 2,
            screen_height * 0.65 - discard_button.height // 2
        )
        screen.blit(
            discard_button.image,
            (discard_button.x, discard_button.y)
        )
        discard_button.action = lambda session_data: discard_and_go_back_to_path_selection(session_data)
        session_data['active_buttons'] += [discard_button]

    return session_data