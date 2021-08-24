import re
from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response


# creating functions for CRUD Operations
#creating read function
def crud(request):
    return render(request,'crud.html')

@api_view(['GET'])
def readCustomerDetails(request):
    #creating query set for studentModel
    q_set=customerCrudModel.objects.all()
    #creating serializer
    serializer=customerCrudSerializer(q_set,many=True)
    return Response(serializer.data)


#Creating create function

@api_view(['POST','GET'])
def createCustomerDetails(request):
    q_set=customerCrudModel.objects.all()

    serializer=customerCrudSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST','GET'])
def updateCustomerDetails(request,pk):
    id=pk


    q_set=customerCrudModel.objects.get(pk=id)

    serializer=customerCrudSerializer(instance=q_set,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE','GET'])
def deleteCustomerDetails(request,pk):
    id=pk
    
    if id is not None:
        q_set=customerCrudModel.objects.get(pk=id)

        q_set.delete()
        return Response('Deleted successfully')
    else:
        return Response('INvalid id')

  
    