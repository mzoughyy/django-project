# Generated by Django 4.1.7 on 2023-03-12 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0064_personel_date_joined'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personel',
            old_name='contart',
            new_name='contrat',
        ),
    ]