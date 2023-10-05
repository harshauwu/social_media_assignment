import pandas as pd
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def update_polarity(**kwargs):
    ti = kwargs['ti']
    try:
        reddit_comment_csv = ti.xcom_pull(key='reddit_post_comment_raw_data', task_ids=['extract_post_comment_task'])[0]

        # Data Collection:
        # Read the CSV file into a DataFrame.
        df = pd.read_csv(reddit_comment_csv)

        # Text Preprocessing
        # Specify the columns you want to drop
        # columns_to_drop = ['post_id', 'post_author', 'comment_auther', 'comment_score', 'comment_created_utc', 'comment_permalink', 'is_root_comment', 'comment_author_flair_text']

        # Drop the specified columns
        # df.drop(columns=columns_to_drop, inplace=True)

        # Lowercasing:
        # Apply lowercasing to the 'comment_body' column
        df['process_comment_body'] = df['comment_body'].str.lower()

        # Removing Punctuation:
        # Apply the remove_punctuation function to the 'process_comment_body' column
        df['process_comment_body'] = df['process_comment_body'].apply(remove_punctuation)

        # Define a string-based regex pattern to match emoticons
        emoticon_pattern = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FB00-\U0001FBFF\U0001FC00-\U0001FCFF\U0001FD00-\U0001FDFF\U0001FE00-\U0001FEFF\U0001FF00-\U0001FFFF]+'
    
        # Apply the emoticon removal to the 'process_comment_body' column with regex=True
        df['process_comment_body'] = df['process_comment_body'].str.replace(emoticon_pattern, '', regex=True)

        # Download the NLTK stopwords list and create a set
        stopwords_set = set(stopwords.words('english'))

        # Define a function to remove stopwords from a text
        def remove_stopwords(text):
            return ' '.join([word for word in text.split() if word.lower() not in stopwords_set])
        
        # Apply the remove_stopwords function to the 'process_comment_body' column
        df['process_comment_body'] = df['process_comment_body'].apply(remove_stopwords)

        # Initialize the VADER sentiment analyzer
        nltk.download('vader_lexicon')
        sid = SentimentIntensityAnalyzer()

        # You can access the 'process_comment_body' column and calculate sentiment scores
        df['sentiment_scores'] = df['process_comment_body'].apply(lambda x: sid.polarity_scores(x))

        # Extract the compound sentiment score (a normalized score) and add it as a new column
        df['compound_sentiment'] = df['sentiment_scores'].apply(lambda x: x['compound'])


        df['sentiment'] = df['compound_sentiment'].apply(classify_sentiment)

        # Specify the path where you want to save the CSV file
        csv_file_path = "/home/airflow/starbucks_post_comment_process_data.csv"
        
        # Write the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)

        ti.xcom_push(key='reddit_post_comment_process_data', value=csv_file_path)

    except Exception as e:
        # Handle the exception here (e.g., log it, send an alert, etc.)
        print(f"An error occurred in initial_data_transformation: {str(e)}")
        raise e    
    

# Define a function to remove punctuation using regex
def remove_punctuation(text):
    # Replace all punctuation characters with an empty string
    return ''.join([char for char in text if char not in string.punctuation])

# Classify sentiment as 'positive', 'neutral', or 'negative' based on compound score thresholds
def classify_sentiment(compound_score):
    if compound_score >= 0.05:
        return 'positive'
    elif compound_score <= -0.05:
        return 'negative'
    else:
        return 'neutral'
