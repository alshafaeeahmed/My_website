# Generated by Django 3.0.2 on 2021-01-22 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0030_auto_20210121_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='is_active',
        ),
    ]
