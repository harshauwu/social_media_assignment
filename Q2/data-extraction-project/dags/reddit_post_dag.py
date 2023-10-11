from airflow import DAG
from datetime import datetime, timedelta
import numpy as np

from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

from raw_data_table_operator import RawDataTableOperator
from process_data_table_operator import ProcessDataTableOperator
from reddit_data_extractor import extract_post_data
from data_transformation import reddit_data_transformation


# Define default arguments for the DAG
default_args = {
    'start_date': datetime(2023, 10, 1),        # The date when the DAG will start running
    'retries': 1,                               # Number of times to retry the task on failure
    'retry_delay': timedelta(minutes=1),        # Time delay between retries
    'log_level': 'WARNING'
}
    

# Create the DAG instance
with DAG('Reddit_Post_Dag',
          default_args=default_args, 
          description="This is Reddit post data extraction dag",
          schedule_interval=None, 
          tags=["Reddit", "Post"]
        ) as dag:

    # Define Airflow connection ID for MySQL
    mysql_conn_id = Variable.get("mysql_connection_id")

    # Define the task with the PythonOperator
    extract_post_task = PythonOperator(
        task_id='extract_post_task',
        python_callable=extract_post_data, 
        provide_context=True,  # This is required to access context variables like mysql_conn_id
        dag=dag,
    )

    raw_data_insert_task = RawDataTableOperator(
        task_id='raw_data_insert_task',
        source_task_id='extract_post_task',  # Task ID of the source task that provides data
        table_name="reddit_post_raw",
        mysql_conn_id=mysql_conn_id,
        dag=dag,
    )

    # Define the task with the PythonOperator
    data_transformation_task = PythonOperator(
        task_id='data_transformation_task',
        python_callable=reddit_data_transformation, 
        provide_context=True,  # This is required to access context variables like mysql_conn_id
        dag=dag,
    )

    processed_data_insert_task = ProcessDataTableOperator(
        task_id='processed_data_insert_task',
        source_task_id='data_transformation_task',  # Task ID of the source task that provides data
        table_name="reddit_posts",
        mysql_conn_id=mysql_conn_id,
        dag=dag,
    )

    extract_post_task >> raw_data_insert_task >> data_transformation_task >> processed_data_insert_task