from airflow.models import BaseOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.decorators import apply_defaults
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime
import pandas as pd
from airflow import settings
from sqlalchemy import create_engine
from airflow.models import Connection

class YouTubeProcessDataTableOperator(BaseOperator):
    @apply_defaults
    def __init__(
        self,
        source_task_id: str,
        table_name: str,
        mysql_conn_id: str = "mysql_default",
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.source_task_id = source_task_id
        self.mysql_conn_id = mysql_conn_id
        self.table_name = table_name

    def execute(self, context):
        self.log.info(f"Executing CustomMySqlOperator with data from task: {self.source_task_id}")
        youTube_post_csv = context['task_instance'].xcom_pull(key='youTube_video_process_data', task_ids=['data_transformation_task'])[0]
        
        # Create if the table not exists 
        self.create_table(context)
        self.processed_data_ingestion(context, youTube_post_csv)

    
    def create_table(self, context):
        create_sql_statement = "CREATE TABLE IF NOT EXISTS " +self.table_name+ "(id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255), view_count INT, like_count INT, comment_count INT, favorite_count INT, duration VARCHAR(255), published_at DATETIME DEFAULT NULL, published_date DATETIME DEFAULT NULL, published_time DATETIME DEFAULT NULL)"
        
        
        create_task = MySqlOperator(
            task_id='table_creation_task',
            sql=create_sql_statement,
            mysql_conn_id=self.mysql_conn_id,
            dag=self.dag  # Reference to your DAG object
        )
        create_task.execute(context)

    def processed_data_ingestion(self, context, file_name):

        conn = settings.Session().query(Connection).filter(Connection.conn_id == self.mysql_conn_id).first()
        print(conn)

        if not conn:
            raise Exception(f"Connection '{self.mysql_conn_id}' not found in Airflow")
        
        # Create the db_connection_str
        db_connection_str = f"mysql+mysqlconnector://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}"
        
        engine = create_engine(db_connection_str)

        df = pd.read_csv(file_name)
        print(df)

        # Save the DataFrame to MySQL
        df.to_sql(con=engine, name=self.table_name, if_exists='replace', index=False , chunksize=3000)
