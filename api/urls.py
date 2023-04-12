from django.urls import path

from .views import *

urlpatterns = [
    path('update_bd', update_bd, name="update_bd"),
]
