# FLASK REQUEST OBJECT
from flask import request
# IMPORT COTROLLER GENERIC
from api.controller.controller import controller_generic
# IMPORT JSON SERIALIZERS
import json

TABLE = 'communes_towns'
COLUMNS = ['id', 'name', 'latitude', 'longitude', 'provinces_townships_id']

def api_communes_towns(app, mysql):

    generic = controller_generic(app, mysql, TABLE, COLUMNS)

    @app.route("/api/v1/{0}".format(TABLE), methods=['GET'])
    def find_all_communes_towns():
        return generic['find_all']()

    @app.route("/api/v1/{0}".format(TABLE), methods=['POST'])
    def create_communes_towns():
        return generic['create'](request)
            
    @app.route("/api/v1/{0}".format(TABLE), methods=['PUT'])
    def update_communes_towns():
        return generic['update'](request)  

    @app.route("/api/v1/{0}/<int:id>".format(TABLE), methods=['GET'])
    def find_by_id_communes_towns(id):
        return generic['find_by_id'](id)

    @app.route("/api/v1/{0}/<int:id>".format(TABLE), methods=['DELETE'])
    def remove_by_id_communes_towns(id):
        return generic['delete_by_id'](id)
                                         