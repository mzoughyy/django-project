# Generated by Django 4.1.7 on 2023-03-15 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0017_remove_notification_recipient_notification_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='sent_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
