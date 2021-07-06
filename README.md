# api_yamdb

[![yamdb_workflow](https://github.com/KirillZorikov/yamdb_final/workflows/yamdb_workflow/badge.svg)](https://github.com/KirillZorikov/yamdb_final/actions)

The YaMDb project collects user reviews of the titles. 
Titles can be of various categories. For example: "Books", "Movies", "Music".

With this project, I learned how to work with:

* [Custom permissions](https://github.com/KirillZorikov/yamdb_final/blob/master/api_users/permissions.py)
* [Custom JWT auth](https://github.com/KirillZorikov/yamdb_final/blob/master/api_users/views.py)

### Project links:

* Api: https://kz-api.tk/yamdb/api/v1

* Api documentation: https://kz-api.tk/yamdb/redoc

* Docker image:
[yamdb_final](https://hub.docker.com/repository/docker/kzorikov/yamdb_final)

### Tech:

* Python 3.8.5

* Django 3.0.5 

* DRF

*See the full list of dependencies here: [requirements.txt](https://github.com/KirillZorikov/yamdb_final/blob/master/requirements.txt)*

## Project setup
```
docker-compose build
```

## Project run
```
docker-compose up
```

## Apply migrations
```
docker-compose exec yamdb_prod python manage.py migrate
```

## Create superuser
```
docker-compose exec yamdb_prod python manage.py createsuperuser
```

## Fill the database with dummy data
```
docker-compose exec yamdb_prod python manage.py populate_db
or
docker-compose exec yamdb_prod python manage.py loaddata fixtures.json
```
