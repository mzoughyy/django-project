from django.db import models
from django.contrib.auth.models import User 
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from twilio.rest import Client
import csv
from Syndic.settings import BASE_DIR


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.BigIntegerField(default=4)
    appartment = models.CharField(max_length=250,choices=[],default="AS")
    parking_spot = models.CharField(max_length=250,choices=[],default="AS")
    CIN = models.BigIntegerField(default=1235)
    image=models.ImageField(upload_to="img/%y",null=True,default='/img/23/user.png')    
    credit=models.IntegerField(null=True)


    def __str__(self):
        return self.user.username
    def populate_appartment_choices(self):
        APP_CHOICES = []

        with open('media/csv/appartment.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                APP_CHOICES.append((row['key'], row['value']))

        self._meta.get_field('appartment').choices = APP_CHOICES

    def save(self, *args, **kwargs):
        if not self.appartment.field.choices:
            self.populate_appartment_choices()
        super().save(*args, **kwargs)


    def populate_parking_choices(self):
        PARK_CHOICES = []

        with open('media/csv/parking_spot.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                PARK_CHOICES.append((row['key'], row['value']))

        self._meta.get_field('parking_spot').choices = PARK_CHOICES

    def save(self, *args, **kwargs):
        if not self.parking_spot.field.choices:
            self.populate_parking_choices()
        super().save(*args, **kwargs)
      

# Call populate_appartment_choices() before using the profile model
profile().populate_appartment_choices()
profile().populate_parking_choices()

class personel(models.Model):
    name=models.CharField(max_length=255)
    contart = models.FileField(upload_to="contrat/%y", max_length=254,null=True)
    congée= models.IntegerField()

class Appartment(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    number=models.IntegerField()
