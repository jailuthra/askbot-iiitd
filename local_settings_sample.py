import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Copy this file to local_settings.py on your local machine to run using runserver command
