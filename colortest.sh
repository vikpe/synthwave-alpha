#!/bin/bash
#
#   This file echoes a bunch of color codes to the
#   terminal to demonstrate what's available.  Each
#   line is the color code of one forground color,
#   out of 17 (default + 16 escapes), followed by a
#   test use of that color on all nine background
#   colors (default + 8 escapes).
#

# config
text='test'
fgs=('m' '1m' '30m' '1;30m' '31m' '1;31m' '32m' '1;32m' '33m' '1;33m' '34m' '1;34m' '35m' '1;35m' '36m' '1;36m' '37m' '1;37m')
bgs=('40m' '41m' '42m' '43m' '44m' '45m' '46m' '47m')

padding_size=2
separator_size=2

# script
pad_str=$(printf "%${padding_size}s" "")
sep_str=$(printf "%${separator_size}s" "")
reset_fg="\033["
reset_all="${reset_fg}0m"

column_size=$((${#text} + (2 * padding_size) + separator_size))
header_indent_size=$((2 * $column_size))

echo

printf "%${header_indent_size}s" ""

for bg in "${bgs[@]}"; do
    printf "%${column_size}s" "$bg$pad_str$sep_str"
done

echo

for fg in "${fgs[@]}"; do
    printf "%${column_size}s $reset_fg$fg$pad_str$text$pad_str" $fg
    for bg in "${bgs[@]}"; do
        echo -en "$EINS$sep_str$reset_fg$fg$reset_fg$bg$pad_str$text$pad_str$reset_all"
    done
    echo
done

echo
