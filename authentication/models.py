from django.db import models
from django.contrib.auth.models import User 
from django.views import generic
from django.urls import reverse_lazy
from twilio.rest import Client
import csv
from django.utils import timezone
from Syndic.settings import BASE_DIR
from django.shortcuts import render, redirect

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.BigIntegerField(default=4)
    appartment = models.CharField(max_length=250,choices=[],default="AS")
    parking_spot = models.CharField(max_length=250,choices=[],default="AS")
    second_parking = models.CharField(max_length=255,choices=[],default="AS")
    CIN = models.BigIntegerField(default=1235)
    image=models.ImageField(upload_to="img/%y",null=True,default='/img/23/user.png')    
    credit=models.IntegerField(null=True)
 


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"  
    

    def populate_appartment_choices(self):
        APP_CHOICES = []

        with open('media/csv/appartment.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                APP_CHOICES.append((row['key'], row['value']))

        self._meta.get_field('appartment').choices = APP_CHOICES

    def populate_parking_choices(self):
        PARK_CHOICES = []

        with open('media/csv/parking_spot.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                PARK_CHOICES.append((row['key'], row['value']))

        self._meta.get_field('parking_spot').choices = PARK_CHOICES
    def populate_parking1_choices(self):
        PARK_CHOICES = []

        with open('media/csv/parking_spot.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                PARK_CHOICES.append((row['key'], row['value']))

        self._meta.get_field('second_parking').choices = PARK_CHOICES


    def save(self, *args, **kwargs):
        if not self._meta.get_field('appartment').choices:
            self.populate_appartment_choices()
        if not self._meta.get_field('parking_spot').choices:
            self.populate_parking_choices()
        if not self._meta.get_field('second_parking').choices:
            self.populate_parking_choices()

        super().save(*args, **kwargs)

# Create an instance of Profile and call the methods on that instance
profile_instance = profile()
profile_instance.populate_appartment_choices()
profile_instance.populate_parking_choices()
profile_instance.populate_parking1_choices()
class ChatMessage(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    msg_sender = models.ForeignKey(profile, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(profile, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body
class personel(models.Model):
    name=models.CharField(max_length=255)
    contrat = models.FileField(upload_to="contrat/%y", max_length=254,null=True)
    congée= models.IntegerField()
    date_joined=models.DateTimeField(default=timezone.now)

class Appartment(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    number=models.IntegerField()
    def __str__(self):
        return f"{self.name} - {self.number}"
STATUS = [
    ("Done", "Done"),
    ("Pending", "Pending"),

]
class Fournisseurs(models.Model):
    class Meta:
        verbose_name='Fournisseur'
    name=models.CharField(max_length=255)
    travaux_type=models.CharField(max_length=255)
    frais=models.IntegerField(null=True)
    date=models.DateTimeField(default=timezone.now)
    contract=models.FileField(upload_to="Fournisseur_Contracts")
    status = models.CharField(max_length=250,choices=STATUS,default="AS")

    def __str__(self):
        return self.travaux_type
