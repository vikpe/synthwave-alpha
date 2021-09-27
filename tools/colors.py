import colorsys

import attr


# formats
class ColorSpace(object):
    def __iter__(self):
        for val in self.__dict__.values():
            yield val


@attr.s
class RGB(ColorSpace):
    r = attr.ib(default=0, converter=int)
    g = attr.ib(default=0, converter=int)
    b = attr.ib(default=0, converter=int)


@attr.s
class HLS(ColorSpace):
    h = attr.ib(default=0, converter=float)
    l = attr.ib(default=0, converter=float)
    s = attr.ib(default=0, converter=float)


@attr.s
class HSV(ColorSpace):
    h = attr.ib(default=0, converter=float)
    s = attr.ib(default=0, converter=float)
    v = attr.ib(default=0, converter=float)


@attr.s
class YIQ(ColorSpace):
    y = attr.ib(default=0, converter=float)
    i = attr.ib(default=0, converter=float)
    q = attr.ib(default=0, converter=float)


@attr.s
class CMYK(ColorSpace):
    c = attr.ib(default=0, converter=float)
    m = attr.ib(default=0, converter=float)
    y = attr.ib(default=0, converter=float)
    k = attr.ib(default=0, converter=float)


# parse
def parse_hex(_hex) -> str:
    result = _hex.lstrip("#")
    if 3 == len(result):
        return "".join(c * 2 for c in result)
    else:
        return result


def parse_rgb(args) -> RGB:
    return RGB(*args)


# classes
@attr.s
class Color(object):
    rgb = attr.ib(converter=parse_rgb)

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
def rgb_to_yiq(rgb) -> YIQ:
    return YIQ(*colorsys.rgb_to_yiq(*rgb))


def yiq_to_rgb(yiq) -> RGB:
    return RGB(*colorsys.yiq_to_rgb(*yiq))


def rgb_to_hls(rgb) -> HLS:
    return HLS(*colorsys.rgb_to_hls(*rgb))


def hls_to_rgb(hls) -> RGB:
    return RGB(*colorsys.hls_to_rgb(*hls))


def rgb_to_hsv(rgb) -> HSV:
    return HSV(*colorsys.rgb_to_hsv(*rgb))


def hsv_to_rgb(hsv) -> RGB:
    return RGB(*colorsys.hsv_to_rgb(*hsv))


RGB_SCALE = 255.0
CMYK_SCALE = 100.0


def rgb_to_cmyk(rgb) -> CMYK:
    r, g, b = rgb

    if (r == 0) and (g == 0) and (b == 0):
        return CMYK(0, 0, 0, CMYK_SCALE)  # black

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


def cmyk_to_rgb(cmyk) -> RGB:
    c, m, y, k = cmyk
    r = RGB_SCALE * (1.0 - (c + k) / CMYK_SCALE)
    g = RGB_SCALE * (1.0 - (m + k) / CMYK_SCALE)
    b = RGB_SCALE * (1.0 - (y + k) / CMYK_SCALE)
    return RGB(r, g, b)


def int_to_hex(_int: int) -> str:
    template = "{:02x}" if _int < 16 else "{:x}"
    return template.format(_int)


def hex_to_int(_hex: str) -> int:
    return int(_hex, 16)


def rgb_to_hex(rgb) -> str:
    return "".join(map(int_to_hex, rgb))


def hex_to_rgb(_hex) -> RGB:
    result = parse_hex(_hex)
    hlen = len(result)
    pairs = hlen // 3
    r, g, b = [hex_to_int(result[i : i + pairs]) for i in range(0, hlen, pairs)]
    return RGB(r, g, b)


# operations
def lerp(v1: float, v2: float, factor: float) -> float:
    return v1 + ((v2 - v1) * factor)


def blend(color1: Color, color2: Color, factor: float = 0.5) -> Color:
    r = lerp(color1.rgb.r, color2.rgb.r, factor)
    g = lerp(color1.rgb.g, color2.rgb.g, factor)
    b = lerp(color1.rgb.b, color2.rgb.b, factor)

    return Color(RGB(r, g, b))


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
