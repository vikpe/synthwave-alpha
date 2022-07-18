from sa import Colors, Palettes
from sa_functions import (
    save_palette_as_image,
    placeholder,
    read_template,
    palette_to_table,
    array_transpose,
    template_to_file, replace_colors_in_string,
)

assets_dir = "../.github/assets"
save_palette_as_image(Palettes.BASE, f"{assets_dir}/palette_base.png", size=64)
save_palette_as_image(Palettes.EXTENDED, f"{assets_dir}/palette_extended.png")
save_palette_as_image(Palettes.TERMINAL, f"{assets_dir}/palette_terminal.png")

# script
readme = f"""
![]({'./.github/assets/synthwave_alpha_logo.png'})
> {'Synthwave inspired color palette'}

## Palette

### Base
![](./.github/assets/palette_base.png)

{palette_to_table(array_transpose(Palettes.BASE))}

### Terminal / 16-color
![](./.github/assets/palette_terminal.png)

{palette_to_table(array_transpose(Palettes.TERMINAL))}

### Extended
![](./.github/assets/palette_extended.png)

{palette_to_table(array_transpose(Palettes.EXTENDED))}

## Sample implementations

### Terminal
> Open terminal settings and set colors according to [the terminal / 16-color table](#terminal--16-color).

![](./.github/assets/screenshot_terminal.png)

### [Fish](https://fishshell.com/)
> See [fish.sh](./implementations/fish.sh) for instructions/setup.

![](./.github/assets/screenshot_fish.png)

### [Starship](https://starship.rs/)
> See [starship.toml](./implementations/starship.toml) for instructions/setup.

![](./.github/assets/screenshot_starship.png)

### [FZF](https://github.com/junegunn/fzf)
> See [fzf.sh](./implementations/fzf.sh) for instructions/setup.

![](./.github/assets/screenshot_fzf.png)

<!--
## VCS / Diff

Status | C | Hex
--- | --- | ---
Added gutter | {placeholder(Colors.GREEN_DARKER.hex, size=24)} | #{Colors.GREEN_DARKER.hex}
Added background | {placeholder(Colors.GREEN_DARKEST.hex, size=24)} | #{Colors.GREEN_DARKEST.hex}
Deleted gutter | {placeholder(Colors.RED_DARKER.hex, size=24)} | #{Colors.RED_DARKER.hex}
Deleted background | {placeholder(Colors.RED_DARKEST.hex, size=24)} | #{Colors.RED_DARKEST.hex}
Modified gutter | {placeholder(Colors.BLUE_DARKER.hex, size=24)} | #{Colors.BLUE_DARKER.hex}
Modified background | {placeholder(Colors.BLUE_DARKEST.hex, size=24)} | #{Colors.BLUE_DARKEST.hex}
Conflict gutter | {placeholder(Colors.YELLOW_DARKER.hex, size=24)} | #{Colors.YELLOW_DARKER.hex}
Conflict background | {placeholder(Colors.YELLOW_DARKEST.hex, size=24)} | #{Colors.YELLOW_DARKEST.hex}
-->
"""

print(replace_colors_in_string(readme, Colors))

templates = ["fish.sh", "fzf.sh", "starship.toml"]

for filename in templates:
    template_to_file(filename, Colors, f"../implementations/{filename}")
