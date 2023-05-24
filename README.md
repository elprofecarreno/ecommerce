## CREATE FILE .env

```shell
MYSQL_ROOT_PASSWORD=123456
MYSQL_DATABASE=ecommerce
```

## CREATE CONTAINER

```shell
docker build -t mysql-ecommerce:1.0.0 .
docker run -d -p 3306:3306 --env-file=.env --name ecommerce-db mysql-ecommerce:1.0.0
```

## DELETE CONTAINER

```shell
docker stop ecommerce-db && docker rm -f ecommerce-db
```