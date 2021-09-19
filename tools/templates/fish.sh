# https://fishshell.com/docs/current/cmds/set_color.html#cmd-set-color

set -U fish_color_normal {C_WHITE_DARK} # default color
set -U fish_color_command {C_MAGENTA} # commands like echo
set -U fish_color_keyword {C_MAGENTA} # keywords like if - this falls back on the command color if unset
set -U fish_color_quote {C_CYAN} # quoted text like "abc"
set -U fish_color_redirection {C_YELLOW} # IO redirections like >/dev/null
set -U fish_color_end {C_YELLOW} # process separators like ';' and '&'
set -U fish_color_error {C_WHITE_DARK} # syntax errors
set -U fish_color_param {C_WHITE} # ordinary command parameters
set -U fish_color_comment {C_CYAN} # comments like '# important'
set -U fish_color_selection normal # selected text in vi visual mode
set -U fish_color_operator {C_YELLOW} # parameter expansion operators like '*' and '~'
set -U fish_color_escape {C_GREEN_DARK} # character escapes like 'n' and 'x70'
set -U fish_color_autosuggestion {C_WHITE_DARKER} # autosuggestions (the proposed rest of a command)
set -U fish_color_cwd normal # the current working directory in the default prompt
set -U fish_color_user normal # the username in the default prompt
set -U fish_color_host normal # the hostname in the default prompt
set -U fish_color_host_remote normal # the hostname in the default prompt for remote sessions (like ssh)
set -U fish_color_cancel normal # the '^C' indicator on a canceled command
set -U fish_color_search_match normal # history search matches and selected pager items (background only)
set -U fish_pager_color_progress normal # the progress bar at the bottom left corner
set -U fish_pager_color_background --background=normal # the background color of a line
set -U fish_pager_color_prefix {C_WHITE_DARK} --underline # the prefix string, i.e. the string that is to be completed
set -U fish_pager_color_completion {C_WHITE_DARKER} # the completion itself, i.e. the proposed rest of the string
set -U fish_pager_color_description {C_WHITE_DARKER} # the completion description
set -U fish_pager_color_selected_background --background={C_BLACK_DARK} # background of the selected completion
set -U fish_pager_color_selected_prefix 0be6a8 --bold --underline # prefix of the selected completion
set -U fish_pager_color_selected_completion {C_GREEN} # suffix of the selected completion
set -U fish_pager_color_selected_description {C_WHITE_DARK} # description of the selected completion
set -U fish_pager_color_secondary_background # background of every second unselected completion
set -U fish_pager_color_secondary_prefix {C_WHITE_DARK} --underline # prefix of every second unselected completion
set -U fish_pager_color_secondary_completion {C_WHITE_DARKER} # suffix of every second unselected completion
set -U fish_pager_color_secondary_description {C_WHITE_DARKER} # description of every second unselected completion
