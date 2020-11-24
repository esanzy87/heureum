"""
API Views for User model
"""
from django.contrib.auth import get_user_model, login
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from ..serializers import UserSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    """
    Create a new user
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LoginView(generics.GenericAPIView, mixins.CreateModelMixin):
    """
    View to login
    """
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Returns user
        """
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.validated_data.get('user')
        login(request, user)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)


class MeView(generics.ListAPIView):
    """
    Loggedin User Info
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return self.queryset.filter(id=self.request.user.id).all()
