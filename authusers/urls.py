from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CustomUserCreate, DashboardView, ObtainTokenPairView, VerifyOTPView

urlpatterns = [ 
    path('users/register/', CustomUserCreate.as_view(), name='registerview'),
    path('token/obtain/', ObtainTokenPairView.as_view(), name='tokencreate-view'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='tokenrefresh-view'),
    path('verify/', VerifyOTPView.as_view(), name='verifyotp'),
    path('dashboard/', DashboardView.as_view(), name='dashboardview'),
    
]

