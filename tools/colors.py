import colorsys
from collections import namedtuple
import attr

# formats
RGB = namedtuple("RGB", ["r", "g", "b"])
HLS = namedtuple("HLS", ["h", "l", "s"])
HSV = namedtuple("HSV", ["h", "s", "v"])
YIQ = namedtuple("YIQ", ["y", "i", "q"])
CMYK = namedtuple("CMYK", ["c", "m", "y", "k"])


# parse
def parse_hex(_hex) -> str:
    result = _hex.lstrip("#")
    if 3 == len(result):
        return "".join(c * 2 for c in result)
    else:
        return result


# classes
@attr.s
class Color(object):
    rgb = attr.ib()

    @classmethod
    def from_hex(cls, _hex):
        return cls(hex_to_rgb(_hex))

    @property
    def hex(self):
        return rgb_to_hex(self.rgb)

    @property
    def cmyk(self):
        return rgb_to_cmyk(self.rgb)

    @property
    def hls(self):
        return rgb_to_hls(self.rgb)

    @property
    def hsv(self):
        return rgb_to_hsv(self.rgb)

    @property
    def yiq(self):
        return rgb_to_yiq(self.rgb)


# conversion
def rgb_to_yiq(rgb):
    return YIQ(*colorsys.rgb_to_yiq(*rgb))


def yiq_to_rgb(yiq):
    return RGB(*colorsys.yiq_to_rgb(*yiq))


def rgb_to_hls(rgb):
    return HLS(*colorsys.rgb_to_hls(*rgb))


def hls_to_rgb(hls):
    return RGB(*colorsys.hls_to_rgb(*hls))


def rgb_to_hsv(rgb):
    return HSV(*colorsys.rgb_to_hsv(*rgb))


def hsv_to_rgb(hsv):
    return RGB(*colorsys.hsv_to_rgb(*hsv))


RGB_SCALE = 255.0
CMYK_SCALE = 100.0


def rgb_to_cmyk(rgb: tuple) -> tuple:
    r, g, b = rgb

    if (r == 0) and (g == 0) and (b == 0):
        return 0, 0, 0, CMYK_SCALE  # black

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    y = 1 - b / RGB_SCALE

    # extract out k [0,1]
    min_cmy = min(c, m, y)
    c = c - min_cmy
    m = m - min_cmy
    y = y - min_cmy
    k = min_cmy

    # rescale to the range [0,cmyk_scale]
    return CMYK(*[c * CMYK_SCALE, m * CMYK_SCALE, y * CMYK_SCALE, k * CMYK_SCALE])


def cmyk_to_rgb(cmyk: tuple) -> tuple:
    c, m, y, k = cmyk
    r = RGB_SCALE * (1.0 - (c + k) / CMYK_SCALE)
    g = RGB_SCALE * (1.0 - (m + k) / CMYK_SCALE)
    b = RGB_SCALE * (1.0 - (y + k) / CMYK_SCALE)
    return tuple(map(int, [r, g, b]))


def int_to_hex(_int: int) -> str:
    template = "{:02x}" if _int < 16 else "{:x}"
    return template.format(_int)


def hex_to_int(_hex: str) -> int:
    return int(_hex, 16)


def rgb_to_hex(rgb: tuple) -> str:
    return "".join(map(int_to_hex, rgb))


def hex_to_rgb(_hex):
    result = parse_hex(_hex)
    hlen = len(result)
    pairs = hlen // 3
    return tuple(hex_to_int(result[i : i + pairs]) for i in range(0, hlen, pairs))


# operations
def lerp(v1: float, v2: float, factor: float) -> float:
    return v1 + ((v2 - v1) * factor)


def blend(color1: Color, color2: Color, factor: float = 0.5) -> Color:
    r = lerp(color1.rgb.r, color2.rgb.r, factor)
    g = lerp(color1.rgb.g, color2.rgb.g, factor)
    b = lerp(color1.rgb.b, color2.rgb.b, factor)

    return Color((int(r), int(g), int(b)))


def shade(color: Color, factor: float) -> Color:
    return blend(color, Color(RGB(0, 0, 0)), factor=factor)


def tone(color: Color, factor: float) -> Color:
    return blend(color, Color(RGB(127, 127, 127)), factor=factor)


def tint(color: Color, factor: float) -> Color:
    return blend(color, Color(RGB(255, 255, 255)), factor=factor)


"""
def hue(color: Color, factor: float) -> Color:
    pass


def saturate(color: Color, factor: float) -> Color:
    pass


def desaturate(color: Color, factor: float) -> Color:
    pass
    
def grayscale(color: Color, factor: float) -> Color:
    pass
"""
