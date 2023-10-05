import pandas as pd


def reddit_data_transformation(**kwargs):
    ti = kwargs['ti']
    try:
        reddit_post_csv = ti.xcom_pull(key='reddit_post_raw_data', task_ids=['extract_post_task'])[0]

        # Read the CSV file into a DataFrame.
        df = pd.read_csv(reddit_post_csv)
        print(df)

        # Assuming 'created' contains Unix timestamps (seconds since epoch)
        df['created'] = pd.to_datetime(df['created'], unit='s')

        # Extract date and time into separate columns
        df['created_date'] = df['created'].dt.date
        df['created_time'] = df['created'].dt.time

        # Sort the DataFrame in descending order based on the 'created' column
        df.sort_values(by='created', ascending=False, inplace=True)

        # Reset the index if needed
        df.reset_index(drop=True, inplace=True)


        # Correct data types
        df['score'] = df['score'].astype(int)
        df['comms_num'] = df['comms_num'].astype(int)
        df['created'] = pd.to_datetime(df['created'], unit='s')  # Assuming 'Created' represents Unix timestamps

        # Check the data types after correction
        print(df.dtypes)

        # Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # Reset the index
        df.reset_index(drop=True, inplace=True)

        print(df)
        
        # Specify the path where you want to save the CSV file
        csv_file_path = '/home/airflow/starbucks_post_process_data.csv'

        # Write the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)

        ti.xcom_push(key='reddit_post_process_data', value=csv_file_path)

    except Exception as e:
        # Handle the exception here (e.g., log it, send an alert, etc.)
        print(f"An error occurred in initial_data_transformation: {str(e)}")
        raise e
    