# IMPOR FLASK LIB
from flask import render_template

def app_index_view(app):

    @app.route('/')
    @app.route('/admin/index')
    def index_view():        
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
                    {'href': '/admin/regiones', 'title': 'Regiones', 'icon' : 'mdi mdi mdi-earth'},
                ]
        data = {
            'title' : title,
            'user_data': user_data,
            'menus' : menus,
        }                
        return render_template('admin/index.html', data=data)
