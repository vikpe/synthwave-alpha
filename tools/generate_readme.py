# methods
def placeholder(hex, text='+', size=48):
    return f'![](https://via.placeholder.com/{size}/{hex}/?text={text})'

screenshot_placeholder = placeholder('dddddd', text='screenshot', size='640x240')

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

# palettes
p_default = [
    [c_yellow],
    [c_magenta],
    [c_purple],
    [c_blue],
    [c_cyan],
    [c_white],
    [c_black],
]

p_extended = [
    [c_yellow, c_red, c_magenta, c_purple, c_blue, c_cyan, c_green, c_white, c_white_darker],
    [c_yellow_dark, c_red_dark, c_magenta_dark, c_purple_dark, c_blue_dark, c_cyan_dark, c_green_dark, c_white_dark,
     c_black]
]

p_full = [
    [c_yellow, c_red, c_magenta, c_purple, c_blue, c_cyan, c_green, c_white, c_black_light],
    [c_yellow_dark, c_red_dark, c_magenta_dark, c_purple_dark, c_blue_dark, c_cyan_dark, c_green_dark, c_white_dark,
     c_black],
    [c_yellow_darker, c_red_darker, c_magenta_darker, c_purple_darker, c_blue_darker, c_cyan_darker, c_green_darker,
     c_white_darker, c_black_dark],
    [c_yellow_darkest, c_red_darkest, c_magenta_darkest, c_purple_darkest, c_blue_darkest, c_cyan_darkest,
     c_green_darkest],
]

# script
print(f'''
![]({'https://raw.githubusercontent.com/vikpe/synthwave/main/assets/synthwave_alpha_logo.png'})
> {'Synthwave inspired color palette'}
''')

print('## Palette')

print('### Base')

for shades in p_default:
    for color in shades:
        print(placeholder(color))

print()

print('### Extended')

for shades in p_extended:
    for color in shades:
        print(placeholder(color, size=36))
    print()

print()

# print(palette_to_table(p_extended))

print('### Full')

for shades in p_full:
    for color in shades:
        print(placeholder(color, size=36))
    print()

print()

# print(palette_to_table(p_full))

print(f'''
## Terminal

{screenshot_placeholder}

**Default**

{placeholder(c_white)}
{placeholder(c_black)}

**Highlight**

{placeholder(c_black)}
{placeholder(c_green)}

**Palette**
''')

dark_colors = [
    c_black_dark,
    c_red_dark,
    c_green_dark,
    c_yellow_dark,
    c_blue_dark,
    c_magenta_dark,
    c_cyan_dark,
    c_white_darker,
]

for color in dark_colors:
    print(placeholder(color))

print()

light_colors = [
    c_white_darker,
    c_red,
    c_green,
    c_yellow,
    c_blue,
    c_magenta,
    c_cyan,
    c_white_dark,
]

for color in light_colors:
    print(placeholder(color))

print()

print(f'''
## Fish
{screenshot_placeholder}
```sh
# https://fishshell.com/docs/current/cmds/set_color.html#cmd-set-color

set -U fish_color_normal {c_white_dark} # default color
set -U fish_color_command {c_magenta} # commands like echo
set -U fish_color_keyword {c_magenta} # keywords like if - this falls back on the command color if unset
set -U fish_color_quote {c_cyan} # quoted text like "abc"
set -U fish_color_redirection {c_yellow} # IO redirections like >/dev/null
set -U fish_color_end {c_yellow} # process separators like ';' and '&'
set -U fish_color_error {c_white_dark} # syntax errors
set -U fish_color_param {c_white} # ordinary command parameters
set -U fish_color_comment {c_cyan} # comments like '# important'
set -U fish_color_selection normal # selected text in vi visual mode
set -U fish_color_operator {c_yellow} # parameter expansion operators like '*' and '~'
set -U fish_color_escape {c_green_dark} # character escapes like 'n' and 'x70'
set -U fish_color_autosuggestion {c_white_darker} # autosuggestions (the proposed rest of a command)
set -U fish_color_cwd normal # the current working directory in the default prompt
set -U fish_color_user normal # the username in the default prompt
set -U fish_color_host normal # the hostname in the default prompt
set -U fish_color_host_remote normal # the hostname in the default prompt for remote sessions (like ssh)
set -U fish_color_cancel normal # the '^C' indicator on a canceled command
set -U fish_color_search_match normal # history search matches and selected pager items (background only)
set -U fish_pager_color_progress normal # the progress bar at the bottom left corner
set -U fish_pager_color_background --background=normal # the background color of a line
set -U fish_pager_color_prefix {c_white_dark} --underline # the prefix string, i.e. the string that is to be completed
set -U fish_pager_color_completion {c_white_darker} # the completion itself, i.e. the proposed rest of the string
set -U fish_pager_color_description {c_white_darker} # the completion description
set -U fish_pager_color_selected_background --background={c_black_dark} # background of the selected completion
set -U fish_pager_color_selected_prefix 0be6a8 --bold --underline # prefix of the selected completion
set -U fish_pager_color_selected_completion {c_green} # suffix of the selected completion
set -U fish_pager_color_selected_description {c_white_dark} # description of the selected completion
set -U fish_pager_color_secondary_background # background of every second unselected completion
set -U fish_pager_color_secondary_prefix {c_white_dark} --underline # prefix of every second unselected completion
set -U fish_pager_color_secondary_completion {c_white_darker} # suffix of every second unselected completion
set -U fish_pager_color_secondary_description {c_white_darker} # description of every second unselected completion
```

## FZF
{screenshot_placeholder}
```sh
export FZF_DEFAULT_OPTS='
 --color=fg:#{c_white_darker},bg:#{c_black},hl:#{c_white_dark}
 --color=fg+:#{c_green},bg+:#{c_black_dark},hl+:#{c_green}
 --color=info:#55a7fb,prompt:#{c_green},pointer:#{c_magenta}
 --color=marker:#{c_green},spinner:#{c_blue},header:#{c_cyan}
 '
```


## Starship
Using a [Nerd Font](https://www.nerdfonts.com/)

{screenshot_placeholder}

```toml
[character]
success_symbol = "[❯](bold green)"
error_symbol = "[❯](bold red)"

[cmd_duration]
format = "[took $duration](#{c_white_darker}) "

[directory]
read_only = " "
style = "#{c_cyan} bold"

[git_branch]
format = "[on](#{c_white_darker}) [ $branch](#{c_magenta}) "

[package]
style = ""
format = "[is](#{c_white_darker}) [$version](#{c_white}) "

[nodejs]
format = "[<node $version>](#{c_yellow}) "
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
