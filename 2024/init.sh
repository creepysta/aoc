#!/usr/bin/env bash
# set -eux

year=2024
day=$1
session_token_path="${HOME}/.aoc.session"


if [[ -z "$day" ]]; then
    echo "No argument supplied. Exiting";
    return 1;
fi


dir_name=day$day
inp_file="$dir_name/in.txt"

if [[ -d "$dir_name" ]]; then
    echo "$dir_name already exists.";
else
    echo "Initializing $dir_name ..."
    mkdir $dir_name
    cp ./.cr.template $dir_name/a.cr
    cp ./.py.template $dir_name/a.py
    sed -i '' -e "s/{DAY_XX}/$dir_name/g" "$dir_name/a.cr"
    sed -i '' -e "s/{DAY_XX}/$dir_name/g" "$dir_name/a.py"
fi


if [[ -f "$session_token_path" ]]; then
    if [[ ! -f "$inp_file" ]]; then
        session=$(cat $session_token_path)
        curl -H "cookie: $session;" "https://adventofcode.com/$year/day/$(expr $day + 0)/input" > "$inp_file"
    fi
else
    cat $session_token_path
    echo "Cannot find session token at $session_token_path. Going to skip downloading input.";
fi

cd $dir_name

# set +eux
