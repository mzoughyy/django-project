# Generated by Django 4.1.2 on 2023-05-09 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0024_contact_recu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='recu',
            new_name='image',
        ),
    ]