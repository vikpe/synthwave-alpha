# https://fishshell.com/docs/current/cmds/set_color.html#cmd-set-color

set -U fish_color_normal {WHITE_DARK.hex} # default color
set -U fish_color_command {MAGENTA.hex} # commands like echo
set -U fish_color_keyword {MAGENTA.hex} # keywords like if - this falls back on the command color if unset
set -U fish_color_quote {CYAN.hex} # quoted text like "abc"
set -U fish_color_redirection {YELLOW.hex} # IO redirections like >/dev/null
set -U fish_color_end {YELLOW.hex} # process separators like ';' and '&'
set -U fish_color_error {WHITE_DARK.hex} # syntax errors
set -U fish_color_param {WHITE.hex} # ordinary command parameters
set -U fish_color_comment {WHITE_DARKER.hex} # comments like '# important'
set -U fish_color_selection normal # selected text in vi visual mode
set -U fish_color_operator {YELLOW.hex} # parameter expansion operators like '*' and '~'
set -U fish_color_escape {CYAN_DARK.hex} # character escapes like 'n' and 'x70'
set -U fish_color_autosuggestion {WHITE_DARKER.hex} # autosuggestions (the proposed rest of a command)
set -U fish_color_cwd normal # the current working directory in the default prompt
set -U fish_color_user normal # the username in the default prompt
set -U fish_color_host normal # the hostname in the default prompt
set -U fish_color_host_remote normal # the hostname in the default prompt for remote sessions (like ssh)
set -U fish_color_cancel normal # the '^C' indicator on a canceled command
set -U fish_color_search_match normal # history search matches and selected pager items (background only)
set -U fish_pager_color_progress normal # the progress bar at the bottom left corner
set -U fish_pager_color_background --background=normal # the background color of a line
set -U fish_pager_color_prefix {WHITE_DARK.hex} --underline # the prefix string, i.e. the string that is to be completed
set -U fish_pager_color_completion {WHITE_DARKER.hex} # the completion itself, i.e. the proposed rest of the string
set -U fish_pager_color_description {WHITE_DARKER.hex} # the completion description
set -U fish_pager_color_selected_background --background=normal # background of the selected completion
set -U fish_pager_color_selected_prefix {GREEN.hex} --bold --underline # prefix of the selected completion
set -U fish_pager_color_selected_completion {GREEN.hex} # suffix of the selected completion
set -U fish_pager_color_selected_description {WHITE.hex} # description of the selected completion
set -U fish_pager_color_secondary_background normal # background of every second unselected completion
set -U fish_pager_color_secondary_prefix {WHITE_DARK.hex} --underline # prefix of every second unselected completion
set -U fish_pager_color_secondary_completion {WHITE_DARKER.hex} # suffix of every second unselected completion
set -U fish_pager_color_secondary_description {WHITE_DARKER.hex} # description of every second unselected completion
