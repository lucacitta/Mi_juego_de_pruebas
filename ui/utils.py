import pygame
import random

def draw_text(text, font, text_color, surface, x, y, bg_color=None, line_spacing=5):
    # Dividir el texto en líneas si hay saltos de línea o si es muy largo
    lines = text.splitlines()

    for i, line in enumerate(lines):
        textobj = font.render(line, True, text_color)
        textrect = textobj.get_rect(center=(x, y + i * (font.get_height() + line_spacing)))

        # Si se proporciona un color de fondo, dibuja un rectángulo detrás del texto
        if bg_color:
            bg_rect = textrect.inflate(10, 10)
            pygame.draw.rect(surface, bg_color, bg_rect)

        # Dibuja el texto en la superficie
        surface.blit(textobj, textrect)

def road_choices_generator(choices_amount, session_data):
    road_choices = []
    roads = [
        'fight','fight','fight','fight','fight','fight','fight',
        'event','event','event',
        'chest',
        'rest','rest','rest',
        'recharge','recharge','recharge',
        'store','store','store'
    ]
    for i in range(choices_amount):
        road_choice = 'fight' if \
            session_data['road_choices_made'] == 0 and i == 0 else\
            random.choice(roads)

        while i != 0 and road_choice in road_choices:
            road_choice = random.choice(roads)

        road_choices.append(road_choice)

    for i in range(len(road_choices)):
        fight_types = [
            'strong_fight',
            'weak_fight',
        ]
        if road_choices[i] == 'fight':
            road_choices[i] = random.choice(fight_types)

    session_data['road_choices'] = road_choices

    return session_data

def equip_and_go_back_to_path_selection(session_data):
    equipment = session_data['tmp'].pop('equipment')
    session_data['hero'].equip(equipment)
    session_data['actual_state'] = 'path_selection'
    return session_data

def discard_and_go_back_to_path_selection(session_data):
    session_data['tmp'].pop('equipment')
    session_data['actual_state'] = 'path_selection'
    return session_data