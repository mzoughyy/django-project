# Generated by Django 4.1.2 on 2023-05-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0081_remove_profile_friends_remove_profile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]