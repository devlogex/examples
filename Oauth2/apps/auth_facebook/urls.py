from django.urls import path
from .views import (
    LoginFacebookView,
)

urlpatterns = [
    path("", LoginFacebookView.as_view(), name="login-fb"),
]