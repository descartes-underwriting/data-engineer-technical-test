SHELL := /bin/bash
PYTHON := python3
SRC_DIR := src/data-engineer-technical-test
AIRFLOW_DIR := airflow


# Helper
# ---------


help:  ## List all the recipies of Makefile
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | column -t -s '#'
.PHONY: help


# Airflow
# -------


add-dags:  ## Copy src/**/*.py script into airflow/dags used in container
	@echo "+++ add_dags"
	@source scripts/airflow_configuration.sh && add_dags
.PHONY: add-dags

remove-dags:  ## Remove airflow/dags used in container
	@echo "+++ remove_dags"
	@source scripts/airflow_configuration.sh && remove_dags
.PHONY: remove-dags


# Python
# -------

install-requirements: ## Install python requirements
	@${PYTHON} -m pip install -r requirements.txt
.PHONY: install requirements


run-pipeline:  ## Remove airflow/dags used in container
	@echo "+++ run-pipeline"
	@${PYTHON} ${SRC_DIR}/database.py
	@${PYTHON} ${SRC_DIR}/locations.py
	@${PYTHON} ${SRC_DIR}/api.py
	@${PYTHON} ${SRC_DIR}/payouts.py
.PHONY: run-pipeline


# Docker
# ------


launch-airflow-containers: ## Launch airflow containers
	@echo "+++ launch-airflow"
	@docker compose -f ${AIRFLOW_DIR}/docker-compose.yaml up -d 
.PHONY: launch-airflow-containers

stop-airflow-containers: ## Stop and remove airflow containers
	@echo "+++ stop-airflow-container"
	@docker compose -f ${AIRFLOW_DIR}/docker-compose.yaml down 
.PHONY: stop-airflow-containers
