
from rest_framework import serializers
from .models import customerMixinModel

class customerMixinSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerMixinModel
        fields="__all__"