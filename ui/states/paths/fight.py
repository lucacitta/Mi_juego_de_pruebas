import pygame

from elements.fonts import big_font, medium_font, tiny_font
from elements.colors import black, tan, disabled_green, disabled_blue, green, blue, red, disabled_red
from utils import draw_text, convert_to_grayscale

def draw_enemy(screen, screen_width, screen_height, enemy):
    enemy_rect_x = screen_width // 2.2 - 15
    enemy_rect_y = (screen_height * 0.17) - 80

    enemy_box_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/enemy_box.png'),
        (420, 300)
    )

    screen.blit(enemy_box_image, (enemy_rect_x, enemy_rect_y))

    draw_text(
        text=enemy.nombre,
        font=medium_font,
        text_color=black,
        surface=screen,
        x=enemy_rect_x + 308,
        y=enemy_rect_y + 43,
    )

    enemy_image = pygame.transform.scale(
        pygame.image.load('ui/assets/enemies/strong/gigante_de_escarcha.png'),
        (175, 225)
    )
    if enemy.vida <= 0:
        enemy_image = convert_to_grayscale(enemy_image)

    screen.blit(enemy_image, (enemy_rect_x + 20, enemy_rect_y + 25))

    draw_text(
        text=f'Estadisticas:\n\nHP: {enemy.vida}/{enemy.vidaMaxima}\nAtk: {enemy.danio}\nDef: {enemy.armadura}\nDex: {enemy.agilidad}',
        font=medium_font,
        text_color=black,
        surface=screen,
        x=enemy_rect_x + 311,
        y=enemy_rect_y + 105,
    )

def draw_action_buttons(session_data, screen, screen_width, screen_height):
    hero = session_data['hero']
    enemy = session_data['actual_enemy']
    action_rect_x = screen_width * 0.05
    action_rect_y = screen_height * 0.285

    action_box_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/action_box.png'),
        (200, 200)
    )
    screen.blit(action_box_image, (action_rect_x, action_rect_y))

    # Attack button
    attack_button = session_data['buttons']['attack_button']
    attack_button.move_to(
        action_rect_x + 13,
        action_rect_y + 18
    )
    attack_button.color = red
    session_data['active_buttons'] = [attack_button]
    attack_button.draw(screen)

    # Potion button
    potion_button = session_data['buttons']['potion_button']
    potion_button.move_to(
        action_rect_x + 13,
        action_rect_y + 79
    )
    if (
        hero.pociones <= 0 or
        hero.vida == hero.vidaMaxima or
        session_data['tmp'].get('fight_finished', False)
    ):
        potion_button.color = disabled_green
    else:
        potion_button.color = green
        session_data['active_buttons'].append(potion_button)
    potion_button.draw(screen)

    # Escape button
    escape_button = session_data['buttons']['escape_button']
    escape_button.move_to(
        action_rect_x + 13,
        action_rect_y + 135
    )
    if(
        False
        # or enemy.is_boss: TODO
    ):
        escape_button.color = disabled_blue
    else:
        escape_button.color = blue
        session_data['active_buttons'].append(escape_button)
    escape_button.draw(screen)

def split_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    return lines

def draw_fight_logs(session_data, screen):
    logs_box_rect_x = 10
    logs_box_rect_y = 10

    logs_box_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/logs_box.png'),
        (300, 150)
    )
    
    if fight_log := session_data['tmp'].get('fight_log', []):

        logs_y = logs_box_rect_y + 15

        screen.blit(logs_box_image, (logs_box_rect_x, logs_box_rect_y))

        for log in fight_log:
            lines = split_text(log, tiny_font, logs_box_image.get_width() - 20)
            
            for line in lines:
                log_surface = tiny_font.render(line, True, black)
                screen.blit(log_surface, (logs_box_rect_x + 10, logs_y))
                logs_y += log_surface.get_height() + 8

            pygame.draw.line(
                screen,
                tan,
                (logs_box_rect_x + 20, logs_y),
                (logs_box_rect_x + logs_box_image.get_width() - 20, logs_y),
                1
            )

def draw_after_fight_message(session_data, screen, screen_width, screen_height):
    hero = session_data['hero']
    enemy = session_data['actual_enemy']
    after_fight_rect_x = screen_width * 0.02
    after_fight_rect_y = (screen_height * 0.17) - 80
    continue_button = session_data['buttons']['continue_button']

    after_fight_box_image = pygame.transform.scale(
        pygame.image.load('ui/assets/backgrounds/vertical_message.png'),
        (300, 300)
    )
    after_fight_bot_width = after_fight_box_image.get_width()
    screen.blit(after_fight_box_image, (after_fight_rect_x, after_fight_rect_y))

    gold_earned = session_data['tmp'].get('gold_earned', 0)
    texts = {
        'win': {
            'title': 'Victoria!',
            'text': f'Has derrotado a \nj{enemy.nombre}!\n\nOro obtenido: {gold_earned}',
        },
        'death': {
            'title': 'Derrota...',
            'text': f'Has sido derrotado por \n{enemy.nombre}...', 
        },
        'escape': {
            'title': 'Huida!',
            'text': 'Has logrado escapar\n de la pelea...',
        }
    }

    draw_text(
        text=texts[session_data['tmp']['reason']]['title'],
        font=big_font,
        text_color=black,
        surface=screen,
        x=after_fight_rect_x + 150,
        y=after_fight_rect_y + 30,
    )

    draw_text(
        text=texts[session_data['tmp']['reason']]['text'],
        font=medium_font,
        text_color=black,
        surface=screen,
        x=after_fight_rect_x + 150,
        y=after_fight_rect_y + 85,
    )

    continue_button.move_to(
        after_fight_rect_x + 150 - continue_button.width // 2,
        after_fight_rect_y + 200
    )

    screen.blit(
        continue_button.image,
        (continue_button.x, continue_button.y)
    )
    continue_button.action = lambda session_data: session_data.update({'actual_state': 'path_selection', 'tmp': {}})
    session_data['active_buttons'] = [continue_button]

def fight(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    enemy = session_data['actual_enemy']
    fight_finished = session_data['tmp'].get('fight_finished', False)

    draw_enemy(screen, screen_width, screen_height, enemy)
    draw_fight_logs(session_data, screen)

    if not fight_finished:
        draw_action_buttons(session_data, screen, screen_width, screen_height)
    else:
        draw_after_fight_message(session_data, screen, screen_width, screen_height)
    return session_data