from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


def vs_home(request):
    return render(request,'vs.html')

class customerVS(viewsets.ViewSet):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def create(self,request):
        queryset=customerVSModel.objects.all()
        serializer=customerVSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'new customer created'})
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        queryset=customerVSModel.objects.all()
        serializer=customerVSSerializer(queryset,many=True)
        
        return Response(serializer.data)

    def update(self,request,pk):
        id=pk
        queryset=customerVSModel.objects.get(pk=id)
        serializer=customerVSSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'updated customer details'})
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        id=pk
        queryset=customerVSModel.objects.get(id=id)
        serializer=customerVSSerializer(queryset)
        
        return Response(serializer.data)

    def destroy(self,request,pk):
        id=pk
        queryset=customerVSModel.objects.get(pk=id)
        queryset.delete()
        
        return Response({'msg':'customer data destroyed'})