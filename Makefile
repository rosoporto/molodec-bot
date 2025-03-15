run:
	python3 -m bot

load_json:
	python3 -m utils.handler_json

docker_build:
	docker build -t molodec-bot .

run_container:
	docker run --rm -v $(pwd)/base:/app/base -v $(pwd)/logs:/app/logs -v $(pwd)/.env:/app/.env molodec-bot

run_container_light:
	docker run --rm molodec-bot

docker_build_compose:
	docker-compose up --build

docker_compose_dowb:
	docker-compose down
