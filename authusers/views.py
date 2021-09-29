from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer

from .models import CustomUser

class CustomUserCreate(APIView):
    """
    Creates a user
    """
    permission_classes = (permissions.AllowAny, )
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class DashboardView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        return Response(data={"message": "welcome home"}, status=status.HTTP_200_OK)