from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import random
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password')
        extra_kwargs = {
            'phone_number':  {'required': False}, 
            'username': {'required': True},
            'password': {'required': False}
            }
    

    def create(self, validated_data):
      
        username = validated_data.get('username')
        user_email = validated_data.get('email', None)
        phone = validated_data.get('phone_number', None)
        # temporary code
        num_code = [str(random.choice([x for x in range(10)])) for _ in range(5)]
        password = ''.join(num_code)
       
        if user_email:
            user = CustomUser.objects.create_user(username, user_email, password)
            user.save()
            return user
        elif phone:
            user = CustomUser.objects.create_user(username, phone, password)
            user.save()
            return user
        return ''
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # add custom claims here
        return token

