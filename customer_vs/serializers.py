
from rest_framework import serializers
from .models import *

class customerVSSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerVSModel
        fields="__all__"