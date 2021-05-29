# Generated by Django 3.0.5 on 2021-05-03 05:07

import api.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название категории', max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Уникальное имя, используется в url', max_length=60, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Здесь можно поделиться своими мыслями по поводу отзыва', verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название жанра', max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Уникальное имя, используется в url', max_length=60, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Здесь вы можете написать свои мысли по поводу произведения', verbose_name='Текст отзыва')),
                ('score', models.PositiveSmallIntegerField(db_index=True, help_text='Оценка произведения по шкале от 1 до 10', validators=[django.core.validators.MinValueValidator(1, 'Минимальное значение = 1'), django.core.validators.MaxValueValidator(10, 'Максимальное значение = 10')], verbose_name='Оценка')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('score',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название произведения', max_length=50, verbose_name='Название')),
                ('year', models.PositiveSmallIntegerField(blank=True, db_index=True, help_text='Год создания произведения', null=True, validators=[api.validators.validate_year], verbose_name='Год')),
                ('description', models.TextField(blank=True, help_text='Чему посвящено произведение', null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, help_text='К какой категории относится произведение', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='api.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(blank=True, help_text='К какому жанру относится произведение', to='api.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ('year',),
            },
        ),
    ]
