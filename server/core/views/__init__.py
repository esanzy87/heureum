"""
exported view classes and routes of core app
"""
from rest_framework import routers
from .user import (
    RegisterView,
    LoginView,
    MeView,
)


router = routers.DefaultRouter()
