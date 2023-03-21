# Generated by Django 4.1.7 on 2023-03-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0054_alter_profile_parking_spot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='parking_spot',
            field=models.CharField(choices=[('Parking Spot', 'Parking Spot'), ('P1', 'p1'), ('P2', 'p2'), ('P3', 'p3'), ('P4', 'p4'), ('P5', 'p5'), ('P6', 'p6'), ('P7', 'p7')], default='AS', max_length=250),
        ),
    ]
