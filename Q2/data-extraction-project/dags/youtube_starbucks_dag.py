from airflow import DAG
from datetime import datetime, timedelta
import numpy as np

from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

from starbucks_data_table_operator import StarbucksDataTableOperator
from youTube_data_extractor import extract_youtube_starbucks_details


# Define default arguments for the DAG
default_args = {
    'start_date': datetime(2023, 10, 1),        # The date when the DAG will start running
    'retries': 1,                               # Number of times to retry the task on failure
    'retry_delay': timedelta(minutes=1),        # Time delay between retries
    'log_level': 'WARNING'
}

# Create the DAG instance
with DAG('YouTube_starbucks_Dag',
          default_args=default_args, 
          description="This is Youtube Starbucks data extraction dag",
          schedule_interval=None, 
          tags=["Reddit", "Post"]
        ) as dag:

    # Define Airflow connection ID for MySQL
    mysql_conn_id = Variable.get("mysql_connection_id")

    # Define the task with the PythonOperator
    extract_chanel_data_task = PythonOperator(
        task_id='extract_chanel_data_task',
        python_callable=extract_youtube_starbucks_details, 
        provide_context=True,  # This is required to access context variables like mysql_conn_id
        dag=dag,
    )

    save_starbucks_task = StarbucksDataTableOperator(
        task_id='save_starbucks_task',
        source_task_id='extract_chanel_data_task',  # Task ID of the source task that provides data
        table_name="organization_table",
        mysql_conn_id=mysql_conn_id,
        dag=dag,
    )

    extract_chanel_data_task >> save_starbucks_task 