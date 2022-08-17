from django.db import models # noqa

# Create your models here.


class Rate(models.Model):
    base_currency_type = models.CharField(max_length=3)
    currency_type = models.CharField(max_length=3)
    sale = models.DecimalField(max_digits=10, decimal_places=4)
    buy = models.DecimalField(max_digits=10, decimal_places=4)
    source = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    email_from = models.EmailField()
    email_to = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=10_000)
