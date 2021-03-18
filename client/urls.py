from django.urls import path
from . import views

app_name = 'client'
urlpatterns = [
    # ex: /webapp/
    path('', views.listUserData, name='listUserData'),

]

