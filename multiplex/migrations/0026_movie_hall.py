# Generated by Django 3.0.2 on 2021-01-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0025_auto_20210119_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='hall',
            field=models.CharField(choices=[('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')], default='A', max_length=10),
        ),
    ]
