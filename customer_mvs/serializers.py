
from rest_framework import serializers
from .models import *

class customerMVSSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerMVSModel
        fields="__all__"