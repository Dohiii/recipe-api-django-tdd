# recipe-api-django-tdd
Recipe Api 
My pet project backend API for recipes app


Docker Commands:docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose run --rm app sh -c "django-admin startapp core"
docker-compose up -d
docker-compose up
docker-compose down
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "python manage.py test"
 

DataBase Commands:
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"


Custom django commands:
slowing down the django to wait for database:
docker-compose run --rm app sh -c "python manage.py wait_for_db"

