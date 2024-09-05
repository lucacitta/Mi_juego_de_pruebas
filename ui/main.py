import sys

import pygame
pygame.init()

from states.class_selection import class_selection
from states.name_selection import name_selection
from states.path_selection import path_selection
from elements.status_bar import draw_status_bar
from elements.buttons import load_buttons
from states.introduction import introduction
from states.setup import setup

from states.paths import rest, chest, recharge


class Game():
    def __init__(self, screen, screen_width, screen_height, background_image, states, session_data):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_image = background_image
        self.states = states
        self.session_data = session_data

    def _event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.session_data['active_buttons']:
                    if button.rect.collidepoint(event.pos):
                        button.action(session_data)
                    elif self.session_data['text_input_active']:
                        self.session_data['text_input_active'] = False
            if event.type == pygame.KEYDOWN:
                    if self.session_data['text_input_active']:
                        if event.key == pygame.K_RETURN:
                            self.session_data['text_input_active'] = False
                            self.session_data['actual_state'] = 'class_selection'
                        elif event.key == pygame.K_BACKSPACE:
                            self.session_data['player_name'] = self.session_data['player_name'][:-1]
                        else:
                            if len(self.session_data['player_name']) < 15: 
                                self.session_data['player_name'] += event.unicode

    def game_loop(self):
        while True:
            screen.blit(self.background_image, (0, 0))

            self._event_handler()

            actual_state_function = self.states[self.session_data['actual_state']]
            self.session_data = actual_state_function(self.session_data)

            if self.session_data['show_status_bar']:
                if self.session_data['is_first_time']:
                    self.session_data['is_first_time'] = False
                    from source.seres import Protagonista
                    hero = Protagonista(
                        nombre=session_data['player_name'],
                        clase='asesino'
                    )
                    hero.ActualizarStats()
                    session_data['hero'] = hero
                    session_data['hero'].vidaPerdida = 20
                    session_data['hero'].ActualizarStats()
                    session_data['player_image'] = f'ui/assets/classes/assasin.png'
                    session_data['player_name'] = 'Luca'
                self.session_data = draw_status_bar(self.session_data)

            # Update screen
            pygame.display.flip()
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")

if __name__ == '__main__':

    screen, screen_width, screen_height, background_image = setup()

    states = {
        'introduction': introduction,
        'name_selection': name_selection,
        'class_selection': class_selection,
        'path_selection': path_selection,

        # paths
        'rest': rest,
        'chest': chest,
        'recharge': recharge,
    }

    session_data = {

        'is_first_time': True, #for testing purposes

        # 'actual_state': 'introduction',
        'actual_state': 'path_selection',
        'screen': screen,
        'background_image': background_image,
        'buttons':load_buttons(),
        'active_buttons': [],
        'show_introduction': False,
        'text_input_active': False,
        'player_name': '',
        'show_status_bar': True, #True for testing purposes
        'road_choices_made': 0,
        'tmp': {},
    }

    game = Game(
        screen=screen,
        screen_width=screen_width,
        screen_height=screen_height,
        background_image=background_image,
        states=states,
        session_data=session_data,
    )

    game.game_loop()
