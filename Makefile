run:
	python3 -m bot

load_json:
	python3 -m utils.handler_json

docker_up:
	docker-compose up -d --build

docker_run:
	docker-compose up -d

docker_start:
	docker-compose start

docker_stop:
	docker-compose stop

docker_down:
	docker-compose down

docker_logs:
	docker-compose logs -f