## CREATE CONTAINER
docker build -t mysql-ecommerce:1.0.0 .
docker run -d -p 3306:3306 --env-file=.env --name ecommerce-db mysql-ecommerce:1.0.0

## DELETE CONTAINER
docker stop ecommerce-db && docker rm -f ecommerce-db