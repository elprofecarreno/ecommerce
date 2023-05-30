## API REST ECOMMERCE

## CREATE FILE .env

```shell
APP_WEB_PORT=9001
APP_WEB_HOST=0.0.0.0
API_REST_PORT=9000
API_REST_HOST=0.0.0.0
```

### INSTALL VIRTUAL ENVIRONMENT LIB

```shell
pip install virtualenv
```

### CREATE VIRTUAL ENVIRONMENT

```shell
virtualenv env
```

### ACTIVATE VIRTUAL ENVIRONMENT (WINDOWS)

```shell
. env/Scripts/activate
```

### INSTALL PYTHON LIB

```shell
pip install -r requirements.txt
```

### DEPLOY API REST

```shell
python manage.py
```