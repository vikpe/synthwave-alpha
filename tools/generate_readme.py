class Color:
    hex: str
    name: str

    def __init__(self, hex: str, name='') -> None:
        self.hex = hex;
        self.name = name;

    def placeholder(self, size=64):
        return f'![](https://via.placeholder.com/{size}/{self.hex}/?text=+)'


class Palette:
    name: str
    colors: list

    def __init__(self, name: str, colors: list) -> None:
        self.name = name
        self.colors = colors


def md_table(rows: list) -> str:
    HEADER_ROW_DELIMITER = '---'
    CELL_DELIMITER = ' | '

    header_row = rows[0]
    header_separator_row = [HEADER_ROW_DELIMITER] * len(header_row)
    all_rows = [header_row] + [header_separator_row] + rows[1:]

    return "\n".join(
        CELL_DELIMITER.join(row) for row in all_rows
    )


def palette_to_table(pal: Palette, placeholder_size=24):
    header_row = ["Name", "C", "HEX"]
    body_rows = [[color.name, color.placeholder(placeholder_size), color.hex] for color in pal.colors]

    return md_table([header_row] + body_rows)


color_yellow = Color('f9f972', 'Yellow')
color_yellow_dark = Color('adad3e', 'Yellow Dark')
color_red = Color('e80c72', 'Red')
color_red_dark = Color('9c044b', 'Red Dark')
color_magenta = Color('ff00f6', 'Magenta')
color_magenta_dark = Color('b312ad', 'Magenta Dark')
color_purple = Color('aa54f8', 'Purple')
color_purple_dark = Color('6c29ab', 'Purple Dark')
color_blue = Color('55a7fb', 'Blue')
color_blue_dark = Color('2a6cad', 'Blue Dark')
color_cyan = Color('00fbfd', 'Cyan')
color_cyan_dark = Color('00b0b0', 'Cyan Dark')
color_green = Color('0be6a8', 'Green')
color_green_dark = Color('04996f', 'Green Dark')
color_white = Color('f2f2e3', 'White')
color_white_dark = Color('b9b1bb', 'White Dark')
color_white_darker = Color('7f6f93', 'White Darker')
color_black = Color('241b30', 'Black')
color_black_light = Color('312541', 'Black Light')
color_black_dark = Color('1d1627', 'Black Dark')

palette_default = Palette(
    "default",
    [
        color_yellow,
        color_red,
        color_magenta,
        color_purple,
        color_blue,
        color_cyan,
        color_green,
        color_white,
        color_black,
    ]
)

palette_color_dark = Palette(
    "dark",
    [
        color_yellow_dark,
        color_red_dark,
        color_magenta_dark,
        color_purple_dark,
        color_blue_dark,
        color_cyan_dark,
        color_green_dark,
    ]
)

repo_logo_url = 'https://raw.githubusercontent.com/vikpe/synthwave/main/assets/synthwave_alpha_logo.png'
repo_description = 'Synthwave inspired color palette'

print(
    f'''
![]({repo_logo_url})
> {repo_description}
'''
)

print('## Base palette')

for color in palette_default.colors:
    print(color.placeholder())

print()

print(palette_to_table(palette_default))

todo = f'''
## Extended palette

![](https://via.placeholder.com/64/474034/?text=+)
![](https://via.placeholder.com/64/421637/?text=+)
![](https://via.placeholder.com/64/481950/?text=+)
![](https://via.placeholder.com/64/361F4F/?text=+)
![](https://via.placeholder.com/64/263050/?text=+)
![](https://via.placeholder.com/64/1B4150/?text=+)
![](https://via.placeholder.com/64/1c3b40/?text=+)

![](https://via.placeholder.com/64/696437/?text=+)
![](https://via.placeholder.com/64/60103E/?text=+)
![](https://via.placeholder.com/64/6C176F/?text=+)
![](https://via.placeholder.com/64/48226E/?text=+)
![](https://via.placeholder.com/64/27446f/?text=+)
![](https://via.placeholder.com/64/126670/?text=+)
![](https://via.placeholder.com/64/145a50/?text=+)

{color_yellow_dark.placeholder()}
{color_red_dark.placeholder()}
{color_magenta_dark.placeholder()}
{color_purple_dark.placeholder()}
{color_blue_dark.placeholder()}
{color_cyan_dark.placeholder()}
{color_green_dark.placeholder()}

{color_yellow.placeholder()}
{color_red.placeholder()}
{color_magenta.placeholder()}
{color_purple.placeholder()}
{color_blue.placeholder()}
{color_cyan.placeholder()}
{color_green.placeholder()}

{color_white.placeholder()}
{color_white_dark.placeholder()}
{color_white_darker.placeholder()}
{color_black_light.placeholder()}
{color_black.placeholder()}
{color_black_dark.placeholder()}

C | Hex | C | Hex | C | Hex
--- | --- | --- | --- | --- | ---
{color_yellow.placeholder(size=24)} | #{color_yellow.hex} | {color_yellow_dark.placeholder(size=24)} | #adad3e
![](https://via.placeholder.com/24/e80c72/?text=+) | #e80c72 | ![](https://via.placeholder.com/24/9c044b/?text=+) | #9c044b
![](https://via.placeholder.com/24/ff00f6/?text=+) | #ff00f6 | ![](https://via.placeholder.com/24/b312ad/?text=+) | #b312ad
![](https://via.placeholder.com/24/aa54f8/?text=+) | #aa54f8 | ![](https://via.placeholder.com/24/6c29ab/?text=+) | #6c29ab
![](https://via.placeholder.com/24/55a7fb/?text=+) | #55a7fb | ![](https://via.placeholder.com/24/2a6cad/?text=+) | #2a6cad
![](https://via.placeholder.com/24/00fbfd/?text=+) | #00fbfd | ![](https://via.placeholder.com/24/00b0b0/?text=+) | #00b0b0
![](https://via.placeholder.com/24/0be6a8/?text=+) | #0be6a8 | ![](https://via.placeholder.com/24/04996f/?text=+) | #04996f
![](https://via.placeholder.com/24/f2f2e3/?text=+) | #f2f2e3 | ![](https://via.placeholder.com/24/b9b1bb/?text=+) | #b9b1bb | ![](https://via.placeholder.com/24/7f6f93/?text=+) | #7f6f93
![](https://via.placeholder.com/24/312541/?text=+) | #312541 | ![](https://via.placeholder.com/24/241b30/?text=+) | #241b30 | ![](https://via.placeholder.com/24/1d1627/?text=+) | #1d1627


## Terminal

**Default**

{color_white.placeholder()}
{color_black.placeholder()}

**Highlight**

{color_black.placeholder()}
{color_green.placeholder()}

**Palette**

{color_black_dark.placeholder()}
{color_red_dark.placeholder()}
{color_green_dark.placeholder()}
{color_yellow_dark.placeholder()}
{color_blue_dark.placeholder()}
{color_magenta_dark.placeholder()}
{color_cyan_dark.placeholder()}
{color_white_darker.placeholder()}

{color_white_darker.placeholder()}
{color_red.placeholder()}
{color_green.placeholder()}
{color_yellow.placeholder()}
{color_blue.placeholder()}
{color_magenta.placeholder()}
{color_cyan.placeholder()}
{color_white_dark.placeholder()}


## Fish
```sh
# The colors used by fish for syntax highlighting can be configured by changing the values of a various variables.
# The value of these variables can be one of the colors accepted by the set_color command.
# The modifier switches accepted by set_color like --bold, --dim, --italics, --reverse and --underline are also accepted.
# https://fishshell.com/docs/current/cmds/set_color.html#cmd-set-color

set -U fish_color_normal {color_white_dark.hex} # default color
set -U fish_color_command {color_magenta.hex} # commands like echo
set -U fish_color_keyword {color_magenta.hex} # keywords like if - this falls back on the command color if unset
set -U fish_color_quote {color_cyan.hex} # quoted text like "abc"
set -U fish_color_redirection {color_yellow.hex} # IO redirections like >/dev/null
set -U fish_color_end {color_yellow.hex} # process separators like ';' and '&'
set -U fish_color_error {color_white_dark.hex} # syntax errors
set -U fish_color_param {color_white.hex} # ordinary command parameters
set -U fish_color_comment {color_cyan.hex} # comments like '# important'
set -U fish_color_selection normal # selected text in vi visual mode
set -U fish_color_operator {color_yellow.hex} # parameter expansion operators like '*' and '~'
set -U fish_color_escape {color_green_dark.hex} # character escapes like 'n' and 'x70'
set -U fish_color_autosuggestion {color_white_darker.hex} # autosuggestions (the proposed rest of a command)
set -U fish_color_cwd normal # the current working directory in the default prompt
set -U fish_color_user normal # the username in the default prompt
set -U fish_color_host normal # the hostname in the default prompt
set -U fish_color_host_remote normal # the hostname in the default prompt for remote sessions (like ssh)
set -U fish_color_cancel normal # the '^C' indicator on a canceled command
set -U fish_color_search_match normal # history search matches and selected pager items (background only)
set -U fish_pager_color_progress normal # the progress bar at the bottom left corner
set -U fish_pager_color_background --background=normal # the background color of a line
set -U fish_pager_color_prefix {color_white_dark.hex} --underline # the prefix string, i.e. the string that is to be completed
set -U fish_pager_color_completion {color_white_darker.hex} # the completion itself, i.e. the proposed rest of the string
set -U fish_pager_color_description {color_white_darker.hex} # the completion description
set -U fish_pager_color_selected_background --background={color_black_dark.hex} # background of the selected completion
set -U fish_pager_color_selected_prefix 0be6a8 --bold --underline # prefix of the selected completion
set -U fish_pager_color_selected_completion {color_green.hex} # suffix of the selected completion
set -U fish_pager_color_selected_description {color_white_dark.hex} # description of the selected completion
set -U fish_pager_color_secondary_background # background of every second unselected completion
set -U fish_pager_color_secondary_prefix {color_white_dark.hex} --underline # prefix of every second unselected completion
set -U fish_pager_color_secondary_completion {color_white_darker.hex} # suffix of every second unselected completion
set -U fish_pager_color_secondary_description {color_white_darker.hex} # description of every second unselected completion
```

## FZF
```sh
export FZF_DEFAULT_OPTS='
 --color=fg:#{color_white_darker.hex},bg:#{color_black.hex},hl:#{color_white_dark.hex}
 --color=fg+:#{color_green.hex},bg+:#{color_black_dark.hex},hl+:#{color_green.hex}
 --color=info:#55a7fb,prompt:#{color_green.hex},pointer:#{color_magenta.hex}
 --color=marker:#{color_green.hex},spinner:#{color_blue.hex},header:#{color_cyan.hex}
 '
```


## Starship
Using a [Nerd Font](https://www.nerdfonts.com/)

```toml
[character]
success_symbol = "[❯](bold green)"
error_symbol = "[❯](bold red)"

[cmd_duration]
format = "[took $duration](#{color_white_darker.hex}) "

[directory]
read_only = " "
style = "#{color_cyan.hex} bold"

[git_branch]
format = "[on](#{color_white_darker.hex}) [ $branch](#{color_magenta.hex}) "

[package]
style = ""
format = "[is](#{color_white_darker.hex}) [$version](#{color_white.hex}) "

[nodejs]
format = "[<node $version>](#{color_yellow.hex}) "
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
Conflict background | ![](https://via.placeholder.com/24/474034/?text=+) | #474034'''

print(todo)
