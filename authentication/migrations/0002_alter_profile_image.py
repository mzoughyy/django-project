# Generated by Django 4.1.7 on 2023-02-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='user.png', upload_to='static/img/profile_pics'),
        ),
    ]
