# Generated by Django 2.2.3 on 2019-07-18 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0004_auto_20190718_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release',
            field=models.DateField(),
        ),
    ]
