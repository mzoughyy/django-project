# Generated by Django 4.1.7 on 2023-02-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0027_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/img/23/person.jpg', null=True, upload_to='img/%y'),
        ),
    ]
