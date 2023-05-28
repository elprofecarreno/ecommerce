# IMPOR FLASK LIB
from flask import Flask
# IMPORT FLASK POLICE CORS
from flask_cors import CORS
# IMPORT MYSQL LIB CONNECTION
from flask_mysqldb import MySQL
# IMPORT LIB OPERATION SYSTEM
import os
# IMPORT LOAD ENVIRONMENT (FILE .env)
from dotenv import load_dotenv
load_dotenv()

# API REST CONTROLLER
from api.controller.controller_genders import api_genders
from api.controller.controller_documents import api_documents
from api.controller.controller_regiones_states import api_regiones_states
from api.controller.controller_provinces_townships import api_provinces_townships

# SE HABILITA ACCESO PARA API DESDE EL ORIGEN *
app = Flask(__name__)
CORS(app)

cors = CORS(app, resource ={
    # RUTA O RUTAS HABILTADAS PARA EL ORIGEN *
    r"/api/v1/*" : {
        "origins" : "*"
    }
})

# CONNECTION DATABASE
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT'))
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
mysql = MySQL(app)

# SE AGREGAN CONTROLADORES DE LAS APIS REST
api_genders(app, mysql)
api_documents(app, mysql)
api_regiones_states(app, mysql)
api_provinces_townships(app, mysql)

# DESPLIEGUE SERVICIO PROPIO DE FLASK (SOLO PARA PRUEBAS). 
# EN DONDE AL DEFINI 0.0.0.0 SE 
# HABILITA EL USO DE LA IP LOCAL, IP DE RED, ETC. 
# PARA EL PUERTO 9000
if __name__ == '__main__' :
    app.run(host=os.getenv('APP_HOST'), port=int(os.getenv('APP_PORT')), debug=True)