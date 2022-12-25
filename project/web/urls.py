from django.urls import path
from .views import get_landing_page


urlpatterns = [
    path('<id>/', get_landing_page),
]