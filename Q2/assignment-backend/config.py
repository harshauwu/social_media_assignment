import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database Configuration
MYSQL_DATABASE_HOST = os.getenv('MYSQL_DATABASE_HOST')
MYSQL_DATABASE_USER = os.getenv('MYSQL_DATABASE_USER')
MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_DATABASE_PASSWORD')
MYSQL_DATABASE_DB = os.getenv('MYSQL_DATABASE_DB')

# Create SQLALCHEMY_DATABASE_URI using the above variables
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}/{MYSQL_DATABASE_DB}"

SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications (optional)

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')
REDDIT_USER_NAME = os.getenv('REDDIT_USER_NAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')