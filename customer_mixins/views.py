
from django.shortcuts import render
from .models import customerMixinModel
from .serializers import customerMixinSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin


# Creating function for html page

def mixin_home(request):
    return render(request,'mixin.html')



#creating create and read functions in one  class
class customerCRMixin(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=customerMixinModel.objects.all()
    serializer_class=customerMixinSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

#creating update,retrieve and destroy functions in one  class

class customerRUDMixin(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=customerMixinModel.objects.all()
    serializer_class=customerMixinSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
    
    