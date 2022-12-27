from django.urls import path
from .views import get_landing_page, get_test_page


urlpatterns = [
    # path('test/', get_test_page),
    path('<id>/', get_landing_page),
]