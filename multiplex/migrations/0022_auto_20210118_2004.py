# Generated by Django 3.0.2 on 2021-01-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0021_movie_limitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
