# Generated by Django 4.1.7 on 2023-03-02 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0036_sms'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sms',
        ),
    ]