from sa_functions import save_palette_as_image, placeholder, from_template


# colors
class C:
    @classmethod
    def as_dict(cls):
        return {f'C_{k}': v for k, v in cls.__dict__.items() if not k.startswith('__')}

    YELLOW = 'f9f972'
    YELLOW_DARK = 'adad3e'
    YELLOW_DARKER = '696437'
    YELLOW_DARKEST = '474034'

    RED = 'e80c72'
    RED_DARK = '9c044b'
    RED_DARKER = '60103e'
    RED_DARKEST = '421637'

    MAGENTA = 'ff00f6'
    MAGENTA_DARK = 'b312ad'
    MAGENTA_DARKER = '6C176f'
    MAGENTA_DARKEST = '481950'

    PURPLE = 'aa54f8'
    PURPLE_DARK = '6c29ab'
    PURPLE_DARKER = '48226e'
    PURPLE_DARKEST = '361F4f'

    BLUE = '55a7fb'
    BLUE_DARK = '2a6cad'
    BLUE_DARKER = '27446f'
    BLUE_DARKEST = '263050'

    CYAN = '00fbfd'
    CYAN_DARK = '00b0b0'
    CYAN_DARKER = '126670'
    CYAN_DARKEST = '1B4150'

    GREEN = '0be6a8'
    GREEN_DARK = '04996f'
    GREEN_DARKER = '145a50'
    GREEN_DARKEST = '1c3b40'

    WHITE = 'f2f2e3'
    WHITE_DARK = 'b9b1bb'
    WHITE_DARKER = '7f6f93'

    BLACK = '241b30'
    BLACK_LIGHT = '312541'
    BLACK_DARK = '1d1627'


# palettes
p_default = [
    [
        C.YELLOW,
        C.MAGENTA,
        C.PURPLE,
        C.BLUE,
        C.CYAN,
        C.WHITE,
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
        C.WHITE,
        C.WHITE_DARKER
    ],
    [
        C.YELLOW_DARK,
        C.RED_DARK,
        C.MAGENTA_DARK,
        C.PURPLE_DARK,
        C.BLUE_DARK,
        C.CYAN_DARK,
        C.GREEN_DARK,
        C.WHITE_DARK,
        C.BLACK
    ]
]

p_full = [
    [
        C.YELLOW,
        C.RED,
        C.MAGENTA,
        C.PURPLE,
        C.BLUE,
        C.CYAN,
        C.GREEN,
        C.WHITE,
        C.BLACK_LIGHT],
    [
        C.YELLOW_DARK,
        C.RED_DARK,
        C.MAGENTA_DARK,
        C.PURPLE_DARK,
        C.BLUE_DARK,
        C.CYAN_DARK,
        C.GREEN_DARK,
        C.WHITE_DARK,
        C.BLACK],
    [
        C.YELLOW_DARKER,
        C.RED_DARKER,
        C.MAGENTA_DARKER,
        C.PURPLE_DARKER,
        C.BLUE_DARKER,
        C.CYAN_DARKER,
        C.GREEN_DARKER,
        C.WHITE_DARKER,
        C.BLACK_DARK],
    [
        C.YELLOW_DARKEST,
        C.RED_DARKEST,
        C.MAGENTA_DARKEST,
        C.PURPLE_DARKEST,
        C.BLUE_DARKEST,
        C.CYAN_DARKEST,
        C.GREEN_DARKEST
    ],
]

p_terminal = [
    [
        C.BLACK_DARK,
        C.RED_DARK,
        C.GREEN_DARK,
        C.YELLOW_DARK,
        C.BLUE_DARK,
        C.MAGENTA_DARK,
        C.CYAN_DARK,
        C.WHITE_DARKER,
    ],
    [
        C.WHITE_DARKER,
        C.RED,
        C.GREEN,
        C.YELLOW,
        C.BLUE,
        C.MAGENTA,
        C.CYAN,
        C.WHITE_DARK,
    ]
]

assets_dir = "../assets"
save_palette_as_image(p_default, f"{assets_dir}/palette_default.png", size=64)
save_palette_as_image(p_extended, f"{assets_dir}/palette_extended.png")
save_palette_as_image(p_full, f"{assets_dir}/palette_full.png")
save_palette_as_image(p_terminal, f"{assets_dir}/palette_terminal.png")

# script
screenshot_placeholder = placeholder('dddddd', text='screenshot', size='640x240')

print(f'''
![]({'./assets/synthwave_alpha_logo.png'})
> {'Synthwave inspired color palette'}

## Palette

### Base
![](./assets/palette_default.png)

### Extended
![](./assets/palette_extended.png)

### Full
![](./assets/palette_full.png)

## Terminal
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
{from_template('fish.sh', C.as_dict())}
```

## FZF
{screenshot_placeholder}
```sh
{from_template('fzf.sh', C.as_dict())}
```

## Starship
Using a [Nerd Font](https://www.nerdfonts.com/)

{screenshot_placeholder}

```toml
{from_template('starship.toml', C.as_dict())}
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
''')
