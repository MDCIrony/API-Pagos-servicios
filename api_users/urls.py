from django.urls import path
from .views import get_user

# from .views import register_new


urlpatterns = [
    path('get-users/<str:username>/', get_user, name='get_user'),
]
