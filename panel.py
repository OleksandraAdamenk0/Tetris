import pygame.surface

from abc import ABC, abstractmethod


class Panel(pygame.Surface, ABC):
    def __init__(self, surf_size, background_color):
        self.__background_color = background_color
        super().__init__(surf_size)

    @abstractmethod
    def update(self):
        self.fill(self.__background_color)
