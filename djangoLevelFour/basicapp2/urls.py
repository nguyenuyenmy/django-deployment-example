from django.urls import path
from basicapp2 import views

#TEMPLATE TAGGING
app_name = 'basicapp2'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]