from django.urls import path , include
from .views import register_view , login_view ,home_view
from .views import  AccountViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('account',AccountViewSet)

urlpatterns = [
    path('', register_view, name='register'),
    path('login/',login_view, name='login'),
    path('home/',home_view, name='home'),
    path('',include(router.urls)),
]
