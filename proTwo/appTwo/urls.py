from django.urls import path
from appTwo import views

urlpatterns = [
    path('', views.users, name='users'),
    path('', views.homepage, name='homepage'),
    path('', views.help, name='help'),
    path('', views.formpage, name='formpage'),
]
