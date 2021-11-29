from django.contrib.auth.models import User
from rest_framework import serializers


class LoginFacebookSerializer(serializers.Serializer):
    access_token = serializers.CharField()

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    class Meta:
        model=User
        fields=['email', 'username']
