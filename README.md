# api_yamdb

The YaMDb project collects user reviews of the titles. 
Titles can be of various categories. For example: "Books", "Movies", "Music".

Production version on a running server: http://kz-api.tk/yamdb/api/v1

Api documentation: http://kz-projects.tk/yamdb/redoc

Workflow status badge:
[![yamdb_workflow](https://github.com/KirillZorikov/yamdb_final/workflows/yamdb_workflow/badge.svg)](https://github.com/KirillZorikov/yamdb_final/actions)

You can download docker images from the following link:
[yamdb final](https://hub.docker.com/repository/docker/kzorikov/yamdb_final).

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
