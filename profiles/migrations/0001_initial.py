# Generated by Django 3.2 on 2021-05-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('useremail', models.CharField(max_length=100)),
                ('userfname', models.CharField(max_length=100)),
                ('userlname', models.CharField(max_length=100)),
                ('userbirth', models.CharField(max_length=100)),
            ],
        ),
    ]
