# config.py

# Database Configuration
MYSQL_DATABASE_HOST = 'assignment-backend-mysql-1'
MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = '123123'
MYSQL_DATABASE_DB = 'social_media_db'

# Create SQLALCHEMY_DATABASE_URI using the above variables
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}/{MYSQL_DATABASE_DB}"

SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications (optional)

# Reddit API credentials
REDDIT_CLIENT_ID = 'izlVfPwECjziab_rpf2D_A'
REDDIT_CLIENT_SECRET = 'LhjN-wepGfUncebvFygM2gVlOxRPBw'
REDDIT_USER_AGENT = 'testscript by u/fakebot3'