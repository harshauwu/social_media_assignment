# app.py

from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from db.db_connection import db
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)


# Configure the app with the database settings from config.py
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    # SQLALCHEMY_TRACK_MODIFICATIONS=SQLALCHEMY_TRACK_MODIFICATIONS

# db = SQLAlchemy(app)

# Initialize the SQLAlchemy instance
with app.app_context():
    db.init_app(app)

# Import controllers
from controllers import social_media_controller

@app.route("/")
def hello():
    return "Welcome My Social Media Analytics!!"
    
# Import routes
from routes.reddit_routes import reddit_routes

# Register routes
app.register_blueprint(reddit_routes, url_prefix='/reddit')


if __name__ == '__main__':
    port = 5050 # int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
