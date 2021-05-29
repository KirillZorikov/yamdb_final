from datetime import date

from django.core.exceptions import ValidationError


def validate_year(value):
    if value > date.today().year:
        raise ValidationError(
            f'Значение года {value} не может быть использовано!'
        )
