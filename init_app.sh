docker build . -t chatapp:v1

docker network create --subnet 172.19.0.0/24 --gateway 172.19.0.1 \
--ip-range=172.19.0.2/24 --driver=bridge --label=chatappnetwork br04

docker run -d -p 3306:3306 --name mysqldata -e  MYSQL_ROOT_PASSWORD=password --network br04 --ip 172.19.0.3 mysql


docker run -d --name chat -p 80:5000 --network br04 chatapp:v1
