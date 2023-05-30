# IMPOR FLASK LIB
from flask import Flask
# IMPORT LIB OPERATION SYSTEM
import os
# IMPORT LOAD ENVIRONMENT (FILE .env)
from dotenv import load_dotenv
load_dotenv()

# API REST CONTROLLER
from app.views.index_view import app_index_view
from app.views.regiones_view import app_regiones_view

# LOAD PATH PARENTS FOLDER 
BASE_DIR = os.path.abspath(os.getcwd())
print('BASE_DIR: ', BASE_DIR)

# CREATE TEMPLATE FOLDER 
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'app', 'templates')
print('TEMPLATE_FOLDER: ', TEMPLATE_FOLDER)

# CREATE STATIC_FOLDER FOLDER 
STATIC_FOLDER = os.path.join(BASE_DIR, 'app', 'static')
print('STATIC_FOLDER: ', STATIC_FOLDER)

# CREATE FLASK APP 
app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)

# ADD VIEWS (CONTROLLERS)
app_index_view(app)
app_regiones_view(app)

# DEPLOY API REST (ONLY DEVELOPMENT AND TEST SERVER) 
if __name__ == '__main__' :
    app.run(host=os.getenv('APP_WEB_HOST'), port=int(os.getenv('APP_WEB_PORT')), debug=True)