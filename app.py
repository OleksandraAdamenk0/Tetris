import os
from typing import List

import pygame

from consts import SIZES, COLORS, FPS, CORDS, SPAWN_CORDS, SCORE_FILE_NAME
from game import GamePanel
from info import InfoPanel


def file_reader(file_name):
    with open(file_name, "r") as file:
        return file.read()


def file_writer(file_name, data):
    with open(file_name, "w") as file:
        file.write(data)


def check_keys(e: List[pygame.event.Event], keys: List[int]) -> List:
    result = [0 for i in keys]
    for i in e:
        for ind, type_num in enumerate(keys):
            if i.key == type_num:
                result[ind] = 1
    return result


class App:
    def __init__(self):
        # modes
        self.play_mode = True
        self.pause_mode = False
        self.game_over_mode = False
        self.restart_cmd = False

        # keyboard keys
        self.K_Left = False
        self.K_Right = False

        # pygame setups
        pygame.init()
        self.window = pygame.display.set_mode(SIZES.get("window"))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris game")
        pygame.display.set_icon(pygame.image.load(os.path.join('img', 'icon.png')))

        # output setings
        self.font = pygame.font.Font(pygame.font.get_default_font(), 48)
        self.pause_text = self.font.render("Pause", True, COLORS.get("font"))
        self.game_over_text = self.font.render("Game over", True, COLORS.get("font"))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.restart_text = self.font.render("Press enter to restart", True, COLORS.get("font"))

        self.info = InfoPanel(SIZES.get("info"), COLORS.get("info-background"), int(file_reader(SCORE_FILE_NAME)),
                              COLORS.get("font"))
        self.game = GamePanel(SIZES.get("game"), COLORS.get("game-background"), self.info.score)
        self.mode_handler()

    def check_event(self, e: List[pygame.event.Event]):
        for event in e:

            # check windows closing
            if event.type == pygame.QUIT:
                self.write_score()
                pygame.quit()
                quit()

            # keyboard
            if event.type == pygame.KEYDOWN:
                # pause
                if any(event.key == i for i in (pygame.K_ESCAPE, pygame.K_BACKSPACE, pygame.K_RETURN)):
                    self.pause_mode = not self.pause_mode
                    self.play_mode = not self.play_mode

                # left right
                if any(event.key == i for i in (pygame.K_LEFT, pygame.K_a)):
                    self.K_Left = True
                if any(event.key == i for i in (pygame.K_RIGHT, pygame.K_d)):
                    self.K_Right = True

                # rotation
                if event.key == pygame.K_SPACE:
                    if self.play_mode:
                        self.game.rotation = True
                    if self.game_over_mode:
                        self.restart_cmd = True

    def mode_handler(self):
        while True:
            # get events
            events = pygame.event.get()

            # check windows closing and keyboard input
            self.check_event(events)

            # game over check
            if self.game.map[0][SPAWN_CORDS[0] - 1] or self.game.map[0][SPAWN_CORDS[0]] or self.game.map[0][SPAWN_CORDS[0] + 1]:
                self.game_over_mode = True
                self.play_mode = False
                self.play_mode = False
                self.write_score()

            # play mode
            if self.play_mode:
                self.play()

            # pause mode
            if self.pause_mode:
                self.pause()

            # game over mode
            if self.game_over_mode:
                self.game_over()

            # display
            pygame.display.flip()
            self.clock.tick(FPS)

    def play(self):

        # setup figure movement
        if self.K_Left and not self.K_Right:
            self.game.movement_vector.x = -1
            self.K_Left = False
        if self.K_Right and not self.K_Left:
            self.game.movement_vector.x = 1
            self.K_Right = False

        # game logic
        self.game.update()
        self.info.update()

        # score changing
        self.info.score = self.game.score

        # draw
        self.window.fill(COLORS.get("background"))
        self.window.blit(self.game, CORDS.get("game"))
        self.window.blit(self.info, CORDS.get("info"))

    def pause(self):
        self.window.fill(COLORS.get("background"))
        self.window.blit(self.pause_text,
                         ((self.window.get_width() - self.pause_text.get_width()) / 2,
                          (self.window.get_height() - self.pause_text.get_height()) / 2))

    def write_score(self):
        if self.info.score > self.info.max_score:
            file_writer(SCORE_FILE_NAME, str(self.info.score))

    def game_over(self):
        self.window.fill(COLORS.get("background"))
        game_over_text_y = (self.window.get_height() - (self.game_over_text.get_height() + self.restart_text.get_height())) / 2
        restart_text_y = (self.window.get_height() - (self.game_over_text.get_height() + self.restart_text.get_height())) / 2 + self.game_over_text.get_height()
        self.window.blit(self.game_over_text,
                         ((self.window.get_width() - self.game_over_text.get_width()) / 2, game_over_text_y))
        self.window.blit(self.restart_text,
                         ((self.window.get_width() - self.restart_text.get_width()) / 2, restart_text_y))

        if self.restart_cmd:
            self.restart()

    def restart(self):
        self.play_mode = True
        self.pause_mode = False
        self.game_over_mode = False
        self.restart_cmd = False
        self.info = InfoPanel(SIZES.get("info"), COLORS.get("info-background"), int(file_reader(SCORE_FILE_NAME)),
                              COLORS.get("font"))
        self.game = GamePanel(SIZES.get("game"), COLORS.get("game-background"), self.info.score)

