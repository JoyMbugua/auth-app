from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
import pyotp
import base64
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer

from django.utils.decorators import method_decorator

from .models import CustomUser
from .email import send_otp_mail


class CustomUserCreate(APIView):
    """
    Creates a user
    """
    permission_classes = (permissions.AllowAny, )

 
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            if user:
                user.counter += 1
                user.save()
                key = base64.b32encode(user.username.encode())
                hotp = pyotp.HOTP(key).at(user.counter)
                print("HOT",hotp)
                send_otp_mail(user.username, user.email, hotp)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class DashboardView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        return Response(data={"message": "welcome home"}, status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    """
    verifies entered otp
    """
    def post(self, request):
        user = CustomUser.objects.last()
        if user is not None:
            key = base64.b32encode(user.username.encode())
            otp = pyotp.HOTP(key)
            if otp.verify(request.data['otpCode'], user.counter):
                user.isVerified = True
                user.code = otp.at(user.counter)
                user.save()
                return Response({'status': 200})
            else:
                print('Not it!')
        return Response({'status': 400})

        

