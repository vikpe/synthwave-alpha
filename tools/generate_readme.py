from sa_functions import (
    save_palette_as_image,
    placeholder,
    from_template,
    palette_to_table,
    array_transpose,
    class_as_dict,
)

from colors import blend, shade, tint, hex_to_color as h2c

shades = [x * 0.1 for x in range(0, 11)]
print(shades)
p_tints = [tint(h2c("e80c72"), s).hex for s in shades]
p_shades = [shade(h2c("e80c72"), s).hex for s in shades]
p_blend = [blend(h2c("f9f972"), h2c("55a7fb"), s).hex for s in shades]

print(p_tints)
save_palette_as_image([p_tints], "p_tints.png")

print(p_shades)
save_palette_as_image([p_shades], "p_shades.png")

print(p_tints)
save_palette_as_image([p_blend], "p_blend.png")

C_BLACK = h2c("241b30")


# colors
class C:
    WHITE_LIGHT = "f9f9f1"
    WHITE = "f2f2e3"
    WHITE_DARK = "b9b1bb"
    WHITE_DARKER = "7f6f93"

    BLACK = "241b30"
    BLACK_LIGHT = "312541"
    BLACK_DARK = "1d1627"
    BLACK_DARKER = "140f1a"

    YELLOW = "f9f972"
    YELLOW_DARK = "adad3e"
    YELLOW_DARKER = blend(h2c(YELLOW_DARK), C_BLACK).hex
    YELLOW_DARKEST = blend(h2c(YELLOW_DARKER), C_BLACK).hex

    RED = "e80c72"
    RED_DARK = "9c044b"
    RED_DARKER = blend(h2c(RED_DARK), C_BLACK).hex
    RED_DARKEST = blend(h2c(RED_DARKER), C_BLACK).hex

    MAGENTA = "ff00f6"
    MAGENTA_DARK = "b312ad"
    MAGENTA_DARKER = blend(h2c(MAGENTA_DARK), C_BLACK).hex
    MAGENTA_DARKEST = blend(h2c(MAGENTA_DARKER), C_BLACK).hex

    PURPLE = "aa54f8"
    PURPLE_DARK = "6c29ab"
    PURPLE_DARKER = blend(h2c(PURPLE_DARK), C_BLACK).hex
    PURPLE_DARKEST = blend(h2c(PURPLE_DARKER), C_BLACK).hex

    BLUE = "55a7fb"
    BLUE_DARK = "2a6cad"
    BLUE_DARKER = blend(h2c(BLUE_DARK), C_BLACK).hex
    BLUE_DARKEST = blend(h2c(BLUE_DARKER), C_BLACK).hex

    CYAN = "00fbfd"
    CYAN_DARK = "00b0b0"
    CYAN_DARKER = blend(h2c(CYAN_DARK), C_BLACK).hex
    CYAN_DARKEST = blend(h2c(CYAN_DARKER), C_BLACK).hex

    GREEN = "0be6a8"
    GREEN_DARK = "04996f"
    GREEN_DARKER = blend(h2c(GREEN_DARK), C_BLACK).hex
    GREEN_DARKEST = blend(h2c(GREEN_DARKER), C_BLACK).hex


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

{placeholder(C.WHITE)}
{placeholder(C.BLACK)}

**Highlight**

{placeholder(C.BLACK)}
{placeholder(C.GREEN)}

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
