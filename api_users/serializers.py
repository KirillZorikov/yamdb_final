from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name',
            'last_name',
            'username',
            'role',
            'bio',
            'email',
        )
        model = User


class CustomTokenObtainSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField()


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
