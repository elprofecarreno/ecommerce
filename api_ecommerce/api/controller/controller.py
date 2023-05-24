# IMPORT TRACE ERROR 
import traceback
# IMPORT DATA ACCESS OBJECT (DAO)
from api.dao.dao import dao_generic
# IMPORT JSON SERIALIZERS
import json
# IMPORT LIB MAKERESPONSE
from flask import make_response

CONTENT_TYPE_JSON_UTF8 = 'application/json; charset=utf-8'

def controller_generic(app, mysql, table, columns):

    dao = dao_generic(app, mysql, table, columns)

    def find_all():
        print('find_all')
        print('debug: ', app.debug)
        try:
            item =  dao['select_all']()
            # RETURN DICTIONARY AND STATUS CODE
            return response(item, CONTENT_TYPE_JSON_UTF8, 200)
        except Exception:
            traceback.print_exc()
            return response(None, CONTENT_TYPE_JSON_UTF8, 500)

    def create(request):
        print('create')
        try:
            payload = request.get_json()
            print('payload: ', payload)
            item =  dao['insert'](payload)
            # RETURN DICTIONARY AND STATUS CODE
            return response(item, CONTENT_TYPE_JSON_UTF8, 201)
        except Exception:
            traceback.print_exc()
            return response(None, CONTENT_TYPE_JSON_UTF8, 500)

    def update(request):
        print('update')
        try:
            payload = request.get_json()
            print('payload: ', payload)
            item =  dao['select_by_id'](list(payload.values())[0])
            if item is None:
                return response(None, CONTENT_TYPE_JSON_UTF8, 404)   
            else :
                item = dao['update'](payload)
                # RETURN DICTIONARY AND STATUS CODE
                return response(item, CONTENT_TYPE_JSON_UTF8, 200)
        except Exception:
            traceback.print_exc()  
            return response(None, CONTENT_TYPE_JSON_UTF8, 500)

    def find_by_id(id):
        print('find_by_id: ', id)
        try:
            print('id: ', id)
            item =  dao['select_by_id'](id)
            if item is None :
                return response(None, CONTENT_TYPE_JSON_UTF8, 404)   
            else :
                # RETURN DICTIONARY AND STATUS CODE
                return response(item, CONTENT_TYPE_JSON_UTF8, 200)
        except Exception:
            traceback.print_exc()
            return response(None, CONTENT_TYPE_JSON_UTF8, 500)

    def delete_by_id(id):
        print('delete_by_id: ', id)
        try:
            print('id: ', id)
            item =  dao['select_by_id'](id)
            if item is None :
                return response(None, CONTENT_TYPE_JSON_UTF8, 404)   
            else :
                item = dao['delete_by_id'](id)
                # RETURN DICTIONARY AND STATUS CODE
                return response(item, CONTENT_TYPE_JSON_UTF8, 200)
        except Exception:
            traceback.print_exc()
            return response(None, CONTENT_TYPE_JSON_UTF8, 500)

    def response(payload, content_type, status_code):
        print('payload: ', payload)
        if payload and payload != []:
            resp = make_response(json.dumps(payload, sort_keys=False))
        else: 
            resp = make_response()
        resp.headers['Content-Type'] = content_type
        resp.status_code = status_code
        return resp

    # Assign the dynamic function to app dynamically
    #setattr(app, f"find_all_{table}", find_all)
    # PUBLIC LOCAL METHOD
    return {
        "find_all": find_all,
        "create_": create,
        "update": update,
        "find_by_id": find_by_id,
        "delete_by_id": delete_by_id,
    }