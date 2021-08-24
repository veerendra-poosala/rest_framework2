
from django.urls import path,include
from customer_vs import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('vs/',views.customerVS,basename='customer_vs')


urlpatterns = [
    path('vs/',views.vs_home,name='vs_home'),
    path('cr/',include(router.urls)),
   
]