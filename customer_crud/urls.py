from django.urls import path

from .views import *

urlpatterns = [
    path('c/',crud,name='crud'),
    path('post/',createCustomerDetails),
    path('read/',readCustomerDetails),
    path('update/<int:pk>',updateCustomerDetails),
    path('delete/<int:pk>',deleteCustomerDetails),
    
]