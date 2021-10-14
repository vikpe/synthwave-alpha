from sa import Colors, Palettes
from sa_functions import (
    save_palette_as_image,
    placeholder,
    from_template,
    palette_to_table,
    array_transpose,
    class_as_dict,
)

assets_dir = "../assets"
save_palette_as_image(Palettes.BASE, f"{assets_dir}/palette_base.png", size=64)
save_palette_as_image(Palettes.EXTENDED, f"{assets_dir}/palette_extended.png")
save_palette_as_image(Palettes.TERMINAL, f"{assets_dir}/palette_terminal.png")

# script
readme = f"""
![]({'./assets/synthwave_alpha_logo.png'})
> {'Synthwave inspired color palette'}

## Palette

### Base
![](./assets/palette_base.png)

### Terminal
![](./assets/palette_terminal.png)

### Extended
![](./assets/palette_extended.png)

{palette_to_table(array_transpose(Palettes.EXTENDED))}

## Terminal
![](./assets/screenshot_terminal.png)

### Fish
![](./assets/screenshot_fish.png)
```sh
{from_template('fish.sh')}
```

### Fish + Starship
![](./assets/screenshot_fish_starship.png)

```toml
{from_template('starship.toml')}
```

### FZF
![](./assets/screenshot_fzf.png)
```sh
{from_template('fzf.sh')}
```

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
--!>
"""

print(readme.format(**class_as_dict(Colors)))
