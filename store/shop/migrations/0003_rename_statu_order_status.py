# Generated by Django 4.0 on 2021-12-29 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_category_statu_order_statu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='statu',
            new_name='status',
        ),
    ]