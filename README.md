
![](./assets/synthwave_alpha_logo.png)
> Synthwave inspired color palette

## Palette

### Base
![](./assets/palette_base.png)

### Terminal
![](./assets/palette_terminal.png)

### Extended
![](./assets/palette_extended.png)

C | HEX | C | HEX | C | HEX | C | HEX
--- | --- | --- | --- | --- | --- | --- | ---
![](https://via.placeholder.com/20/f9f972/?text=+) | `f9f972` | ![](https://via.placeholder.com/20/adad3e/?text=+) | `adad3e` | ![](https://via.placeholder.com/20/696437/?text=+) | `696437` | ![](https://via.placeholder.com/20/474034/?text=+) | `474034`
![](https://via.placeholder.com/20/e60a70/?text=+) | `e60a70` | ![](https://via.placeholder.com/20/9a0048/?text=+) | `9a0048` | ![](https://via.placeholder.com/20/5f0e3c/?text=+) | `5f0e3c` | ![](https://via.placeholder.com/20/421536/?text=+) | `421536`
![](https://via.placeholder.com/20/ff00f6/?text=+) | `ff00f6` | ![](https://via.placeholder.com/20/b300ad/?text=+) | `b300ad` | ![](https://via.placeholder.com/20/6c0e6f/?text=+) | `6c0e6f` | ![](https://via.placeholder.com/20/481550/?text=+) | `481550`
![](https://via.placeholder.com/20/aa54f9/?text=+) | `aa54f9` | ![](https://via.placeholder.com/20/6e29ad/?text=+) | `6e29ad` | ![](https://via.placeholder.com/20/49226f/?text=+) | `49226f` | ![](https://via.placeholder.com/20/371f50/?text=+) | `371f50`
![](https://via.placeholder.com/20/55a8fb/?text=+) | `55a8fb` | ![](https://via.placeholder.com/20/2a6daf/?text=+) | `2a6daf` | ![](https://via.placeholder.com/20/274470/?text=+) | `274470` | ![](https://via.placeholder.com/20/263050/?text=+) | `263050`
![](https://via.placeholder.com/20/00fbfd/?text=+) | `00fbfd` | ![](https://via.placeholder.com/20/00b0b1/?text=+) | `00b0b1` | ![](https://via.placeholder.com/20/126671/?text=+) | `126671` | ![](https://via.placeholder.com/20/1b4151/?text=+) | `1b4151`
![](https://via.placeholder.com/20/0ae4a4/?text=+) | `0ae4a4` | ![](https://via.placeholder.com/20/00986c/?text=+) | `00986c` | ![](https://via.placeholder.com/20/125a4e/?text=+) | `125a4e` | ![](https://via.placeholder.com/20/1b3b3f/?text=+) | `1b3b3f`
![](https://via.placeholder.com/20/f9f9f1/?text=+) | `f9f9f1` | ![](https://via.placeholder.com/20/f2f2e3/?text=+) | `f2f2e3` | ![](https://via.placeholder.com/20/b9b1bc/?text=+) | `b9b1bc` | ![](https://via.placeholder.com/20/7f7094/?text=+) | `7f7094`
![](https://via.placeholder.com/20/3a3245/?text=+) | `3a3245` | ![](https://via.placeholder.com/20/241b30/?text=+) | `241b30` | ![](https://via.placeholder.com/20/1a1322/?text=+) | `1a1322` | ![](https://via.placeholder.com/20/0f0b14/?text=+) | `0f0b14`


## Implementations

### Terminal
![](./assets/screenshot_terminal.png)

## Fish
![](./assets/screenshot_fish.png)
```sh
# https://fishshell.com/docs/current/cmds/set_color.html#cmd-set-color

set -U fish_color_normal WHITE # default color
set -U fish_color_command BRMAGENTA # commands like echo
set -U fish_color_keyword BRMAGENTA # keywords like if - this falls back on the command color if unset
set -U fish_color_quote BRCYAN # quoted text like "abc"
set -U fish_color_redirection BRYELLOW # IO redirections like >/dev/null
set -U fish_color_end BRYELLOW # process separators like ';' and '&'
set -U fish_color_error WHITE # syntax errors
set -U fish_color_param BRWHITE # ordinary command parameters
set -U fish_color_comment BRBLACK # comments like '# important'
set -U fish_color_selection normal # selected text in vi visual mode
set -U fish_color_operator BRYELLOW # parameter expansion operators like '*' and '~'
set -U fish_color_escape CYAN # character escapes like 'n' and 'x70'
set -U fish_color_autosuggestion BRBLACK # autosuggestions (the proposed rest of a command)
set -U fish_color_cwd normal # the current working directory in the default prompt
set -U fish_color_user normal # the username in the default prompt
set -U fish_color_host normal # the hostname in the default prompt
set -U fish_color_host_remote normal # the hostname in the default prompt for remote sessions (like ssh)
set -U fish_color_cancel normal # the '^C' indicator on a canceled command
set -U fish_color_search_match normal # history search matches and selected pager items (background only)
set -U fish_pager_color_progress normal # the progress bar at the bottom left corner
set -U fish_pager_color_background --background=normal # the background color of a line
set -U fish_pager_color_prefix WHITE --underline # the prefix string, i.e. the string that is to be completed
set -U fish_pager_color_completion BRBLACK # the completion itself, i.e. the proposed rest of the string
set -U fish_pager_color_description BRBLACK # the completion description
set -U fish_pager_color_selected_background --background=normal # background of the selected completion
set -U fish_pager_color_selected_prefix BRGREEN --bold --underline # prefix of the selected completion
set -U fish_pager_color_selected_completion BRGREEN # suffix of the selected completion
set -U fish_pager_color_selected_description BRWHITE # description of the selected completion
set -U fish_pager_color_secondary_background normal # background of every second unselected completion
set -U fish_pager_color_secondary_prefix WHITE --underline # prefix of every second unselected completion
set -U fish_pager_color_secondary_completion BRBLACK # suffix of every second unselected completion
set -U fish_pager_color_secondary_description BRBLACK # description of every second unselected completion

```

## FZF
![](./assets/screenshot_fzf.png)
```sh
# https://github.com/junegunn/fzf/wiki/Color-schemes

export FZF_DEFAULT_OPTS='
--layout=reverse
--color=fg:#7f7094,bg:-1,hl:#b9b1bc
--color=fg+:#00986c,bg+:#241b30,hl+:#0ae4a4
--color=info:#aa54f9,prompt:#0ae4a4,pointer:#241b30
--color=marker:#0ae4a4,spinner:#aa54f9,header:#f9f972
'

```

## Starship
Using a [Nerd Font](https://www.nerdfonts.com/)

![](https://via.placeholder.com/640x240/dddddd/?text=screenshot)

```toml
[character]
success_symbol = "[❯](bold 0ae4a4)"
error_symbol = "[❯](bold e60a70)"

[cmd_duration]
format = "[took $duration](#7f7094) "

[directory]
read_only = " "
style = "#00fbfd bold"

[git_branch]
format = "[on](#7f7094) [ $branch](#ff00f6) "

[package]
style = ""
format = "[is](#7f7094) [$version](#f2f2e3) "

[nodejs]
format = "[<node $version>](#f9f972) "

```

## VCS / Diff

Status | C | Hex
--- | --- | ---
Added gutter | ![](https://via.placeholder.com/24/125a4e/?text=+) | #125a4e
Added background | ![](https://via.placeholder.com/24/1b3b3f/?text=+) | #1b3b3f
Deleted gutter | ![](https://via.placeholder.com/24/5f0e3c/?text=+) | #5f0e3c
Deleted background | ![](https://via.placeholder.com/24/421536/?text=+) | #421536
Modified gutter | ![](https://via.placeholder.com/24/274470/?text=+) | #274470
Modified background | ![](https://via.placeholder.com/24/263050/?text=+) | #263050
Conflict gutter | ![](https://via.placeholder.com/24/696437/?text=+) | #696437
Conflict background | ![](https://via.placeholder.com/24/474034/?text=+) | #474034

