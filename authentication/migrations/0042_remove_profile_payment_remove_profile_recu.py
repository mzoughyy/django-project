# Generated by Django 4.1.7 on 2023-03-05 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0041_profile_payment_profile_recu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='recu',
        ),
    ]
