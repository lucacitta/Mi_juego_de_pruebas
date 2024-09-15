from elements.fonts import big_font, medium_font
from elements.colors import black, white
from utils import draw_text

def rest(session_data):
    screen = session_data['screen']
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    continue_button = session_data['buttons']['continue_button']

    draw_text(
        'Welcum to the rest',
        big_font,
        black,
        screen,
        screen_width // 2,
        100,
        white
    )

    draw_text(
        'Decides descansar junto a la hoguera, recuperando toda tu vida\ny poniendote de buen humor\nes importante estar de buen humor...',
        medium_font,
        black,
        screen,
        screen_width // 2,
        250,
        white
    )

    session_data['hero'].rest()

    continue_button.move_to(
        screen_width * 0.85 - continue_button.width // 2,
        screen_height * 0.65 - continue_button.height // 2
    )
    screen.blit(
        continue_button.image,
        (continue_button.x, continue_button.y)
    )
    continue_button.action = lambda session_data: session_data.update({
        'actual_state':'path_selection',
        'road_choices_remaining': session_data['road_choices_remaining'] - 1
        }
    )
    session_data['active_buttons'] = [continue_button]

    return session_data