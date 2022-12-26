from django.urls import path
from .views import *

urlpatterns = [
    path('test/', get_something, name='test')
]