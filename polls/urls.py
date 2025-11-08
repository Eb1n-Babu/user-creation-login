from django.urls import path
from .views import index , details

urlpatterns = [
    path('',index,name='index'),
    path('<int:question_id>/',details,name='details'),


]