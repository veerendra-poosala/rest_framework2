from django.db.models import fields
from rest_framework import serializers
from .models import *

class customerCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerCrudModel
        fields="__all__"