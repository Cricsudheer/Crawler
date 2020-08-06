from django.urls import path
from .import views

app_name = 'crawler'
urlpatterns =[
    path('',views.index,name='index'),
    path('formpage/',views.search_form_view , name='searchform'),
    path('formpage/<str:handle>/',views.person, name= 'person'),
    path('user_login/',views.user_login,name ='user_login'),
    path('logout/',views.user_logout,name='logout'),
    # path('register/',views.register,name='register'),
]