# Generated by Django 4.1.7 on 2023-03-15 12:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Resident', '0016_notification_recipient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='recipient',
        ),
        migrations.AddField(
            model_name='notification',
            name='recipient',
            field=models.ManyToManyField(related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
