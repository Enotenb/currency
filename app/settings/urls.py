from django.contrib import admin
from django.urls import path, include
from currency import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view()),
    path('contact-us/', views.ContactUsListView.as_view(), name='contact_us'),
    path('contact-us/create/', views.ContactUsCreateView.as_view(), name='contactus_create'),

    path('currency/', include('currency.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
]
