## API REST ECOMMERCE

## CREATE FILE .env

```shell
MYSQL_ROOT_PASSWORD=123456
MYSQL_DATABASE=ecommerce
MYSQL_USER=root
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