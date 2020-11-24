"""
URLs for core app
"""
from django.urls import path
from .views import (
    router,
    RegisterView,
    LoginView,
    MeView,
)


urlpatterns = router.urls + [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/me/', MeView.as_view(), name='me'),
]
