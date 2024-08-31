start-dev: 
	uvicorn app.main:app --reload

start:
	uvicorn app.main:app

psql-up:
	docker compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans db

psql-down:
	sudo docker compose -f docker-compose.yml down -v --remove-orphans