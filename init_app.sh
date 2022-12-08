docker build . -t chatapp:v1
docker run -d --name chat -p 80:5000 chatapp:v1
