from django.urls import path 
from . import views

app_name='reports'
urlpatterns=[
    path('', views.index, name='index'),
    path('dice_roll_result', views.dice_roll_result, name='dice_roll_result'),
    path('dice_roll', views.dice_roll, name='dice_roll')
]