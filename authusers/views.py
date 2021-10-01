from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
import pyotp
import base64
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer

from .models import CustomUser
from .models import MagicLink
from .utils import send_operations

class UserLogin(APIView):
    """
    view for handling login post requests
    """
    def post(self, request):
        # check if a user with that email exists
        email = request.data.get('email')
        phone = request.data.get('phone_number')
        user = None
        try:
            if email:
                user = CustomUser.objects.get(email=email)
            if phone:
                users = CustomUser.objects.all()
                user = CustomUser.objects.get(phone_number=phone)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        send_operations(request, user)
        return Response({'status':201, 'userdata': user.username})


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

                send_operations(request, user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DashboardView(APIView):
    """
    a protected view
    """
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        return Response(data={"message": "welcome home"}, status=status.HTTP_200_OK)

class VerifyOTPView(APIView):
    """
    verifies entered otp and manually generates a jwt token for a user
    """

    def get_tokens_for_user(self, user, otp):
        """
        generates jwt with otp code
        """
        refresh = RefreshToken.for_user(user)
        refresh['otp'] = otp
        return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

    def post(self, request):
        username = request.data.get('username')
        print("username",username)
        user = CustomUser.objects.get(username=username)
        if user is not None:
            key = base64.b32encode(user.username.encode())
            otp = pyotp.HOTP(key)
            if otp.verify(request.data['otpCode'], user.counter):
                user.isVerified = True
                user.code = otp.at(user.counter)
                user.save()
                token = self.get_tokens_for_user(user, user.code)
                return Response({'status': 200, 'message': 'otp verified', 'token': token})
            else:
                return Response({'status': 400, 'message': 'wrong otp code'})
        return Response({'status': 400, 'message': 'user does not exist'})


class LoginUserFromEmail(APIView):
    """
    creates a jwt from url associated with user
    """
    def post(self,request):
        user = CustomUser.objects.last()

        if user is not None:
            magic_link = MagicLink.objects.get(user=user)
            magic_link_token = magic_link.get_tokens_for_user(user)

            return Response({'status': 200, 'message': 'magiclink ok', 'token': magic_link_token})
        return Response({'status': 400, 'message': 'user does not exist'})

