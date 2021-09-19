from sa_functions import save_palette_as_image, placeholder, from_template

# colors
c_yellow = 'f9f972'
c_yellow_dark = 'adad3e'
c_yellow_darker = '696437'
c_yellow_darkest = '474034'

c_red = 'e80c72'
c_red_dark = '9c044b'
c_red_darker = '60103e'
c_red_darkest = '421637'

c_magenta = 'ff00f6'
c_magenta_dark = 'b312ad'
c_magenta_darker = '6C176f'
c_magenta_darkest = '481950'

c_purple = 'aa54f8'
c_purple_dark = '6c29ab'
c_purple_darker = '48226e'
c_purple_darkest = '361F4f'

c_blue = '55a7fb'
c_blue_dark = '2a6cad'
c_blue_darker = '27446f'
c_blue_darkest = '263050'

c_cyan = '00fbfd'
c_cyan_dark = '00b0b0'
c_cyan_darker = '126670'
c_cyan_darkest = '1B4150'

c_green = '0be6a8'
c_green_dark = '04996f'
c_green_darker = '145a50'
c_green_darkest = '1c3b40'

c_white = 'f2f2e3'
c_white_dark = 'b9b1bb'
c_white_darker = '7f6f93'

c_black = '241b30'
c_black_light = '312541'
c_black_dark = '1d1627'

colors = {
    'c_yellow': 'f9f972',
    'c_yellow_dark': 'adad3e',
    'c_yellow_darker': '696437',
    'c_yellow_darkest': '474034',

    'c_red': 'e80c72',
    'c_red_dark': '9c044b',
    'c_red_darker': '60103e',
    'c_red_darkest': '421637',

    'c_magenta': 'ff00f6',
    'c_magenta_dark': 'b312ad',
    'c_magenta_darker': '6C176f',
    'c_magenta_darkest': '481950',

    'c_purple': 'aa54f8',
    'c_purple_dark': '6c29ab',
    'c_purple_darker': '48226e',
    'c_purple_darkest': '361F4f',

    'c_blue': '55a7fb',
    'c_blue_dark': '2a6cad',
    'c_blue_darker': '27446f',
    'c_blue_darkest': '263050',

    'c_cyan': '00fbfd',
    'c_cyan_dark': '00b0b0',
    'c_cyan_darker': '126670',
    'c_cyan_darkest': '1B4150',

    'c_green': '0be6a8',
    'c_green_dark': '04996f',
    'c_green_darker': '145a50',
    'c_green_darkest': '1c3b40',

    'c_white': 'f2f2e3',
    'c_white_dark': 'b9b1bb',
    'c_white_darker': '7f6f93',

    'c_black': '241b30',
    'c_black_light': '312541',
    'c_black_dark': '1d1627',
}

# palettes
p_default = [
    [
        c_yellow,
        c_magenta,
        c_purple,
        c_blue,
        c_cyan,
        c_white,
        c_black,
    ]
]

p_extended = [
    [
        c_yellow,
        c_red,
        c_magenta,
        c_purple,
        c_blue,
        c_cyan,
        c_green,
        c_white,
        c_white_darker
    ],
    [
        c_yellow_dark,
        c_red_dark,
        c_magenta_dark,
        c_purple_dark,
        c_blue_dark,
        c_cyan_dark,
        c_green_dark,
        c_white_dark,
        c_black
    ]
]

p_full = [
    [
        c_yellow,
        c_red,
        c_magenta,
        c_purple,
        c_blue,
        c_cyan,
        c_green,
        c_white,
        c_black_light],
    [
        c_yellow_dark,
        c_red_dark,
        c_magenta_dark,
        c_purple_dark,
        c_blue_dark,
        c_cyan_dark,
        c_green_dark,
        c_white_dark,
        c_black],
    [
        c_yellow_darker,
        c_red_darker,
        c_magenta_darker,
        c_purple_darker,
        c_blue_darker,
        c_cyan_darker,
        c_green_darker,
        c_white_darker,
        c_black_dark],
    [
        c_yellow_darkest,
        c_red_darkest,
        c_magenta_darkest,
        c_purple_darkest,
        c_blue_darkest,
        c_cyan_darkest,
        c_green_darkest
    ],
]

p_terminal = [
    [
        c_black_dark,
        c_red_dark,
        c_green_dark,
        c_yellow_dark,
        c_blue_dark,
        c_magenta_dark,
        c_cyan_dark,
        c_white_darker,
    ],
    [
        c_white_darker,
        c_red,
        c_green,
        c_yellow,
        c_blue,
        c_magenta,
        c_cyan,
        c_white_dark,
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
''')

print(f'''
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

{placeholder(c_white)}
{placeholder(c_black)}

**Highlight**

{placeholder(c_black)}
{placeholder(c_green)}

**Palette**

![](./assets/palette_terminal.png)

## Fish
{screenshot_placeholder}
```sh
{from_template('fish.sh', colors)}
```

## FZF
{screenshot_placeholder}
```sh
{from_template('fzf.sh', colors)}
```

## Starship
Using a [Nerd Font](https://www.nerdfonts.com/)

{screenshot_placeholder}

```toml
{from_template('starship.toml', colors)}
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
