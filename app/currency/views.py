# from django.shortcuts import render
from django.http import HttpResponse
from currency.models import ContactUs

from currency.utils import get_password

# Create your views here.


def hello_world(request):
    return HttpResponse('HELLO WORLD')


def generate_password(request):
    password = get_password()
    return HttpResponse(password)


def contact_us(request):
    contact_list = []
    for contacts in ContactUs.objects.all():
        html_string = f' ID: {contacts.id}, Email From: {contacts.email_from}, Email To: {contacts.email_to},' \
                      f'Subject: {contacts.subject}, Message: {contacts.message} <br>'
        contact_list.append(html_string)
    return HttpResponse(str(contact_list))
