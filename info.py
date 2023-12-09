import pygame.font

from panel import Panel


class InfoPanel(Panel):
    def __init__(self, surf_size, background_color, max_score, font_color):
        super().__init__(surf_size, background_color)

        # scores
        self.max_score = max_score
        self.score = 0

        # font
        self.__font_color = font_color
        self.__font = pygame.font.Font(pygame.font.get_default_font(), 20)

        # text
        strings = ["Max score:", str(self.max_score), "Score:", str(self.score)]
        self.__text_lines = [self.__font.render(text, True, self.__font_color) for text in strings]
        self.__gaps = self.get_height() - sum(i.get_height() for i in self.__text_lines)

    def score_update(self):
        self.__text_lines[3] = self.__font.render(str(self.score), True, self.__font_color)

    def update(self):
        self.score_update()
        # draw texts
        super().update()
        self.blit(self.__text_lines[0], (24, self.__gaps / 5 * 2))
        self.blit(self.__text_lines[1], (24, self.__gaps / 5 * 2 + self.__text_lines[0].get_height()))
        self.blit(self.__text_lines[2], (24, self.__gaps / 5 * 3 + sum(self.__text_lines[i].get_height() for i in (0, 1))))
        self.blit(self.__text_lines[3], (24, self.__gaps / 5 * 3 + sum(self.__text_lines[i].get_height() for i in (0, 1, 2))))
