# Generated by Django 2.2.19 on 2021-04-11 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 4, 11, 21, 20, 25, 38624), verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Статья блога',
                'verbose_name_plural': 'Статьи блога',
                'db_table': 'Posts',
                'ordering': ['posted'],
            },
        ),
    ]
