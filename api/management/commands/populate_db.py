import csv

from django.apps import apps
from django.core.management import BaseCommand
from django.db import IntegrityError
from django.utils.dateparse import parse_datetime

from api.models import User

CSV_TABLES = {
    'Category': r'data/category.csv',
    'Genre': r'data/genre.csv',
    'User': r'data/users.csv',
    'Title': r'data/titles.csv',
    # 'GenreTitle': r'data/genre_title.csv',
    'Review': r'data/review.csv',
    'Comment': r'data/comments.csv',
}
REPLACE_FIELDS = {
    'category': 'category_id',
    'author': 'author_id',
    'description': 'bio',
}


def check_fields(model, fields):
    """Проверить наличие поля в модели из соответствующего поля csv таблицы"""
    for field in fields:
        if not getattr(model, field, False):
            raise AttributeError(f'В модели {model} нет поля {field}.')


def process_fields(fields):
    """Заменить поля csv таблицы на валидные поля модели Django."""
    return [
        field if field not in REPLACE_FIELDS else REPLACE_FIELDS[field]
        for field in fields
    ]


def populate(model, table):
    """Сделать записи в модель Django."""
    with open(table, 'rt') as file:
        reader = csv.reader(file, dialect='excel')
        fields, *data_rows = reader
        fields = process_fields(fields)
        check_fields(model, fields)
        for row in data_rows:
            # model.objects.update_or_create(**dict(zip(fields, row)))
            data = dict(zip(fields, row))
            if not model.objects.filter(pk=data['id']).exists():
                try:
                    record = model.objects.create(**data)
                except IntegrityError as error:
                    print(
                        (
                            f'Ошибка: {error}\n'
                            f'При сохранении данных: {data}\n'
                            f'В модель: {model}\n'
                        )
                    )
                    print('--' * 20)
                    continue
                if 'pub_date' in data:
                    record.pub_date = parse_datetime(data['pub_date'])
                    record.save()


class Command(BaseCommand):
    """
    Заносит данные из csv таблицы в модель Django.
    Запуск:
        python manage.py populate_db --model `model_name`
            Заполнит модель `model_name`.
            Необходимо следить за заполненностью связанных моделей.
        python manage.py populate_db
            Заполнит все модели.
    """

    def add_arguments(self, parser):
        parser.add_argument('--model', type=str)

    def handle(self, *args, **kwargs):
        model_arg = kwargs.get('model')
        models = [model_arg] if model_arg else CSV_TABLES.keys()
        for model in models:
            populate(
                User if model == 'User' else apps.get_model('api', model),
                CSV_TABLES[model],
            )
            print(f'Модель {model} - успех!')
            print('--' * 20)
