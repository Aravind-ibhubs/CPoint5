from django.shortcuts import render
from .models import *
from .serialize import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def GloceryList(request):
    gloceryobject = Glocery.objects.all()
    if request.method == "GET":
        gloceryobject = Glocery.objects.all()
        serial_data = GlocerySerialiZer(gloceryobject, many=True)
        return Response(serial_data.data)
    elif request.method == "POST":
        serial_data = GlocerySerialiZer(data=request.data)
        if serial_data.is_valid():
            serial_data.save()        
        return Response(serial_data.data)

