#!/bin/bash

set -e

LOCAL_DAGS_PATH="airflow/dags"
LOCAL_PYTHON_SCRIPT_PATH="src/data-engineer-technical-test/"
FILE_EXCLUDED="variables.py"

function add_dags() {
    find ${LOCAL_PYTHON_SCRIPT_PATH} -maxdepth 1 \
        -type f \
        -not -iname ${FILE_EXCLUDED} \
        -exec cp '{}' "${LOCAL_DAGS_PATH}" ';'
}

function remove_dags() {
    find ${LOCAL_DAGS_PATH} -maxdepth 1\
        -type f \
        -not -iname ${FILE_EXCLUDED} \
        -exec rm '{}' ';'
}
