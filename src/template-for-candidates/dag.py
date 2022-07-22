from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


args = {"owner": "descartes", "start_date": days_ago(1)}

dag = DAG(dag_id="data_engineer_dag", default_args=args, schedule_interval=None)

with dag:
    step_create_database = PythonOperator(
        # Fill me
    )

    step_read_locations = PythonOperator(
        # Fill me
    )

    # Fill me

    step_export_payouts = PythonOperator(
        # Fill me
    )

    step_export_payouts_per_event = PythonOperator(
        # Fill me
    )
    step_export_payouts_per_year = PythonOperator(
        # Fill me
    )

    (
        step_create_database
        >> step_read_locations
        # >> Fill me
        >> [
            step_export_payouts,
            step_export_payouts_per_event,
            step_export_payouts_per_year,
        ]
    )
