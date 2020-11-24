"""
회원 관련 모델
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .base import BaseModel


class UserManager(BaseUserManager):
    """
    UserManager
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves new user
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=email.lower(), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves new superuser
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User (회원)
    """
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=150, blank=True)
    birthdate = models.DateTimeField(null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_verified = models.BooleanField(
        _('email verification status'),
        default=False,
        help_text=_(
            'Designates whether this user has verified email. '
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'users'


class SignupRouteCategory(BaseModel):
    """
    Signup Route Category
    회원가입 경로 구분 기준
    """
    name = models.CharField(
        _('name'),
        max_length=200,
        help_text=_('가입 경로 구분 기준 명칭'),
    )

    class Meta:
        db_table = 'signup_route_category'

    def __str__(self):
        return self.name


class UserRouteMap(BaseModel):
    """
    User Route Map
    회원과 회원 가입경로를 매칭한 테이블
    Many to Many relattion between User and SingupRouteCategory
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routes')
    category = models.ForeignKey(
        SignupRouteCategory,
        on_delete=models.CASCADE,
        help_text=_('가입 경로 구분 기준 명칭')
    )
    comment = models.CharField(
        _('comment'),
        max_length=200,
        help_text=_('좀 더 상세한 가입경로 설명')
    )

    class Meta:
        db_table = 'user_route_map'


class DropoutReasonCategory(BaseModel):
    """
    Dropout Reason Category
    탈회 사유 구분 기준
    """
    name = models.CharField(
        _('name'),
        max_length=200,
        help_text=_('탈회 사유 구분 기준 명칭'),
    )

    class Meta:
        db_table = 'dropout_reason_category'

    def __str__(self):
        return self.name


class UserDropoutReasonMap(BaseModel):
    """
    User Dropout Reason Map
    회원과 회원 탈회 사유를 매칭한 테이블
    Many to Many relattion between User and DropoutReasonCategory
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dropout_reasons')
    category = models.ForeignKey(
        DropoutReasonCategory,
        on_delete=models.CASCADE,
        help_text=_('탈회 사유 구분 기준 명칭')
    )
    comment = models.CharField(
        _('comment'),
        max_length=200,
        help_text=_('좀 더 상세한 탈회사유 설명')
    )

    class Meta:
        db_table = 'user_dropout_reason_map'
