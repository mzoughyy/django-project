# Generated by Django 4.1.7 on 2023-03-12 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Resident', '0010_alter_creditpayment_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravauxPAyment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.IntegerField(null=True)),
                ('recu', models.FileField(null=True, upload_to='recu/')),
                ('paid_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Travaux Payment',
            },
        ),
    ]
