from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .serializers import UserSeralizer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """create a new user in the system"""
    serializer_class = UserSeralizer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):
    """Update the authenticated user"""
    serializer_class = UserSeralizer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        """Retive and Update the authenticated user"""
        return self.request.user
