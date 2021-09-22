import colorsys
from collections import namedtuple

# formats
RGB = namedtuple("RGB", ["r", "g", "b"])
HLS = namedtuple("HLS", ["h", "l", "s"])
HSV = namedtuple("HSV", ["h", "s", "v"])
YIQ = namedtuple("YIQ", ["y", "i", "q"])
CMYK = namedtuple("CMYK", ["c", "m", "y", "k"])


# classes
class Color(RGB):
    @property
    def rgb(self):
        return RGB(*self)

    @property
    def hex(self):
        return color_to_hex(self)

    @property
    def cmyk(self):
        return rgb_to_cmyk(self)

    @property
    def hls(self):
        return rgb_to_hls(*self.rgb)

    @property
    def hsv(self):
        return rgb_to_hsv(*self.rgb)

    @property
    def yiq(self):
        return rgb_to_yiq(*self.rgb)


# conversion
rgb_to_yiq = colorsys.rgb_to_yiq
yiq_to_rgb = colorsys.yiq_to_rgb
rgb_to_hls = colorsys.rgb_to_hls
hls_to_rgb = colorsys.hls_to_rgb
rgb_to_hsv = colorsys.rgb_to_hsv
hsv_to_rgb = colorsys.hsv_to_rgb

RGB_SCALE = 255
CMYK_SCALE = 100


def rgb_to_cmyk(r, g, b):
    if (r == 0) and (g == 0) and (b == 0):
        # black
        return 0, 0, 0, CMYK_SCALE

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / float(RGB_SCALE)
    m = 1 - g / float(RGB_SCALE)
    y = 1 - b / float(RGB_SCALE)

    # extract out k [0,1]
    min_cmy = min(c, m, y)
    c = c - min_cmy
    m = m - min_cmy
    y = y - min_cmy
    k = min_cmy

    # rescale to the range [0,cmyk_scale]
    return c * CMYK_SCALE, m * CMYK_SCALE, y * CMYK_SCALE, k * CMYK_SCALE


def cmyk_to_rgb(c, m, y, k):
    """ """
    r = RGB_SCALE * (1.0 - (c + k) / float(CMYK_SCALE))
    g = RGB_SCALE * (1.0 - (m + k) / float(CMYK_SCALE))
    b = RGB_SCALE * (1.0 - (y + k) / float(CMYK_SCALE))
    return r, g, b


def int_to_hex(_int: int) -> str:
    template = "{:02x}" if _int < 16 else "{:x}"
    return template.format(_int)


def hex_to_int(_hex: str) -> int:
    return int(_hex, 16)


def rgb_to_hex(rgb: tuple) -> str:
    pass


def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    hlen = len(hex)
    pairs = hlen // 3
    return RGB(*tuple(hex_to_int(hex[i : i + pairs]) for i in range(0, hlen, pairs)))


def color_to_hex(color: Color) -> str:
    return "".join(map(int_to_hex, color.rgb))


def hex_to_color(_hex: str) -> Color:
    _int = hex_to_int(_hex)
    r = _int >> 16
    g = _int >> 8 & 0x00FF
    b = _int & 0x0000FF
    return Color(r, g, b)


# operations
def blend_values(v1: int, v2: int, factor: float) -> int:
    return round((v2 - v1) * factor) + v1


def shade_color(color: Color, factor: float = 0.5) -> Color:
    target_level = 0 if factor < 0 else 255
    target_color = Color(target_level, target_level, target_level)

    return blend_color(color, target_color, factor=abs(factor))


def shade_hex_color(_hex: str, factor: float) -> str:
    color = hex_to_color(_hex)
    return shade_color(color, factor).hex


def blend_color(color1: Color, color2: Color, factor: float = 0.5) -> Color:
    r = blend_values(color1.r, color2.r, factor)
    g = blend_values(color1.g, color2.g, factor)
    b = blend_values(color1.b, color2.b, factor)

    return Color(r, g, b)


def blend_hex_color(hex1: str, hex2: str, factor: float = 0.5) -> str:
    color1 = hex_to_color(hex1)
    color2 = hex_to_color(hex2)
    return blend_color(color1, color2, factor).hex
