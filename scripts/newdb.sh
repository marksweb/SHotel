cd ..
cd backend
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py runscript new_db
