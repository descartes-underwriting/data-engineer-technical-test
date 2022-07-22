# Conventions

The task section give specific information related to the [Tasks.md](Tasks.md) instructions.

## Tools

+ make
+ [Docker (20.10.17)](https://docs.docker.com/engine/install/)
+ [Optional] [sqlitebrowser](https://sqlitebrowser.org/dl/)
+ 🚨 Python 3.8 🚨*required by the Airflow docker image*
+ All necessary python packages are listed in the `requirements.txt`

  ```bash
  make install-requirements
  ```

---

## Task 1 - Python

+ The solution should edit the following python files:

  + `database.py`
  + `locations.py`
  + `api.py`
  + `payouts.py`
  + `utils.py`

+ In each of these files, the main functions are already defined, but need to be filled. Their signature can be changed (see below) and any number of additional functions can be created.

+ Python files can be executed using:

  ```bash
  python src/data-engineer-technical-test/database.py
  ```

  and contain small tests to guide the answers

+ Two python decorators are available and 🚨 **must be used** 🚨,

  + `database_operation`
  + `load_statements`

  In addition to the docstring, examples are provided in [../src/data-engineer-technical-test/tests.py](../src/data-engineer-technical-test/tests.py).

+ All SQL statements are to be written in separate files, placed in the following folders: `sql/database`, `sql/locations`, `sql/api` and `sql/payouts`

+ The solution should produce outputs in the `output` folder:

  + The SQLite3 database
  + Various CSV files containing the losses

  🚨These files must be committed along with the solution🚨

+ The full pipeline can be run with

    ```bash
    make run-pipeline
    ```

---

## Task 2 - Airflow

The DAG must be written in [../src/data-engineer-technical-test/dag.py](../src/data-engineer-technical-test/dag.py).

Airflow operations can be executed to:

+ Add DAGs to Airflow:

  ```bash
  make add-dags
  ```

+ Launch Airflow:

  ```bash
  make launch-airflow-containers
  ```

+ Access Airflow via your browser at [http://localhost:8080/](http://localhost:8080/)

  + login: `airflow`
  + password: `airflow`

+ Update DAGs in Airflow:

  ```bash
  make add-dags
  ```

+ Launch the DAG (**data_engineer_dag**) from your browser.

+ Stop Airflow:

  ```bash
  make remove-airflow-containers
  ```
