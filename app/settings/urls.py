from django.contrib import admin
from django.urls import path

from currency.views import hello_world, generate_password, contact_us, index, rate_list, rate_create, rate_update,\
    rate_details, rate_delete, source_list, source_create, source_details, source_update, source_delete

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello-world/', hello_world),

    path('generate-password/', generate_password),

    path('rate/list/', rate_list),

    path('rate/create/', rate_create),

    path('rate/update/<int:rate_id>/', rate_update),

    path('rate/details/<int:rate_id>/', rate_details),

    path('rate/delete/<int:rate_id>/', rate_delete),

    path('source/list/', source_list),

    path('source/create/', source_create),

    path('source/details/<int:source_id>/', source_details),

    path('source/update/<int:source_id>/', source_update),

    path('source/delete/<int:source_id>/', source_delete),

    path('', index),

    path('contact-us/', contact_us),

]
