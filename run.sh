#!/bin/bash
#
PYTHON_INTERPRETER="python3"
DMENU_COMMAND="dmenu"

MEMO_REPOSITORY="<MEMO-TREE REPOSITORY PATH>"

MEMO_SCRIPT="${MEMO_REPOSITORY}/main.py"
MEMO_CSV_FILE="${MEMO_REPOSITORY}/memo_file.csv"
MEMO_COMMAND="${PYTHON_INTERPRETER} ${MEMO_SCRIPT} -f ${MEMO_CSV_FILE}"

# set initial values
MEMO_PATH=""
MEMO_OPT=$(${MEMO_COMMAND})

while [[ -n "${MEMO_OPT}" ]]; do

    # select and check success
    if ! MEMO_SUB_PATH=$(echo "${MEMO_OPT}" | ${DMENU_COMMAND}) ; then
        exit $?
    fi

    # append selection
    MEMO_PATH="${MEMO_PATH} ${MEMO_SUB_PATH}"

    # get options
    # shellcheck disable=SC2086
    MEMO_OPT=$(${MEMO_COMMAND} ${MEMO_PATH})
done
