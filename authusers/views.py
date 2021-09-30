from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
import pyotp
import base64
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer


from .models import CustomUser
from .email import send_otp_mail
from .models import MagicLink


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

                # generate otp code with username
                key = base64.b32encode(user.username.encode())
                hotp = pyotp.HOTP(key).at(user.counter)

                # generate a magic link object for the user
                magiclink = MagicLink.objects.create(user=user, email=user.email, code=hotp)
                link=magiclink.generate_url(request)
                send_otp_mail(user.username, user.email, hotp, link)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ObtainTokenPairView(TokenObtainPairView):
    """
    creates a token from serializer
    """
    serializer_class = MyTokenObtainPairSerializer


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
        user = CustomUser.objects.last()
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
                print('Not it!')
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
