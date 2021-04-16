from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4, validators=[UniqueValidator(queryset=User.objects.all())])

    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=155, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    
        # def validation(self, data): #attrs
        #     email = data.get('email', '')
        #     if User.objects.filter(email=email).exists():
        #         raise serializers.ValidationError({'email': 'Email is already use'})
        #     return super().validation(data)

        def create(self, valid_data):
            return User.objects.create_user(valid_data)
