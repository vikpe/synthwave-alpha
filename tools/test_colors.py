import colors

# contants
RGB_WHITE = colors.RGB(255, 255, 255)
RGB_GRAY = colors.RGB(127, 127, 127)
RGB_BLACK = colors.RGB(0, 0, 0)
RGB_RED = colors.RGB(255, 0, 0)
RGB_GREEN = colors.RGB(0, 255, 0)
RGB_BLUE = colors.RGB(0, 0, 255)

HEX_WHITE = "ffffff"
HEX_GRAY = "7f7f7f"
HEX_BLACK = "000000"
HEX_RED = "ff0000"
HEX_GREEN = "00ff00"
HEX_BLUE = "0000ff"

CMYK_WHITE = colors.CMYK(0, 0, 0, 0)
CMYK_GRAY = colors.CMYK(0, 0, 0, 50.19607843137255)
CMYK_BLACK = colors.CMYK(0, 0, 0, 100)
CMYK_RED = colors.CMYK(0, 100, 100, 0)
CMYK_GREEN = colors.CMYK(100, 0, 100, 0)
CMYK_BLUE = colors.CMYK(100, 100, 0, 0)

COLOR_WHITE = colors.Color(RGB_WHITE)
COLOR_GRAY = colors.Color(RGB_GRAY)
COLOR_BLACK = colors.Color(RGB_BLACK)
COLOR_RED = colors.Color(RGB_RED)
COLOR_GREEN = colors.Color(RGB_GREEN)
COLOR_BLUE = colors.Color(RGB_BLUE)


# classes
def test_color():
    color = colors.Color(RGB_RED)
    assert color == colors.Color.from_hex(HEX_RED)
    assert color.rgb == RGB_RED
    assert color.hex == HEX_RED
    assert color.cmyk == CMYK_RED
    assert color.hls == colors.HLS(0, 127.5, -1.007905138339921)
    assert color.hsv == colors.HSV(0, 1, 255)
    assert color.yiq == colors.YIQ(76.5, 152.745, 54.315)


# parse
def test_parse_hex():
    assert colors.parse_hex("ff00ff") == "ff00ff"
    assert colors.parse_hex("#ff00ff") == "ff00ff"
    assert colors.parse_hex("f0f") == "ff00ff"
    assert colors.parse_hex("#f0f") == "ff00ff"


# conversion
def test_hex_to_rgb():
    assert colors.hex_to_rgb(HEX_WHITE) == RGB_WHITE
    assert colors.hex_to_rgb(HEX_GRAY) == RGB_GRAY
    assert colors.hex_to_rgb(HEX_BLACK) == RGB_BLACK
    assert colors.hex_to_rgb(HEX_RED) == RGB_RED
    assert colors.hex_to_rgb(HEX_GREEN) == RGB_GREEN
    assert colors.hex_to_rgb(HEX_BLUE) == RGB_BLUE


def test_rgb_to_hex():
    assert colors.rgb_to_hex(RGB_WHITE) == HEX_WHITE
    assert colors.rgb_to_hex(RGB_GRAY) == HEX_GRAY
    assert colors.rgb_to_hex(RGB_BLACK) == HEX_BLACK
    assert colors.rgb_to_hex(RGB_RED) == HEX_RED
    assert colors.rgb_to_hex(RGB_GREEN) == HEX_GREEN
    assert colors.rgb_to_hex(RGB_BLUE) == HEX_BLUE


def test_rgb_to_cmyk():
    assert colors.rgb_to_cmyk(RGB_WHITE) == CMYK_WHITE
    assert colors.rgb_to_cmyk(RGB_GRAY) == CMYK_GRAY
    assert colors.rgb_to_cmyk(RGB_BLACK) == CMYK_BLACK
    assert colors.rgb_to_cmyk(RGB_RED) == CMYK_RED
    assert colors.rgb_to_cmyk(RGB_GREEN) == CMYK_GREEN
    assert colors.rgb_to_cmyk(RGB_BLUE) == CMYK_BLUE


def test_cmyk_to_rgb():
    assert colors.cmyk_to_rgb(CMYK_WHITE) == RGB_WHITE
    assert colors.cmyk_to_rgb(CMYK_GRAY) == RGB_GRAY
    assert colors.cmyk_to_rgb(CMYK_BLACK) == RGB_BLACK
    assert colors.cmyk_to_rgb(CMYK_RED) == RGB_RED
    assert colors.cmyk_to_rgb(CMYK_GREEN) == RGB_GREEN
    assert colors.cmyk_to_rgb(CMYK_BLUE) == RGB_BLUE


# operations
def test_lerp():
    assert colors.lerp(10, 0, 0) == 10
    assert colors.lerp(0, 10, 0.5) == 5
    assert colors.lerp(10, 1, 0.5) == 5.5
    assert colors.lerp(1, 2, 0.5) == 1.5
    assert colors.lerp(1, 2, 1) == 2


def test_blend():
    assert colors.blend(COLOR_WHITE, COLOR_BLACK, 0) == COLOR_WHITE
    assert colors.blend(COLOR_WHITE, COLOR_BLACK, 0.5) == COLOR_GRAY
    assert colors.blend(COLOR_WHITE, COLOR_BLACK, 1) == COLOR_BLACK
    assert colors.blend(COLOR_RED, COLOR_BLACK, 0.5) == colors.Color((127, 0, 0))
    assert colors.blend(COLOR_RED, COLOR_BLUE) == colors.Color((127, 0, 127))


def test_shade():
    assert colors.shade(COLOR_WHITE, 0.5) == COLOR_GRAY
    assert colors.shade(COLOR_RED, 0.5) == colors.Color((127, 0, 0))
    assert colors.shade(COLOR_RED, 1) == COLOR_BLACK


def test_tint():
    assert colors.tint(COLOR_BLACK, 0.5) == COLOR_GRAY
    assert colors.tint(COLOR_RED, 0.5) == colors.Color((255, 127, 127))
    assert colors.tint(COLOR_RED, 1) == COLOR_WHITE


def test_tone():
    assert colors.tone(COLOR_RED, 1) == COLOR_GRAY
    assert colors.tone(COLOR_RED, 0.5) == colors.Color((191, 63, 63))
    assert colors.tone(COLOR_WHITE, 1) == COLOR_GRAY
    assert colors.tone(COLOR_WHITE, 0.5) == colors.Color((191, 191, 191))
    assert colors.tone(COLOR_BLACK, 0.5) == colors.Color((63, 63, 63))
    assert colors.tone(COLOR_BLACK, 1) == COLOR_GRAY
