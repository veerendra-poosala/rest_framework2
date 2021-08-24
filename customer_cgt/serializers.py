from django.db.models import fields
from rest_framework import serializers
from .models import *

class customerCGTSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerCGTModel
        fields="__all__"