
from django.urls import path,include

from customer_mvs import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('mvs/',views.customerMVS,basename='customer_mvs')


urlpatterns = [
    path('mvs/',views.mvs_home,name='mvs_home'),

    path('crud/',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
   
]