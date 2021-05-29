from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from .validators import validate_year

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        'Название', max_length=50, help_text='Название категории'
    )
    slug = models.SlugField(
        'Слаг',
        max_length=60,
        unique=True,
        help_text='Уникальное имя, используется в url',
        db_index=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        'Название', max_length=50, help_text='Название жанра'
    )
    slug = models.SlugField(
        'Слаг',
        max_length=60,
        unique=True,
        help_text='Уникальное имя, используется в url',
        db_index=True,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        'Название', max_length=100, help_text='Название произведения'
    )
    year = models.PositiveSmallIntegerField(
        'Год',
        null=True,
        blank=True,
        validators=(validate_year,),
        db_index=True,
        help_text='Год создания произведения',
    )
    description = models.TextField(
        'Описание',
        null=True,
        blank=True,
        help_text='Чему посвящено произведение',
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Жанр',
        help_text='К какому жанру относится произведение',
    )
    category = models.ForeignKey(
        Category,
        related_name='titles',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория',
        help_text='К какой категории относится произведение',
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('year',)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(
        'Текст отзыва',
        help_text='Здесь вы можете написать свои мысли по поводу произведения',
    )
    title = models.ForeignKey(
        Title,
        models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
        help_text='Произведение к которому относится отзыв',
    )
    author = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
        help_text='Автор отзыва',
    )
    score = models.PositiveSmallIntegerField(
        'Оценка',
        validators=[
            validators.MinValueValidator(1, 'Минимальное значение = 1'),
            validators.MaxValueValidator(10, 'Максимальное значение = 10'),
        ],
        help_text='Оценка произведения по шкале от 1 до 10',
        db_index=True,
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('score',)
        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'), name='duplicate_review'
            ),
        ]

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    text = models.TextField(
        'Текст комментария',
        help_text='Здесь можно поделиться своими мыслями по поводу отзыва',
    )
    author = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text='Автор комментария',
    )
    review = models.ForeignKey(
        Review,
        models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
        help_text='Отзыв на который оставлен комментарий',
    )
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[:15]
