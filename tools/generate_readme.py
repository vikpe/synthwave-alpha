from colors import blend, shade, tint, Color
from sa_functions import (
    save_palette_as_image,
    placeholder,
    from_template,
    palette_to_table,
    array_transpose,
    class_as_dict,
)

"""
shades = [x * 0.1 for x in range(0, 11)]
p_tints = [tint(Color.from_hex("e80c72"), s) for s in shades]
p_shades = [shade(Color.from_hex("e80c72"), s) for s in shades]
p_blend = [blend(Color.from_hex("f9f972"), Color.from_hex("55a7fb"), s) for s in shades]

print(p_tints)
save_palette_as_image([p_tints], "p_tints.png")

print(p_shades)
save_palette_as_image([p_shades], "p_shades.png")

print(p_tints)
save_palette_as_image([p_blend], "p_blend.png")
"""

COLOR_YELLOW = Color.from_hex("ffff00")


# colors
class C:
    WHITE_LIGHT = Color.from_hex("f9f9f1")
    WHITE = Color.from_hex("f2f2e3")
    WHITE_DARK = Color.from_hex("b9b1bb")
    WHITE_DARKER = Color.from_hex("7f6f93")

    BLACK = Color.from_hex("241b30")
    BLACK_LIGHT = Color.from_hex("312541")
    BLACK_DARK = Color.from_hex("1d1627")
    BLACK_DARKER = Color.from_hex("140f1a")

    YELLOW = blend(WHITE, COLOR_YELLOW)
    YELLOW_DARK = Color.from_hex("adad3e")
    YELLOW_DARKER = blend(YELLOW_DARK, BLACK)
    YELLOW_DARKEST = blend(YELLOW_DARKER, BLACK)

    RED = Color.from_hex("e80c72")
    RED_DARK = Color.from_hex("9c044b")
    RED_DARKER = blend(RED_DARK, BLACK)
    RED_DARKEST = blend(RED_DARKER, BLACK)

    MAGENTA = Color.from_hex("ff00f6")
    MAGENTA_DARK = Color.from_hex("b312ad")
    MAGENTA_DARKER = blend(MAGENTA_DARK, BLACK)
    MAGENTA_DARKEST = blend(MAGENTA_DARKER, BLACK)

    PURPLE = Color.from_hex("aa54f8")
    PURPLE_DARK = Color.from_hex("6c29ab")
    PURPLE_DARKER = blend(PURPLE_DARK, BLACK)
    PURPLE_DARKEST = blend(PURPLE_DARKER, BLACK)

    BLUE = Color.from_hex("55a7fb")
    BLUE_DARK = Color.from_hex("2a6cad")
    BLUE_DARKER = blend(BLUE_DARK, BLACK)
    BLUE_DARKEST = blend(BLUE_DARKER, BLACK)

    CYAN = Color.from_hex("00fbfd")
    CYAN_DARK = Color.from_hex("00b0b0")
    CYAN_DARKER = blend(CYAN_DARK, BLACK)
    CYAN_DARKEST = blend(CYAN_DARKER, BLACK)

    GREEN = Color.from_hex("0be6a8")
    GREEN_DARK = Color.from_hex("04996f")
    GREEN_DARKER = blend(GREEN_DARK, BLACK)
    GREEN_DARKEST = blend(GREEN_DARKER, BLACK)


# palettes


p_base = [
    [
        C.YELLOW,
        C.MAGENTA,
        C.PURPLE,
        C.BLUE,
        C.CYAN,
        C.BLACK,
    ]
]

p_extended = [
    [
        C.YELLOW,
        C.RED,
        C.MAGENTA,
        C.PURPLE,
        C.BLUE,
        C.CYAN,
        C.GREEN,
        C.WHITE_LIGHT,
        C.BLACK_LIGHT,
    ],
    [
        C.YELLOW_DARK,
        C.RED_DARK,
        C.MAGENTA_DARK,
        C.PURPLE_DARK,
        C.BLUE_DARK,
        C.CYAN_DARK,
        C.GREEN_DARK,
        C.WHITE,
        C.BLACK,
    ],
    [
        C.YELLOW_DARKER,
        C.RED_DARKER,
        C.MAGENTA_DARKER,
        C.PURPLE_DARKER,
        C.BLUE_DARKER,
        C.CYAN_DARKER,
        C.GREEN_DARKER,
        C.WHITE_DARK,
        C.BLACK_DARK,
    ],
    [
        C.YELLOW_DARKEST,
        C.RED_DARKEST,
        C.MAGENTA_DARKEST,
        C.PURPLE_DARKEST,
        C.BLUE_DARKEST,
        C.CYAN_DARKEST,
        C.GREEN_DARKEST,
        C.WHITE_DARKER,
        C.BLACK_DARKER,
    ],
]

p_terminal = [
    [
        C.BLACK,
        C.RED_DARK,
        C.GREEN_DARK,
        C.YELLOW_DARK,
        C.BLUE_DARK,
        C.MAGENTA_DARK,
        C.CYAN_DARK,
        C.WHITE_DARK,
    ],
    [
        C.WHITE_DARKER,
        C.RED,
        C.GREEN,
        C.YELLOW,
        C.BLUE,
        C.MAGENTA,
        C.CYAN,
        C.WHITE,
    ],
]

assets_dir = "../assets"
save_palette_as_image(p_base, f"{assets_dir}/palette_base.png", size=64)
save_palette_as_image(p_extended, f"{assets_dir}/palette_extended.png")
save_palette_as_image(p_terminal, f"{assets_dir}/palette_terminal.png")

# script
screenshot_placeholder = placeholder("dddddd", text="screenshot", size="640x240")

readme = f"""
![]({'./assets/synthwave_alpha_logo.png'})
> {'Synthwave inspired color palette'}

## Palette

### Base
![](./assets/palette_base.png)

### Extended
![](./assets/palette_extended.png)

{palette_to_table(array_transpose(p_extended))}

## Implementations

### Terminal
{screenshot_placeholder}

**Default**

{placeholder(C.WHITE.hex)}
{placeholder(C.BLACK.hex)}

**Highlight**

{placeholder(C.BLACK.hex)}
{placeholder(C.GREEN.hex)}

**Palette**

![](./assets/palette_terminal.png)

## Fish
{screenshot_placeholder}
```sh
{from_template('fish.sh')}
```

## FZF
{screenshot_placeholder}
```sh
{from_template('fzf.sh')}
```

## Starship
Using a [Nerd Font](https://www.nerdfonts.com/)

{screenshot_placeholder}

```toml
{from_template('starship.toml')}
```

## VCS / Diff

Status | C | Hex
--- | --- | ---
Added gutter  | ![](https://via.placeholder.com/24/145a50/?text=+) | #145a50
Added background | ![](https://via.placeholder.com/24/1c3b40/?text=+) | #1c3b40
Deleted gutter  | ![](https://via.placeholder.com/24/60103E/?text=+) | #60103E
Deleted background | ![](https://via.placeholder.com/24/421637/?text=+) | #421637
Modified gutter  | ![](https://via.placeholder.com/24/27446f/?text=+) | #27446f
Modified background | ![](https://via.placeholder.com/24/263050/?text=+) | #263050
Conflict gutter  | ![](https://via.placeholder.com/24/696437/?text=+) | #696437
Conflict background | ![](https://via.placeholder.com/24/474034/?text=+) | #474034
"""

print(readme.format(**class_as_dict(C)))
