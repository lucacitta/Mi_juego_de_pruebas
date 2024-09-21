import pygame

from elements.colors import gray, red, green, blue
from elements.fonts import medium_font
from utils import launch_fight, execute_turn

class Button():
    def __init__(self, name, width, height, color=None, text=None, x=None, y=None, image=None, disable_image=None, font=None):
        self.name = name
        self.width = width
        self.height = height
        self.color = color
        self.actual_color = color
        self.text = text
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (width, height)) if image else None
        self.disable_image = pygame.transform.scale(disable_image, (width, height)) if disable_image else None
        self.font = font if font else medium_font

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        elif self.text:
            text = self.font.render(self.text, True, self.color)
            text_rect = text.get_rect()
            text_rect.center = (self.x + self.width // 2, self.y + self.height // 2)
            screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def action(self): # This method should be overwritten in the actual button
        pass

yes_button = Button(
    name='yes_button',
    width=60,
    height=30,
    image=pygame.image.load("ui/assets/buttons/yes_button.svg")
)

no_button = Button(
    name='no_button',
    width=60,
    height=30,
    image=pygame.image.load("ui/assets/buttons/no_button.svg")
)

continue_button = Button(
    name='continue_button',
    width=150,
    height=40,
    image=pygame.image.load("ui/assets/buttons/continue_button.svg"),
    disable_image=pygame.image.load("ui/assets/buttons/continue_button_disabled.svg")
)

input_box = Button(
    name='input_box',
    width=280,
    height=40,
)

equip_button = Button(
    name='equip_button',
    width=150,
    height=40,
    image=pygame.image.load("ui/assets/buttons/equip_button.svg")
)

discard_button = Button(
    name='discard_button',
    width=150,
    height=40,
    image=pygame.image.load("ui/assets/buttons/discard_button.svg")
)


# Class selection buttons
tank_button = Button(
    name='tank_button',
    width=220,
    height=350,
    image=pygame.image.load("ui/assets/backgrounds/class_choice.png")
)

soldier_button = Button(
    name='soldier_button',
    width=220,
    height=350,
    image=pygame.image.load("ui/assets/backgrounds/class_choice.png")
)

assasin_button = Button(
    name='assasin_button',
    width=220,
    height=350,
    image=pygame.image.load("ui/assets/backgrounds/class_choice.png")
)


# Path selection buttons
strong_fight_button = Button(
    name='strong_fight_button',
    width=150,
    height=150,
    color = gray,
    image=pygame.image.load("ui/assets/buttons/strong_fight_button.png")
)
strong_fight_button.action = lambda session_data: launch_fight(session_data, 'strong')

weak_fight_button = Button(
    name='weak_fight_button',
    width=150,
    height=150,
    color = gray,
    image=pygame.image.load("ui/assets/buttons/weak_fight_button.png")
)
weak_fight_button.action = lambda session_data: launch_fight(session_data, 'weak')

event_button = Button(
    name='event_button',
    width=145,
    height=145,
    color = gray,
    image=pygame.image.load("ui/assets/buttons/event_button.png"),
)

chest_button = Button(
    name='chest_button',
    width=140,
    height=140,
    color = gray,
    image=pygame.image.load("ui/assets/buttons/chest_button.png"),
)
chest_button.action = lambda session_data: session_data.update({'actual_state': 'chest'})

rest_button = Button(
    name='rest_button',
    width=130,
    height=160,
    color = gray,
    image=pygame.image.load("ui/assets/buttons/rest_button.png"),
)
rest_button.action = lambda session_data: session_data.update({'actual_state': 'rest'})

recharge_button = Button(
    name='recharge_button',
    width=120,
    height=150,
    color = gray,
    image=pygame.image.load("ui/assets/buttons/recharge_button.png"),
)
recharge_button.action = lambda session_data: session_data.update({'actual_state': 'recharge'})

store_button = Button(
    name='store_button',
    width=120,
    height=150,
    color = gray,
    image=pygame.image.load("ui/assets/buttons/store_button.png"),
)

# Action buttons

attack_button = Button(
    name='attack_button',
    width=174,
    height=45,
    text='Atacar',
    color = red
)
attack_button.action = lambda session_data: execute_turn(session_data, 'attack')

potion_button = Button(
    name='potion_button',
    width=174,
    height=45,
    text='Pocion',
    color = green
)
potion_button.action = lambda session_data: execute_turn(session_data, 'potion')

escape_button = Button(
    name='escape_button',
    width=174,
    height=45,
    text='Huir',
    color = blue
)
escape_button.action = lambda session_data: execute_turn(session_data, 'escape')

def load_buttons():
    return {
        'yes_button': yes_button,
        'no_button': no_button,
        'continue_button': continue_button,
        'input_box': input_box,
        'equip_button': equip_button,
        'discard_button': discard_button,

        'tank_button': tank_button,
        'soldier_button': soldier_button,
        'assasin_button': assasin_button,

        'strong_fight_button': strong_fight_button,
        'weak_fight_button': weak_fight_button,
        'event_button': event_button,
        'chest_button': chest_button,
        'rest_button': rest_button,
        'recharge_button': recharge_button,
        'store_button': store_button,

        'attack_button': attack_button,
        'potion_button': potion_button,
        'escape_button': escape_button
    }
