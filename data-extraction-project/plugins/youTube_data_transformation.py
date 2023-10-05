import pandas as pd


def youTube_data_transformation(**kwargs):
    ti = kwargs['ti']
    try:
        youtube_post_csv = ti.xcom_pull(key='youTube_vide_raw_data', task_ids=['extract_youtube_post_task'])[0]

        # Read the CSV file into a DataFrame.
        df = pd.read_csv(youtube_post_csv)
        print(df)

        # Data cleaning and processing
        # Handle missing data (replace missing values with 0)
        df['like_count'] = df['like_count'].astype(int).fillna(0)
        df['comment_count'] = df['comment_count'].astype(int).fillna(0)
        df['favorite_count'] = df['favorite_count'].astype(int).fillna(0)

        # Assuming 'created' contains Unix timestamps (seconds since epoch)
        df['published_at'] = pd.to_datetime(df['published_at'])

        # Extract date and time into separate columns
        df['published_date'] = df['published_at'].dt.date
        df['published_time'] = df['published_at'].dt.time

        # Specify the path where you want to save the CSV file
        csv_file_path = '/home/airflow/youTube_video_process_data.csv'

        # Write the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)

        ti.xcom_push(key='youTube_video_process_data', value=csv_file_path)

    except Exception as e:
        # Handle the exception here (e.g., log it, send an alert, etc.)
        print(f"An error occurred in initial_data_transformation: {str(e)}")
        raise e    