# IMPOR FLASK LIB
from flask import render_template
# FLASK REQUEST OBJECT
from flask import request
# IMPORT LIBRARIES ERROR TRACE, OPERATION SYSTEM AND REQUESTS CLIENT API REST 
import traceback, os, requests

def app_regiones_view(app):

    API_REST_HOST = os.getenv('API_REST_HOST')
    API_REST_PORT = os.getenv('API_REST_PORT')

    @app.route('/admin/regiones',  methods=['GET', 'POST', 'DELETE'])
    def regiones_view():
        print('METHOD: ', request.method)
        title = 'E-commerce ADMIN'
        user_data = {
            'username' : 'Henry Klein',
            'profile' : 'ADMIN',
            'image' : 'assets/images/faces/face15.jpg',
        }
        menus = [
                    {'href': '/admin/index', 'title': 'Categories', 'icon' : 'mdi mdi-earth'},
                    {'href': '/admin/index', 'title': 'Communes', 'icon' : 'mdi mdi-file-document-box'},
                    {'href': '/admin/index', 'title': 'Documents', 'icon' : 'mdi mdi-file-document-box'},
                    {'href': '/admin/index', 'title': 'Genders', 'icon' : 'mdi mdi-file-document-box'},
                    {'href': '/admin/index', 'title': 'Products', 'icon' : 'mdi mdi-panorama'},
                    {'href': '/admin/index', 'title': 'Provinces', 'icon' : 'mdi mdi-image-filter-hdr'},
                    {'href': '/admin/regiones', 'title': 'Regiones', 'icon' : 'mdi mdi-earth'},
                ]

        message = {
            'type': 'warning d-none',
            'text': ''
        }
        if request.method == 'POST':
            transaction = request.form.get('transaction')
            print('transaction: ', transaction)
            if transaction == 'create':
                regiones_create(request)
                message = {
                    'type': 'success',
                    'text': 'Created Region'
                }                
            elif transaction == 'update':
                regiones_update(request)
                message = {
                    'type': 'success',
                    'text': 'Updated Region ' +  request.form.get('id')
                }                  
            elif transaction == 'delete':
                id = request.form.get('id')
                if id is not None:
                    regiones_delete(id)
                    message = {
                        'type': 'success',
                        'text': 'Deleted Region ' + id
                    }                      
               
        regiones = []
        try:
            url = 'http://{API_REST_HOST}:{API_REST_PORT}/api/v1/regiones_states'.format(API_REST_HOST=API_REST_HOST, API_REST_PORT=API_REST_PORT)
            print('url: ', url)
            response = requests.get(url)
            regiones = response.json()            
            print('regiones: ', regiones)
        except Exception as e:
            traceback.print_exc()

        data = {
            'title' : title,
            'user_data': user_data,
            'menus' : menus,
            'regiones' : regiones,
        }
        return render_template('admin/regiones.html', data=data, message=message)

    def regiones_create(request):
        print('create: ')
        try:
            name = request.form.get('name')
            latitude = request.form.get('latitude')
            longitude = request.form.get('longitude')
            payload = {
                'name' : name,
                'latitude' : latitude,
                'longitude' : longitude
            }
            url = 'http://{API_REST_HOST}:{API_REST_PORT}/api/v1/regiones_states'.format(API_REST_HOST=API_REST_HOST, API_REST_PORT=API_REST_PORT)
            print('url: ', url)
            response = requests.post(url, json=payload)
            print('response: ', response)
        except Exception as e:
            traceback.print_exc()

    def regiones_update(request):
        print('update: ')
        try:
            id = request.form.get('id')
            name = request.form.get('name')
            latitude = request.form.get('latitude')
            longitude = request.form.get('longitude')
            payload = {
                'id': id,
                'name' : name,
                'latitude' : latitude,
                'longitude' : longitude
            }
            url = 'http://{API_REST_HOST}:{API_REST_PORT}/api/v1/regiones_states'.format(API_REST_HOST=API_REST_HOST, API_REST_PORT=API_REST_PORT)
            print('url: ', url)
            response = requests.put(url, json=payload)
            print('response: ', response)
        except Exception as e:
            traceback.print_exc()            
        
    def regiones_delete(id):
        print('delete: ', id)
        try:
            url = 'http://{API_REST_HOST}:{API_REST_PORT}/api/v1/regiones_states/{id}'.format(API_REST_HOST=API_REST_HOST, API_REST_PORT=API_REST_PORT, id=id)
            print('url: ', url)
            response = requests.delete(url)
            print('response: ', response)
        except Exception as e:
            traceback.print_exc()