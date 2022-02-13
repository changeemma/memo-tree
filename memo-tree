#!/bin/bash
#
selection=""
options=$(python main.py)

# shellcheck disable=SC2236
while [[ ! -z "$options" ]]; do
    # select
    s=$(echo "$options" | dmenu)

    # append selection
    selection="$selection $s"

    # get options
    # shellcheck disable=SC2086
    options=$(python main.py $selection)
done
