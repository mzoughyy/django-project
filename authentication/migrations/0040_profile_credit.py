# Generated by Django 4.1.7 on 2023-03-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0039_rename_personels_personel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='credit',
            field=models.IntegerField(null=True),
        ),
    ]
