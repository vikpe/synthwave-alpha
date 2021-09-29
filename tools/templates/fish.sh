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
