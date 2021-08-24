from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def mvs_home(request):
    return render(request,'mvs.html')
    
class customerMVS(viewsets.ModelViewSet):
    queryset=customerMVSModel.objects.all()
    serializer_class=customerMVSSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
