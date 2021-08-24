
from django.urls import path
from .views import createCustomerCGT,cgt_home,readCustomerCGT,RUDCustomerCGT

urlpatterns = [
    path('cgt/',cgt_home,name='cgt_home'),
    path('cgt_create/',createCustomerCGT.as_view()),
    path('cgt_read/',readCustomerCGT.as_view()),
    path('cgt_rud/<int:pk>/',RUDCustomerCGT.as_view()),
  
]