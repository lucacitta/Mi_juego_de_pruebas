import pygame
import random as r

from source.acciones import generadorEnemigos, ataque, drop

def draw_text(text, font, text_color, surface, x, y, bg_color=None, line_spacing=5, bf_rect=None):
    # Dividir el texto en líneas si hay saltos de línea o si es muy largo
    lines = text.splitlines()

    for i, line in enumerate(lines):
        textobj = font.render(line, True, text_color)
        textrect = textobj.get_rect(center=(x, y + i * (font.get_height() + line_spacing)))

        # Si se proporciona un color de fondo, dibuja un rectángulo detrás del texto
        if bg_color:
            bg_rect = textrect.inflate(10, 10) if bf_rect is None else bf_rect
            pygame.draw.rect(surface, bg_color, bg_rect)

        # Dibuja el texto en la superficie
        surface.blit(textobj, textrect)

def convert_to_grayscale(image):
    grayscale_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            r, g, b, a = image.get_at((x, y))
            gray = int(0.3 * r + 0.59 * g + 0.11 * b)
            grayscale_image.set_at((x, y), (gray, gray, gray, a))
    return grayscale_image

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
            session_data['road_choices_remaining'] == 10 and i == 0 else\
            r.choice(roads)

        while i != 0 and road_choice in road_choices:
            road_choice = r.choice(roads)

        road_choices.append(road_choice)

    for i in range(len(road_choices)):
        fight_types = [
            'strong_fight',
            'weak_fight',
        ]
        if road_choices[i] == 'fight':
            road_choices[i] = r.choice(fight_types)

    session_data['road_choices'] = road_choices

    return session_data

def equip_and_go_back_to_path_selection(session_data):
    equipment = session_data['tmp'].pop('equipment')
    session_data['hero'].equip(equipment)
    session_data['road_choices_remaining'] -= 1
    session_data['actual_state'] = 'path_selection'
    return session_data

def discard_and_go_back_to_path_selection(session_data):
    session_data['tmp'].pop('equipment')
    session_data['actual_state'] = 'path_selection'
    session_data['road_choices_remaining'] -= 1
    return session_data

def launch_fight(session_data, fight_type):
    fight_type_dict = {
        'weak': 'debil',
        'strong': 'fuerte',
    }
    session_data['actual_state'] = 'fight'
    session_data['actual_enemy'] = generadorEnemigos(fight_type_dict[fight_type])
    session_data['tmp'] = {}
    return session_data

def execute_turn(session_data, action):
    hero = session_data['hero']
    enemy = session_data['actual_enemy']

    if action == 'attack':
        if hero.agilidad > enemy.agilidad:
            aux = ((hero.agilidad-enemy.agilidad)/100)
            if (0.5+aux)>r.random():
                session_data['hero'], session_data['actual_enemy'], messages = ataque(heroe=hero,enemigo=enemy, atacando=0)
            else:
                session_data['hero'], session_data['actual_enemy'], messages = ataque(enemigo=enemy,heroe=hero, atacando=1)
        elif hero.agilidad < enemy.agilidad:
            aux = ((enemy.agilidad-hero.agilidad)/100)
            if (aux+0.5)>r.random():
                session_data['hero'], session_data['actual_enemy'], messages = ataque(enemigo=enemy,heroe=hero, atacando=1)
            else:
                session_data['hero'], session_data['actual_enemy'], messages = ataque(heroe=hero,enemigo=enemy, atacando=0)
        else:
            if 0.5 < r.random():
                session_data['hero'], session_data['actual_enemy'], messages = ataque(heroe=hero,enemigo=enemy, atacando=0)
            else:
                session_data['hero'], session_data['actual_enemy'], messages = ataque(enemigo=enemy,heroe=hero, atacando=1)
        
        # Extra attacks
        if hero.agilidad >= enemy.agilidad * 2:
            session_data['hero'], session_data['actual_enemy'], extra_message = ataque(heroe=hero,enemigo=enemy, atacando=4)
        elif enemy.agilidad >= hero.agilidad * 2:
            session_data['hero'], session_data['actual_enemy'], extra_message = ataque(enemigo=enemy, heroe=hero, atacando=5)
        else:
            extra_message = []

        messages += extra_message
    elif action == 'potion':
        hero.use_potion()
        messages = [f'{hero.nombre} ha usado una poción y se ha curado {hero.pocionesCuracion} puntos de vida']
        session_data['hero'], session_data['actual_enemy'], message = ataque(enemigo=enemy, heroe=hero, atacando=2)
        messages += message
    elif action == 'escape':
        scape_extra_chance = (hero.agilidad - enemy.agilidad) / 100
        if (0.5 + scape_extra_chance) < r.random():
            session_data['tmp'] = {'fight_finished': True, 'reason': 'escape'}
            return session_data
        session_data['hero'], session_data['actual_enemy'], messages = ataque(enemigo=enemy, heroe=hero, atacando=3)
    
    if session_data['hero'].vida <= 0:
        session_data['tmp'] = {'fight_finished': True, 'reason': 'death'}
        return session_data
    
    if session_data['actual_enemy'].vida <= 0:
        gold_earned = drop(heroe=hero, enemigo=enemy)
        session_data['tmp'] = {'fight_finished': True, 'reason': 'win', 'gold_earned': gold_earned}
        return session_data

    if session_data['tmp'].get('fight_log') is None:
        session_data['tmp']['fight_log'] = []
    session_data['tmp']['fight_log'] = messages
    return session_data