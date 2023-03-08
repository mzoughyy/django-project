# Generated by Django 4.1.7 on 2023-03-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0033_delete_sms'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=160)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]
