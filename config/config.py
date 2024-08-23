import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '7877109134vije')
    UPLOAD_DIRECTORY = os.path.join(os.path.dirname(__file__), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit
