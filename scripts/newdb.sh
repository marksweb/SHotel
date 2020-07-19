cd ..
cd backend
docker exec -it shotel_backend pipenv run python manage.py makemigrations
docker exec -it shotel_backend pipenv run python manage.py migrate
docker exec -it shotel_backend pipenv run python manage.py runscript new_db
