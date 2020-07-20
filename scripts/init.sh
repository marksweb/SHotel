docker-compose up -d
sleep 10
docker exec -it shotel_backend pipenv run python manage.py migrate
