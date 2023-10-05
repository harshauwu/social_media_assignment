from app import db
from datetime import datetime
from flask import jsonify
import joblib 
import pandas as pd
import json
from db.models.schedule_posts import SchedulePost  # Import the SchedulePost model

def save_post(data):
    try:
        # Create a new SchedulePost object
        new_post = SchedulePost(
            title = data["title"],
            url = "https://example.com",
            body = data['text'],
            created_at = datetime.utcnow(),  # Use the current UTC time
            updated_at = datetime.utcnow(),  # Use the current UTC time
        )
        # Add the new_post to the session and commit it to the database
        db.session.add(new_post)
        db.session.commit()
        
        # Fetch the saved record by querying the database using the primary key
        saved_record = SchedulePost.query.get(new_post.id)

        # Return the saved record
        return saved_record

    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"
    
def get_all_schedule_posts():
    try:
        posts = SchedulePost.query.all()
        posts_data = []
        for post in posts:
            reddit_post_dict = {
                "id": post.id,
                "title": post.title,
                "body": post.body
            }
            posts_data.append(reddit_post_dict)
        return jsonify(posts_data)
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"     

def get_reddit_like_forecasts(forecast_periods):
    """Generates forecasts for Reddit likes using a trained ARIMA model.

    Args:
        forecast_periods: The number of periods to forecast.

    Returns:
        A JSON string containing the forecasted values and dates.
    """

    # Load the trained ARIMA model
    loaded_arima_model = joblib.load('/app/ml_models/arima/arima_reddit_like_model.pkl')

    # Check if the model is loaded
    if loaded_arima_model is None:
        raise Exception('ARIMA model is not loaded.')

    # Get the last date for which we have data
    last_date = '2023-08-22 00:00:00'
    last_date = pd.to_datetime(last_date)

    try:
        # Generate forecasts using the loaded ARIMA model
        forecasts, stderr, conf_int = loaded_arima_model.forecast(steps=forecast_periods)

        # Validate the forecast dates
        forecast_dates = pd.date_range(start=last_date + pd.DateOffset(1), periods=forecast_periods)
        if not all(forecast_dates > last_date):
            raise Exception('Forecast dates must be in the future.')

        # Create a DataFrame to store the forecasted values and dates
        forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecast': forecasts})

        # Convert the DataFrame to JSON
        json_data = forecast_df.to_json(orient='records')

        # Pretty-print the JSON for readability
        pretty_json_data = json.dumps(json.loads(json_data), indent=4)

        return pretty_json_data
    except Exception as e:
        # Return an error message if anything goes wrong
        return json.dumps({'error': str(e)})

    


  


