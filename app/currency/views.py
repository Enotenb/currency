# from django.shortcuts import render
from django.http import HttpResponse

from currency.utils import get_password

# Create your views here.


def hello_world(request):
    return HttpResponse('HELLO WORLD')


def generate_password(request):
    password = get_password()
    return HttpResponse(password)
