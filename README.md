# recipe-api-django-tdd
Recipe Api 
My pet project backend API for recipes app

Notes for me:
1) What to remember in creating Custom user model
 - UserModel > Hash Password > CLI create superuser
 - BaseUserManager > base class methods > normalize_email create_user, create_superuser
 - add to settings this line: AUTH_USER_MODEL = 'core.User'


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




