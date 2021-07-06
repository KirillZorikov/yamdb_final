# api_yamdb

[![yamdb_workflow](https://github.com/KirillZorikov/yamdb_final/workflows/yamdb_workflow/badge.svg)](https://github.com/KirillZorikov/yamdb_final/actions)

The YaMDb project collects user reviews of the titles. 
Titles can be of various categories. For example: "Books", "Movies", "Music".

With this project, I learned how to work with:

* [Custom permissions](https://github.com/KirillZorikov/yamdb_final/blob/master/api_users/permissions.py)
* [Custom JWT auth](https://github.com/KirillZorikov/yamdb_final/blob/master/api_users/views.py)
* GitHub Actions

### Project links:

* Api: https://kz-api.tk/yamdb/api/v1

* Api documentation: https://kz-api.tk/yamdb/redoc

* Docker image:
[yamdb_final](https://hub.docker.com/repository/docker/kzorikov/yamdb_final)

### Tech:

* [Python 3.8.5](https://www.python.org/)
* [Django 3.0.5](https://www.djangoproject.com/) 
* [DRF](https://www.django-rest-framework.org/)
* [Nginx](https://www.nginx.com/)
* [Gunicorn](https://gunicorn.org/)
* [Docker](https://www.docker.com/)

*See the full list of project dependencies here: [requirements.txt](https://github.com/KirillZorikov/yamdb_final/blob/master/requirements.txt)*

## Project deployment

### Project run
```
docker-compose up
```

### Apply migrations
```
docker-compose exec yamdb_prod python manage.py migrate
```

### Collect static
```
docker-compose exec yamdb_prod python manage.py collectstatic
```

### Create superuser
```
docker-compose exec yamdb_prod python manage.py createsuperuser
```

### Fill the database with dummy data
```
docker-compose exec yamdb_prod python manage.py populate_db
or
docker-compose exec yamdb_prod python manage.py loaddata fixtures.json
```
