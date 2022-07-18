# https://fishshell.com/docs/current/cmds/set_color.html#cmd-set-color

set -U fish_color_normal b9b1bc # default color
set -U fish_color_command ff00f6 # commands like echo
set -U fish_color_keyword ff00f6 # keywords like if - this falls back on the command color if unset
set -U fish_color_quote 00fbfd # quoted text like "abc"
set -U fish_color_redirection f9f972 # IO redirections like >/dev/null
set -U fish_color_end f9f972 # process separators like ';' and '&'
set -U fish_color_error b9b1bc # syntax errors
set -U fish_color_param f2f2e3 # ordinary command parameters
set -U fish_color_comment 7f7094 # comments like '# important'
set -U fish_color_selection normal # selected text in vi visual mode
set -U fish_color_operator f9f972 # parameter expansion operators like '*' and '~'
set -U fish_color_escape 00b0b1 # character escapes like 'n' and 'x70'
set -U fish_color_autosuggestion 7f7094 # autosuggestions (the proposed rest of a command)
set -U fish_color_cwd normal # the current working directory in the default prompt
set -U fish_color_user normal # the username in the default prompt
set -U fish_color_host normal # the hostname in the default prompt
set -U fish_color_host_remote normal # the hostname in the default prompt for remote sessions (like ssh)
set -U fish_color_cancel normal # the '^C' indicator on a canceled command
set -U fish_color_search_match normal # history search matches and selected pager items (background only)
set -U fish_pager_color_progress normal # the progress bar at the bottom left corner
set -U fish_pager_color_background --background=normal # the background color of a line
set -U fish_pager_color_prefix b9b1bc --underline # the prefix string, i.e. the string that is to be completed
set -U fish_pager_color_completion 7f7094 # the completion itself, i.e. the proposed rest of the string
set -U fish_pager_color_description 7f7094 # the completion description
set -U fish_pager_color_selected_background --background=normal # background of the selected completion
set -U fish_pager_color_selected_prefix 0ae4a4 --bold --underline # prefix of the selected completion
set -U fish_pager_color_selected_completion 0ae4a4 # suffix of the selected completion
set -U fish_pager_color_selected_description f2f2e3 # description of the selected completion
set -U fish_pager_color_secondary_background normal # background of every second unselected completion
set -U fish_pager_color_secondary_prefix b9b1bc --underline # prefix of every second unselected completion
set -U fish_pager_color_secondary_completion 7f7094 # suffix of every second unselected completion
set -U fish_pager_color_secondary_description 7f7094 # description of every second unselected completion
