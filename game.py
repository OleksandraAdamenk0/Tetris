from pygame.math import Vector2 as v

from active_figure import ActiveFigure
from static_figure import StaticFigure
from panel import Panel
from consts import EL_SIZE


class GamePanel(Panel):
    def __init__(self, surf_size, background_color, score):
        super().__init__(surf_size, background_color)
        # score
        self.score = score

        # map
        self.map_sizes = v(surf_size[0] / EL_SIZE, surf_size[1] / EL_SIZE)
        self.map = [[0 for cell in range(int(self.map_sizes.x))] for row in range(int(self.map_sizes.y))]

        # figures
        self.figures = [ActiveFigure(EL_SIZE)]
        self.active_figure = self.figures[-1]

        # movement
        self.movement_vector = v(0, 1)
        self.movement_counter = 0
        self.speed = 16
        self.rotation = False

    def spawn_figure(self):
        self.figures.append(ActiveFigure(EL_SIZE))
        self.active_figure = self.figures[-1]

    def check_timer(self) -> bool:
        if self.movement_counter != self.speed:
            self.movement_counter += 1
            return False
        self.movement_counter = 0
        return True

    def check_horizontal_bounds(self, pos):
        return False if pos == -1 or pos == self.map_sizes.x else True

    def check_vertical_bound(self, pos):
        return False if pos == self.map_sizes.y else True

    def apply_vertical_movement(self):

        # check collision
        for cords in self.active_figure.get_cords():
            cords.y += self.movement_vector.y

            # bounds and other figures
            if not self.check_vertical_bound(cords.y) or (cords.y >= 0 and self.map[int(cords.y)][int(cords.x)]):
                self.movement_vector.y = 0
                return

        # move
        self.active_figure.move(v(0, self.movement_vector.y))

    def apply_horizontal_movement(self):

        # check collision
        for cords in self.active_figure.get_cords():
            cords.x += self.movement_vector.x

            if not self.check_horizontal_bounds(cords.x): return  # bounds
            if self.map[int(cords.y)][int(cords.x)]: return  # other figures

        # move
        self.active_figure.move(v(self.movement_vector.x, 0))
        self.movement_vector.x = 0

    def check_full_row(self):
        for index, row in enumerate(reversed(self.map)):
            if all(el == 1 for el in row):
                self.score += 1
                return len(self.map) - index - 1
            if all(el == 0 for el in row):
                return None
        return None

    def delete_row(self, index):
        for figure in self.figures:
            new_cords = [cords for cords in figure.get_cords() if cords.y != index]
            new_cords = [cords + v(0, 1) if cords.y < index else cords for cords in new_cords]
            figure.set_cords(new_cords)

        self.map.pop(index)
        self.map.insert(0, [0 for i in self.map[1]])

    def ground_figure(self):
        for cords in self.active_figure.get_cords():
            self.map[int(cords.y)][int(cords.x)] = 1
        self.figures.remove(self.active_figure)
        self.figures.append(StaticFigure(self.active_figure.ps, self.active_figure.parts, self.active_figure.color))

        full_row_index = self.check_full_row()
        while full_row_index:
            self.delete_row(full_row_index)
            full_row_index = self.check_full_row()

    def check_grounding(self):
        if self.movement_vector.y != 0: return

        # check slicing from ground
        self.movement_vector.y = 1
        self.apply_vertical_movement()
        self.apply_horizontal_movement()

        if self.movement_vector.y != 0: return

        self.ground_figure()
        self.spawn_figure()
        self.movement_vector.y = 1

    def apply_movement(self):
        # check timer
        if not self.check_timer(): return
        # check grounding
        self.check_grounding()
        # move
        self.apply_vertical_movement()
        self.apply_horizontal_movement()

    def apply_rotation(self):
        if not self.rotation: return
        self.rotation = False
        rotated_figure_cords = self.active_figure.get_rotated_figure()
        for cords in rotated_figure_cords:

            if not self.check_vertical_bound(cords.y): return  # vertical bounds
            if not self.check_horizontal_bounds(cords.x): return  # horizontal bounds
            if self.map[int(cords.y)][int(cords.x)]: return  # other figures

        self.active_figure.set_cords(rotated_figure_cords)
        self.active_figure.set_next_mode()

    def clean_figures(self):
        for figure in self.figures:
            if not figure.get_cords():
                self.figures.remove(figure)

    def update(self):
        self.apply_rotation()
        self.apply_movement()
        self.clean_figures()

        super().update()
        for fig in self.figures:
            fig.draw(self)
