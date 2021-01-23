# Generated by Django 3.0.5 on 2020-10-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0009_auto_20201010_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
