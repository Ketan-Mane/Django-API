from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('get-students',getStudent),
    path('post-student',postStudent),
    path('put-student',putStudent),
]
