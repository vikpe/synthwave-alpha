from chromato.operations import blend, shade, tint, hsv_mod
from chromato.spaces import Color

from sa_functions import dark_color_variant

RGB_YELLOW = Color("ffff00")
RGB_WHITE = Color("ffffff")

WHITE = Color("f2f2e3")
BLACK = Color("241b30")
CYAN = Color("00fbfd")
MAGENTA = Color("ff00f6")
BLUE = blend(CYAN, MAGENTA, 1 / 3)
PURPLE = blend(CYAN, MAGENTA, 2 / 3)
YELLOW = blend(WHITE, RGB_YELLOW)

RED = hsv_mod(MAGENTA, 30 / 360, -0.04, -0.1)
GREEN = hsv_mod(CYAN, -18 / 360, -0.04, -0.1)


class Colors:
    WHITE_LIGHT = blend(WHITE, RGB_WHITE)
    WHITE = WHITE
    WHITE_DARKER = Color("7f7094")
    WHITE_DARK = blend(WHITE_DARKER, WHITE)

    BLACK = BLACK
    BLACK_LIGHT = tint(BLACK, 0.1)
    BLACK_DARK = shade(BLACK, 0.3)
    BLACK_DARKER = shade(BLACK, 0.6)

    CYAN = CYAN
    CYAN_DARK = dark_color_variant(CYAN)
    CYAN_DARKER = blend(CYAN_DARK, BLACK)
    CYAN_DARKEST = blend(CYAN_DARKER, BLACK)

    MAGENTA = MAGENTA
    MAGENTA_DARK = dark_color_variant(MAGENTA)
    MAGENTA_DARKER = blend(MAGENTA_DARK, BLACK)
    MAGENTA_DARKEST = blend(MAGENTA_DARKER, BLACK)

    PURPLE = PURPLE
    PURPLE_DARK = dark_color_variant(PURPLE)
    PURPLE_DARKER = blend(PURPLE_DARK, BLACK)
    PURPLE_DARKEST = blend(PURPLE_DARKER, BLACK)

    BLUE = BLUE
    BLUE_DARK = dark_color_variant(BLUE)
    BLUE_DARKER = blend(BLUE_DARK, BLACK)
    BLUE_DARKEST = blend(BLUE_DARKER, BLACK)

    YELLOW = YELLOW
    YELLOW_DARK = dark_color_variant(YELLOW)
    YELLOW_DARKER = blend(YELLOW_DARK, BLACK)
    YELLOW_DARKEST = blend(YELLOW_DARKER, BLACK)

    RED = RED
    RED_DARK = dark_color_variant(RED)
    RED_DARKER = blend(RED_DARK, BLACK)
    RED_DARKEST = blend(RED_DARKER, BLACK)

    GREEN = GREEN
    GREEN_DARK = dark_color_variant(GREEN)
    GREEN_DARKER = blend(GREEN_DARK, BLACK)
    GREEN_DARKEST = blend(GREEN_DARKER, BLACK)


# palettes
class Palettes:
    BASE = [
        [
            Colors.YELLOW,
            Colors.MAGENTA,
            Colors.PURPLE,
            Colors.BLUE,
            Colors.CYAN,
            Colors.BLACK,
        ]
    ]

    EXTENDED = [
        [
            Colors.YELLOW,
            Colors.RED,
            Colors.MAGENTA,
            Colors.PURPLE,
            Colors.BLUE,
            Colors.CYAN,
            Colors.GREEN,
            Colors.WHITE_LIGHT,
            Colors.BLACK_LIGHT,
        ],
        [
            Colors.YELLOW_DARK,
            Colors.RED_DARK,
            Colors.MAGENTA_DARK,
            Colors.PURPLE_DARK,
            Colors.BLUE_DARK,
            Colors.CYAN_DARK,
            Colors.GREEN_DARK,
            Colors.WHITE,
            Colors.BLACK,
        ],
        [
            Colors.YELLOW_DARKER,
            Colors.RED_DARKER,
            Colors.MAGENTA_DARKER,
            Colors.PURPLE_DARKER,
            Colors.BLUE_DARKER,
            Colors.CYAN_DARKER,
            Colors.GREEN_DARKER,
            Colors.WHITE_DARK,
            Colors.BLACK_DARK,
        ],
        [
            Colors.YELLOW_DARKEST,
            Colors.RED_DARKEST,
            Colors.MAGENTA_DARKEST,
            Colors.PURPLE_DARKEST,
            Colors.BLUE_DARKEST,
            Colors.CYAN_DARKEST,
            Colors.GREEN_DARKEST,
            Colors.WHITE_DARKER,
            Colors.BLACK_DARKER,
        ],
    ]

    TERMINAL = [
        [
            Colors.BLACK,
            Colors.RED_DARK,
            Colors.GREEN_DARK,
            Colors.YELLOW_DARK,
            Colors.PURPLE_DARK,
            Colors.MAGENTA_DARK,
            Colors.CYAN_DARK,
            Colors.WHITE_DARK,
        ],
        [
            Colors.WHITE_DARKER,
            Colors.RED,
            Colors.GREEN,
            Colors.YELLOW,
            Colors.PURPLE,
            Colors.MAGENTA,
            Colors.CYAN,
            Colors.WHITE,
        ],
    ]
