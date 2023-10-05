import praw
import pandas as pd

def extract_post_data(**kwargs):
    ti = kwargs['ti'] 

    # Creating a Reddit object with the required parameters
    reddit = praw.Reddit(
        client_id='izlVfPwECjziab_rpf2D_A',
        client_secret='LhjN-wepGfUncebvFygM2gVlOxRPBw',
        redirect_uri="http://localhost:8080",
        user_agent="testscript by u/fakebot3",
    )

    # Get the top 10 posts from the r/python subreddit
    subreddit = reddit.subreddit('starbucks')

    top_posts = subreddit.top(limit=10)

    posts_dict = {
        "title": [],
        "score": [],
        "post_id": [],
        "url": [],
        "comms_num": [],
        "created": [],
        "body": [],
        "author": [],
        "subreddit": []
    }

    for post in top_posts:
        # Get the likes, shares, and time of the post.
        # Push the data to posts_dict.
        posts_dict["title"].append(post.title)
        posts_dict["score"].append(post.score)
        posts_dict["post_id"].append(post.id)
        posts_dict["url"].append(post.url)
        posts_dict["comms_num"].append(post.num_comments)
        posts_dict["created"].append(post.created)
        posts_dict["body"].append(post.selftext)
        posts_dict["author"].append(post.author)
        posts_dict["subreddit"].append(post.subreddit)
        
    posts_df = pd.DataFrame(posts_dict)    
    print(posts_df)
    # Specify the path where you want to save the CSV file
    csv_file_path = "/home/airflow/starbucks_post_data_raw.csv"
    
    # Write the DataFrame to a CSV file
    posts_df.to_csv(csv_file_path, index=False)

    ti.xcom_push(key='reddit_post_raw_data', value=csv_file_path)


def extract_post_comment(**kwargs):

    ti = kwargs['ti']

    # post_ids = ti.xcom_pull(key='reddit_post_ids', task_ids=['post_details_task'])[0]
    # print(post_ids)

    post_ids = ['92x3p6']
    # Creating a Reddit object with the required parameters
    reddit = praw.Reddit(
        client_id='izlVfPwECjziab_rpf2D_A',
        client_secret='LhjN-wepGfUncebvFygM2gVlOxRPBw',
        redirect_uri="http://localhost:8080",
        user_agent="testscript by u/fakebot3",
    )

    # Initialize an empty dictionary to store post comments
    post_comments = {
        "post_id": [],
        "post_author": [],
        "comment_auther": [],
        "comment_id": [],
        "comment_body": [],
        "comment_score": [],
        "comment_created_utc": [],
        "comment_permalink": [],
        "is_root_comment": [],
        "comment_author_flair_text": []
    }

    for post_id in post_ids:
        # Get the post by ID.
        post = reddit.submission(id=post_id)   
        comments = post.comments.list() 

        # Iterate through the comments and get each comment details
        for comment in comments:
            if (comment.id != '_'):
                print(comment.id)
                
                comment_data = reddit.comment(id=str(comment.id))
                if comment_data is None:
                    continue

                post_comments["post_id"].append(post.id)
                post_comments["post_author"].append(post.author)
                post_comments["comment_auther"].append(comment_data.author if comment_data.author else '')
                post_comments["comment_id"].append(comment_data.id)
                post_comments["comment_body"].append(comment_data.body)
                post_comments["comment_score"].append(comment_data.score)
                post_comments["comment_created_utc"].append(comment_data.created_utc)
                post_comments["comment_permalink"].append(comment_data.permalink)
                post_comments["is_root_comment"].append(comment_data.is_root)
                post_comments["comment_author_flair_text"].append(comment_data.author_flair_text)


    df = pd.DataFrame(post_comments)
    print(df)

    # Specify the path where you want to save the CSV file
    csv_file_path = "/home/airflow/starbucks_post_comment_data_raw.csv"
    
    # Write the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    ti.xcom_push(key='reddit_post_comment_raw_data', value=csv_file_path)