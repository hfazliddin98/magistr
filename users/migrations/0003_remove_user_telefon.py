# Generated by Django 4.1.7 on 2023-04-03 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_lavozim'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telefon',
        ),
    ]
