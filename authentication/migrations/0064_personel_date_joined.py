# Generated by Django 4.1.7 on 2023-03-12 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0063_remove_profile_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='personel',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]