from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.models import Variable


def get_reddit_post_details(mysql_connection_id, **kwargs):
    ti = kwargs['ti'] 
    # Define MySQL query with the scraper identifier
    mysql_query = "SELECT post_id FROM reddit_posts" 
    
    hook = MySqlHook(mysql_conn_id=mysql_connection_id)
    connection = hook.get_conn()
    
    cursor = connection.cursor()
    cursor.execute(mysql_query)
    results = cursor.fetchall()
    
    # Converting the fetched rows into a list
    post_ids = [row[0] for row in results]
 
    ti.xcom_push(key='reddit_post_ids', value=post_ids)
