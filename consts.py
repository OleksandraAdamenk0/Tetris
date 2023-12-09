from pygame.math import Vector2 as v

FPS = 60
EL_SIZE = 40
SPAWN_CORDS = (4, -1)
SCORE_FILE_NAME = "maxScore.txt"

SIZES = {
    "window": (375, 812),
    "info": (320, 160),
    "game": (320, 600)
}

CORDS = {
    "info": (26, 26),
    "game": (26, 212)
}

COLORS = {
    "background": (13, 13, 13),
    "info-background": (25, 35, 35),
    "game-background": (44, 52, 52),
    "figures": [(225, 53, 53), (200, 85, 25), (205, 165, 25), (25, 230, 25), (40, 125, 110), (40, 50, 120), (100, 40, 120)],
    "font": (255, 255, 255)
}


def fig_1(xy):
    return [
        [xy, xy + v(0, -1), xy + v(1, 0)],
        [xy, xy + v(1, 0), xy + v(0, 1)],
        [xy, xy + v(0, 1), xy + v(-1, 0)],
        [xy, xy + v(-1, 0), xy + v(0, -1)]
    ]


def fig_2(xy):
    return [
        [xy, xy + v(0, -1), xy + v(-1, 0), xy + v(-1, -1)],
        [xy, xy + v(0, -1), xy + v(-1, 0), xy + v(-1, -1)],
        [xy, xy + v(0, -1), xy + v(-1, 0), xy + v(-1, -1)],
        [xy, xy + v(0, -1), xy + v(-1, 0), xy + v(-1, -1)]
    ]


def fig_3(xy):
    return [
        [xy, xy + v(0, -1), xy + v(0, -2), xy + v(0, -3)],
        [xy, xy + v(1, 0), xy + v(2, 0), xy + v(3, 0)],
        [xy, xy + v(0, 1), xy + v(0, 2), xy + v(0, 3)],
        [xy, xy + v(-1, 0), xy + v(-2, 0), xy + v(-3, 0)]
    ]


def fig_4(xy):
    return [
        [xy, xy + v(0, -1), xy + v(0, -2), xy + v(0, -3), xy + v(1, 0)],
        [xy, xy + v(1, 0), xy + v(2, 0), xy + v(3, 0), xy + v(0, 1)],
        [xy, xy + v(0, 1), xy + v(0, 2), xy + v(0, 3), xy + v(-1, 0)],
        [xy, xy + v(-1, 0), xy + v(-2, 0), xy + v(-3, 0), xy + v(0, -1)]
    ]


def fig_5(xy):
    return [
        [xy, xy + v(0, -1), xy + v(1, 0), xy + v(0, 1)],
        [xy, xy + v(1, 0), xy + v(0, 1), xy + v(-1, 0)],
        [xy, xy + v(0, 1), xy + v(-1, 0), xy + v(0, -1)],
        [xy, xy + v(-1, 0), xy + v(0, -1), xy + v(1, 0)]
    ]


def fig_6(xy):
    return [
        [xy, xy + v(0, 1), xy + v(-1, 0), xy + v(-1, -1)],
        [xy, xy + v(1, 0), xy + v(0, 1), xy + v(-1, 1)],
        [xy, xy + v(0, 1), xy + v(-1, 0), xy + v(-1, -1)],
        [xy, xy + v(1, 0), xy + v(0, 1), xy + v(-1, 1)]
    ]


def fig_7(xy):
    return [
        [xy],
        [xy],
        [xy],
        [xy]
    ]


def fig_8(xy):
    return [
        [xy, xy + v(0, -1), xy + v(-1, 0), xy + v(-1, 1)],
        [xy, xy + v(-1, 0), xy + v(0, 1), xy + v(1, 1)],
        [xy, xy + v(0, -1), xy + v(-1, 0), xy + v(-1, 1)],
        [xy, xy + v(-1, 0), xy + v(0, 1), xy + v(1, 1)]
    ]


def fig_9(xy):
    return [
        [xy, xy + v(0, -1), xy + v(0, -2), xy + v(0, -3), xy + v(-1, 0)],
        [xy, xy + v(1, 0), xy + v(2, 0), xy + v(3, 0), xy + v(0, -1)],
        [xy, xy + v(0, 1), xy + v(0, 2), xy + v(0, 3), xy + v(1, 0)],
        [xy, xy + v(-1, 0), xy + v(-2, 0), xy + v(-3, 0), xy + v(0, 1)]
    ]

