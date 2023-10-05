from airflow import DAG
from datetime import datetime, timedelta
import numpy as np

from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

from reddit_data_extractor import extract_post_comment
from get_post_data import get_reddit_post_details
from comment_raw_data_table_operator import CommentRawDataTableOperator
from sentiment_analysis import update_polarity
from process_comment_data_table_operator import ProcessCommentDataTableOperator

# Define default arguments for the DAG
default_args = {
    'start_date': datetime(2023, 10, 1),        # The date when the DAG will start running
    'retries': 1,                               # Number of times to retry the task on failure
    'retry_delay': timedelta(minutes=1),        # Time delay between retries
    'log_level': 'WARNING'
}
    

# Create the DAG instance
with DAG('Reddit_Post_Comment_Dag',
          default_args=default_args, 
          description="This is Reddit post's comments data extraction dag",
          schedule_interval=None, 
          tags=["Reddit", "Post", "Comments"]
        ) as dag:

    # Define Airflow connection ID for MySQL
    mysql_conn_id = Variable.get("mysql_connection_id")


    # Define the task with the PythonOperator
    post_details_task = PythonOperator(
        task_id='post_details_task',
        python_callable=get_reddit_post_details,
        op_args=[mysql_conn_id],  
        provide_context=True,  # This is required to access context variables like mysql_conn_id
        dag=dag,
    )

    # Define the task with the PythonOperator
    extract_post_comment_task = PythonOperator(
        task_id='extract_post_comment_task',
        python_callable=extract_post_comment, 
        provide_context=True,  # This is required to access context variables like mysql_conn_id
        dag=dag,
    )

    comment_raw_data_insert_task = CommentRawDataTableOperator(
        task_id='comment_raw_data_insert_task',
        source_task_id='extract_post_comment_task',  # Task ID of the source task that provides data
        table_name="reddit_comment_raw_details",
        mysql_conn_id=mysql_conn_id,
        dag=dag,
    )

    sentiment_analysis_task = PythonOperator(
        task_id='sentiment_analysis_task',
        python_callable=update_polarity, 
        provide_context=True,  # This is required to access context variables like mysql_conn_id
        dag=dag,
    )

    processed_comment_data_insert_task = ProcessCommentDataTableOperator(
        task_id='processed_comment_data_insert_task',
        source_task_id='sentiment_analysis_task',  # Task ID of the source task that provides data
        table_name="reddit_post_comments",
        mysql_conn_id=mysql_conn_id,
        dag=dag,
    )

    post_details_task >> extract_post_comment_task >> comment_raw_data_insert_task >> sentiment_analysis_task >> processed_comment_data_insert_task
