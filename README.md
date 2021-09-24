
![](./assets/synthwave_alpha_logo.png)
> Synthwave inspired color palette

## Palette

### Base
![](./assets/palette_base.png)

### Extended
![](./assets/palette_extended.png)

C | HEX | C | HEX | C | HEX | C | HEX
--- | --- | --- | --- | --- | --- | --- | ---
![](https://via.placeholder.com/20/f9f972/?text=+) | `f9f972` | ![](https://via.placeholder.com/20/adad3e/?text=+) | `adad3e` | ![](https://via.placeholder.com/20/686437/?text=+) | `686437` | ![](https://via.placeholder.com/20/463f33/?text=+) | `463f33`
![](https://via.placeholder.com/20/e80c72/?text=+) | `e80c72` | ![](https://via.placeholder.com/20/9c044b/?text=+) | `9c044b` | ![](https://via.placeholder.com/20/600f3d/?text=+) | `600f3d` | ![](https://via.placeholder.com/20/421536/?text=+) | `421536`
![](https://via.placeholder.com/20/ff00f6/?text=+) | `ff00f6` | ![](https://via.placeholder.com/20/b312ad/?text=+) | `b312ad` | ![](https://via.placeholder.com/20/6b166e/?text=+) | `6b166e` | ![](https://via.placeholder.com/20/47184f/?text=+) | `47184f`
![](https://via.placeholder.com/20/aa54f8/?text=+) | `aa54f8` | ![](https://via.placeholder.com/20/6c29ab/?text=+) | `6c29ab` | ![](https://via.placeholder.com/20/48226d/?text=+) | `48226d` | ![](https://via.placeholder.com/20/361e4e/?text=+) | `361e4e`
![](https://via.placeholder.com/20/55a7fb/?text=+) | `55a7fb` | ![](https://via.placeholder.com/20/2a6cad/?text=+) | `2a6cad` | ![](https://via.placeholder.com/20/27436e/?text=+) | `27436e` | ![](https://via.placeholder.com/20/252f4f/?text=+) | `252f4f`
![](https://via.placeholder.com/20/00fbfd/?text=+) | `00fbfd` | ![](https://via.placeholder.com/20/00b0b0/?text=+) | `00b0b0` | ![](https://via.placeholder.com/20/126570/?text=+) | `126570` | ![](https://via.placeholder.com/20/1b4050/?text=+) | `1b4050`
![](https://via.placeholder.com/20/0be6a8/?text=+) | `0be6a8` | ![](https://via.placeholder.com/20/04996f/?text=+) | `04996f` | ![](https://via.placeholder.com/20/145a4f/?text=+) | `145a4f` | ![](https://via.placeholder.com/20/1c3a3f/?text=+) | `1c3a3f`
![](https://via.placeholder.com/20/f9f9f1/?text=+) | `f9f9f1` | ![](https://via.placeholder.com/20/f2f2e3/?text=+) | `f2f2e3` | ![](https://via.placeholder.com/20/b9b1bb/?text=+) | `b9b1bb` | ![](https://via.placeholder.com/20/7f6f93/?text=+) | `7f6f93`
![](https://via.placeholder.com/20/312541/?text=+) | `312541` | ![](https://via.placeholder.com/20/241b30/?text=+) | `241b30` | ![](https://via.placeholder.com/20/1d1627/?text=+) | `1d1627` | ![](https://via.placeholder.com/20/140f1a/?text=+) | `140f1a`


## Implementations

### Terminal
![](https://via.placeholder.com/640x240/dddddd/?text=screenshot)

**Default**

![](https://via.placeholder.com/48/f2f2e3/?text=+)
![](https://via.placeholder.com/48/241b30/?text=+)

**Highlight**

![](https://via.placeholder.com/48/241b30/?text=+)
![](https://via.placeholder.com/48/0be6a8/?text=+)

**Palette**

![](./assets/palette_terminal.png)

## Fish
![](https://via.placeholder.com/640x240/dddddd/?text=screenshot)
```sh
# https://fishshell.com/docs/current/cmds/set_color.html#cmd-set-color

set -U fish_color_normal b9b1bb # default color
set -U fish_color_command ff00f6 # commands like echo
set -U fish_color_keyword ff00f6 # keywords like if - this falls back on the command color if unset
set -U fish_color_quote 00fbfd # quoted text like "abc"
set -U fish_color_redirection f9f972 # IO redirections like >/dev/null
set -U fish_color_end f9f972 # process separators like ';' and '&'
set -U fish_color_error b9b1bb # syntax errors
set -U fish_color_param f2f2e3 # ordinary command parameters
set -U fish_color_comment 00fbfd # comments like '# important'
set -U fish_color_selection normal # selected text in vi visual mode
set -U fish_color_operator f9f972 # parameter expansion operators like '*' and '~'
set -U fish_color_escape 04996f # character escapes like 'n' and 'x70'
set -U fish_color_autosuggestion 7f6f93 # autosuggestions (the proposed rest of a command)
set -U fish_color_cwd normal # the current working directory in the default prompt
set -U fish_color_user normal # the username in the default prompt
set -U fish_color_host normal # the hostname in the default prompt
set -U fish_color_host_remote normal # the hostname in the default prompt for remote sessions (like ssh)
set -U fish_color_cancel normal # the '^C' indicator on a canceled command
set -U fish_color_search_match normal # history search matches and selected pager items (background only)
set -U fish_pager_color_progress normal # the progress bar at the bottom left corner
set -U fish_pager_color_background --background=normal # the background color of a line
set -U fish_pager_color_prefix b9b1bb --underline # the prefix string, i.e. the string that is to be completed
set -U fish_pager_color_completion 7f6f93 # the completion itself, i.e. the proposed rest of the string
set -U fish_pager_color_description 7f6f93 # the completion description
set -U fish_pager_color_selected_background --background=1d1627 # background of the selected completion
set -U fish_pager_color_selected_prefix 0be6a8 --bold --underline # prefix of the selected completion
set -U fish_pager_color_selected_completion 0be6a8 # suffix of the selected completion
set -U fish_pager_color_selected_description b9b1bb # description of the selected completion
set -U fish_pager_color_secondary_background # background of every second unselected completion
set -U fish_pager_color_secondary_prefix b9b1bb --underline # prefix of every second unselected completion
set -U fish_pager_color_secondary_completion 7f6f93 # suffix of every second unselected completion
set -U fish_pager_color_secondary_description 7f6f93 # description of every second unselected completion

```

## FZF
![](https://via.placeholder.com/640x240/dddddd/?text=screenshot)
```sh
export FZF_DEFAULT_OPTS='
--color=fg:#7f6f93,bg:#241b30,hl:#b9b1bb
--color=fg+:#0be6a8,bg+:#1d1627,hl+:#0be6a8
--color=info:#55a7fb,prompt:#0be6a8,pointer:#ff00f6
--color=marker:#0be6a8,spinner:#55a7fb,header:#00fbfd
'

```

## Starship
Using a [Nerd Font](https://www.nerdfonts.com/)

![](https://via.placeholder.com/640x240/dddddd/?text=screenshot)

```toml
[character]
success_symbol = "[❯](bold 0be6a8)"
error_symbol = "[❯](bold e80c72)"

[cmd_duration]
format = "[took $duration](#7f6f93) "

[directory]
read_only = " "
style = "#00fbfd bold"

[git_branch]
format = "[on](#7f6f93) [ $branch](#ff00f6) "

[package]
style = ""
format = "[is](#7f6f93) [$version](#f2f2e3) "

[nodejs]
format = "[<node $version>](#f9f972) "

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

