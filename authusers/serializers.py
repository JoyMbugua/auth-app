from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number')
        extra_kwargs = {
            'phone_number':  {'required': False}, 
            'username': {'required': True}, 
            }

    def create(self, validated_data):
        print("VALIDATED",validated_data)
        username = validated_data.get('username')
        user_email = validated_data.get('email', None)
        phone = validated_data.get('phone_number', None)
      
        if user_email:
            user = CustomUser.objects.create_user(username, user_email)
        elif phone:
            user = CustomUser.objects.create_user(username, phone)
        return user

