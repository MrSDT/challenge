# Generated by Django 3.2 on 2021-05-05 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='slug',
            new_name='url',
        ),
    ]
