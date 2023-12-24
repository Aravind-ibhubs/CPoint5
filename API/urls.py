from django.urls import path
from .views import *

urlpatterns = [
    path('', GloceryList, name="Get Glocery"),
]

