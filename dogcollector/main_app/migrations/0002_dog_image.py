# Generated by Django 4.1.7 on 2023-03-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='image',
            field=models.ImageField(default='cats', upload_to='main_app/static/uploads/'),
        ),
    ]
