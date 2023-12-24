from .models import *
from rest_framework import serializers

class GlocerySerialiZer(serializers.ModelSerializer):
    class Meta:
        model = Glocery
        fields = '__all__'
