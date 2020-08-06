from django.urls import path
from django.urls import include
from django.contrib import admin
from crawler import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('crawler.urls')),
    path('register/',views.register,name='register')
]
