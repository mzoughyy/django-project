# Generated by Django 4.1.7 on 2023-02-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_profile_parking_spot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='appartment',
            field=models.CharField(choices=[('Apprtement Number', 'Appartement Number'), ('A1', 'a1'), ('A2', 'a2'), ('A3', 'a3'), ('A4', 'a4'), ('A5', 'a5'), ('A6', 'a6'), ('A7', 'a7'), ('A8', 'a8'), ('A9', 'a9'), ('A10', 'a10'), ('A11', 'a11'), ('A12', 'a12')], max_length=250),
        ),
    ]
