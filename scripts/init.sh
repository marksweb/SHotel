docker-compose up -d
sleep 10
docker exec -it shotel_backend python manage.py migrate
