# Generated by Django 4.1.7 on 2023-02-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='appartment',
            field=models.CharField(default='N', max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='parking_spot',
            field=models.CharField(default='A', max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.BigIntegerField(default=4),
        ),
    ]