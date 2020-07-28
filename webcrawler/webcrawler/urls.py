
from django.urls import path
from django.urls import  include
from django.contrib import admin
from crawler import views

app_name = 'crawler'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('crawler.urls',namespace= "crawler")),
]
