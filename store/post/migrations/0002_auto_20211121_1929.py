# Generated by Django 3.2.9 on 2021-11-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, verbose_name=models.CharField(max_length=56, unique=True, verbose_name='title')),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=56, unique=True, verbose_name='title'),
        ),
    ]
