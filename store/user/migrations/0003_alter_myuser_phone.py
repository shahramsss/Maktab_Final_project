# Generated by Django 4.0 on 2021-12-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_myuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.BigIntegerField(max_length=56),
        ),
    ]