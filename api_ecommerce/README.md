## API REST ECOMMERCE

## CREATE FILE .env

```shell
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=3C0mM3rCE
MYSQL_DB=ecommerce
APP_PORT=9000
APP_HOST=0.0.0.0
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