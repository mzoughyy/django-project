from django.db import models
from django.contrib.auth.models import User
from authentication.models import profile
from django.utils import timezone
class contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.user.username

class payment(models.Model):
    profile = models.ForeignKey(profile,on_delete=models.CASCADE,null=True)
    payment=models.IntegerField(null=True)
    recu=models.FileField(null=True,upload_to='recu/')
    paid_at = models.DateTimeField(default=timezone.now)
    def save(self, *args, **kwargs):
        self.profile.credit -= self.payment
        self.profile.save()
        super().save(*args, **kwargs)