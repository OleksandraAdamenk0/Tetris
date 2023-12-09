import copy
import random

from figure import Figure
from pygame.math import Vector2 as v
from consts import SPAWN_CORDS, fig_1, fig_2, fig_3, fig_4, fig_5, fig_6, fig_7, fig_8, fig_9


def get_variant(variant):
    variants = [fig_1, fig_2, fig_3, fig_4, fig_5, fig_6, fig_7, fig_8, fig_9]
    return variants[variant]


class ActiveFigure(Figure):
    def __init__(self, part_size):
        self.__variants = get_variant(random.randint(0, 8))
        self.mode = 0

        super().__init__(part_size, self.__variants(v(SPAWN_CORDS))[self.mode])

    def move(self, vector: v):
        for part in self.parts:
            part += vector

    def get_rotated_figure(self):
        next_mode = self.mode + 1 if self.mode + 1 < 4 else 0
        return copy.deepcopy(self.__variants(self.parts[0])[next_mode])

    def set_next_mode(self):
        self.mode = self.mode + 1 if self.mode + 1 < 4 else 0
