from django.urls import path

from .views import *

urlpatterns = [
    path('mx/',mixin_home,name='mixin_home'),
    path('cr/',customerCRMixin.as_view()),
    path('rud/<int:pk>/',customerRUDMixin.as_view()),
    
]