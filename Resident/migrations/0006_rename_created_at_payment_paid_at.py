# Generated by Django 4.1.7 on 2023-03-05 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0005_payment_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='created_at',
            new_name='paid_at',
        ),
    ]
