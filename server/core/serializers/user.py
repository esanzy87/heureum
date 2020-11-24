"""
Serializer classes for User model
"""
from django.contrib.auth import authenticate, get_user_model
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """
    class Meta:
        model = User
        fields = (
            'id', 'password', 'email', 'date_joined', 'last_login',
            'is_superuser', 'is_active', 'is_staff'
        )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6},
        }

    def create(self, validated_data):
        """
        Create a new user with encrypted password and return it
        """
        return get_user_model().objects.create_user(**validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        """
        Update a user, setting in the password
        """
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for the user login process
    """
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """
        Validate and authenticate user
        """
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='login')
        attrs['user'] = user
        return attrs
