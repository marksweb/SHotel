docker-compose up -d
sleep 10
docker exec -it backend python manage.py migrate
