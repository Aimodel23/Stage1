from flask import Flask
from src.user import user_bp
from config.config import UPLOAD_DIRECTORY, SECRET_KEY
import os

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/api')

# Set configuration
app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY
app.config['SECRET_KEY'] = SECRET_KEY

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_DIRECTORY'], exist_ok=True)

@app.route('/')
def index():
    return "Welcome to the Stage1 API!"

if __name__ == '__main__':
    app.run(debug=True)
