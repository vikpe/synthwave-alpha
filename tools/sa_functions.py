from PIL import Image, ImageDraw


# methods
def from_template(filename) -> str:
    with open(f'templates/{filename}') as fp:
        return fp.read()


def placeholder(hex, text='+', size=48):
    return f'![](https://via.placeholder.com/{size}/{hex}/?text={text})'


def palette_to_image(palette: list, size=48):
    (rows, cols) = len(palette), len(palette[0])

    im = Image.new('RGBA', ((size * cols), (size * rows)))
    draw = ImageDraw.Draw(im)

    for row_index, row in enumerate(palette):
        for col_index, color in enumerate(row):
            x0 = col_index * size
            x1 = x0 + size
            y0 = row_index * size
            y1 = y0 + size
            draw.rectangle([x0, y0, x1, y1], fill=f'#{color}')

    return im


def save_palette_as_image(palette: list, filename: str, size=48):
    im = palette_to_image(palette, size=size)
    im.save(filename)
    im.close()


def md_table(rows: list) -> str:
    HEADER_ROW_DELIMITER = '---'
    CELL_DELIMITER = ' | '

    header_row = rows[0]
    header_separator_row = [HEADER_ROW_DELIMITER] * len(header_row)
    all_rows = [header_row] + [header_separator_row] + rows[1:]

    return "\n".join(
        CELL_DELIMITER.join(row) for row in all_rows
    ) + "\n"


def palette_to_table(palette: list, placeholder_size=20):
    header_row = ["C", "HEX"] * len(palette[0])
    body_rows = []

    for shades in palette:
        row = []
        for color in shades:
            row += [placeholder(color, placeholder_size), f'`{color}`']

        body_rows.append(row)

    return md_table([header_row] + body_rows)
