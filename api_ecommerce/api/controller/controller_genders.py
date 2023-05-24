# FLASK REQUEST OBJECT
from flask import request
# IMPORT COTROLLER GENERIC
from api.controller.controller import controller_generic

TABLE = 'genders'
COLUMNS = ['id', 'name', 'description']

def api_genders(app, mysql):

    generic = controller_generic(app, mysql, TABLE, COLUMNS)

    @app.route("/api/v1/{0}".format(TABLE), methods=['GET'])
    def find_all_genders():
        return generic['find_all']()

    @app.route("/api/v1/{0}".format(TABLE), methods=['POST'])
    def create_genders():
        return generic['create'](request)
            
    @app.route("/api/v1/{0}".format(TABLE), methods=['PUT'])
    def update_genders():
        return generic['update'](request)  

    @app.route("/api/v1/{0}/<int:id>".format(TABLE), methods=['GET'])
    def find_by_id_genders(id):
        return generic['find_by_id'](id)

    @app.route("/api/v1/{0}/<int:id>".format(TABLE), methods=['DELETE'])
    def remove_by_id_genders(id):
        return generic['delete_by_id'](id)
                                         