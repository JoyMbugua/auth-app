from django.urls import path
from .views import CustomUserCreate

urlpatterns = [ 
    path('users/register', CustomUserCreate.as_view(), name='registerview')
]