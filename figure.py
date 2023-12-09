import copy
import random

import pygame.surface

from pygame.math import Vector2 as v
from typing import List
from consts import COLORS


class Figure:
    def __init__(self, part_size, parts, color=None):
        self.ps = part_size
        self.parts = parts
        self.color = COLORS.get("figures")[random.randint(0, 6)] if not color else color

    def draw(self, surface: pygame.Surface):
        for part in self.parts:
            pygame.draw.rect(surface, self.color, pygame.Rect(part.x * self.ps, part.y * self.ps, self.ps, self.ps))

    def get_cords(self) -> List[v]:
        return copy.deepcopy(self.parts)

    def set_cords(self, new_cords):
        self.parts = new_cords
