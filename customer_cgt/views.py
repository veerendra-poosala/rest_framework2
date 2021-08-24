from django.shortcuts import render
from .models import customerCGTModel
from .serializers import customerCGTSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

def cgt_home(request):
    return render(request,'cgt.html')

class readCustomerCGT(ListAPIView):
    queryset=customerCGTModel.objects.all()
    serializer_class=customerCGTSerializer


class createCustomerCGT(CreateAPIView):
    queryset=customerCGTModel.objects.all()
    serializer_class=customerCGTSerializer


class RUDCustomerCGT(RetrieveUpdateDestroyAPIView):
    queryset=customerCGTModel.objects.all()
    serializer_class=customerCGTSerializer

