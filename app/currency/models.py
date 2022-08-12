from django.db import models

# Create your models here.


class ContactUs(models.Model):
    email_from = models.EmailField()
    email_to = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=10_000)
