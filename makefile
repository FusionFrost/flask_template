find_open_process:
	ps -ax |grep gunicorn

find_open_port:
	netstat -tulpn | grep 5000

docker_build:
	 docker build -t flask-template .

docker_run:
	docker run flask-template

docker_compose_run:
	/usr/local/bin/docker-compose -f /Users/remagresif/flask_template/Docker-compose.yml -p flask_template up -d --build

