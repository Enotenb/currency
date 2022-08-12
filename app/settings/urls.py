from django.contrib import admin
from django.urls import path

from currency.views import hello_world, generate_password, contact_us

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello-world/', hello_world),

    path('generate-password/', generate_password),

    path('contact-us/', contact_us)
]
