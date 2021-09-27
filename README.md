
![](./assets/synthwave_alpha_logo.png)
> Synthwave inspired color palette

## Palette

### Base
![](./assets/palette_base.png)

### Extended
![](./assets/palette_extended.png)

C | HEX | C | HEX | C | HEX | C | HEX
--- | --- | --- | --- | --- | --- | --- | ---
![](https://via.placeholder.com/20/f8f871/?text=+) | `f8f871` | ![](https://via.placeholder.com/20/abab3c/?text=+) | `abab3c` | ![](https://via.placeholder.com/20/676336/?text=+) | `676336` | ![](https://via.placeholder.com/20/453f33/?text=+) | `453f33`
![](https://via.placeholder.com/20/e80b72/?text=+) | `e80b72` | ![](https://via.placeholder.com/20/9b0048/?text=+) | `9b0048` | ![](https://via.placeholder.com/20/5f0d3c/?text=+) | `5f0d3c` | ![](https://via.placeholder.com/20/411436/?text=+) | `411436`
![](https://via.placeholder.com/20/ff00f6/?text=+) | `ff00f6` | ![](https://via.placeholder.com/20/b200ac/?text=+) | `b200ac` | ![](https://via.placeholder.com/20/6b0d6e/?text=+) | `6b0d6e` | ![](https://via.placeholder.com/20/47144f/?text=+) | `47144f`
![](https://via.placeholder.com/20/aa53f8/?text=+) | `aa53f8` | ![](https://via.placeholder.com/20/6d28ab/?text=+) | `6d28ab` | ![](https://via.placeholder.com/20/48216d/?text=+) | `48216d` | ![](https://via.placeholder.com/20/361e4e/?text=+) | `361e4e`
![](https://via.placeholder.com/20/55a7fa/?text=+) | `55a7fa` | ![](https://via.placeholder.com/20/296bad/?text=+) | `296bad` | ![](https://via.placeholder.com/20/26436e/?text=+) | `26436e` | ![](https://via.placeholder.com/20/252f4f/?text=+) | `252f4f`
![](https://via.placeholder.com/20/00fbfd/?text=+) | `00fbfd` | ![](https://via.placeholder.com/20/00afb0/?text=+) | `00afb0` | ![](https://via.placeholder.com/20/126570/?text=+) | `126570` | ![](https://via.placeholder.com/20/1b4050/?text=+) | `1b4050`
![](https://via.placeholder.com/20/0be6a6/?text=+) | `0be6a6` | ![](https://via.placeholder.com/20/00996c/?text=+) | `00996c` | ![](https://via.placeholder.com/20/125a4e/?text=+) | `125a4e` | ![](https://via.placeholder.com/20/1b3a3f/?text=+) | `1b3a3f`
![](https://via.placeholder.com/20/f8f8f1/?text=+) | `f8f8f1` | ![](https://via.placeholder.com/20/f2f2e3/?text=+) | `f2f2e3` | ![](https://via.placeholder.com/20/b8b1bb/?text=+) | `b8b1bb` | ![](https://via.placeholder.com/20/7f7094/?text=+) | `7f7094`
![](https://via.placeholder.com/20/393144/?text=+) | `393144` | ![](https://via.placeholder.com/20/241b30/?text=+) | `241b30` | ![](https://via.placeholder.com/20/191221/?text=+) | `191221` | ![](https://via.placeholder.com/20/0e0a13/?text=+) | `0e0a13`


## Implementations

### Terminal
![](https://via.placeholder.com/640x240/dddddd/?text=screenshot)

**Default**

![](https://via.placeholder.com/48/f2f2e3/?text=+)
![](https://via.placeholder.com/48/241b30/?text=+)

**Highlight**

![](https://via.placeholder.com/48/241b30/?text=+)
![](https://via.placeholder.com/48/0be6a6/?text=+)

**Palette**

![](./assets/palette_terminal.png)

## Fish
![](https://via.placeholder.com/640x240/dddddd/?text=screenshot)
```sh
# https://fishshell.com/docs/current/cmds/set_color.html#cmd-set-color

set -U fish_color_normal b8b1bb # default color
set -U fish_color_command ff00f6 # commands like echo
set -U fish_color_keyword ff00f6 # keywords like if - this falls back on the command color if unset
set -U fish_color_quote 00fbfd # quoted text like "abc"
set -U fish_color_redirection f8f871 # IO redirections like >/dev/null
set -U fish_color_end f8f871 # process separators like ';' and '&'
set -U fish_color_error b8b1bb # syntax errors
set -U fish_color_param f2f2e3 # ordinary command parameters
set -U fish_color_comment 00fbfd # comments like '# important'
set -U fish_color_selection normal # selected text in vi visual mode
set -U fish_color_operator f8f871 # parameter expansion operators like '*' and '~'
set -U fish_color_escape 00996c # character escapes like 'n' and 'x70'
set -U fish_color_autosuggestion 7f7094 # autosuggestions (the proposed rest of a command)
set -U fish_color_cwd normal # the current working directory in the default prompt
set -U fish_color_user normal # the username in the default prompt
set -U fish_color_host normal # the hostname in the default prompt
set -U fish_color_host_remote normal # the hostname in the default prompt for remote sessions (like ssh)
set -U fish_color_cancel normal # the '^C' indicator on a canceled command
set -U fish_color_search_match normal # history search matches and selected pager items (background only)
set -U fish_pager_color_progress normal # the progress bar at the bottom left corner
set -U fish_pager_color_background --background=normal # the background color of a line
set -U fish_pager_color_prefix b8b1bb --underline # the prefix string, i.e. the string that is to be completed
set -U fish_pager_color_completion 7f7094 # the completion itself, i.e. the proposed rest of the string
set -U fish_pager_color_description 7f7094 # the completion description
set -U fish_pager_color_selected_background --background=191221 # background of the selected completion
set -U fish_pager_color_selected_prefix 0be6a8 --bold --underline # prefix of the selected completion
set -U fish_pager_color_selected_completion 0be6a6 # suffix of the selected completion
set -U fish_pager_color_selected_description b8b1bb # description of the selected completion
set -U fish_pager_color_secondary_background # background of every second unselected completion
set -U fish_pager_color_secondary_prefix b8b1bb --underline # prefix of every second unselected completion
set -U fish_pager_color_secondary_completion 7f7094 # suffix of every second unselected completion
set -U fish_pager_color_secondary_description 7f7094 # description of every second unselected completion

```

## FZF
![](https://via.placeholder.com/640x240/dddddd/?text=screenshot)
```sh
export FZF_DEFAULT_OPTS='
--color=fg:#7f7094,bg:#241b30,hl:#b8b1bb
--color=fg+:#0be6a6,bg+:#191221,hl+:#0be6a6
--color=info:#55a7fb,prompt:#0be6a6,pointer:#ff00f6
--color=marker:#0be6a6,spinner:#55a7fa,header:#00fbfd
'

```

## Starship
Using a [Nerd Font](https://www.nerdfonts.com/)

![](https://via.placeholder.com/640x240/dddddd/?text=screenshot)

```toml
[character]
success_symbol = "[❯](bold 0be6a6)"
error_symbol = "[❯](bold e80b72)"

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
format = "[<node $version>](#f8f871) "

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

