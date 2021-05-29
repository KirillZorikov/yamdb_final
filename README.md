# api_yamdb

The YaMDb project collects user reviews of the titles. 
Titles can be of various categories. For example: "Books", "Movies", "Music".

Production version on a running server: http://84.252.132.216/

Workflow status badge:
![yamdb_workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

You can download docker images from the following link:
[yamdb final](https://hub.docker.com/repository/docker/kzorikov/yamdb_final).

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