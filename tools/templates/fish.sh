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
