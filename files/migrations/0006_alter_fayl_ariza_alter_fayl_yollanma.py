# Generated by Django 4.1.7 on 2023-04-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_fayl_telefon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fayl',
            name='ariza',
            field=models.FileField(blank=True, upload_to='ariza/'),
        ),
        migrations.AlterField(
            model_name='fayl',
            name='yollanma',
            field=models.FileField(blank=True, upload_to='yo`lanma xat/'),
        ),
    ]
