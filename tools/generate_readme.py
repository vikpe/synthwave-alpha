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
screenshot_placeholder = placeholder("dddddd", text="screenshot", size="640x240")

readme = f"""
![]({'./assets/synthwave_alpha_logo.png'})
> {'Synthwave inspired color palette'}

## Palette

### Base
![](./assets/palette_base.png)

### Extended
![](./assets/palette_extended.png)

{palette_to_table(array_transpose(Palettes.EXTENDED))}

## Implementations

### Terminal
{screenshot_placeholder}

**Default**

{placeholder(Colors.WHITE.hex)}
{placeholder(Colors.BLACK.hex)}

**Highlight**

{placeholder(Colors.BLACK.hex)}
{placeholder(Colors.GREEN.hex)}

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

print(readme.format(**class_as_dict(Colors)))
