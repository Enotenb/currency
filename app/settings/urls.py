from django.contrib import admin
from django.urls import path, include
from currency import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),


    path('', views.IndexView.as_view(), name='index'),
    path('contact-us/', views.ContactListView.as_view(), name='contact_us'),
    path('contact-us/create/', views.ContactUsCreateView.as_view(), name='contactus_create'),

    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
]
