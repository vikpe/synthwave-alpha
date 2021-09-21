import colorsys
from collections import namedtuple

from PIL import Image, ImageDraw


def class_as_dict(cls):
    return {f"C_{k}": v for k, v in cls.__dict__.items() if not k.startswith("__")}


def from_template(filename) -> str:
    with open(f"templates/{filename}") as fp:
        return fp.read()


def array_transpose(arr: list) -> list:
    return [*zip(*arr)]


def placeholder(hex, text="+", size=48):
    return f"![](https://via.placeholder.com/{size}/{hex}/?text={text})"


def palette_to_image(palette: list, size=48):
    (rows, cols) = len(palette), len(palette[0])

    im = Image.new("RGBA", ((size * cols), (size * rows)))
    draw = ImageDraw.Draw(im)

    for row_index, row in enumerate(palette):
        for col_index, color in enumerate(row):
            x0 = col_index * size
            x1 = x0 + size
            y0 = row_index * size
            y1 = y0 + size
            draw.rectangle([x0, y0, x1, y1], fill=f"#{color}")

    return im


def save_palette_as_image(palette: list, filename: str, size=48):
    im = palette_to_image(palette, size=size)
    im.save(filename)
    im.close()


def md_table(rows: list) -> str:
    HEADER_ROW_DELIMITER = "---"
    CELL_DELIMITER = " | "

    header_row = rows[0]
    header_separator_row = [HEADER_ROW_DELIMITER] * len(header_row)
    all_rows = [header_row] + [header_separator_row] + rows[1:]

    return "\n".join(CELL_DELIMITER.join(row) for row in all_rows) + "\n"


def palette_to_table(palette: list, placeholder_size=20):
    header_row = ["C", "HEX"] * len(palette[0])
    body_rows = []

    for shades in palette:
        row = []
        for color in shades:
            row += [placeholder(color, size=placeholder_size), f"`{color}`"]

        body_rows.append(row)

    return md_table([header_row] + body_rows)


def int_to_hex(_int: int) -> str:
    template = "{:02x}" if _int < 16 else "{:x}"
    return template.format(_int)


def hex_to_int(_hex: str) -> int:
    return int(_hex, 16)


class Color(namedtuple("ColorRGB", ["r", "g", "b"])):
    @property
    def rgb(self):
        return self.r, self.g, self.b

    @property
    def hex(self):
        return color_to_hex(self)

    @property
    def hls(self):
        return colorsys.rgb_to_hls(*self.rgb)

    @property
    def hsv(self):
        return colorsys.rgb_to_hsv(*self.rgb)


def color_to_hex(color: Color) -> str:
    return "".join(map(int_to_hex, color.rgb))


def hex_to_color(_hex: str) -> Color:
    _int = hex_to_int(_hex)
    r = _int >> 16
    g = _int >> 8 & 0x00FF
    b = _int & 0x0000FF
    return Color(r, g, b)


def blend_values(v1: int, v2: int, factor: float) -> int:
    return round((v2 - v1) * factor) + v1


def shade_hex_color(_hex: str, factor: float) -> str:
    target_color = 0 if factor < 0 else 255
    abs_factor = abs(factor)

    color = hex_to_color(_hex)
    r = blend_values(color.r, target_color, abs_factor)
    g = blend_values(color.g, target_color, abs_factor)
    b = blend_values(color.b, target_color, abs_factor)

    return Color(r, g, b).hex


def blend_color(hex1: str, hex2: str, factor: float = 0.5) -> str:
    rgb1 = hex_to_color(hex1)
    rgb2 = hex_to_color(hex2)

    r = blend_values(rgb1.r, rgb2.r, factor)
    g = blend_values(rgb1.g, rgb2.g, factor)
    b = blend_values(rgb1.b, rgb2.b, factor)

    return Color(r, g, b).hex
