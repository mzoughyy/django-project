from django.db import models
from django.contrib.auth.models import User
from authentication.models import profile,Fournisseurs,Appartment
from django.utils import timezone
class contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.TextField()
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    image=models.FileField(null=True,upload_to='img/reclamation')

    def __str__(self):
        return self.user.username
class TravauxPAyment(models.Model):
    class Meta:
        verbose_name = 'Travaux Payment'

    profile = models.ForeignKey(profile,on_delete=models.CASCADE,null=True)
    traveaux = models.ForeignKey(Fournisseurs,on_delete=models.CASCADE,null=True)
    payment=models.IntegerField(null=True)
    recu=models.FileField(null=True,upload_to='recu/')
    paid_at = models.DateTimeField(default=timezone.now)

class Creditpayment(models.Model):
    class Meta:
        verbose_name = 'Credit Payment'
    Appartment = models.ForeignKey(Appartment,on_delete=models.CASCADE,null=True)
    profile = models.ForeignKey(profile,on_delete=models.CASCADE,null=True)
    payment=models.IntegerField(null=True)
    recu=models.FileField(null=True,upload_to='recu/')
    paid_at = models.DateTimeField(default=timezone.now)
    def save(self, *args, **kwargs):
        self.profile.credit -= self.payment
        self.profile.save()
        super().save(*args, **kwargs)
        
class SendMail(models.Model):
    recipient = models.ManyToManyField(User)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.subject
class EmailUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
