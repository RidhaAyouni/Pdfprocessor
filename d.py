from flask import Flask
from config import Config

# In this code snippet, `app = Flask(__name__)` is creating a Flask application instance.
app = Flask(__name__)
# app.config.from_object(Config)

# Import routes at the end to avoid circular import issues
from app import bp as main_bp
app.register_blueprint(main_bp ,url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)
