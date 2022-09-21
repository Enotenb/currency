from django.db import models # noqa
from currency.model_choices import CurrencyType

# Create your models here.


class Rate(models.Model):
    base_currency_type = models.CharField(
        max_length=3,
        choices=CurrencyType.choices,
        default=CurrencyType.CURRENCY_TYPE_UAH
    )
    currency_type = models.CharField(max_length=3, choices=CurrencyType.choices)
    sale = models.DecimalField(max_digits=10, decimal_places=4)
    buy = models.DecimalField(max_digits=10, decimal_places=4)
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    email_from = models.EmailField()
    email_to = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=10_000)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)


class Source(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, default=None)


class ResponseLog(models.Model):
    response_time = models.FloatField()
    request_method = models.CharField(max_length=10)
    query_params = models.CharField(max_length=254)
    ip = models.CharField(max_length=15)
    path = models.CharField(max_length=300)
