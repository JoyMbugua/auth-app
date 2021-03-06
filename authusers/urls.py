from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CustomUserCreate, DashboardView, LoginUserFromEmail, VerifyOTPView, UserLogin

urlpatterns = [ 
    path('users/register/', CustomUserCreate.as_view(), name='registerview'),
    path('users/login/', UserLogin.as_view(), name='loginview'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='tokenrefresh-view'),
    path('verify/', VerifyOTPView.as_view(), name='verifyotp'),
    path('dashboard/', DashboardView.as_view(), name='dashboardview'),
    path('emaillogin/dashboard/', LoginUserFromEmail.as_view(), name='linktoken-view')   
]

