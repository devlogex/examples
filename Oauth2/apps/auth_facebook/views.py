from django.db import models
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

from .serializers import LoginFacebookSerializer, UserSerializer


class LoginFacebookView(APIView):

    def post(self, request):
        params = LoginFacebookSerializer(data=request.data)
        params.is_valid(raise_exception=True)
        response = requests.get(f"https://graph.facebook.com/me?fields=id,email,name,picture&access_token={params.validated_data['access_token']}")
        data = json.loads(response.content)
        name = data["name"]
        email = data["email"]
        avatar_url = data["picture"]["data"]["url"]
        user = User.objects.filter(email=email).first()
        if not user:
            user = User.objects.create(username=email, email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=201)
