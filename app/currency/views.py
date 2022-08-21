# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from currency.models import ContactUs, Rate

from currency.utils import get_password
# Create your views here.


def hello_world(request):
    return HttpResponse('HELLO WORLD')


def generate_password(request):
    password = get_password()
    return HttpResponse(password)


def index(request):
    return render(request, 'index.html')


def rate_list(request):
    context = {
        'rate_list': Rate.objects.all(),
    }
    return render(request, 'rate_list.html', context=context)


def contact_us(request):
    context = {
        'contact_list': ContactUs.objects.all(),
        }
    return render(request, 'contact_us.html', context=context)
