# Generated by Django 3.0.5 on 2020-10-07 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0003_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]