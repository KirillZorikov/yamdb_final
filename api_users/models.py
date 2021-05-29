from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class CustomUser(AbstractUser):
    role = models.CharField(
        'Роль',
        max_length=50,
        choices=Role.choices,
        default=Role.USER,
        help_text='Группа, к которой принадлежит пользователь.',
    )
    bio = models.CharField(
        'Описание',
        max_length=200,
        blank=True,
        null=True,
        help_text='Описание пользователя.',
    )
    username = models.CharField(
        'Никнейм',
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        help_text='Никнейм пользователя.',
    )
    email = models.EmailField(
        'Email', max_length=100, unique=True, help_text='Email пользователя.',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)

    @property
    def is_admin(self):
        return self.role == Role.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == Role.MODERATOR

    @property
    def is_user(self):
        return self.role == Role.USER

    def __str__(self):
        return self.email


User = get_user_model()
