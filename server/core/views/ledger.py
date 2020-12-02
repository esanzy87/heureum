"""
Viewset classes for model Ledger
"""
from rest_framework import pagination
from ..serializers import (
    BankAccountSerializer,
    BankAccountTransactionRecordSerializer,
    LedgerSerializer,
    LedgerCategorySerializer,
    LedgerRecordSerializer,
    LedgerExpectedRecordSerializer,
    LedgerMonthlyExpectedItemSerializer,
)
from ..models import (
    BankAccount,
    BankAccountTransactionRecord,
    Ledger,
    LedgerCategory,
    LedgerRecord,
    LedgerExpectedRecord,
    LedgerMonthlyExpectedItem,
)
from .base import BaseModelViewSet

class BankAccountModelViewSet(BaseModelViewSet):
    """
    은행 계좌 API
    """
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()
    pagination_class = pagination.LimitOffsetPagination


class BankAccountTransactionRecordModelViewSet(BaseModelViewSet):
    """
    은행 계좌 거래 내역 API
    """
    serializer_class = BankAccountTransactionRecordSerializer
    queryset = BankAccountTransactionRecord.objects.all()
    pagination_class = pagination.LimitOffsetPagination


class LedgerModelViewSet(BaseModelViewSet):
    """
    장부 API
    """
    serializer_class = LedgerSerializer
    queryset = Ledger.objects.all()
    pagination_class = pagination.LimitOffsetPagination


class LedgerCategoryModelViewSet(BaseModelViewSet):
    """
    장부 적요 API
    """
    serializer_class = LedgerCategorySerializer
    queryset = LedgerCategory.objects.all()
    pagination_class = pagination.LimitOffsetPagination


class LedgerRecordModelViewSet(BaseModelViewSet):
    """
    장부 기장 내역 API
    """
    serializer_class = LedgerRecordSerializer
    queryset = LedgerRecord.objects.all()
    pagination_class = pagination.LimitOffsetPagination


class LedgerExpectedRecordModelViewSet(BaseModelViewSet):
    """
    장부 예정 내역 API
    """
    serializer_class = LedgerExpectedRecordSerializer
    queryset = LedgerExpectedRecord.objects.all()
    pagination_class = pagination.LimitOffsetPagination


class LedgerMonthlyExpectedItemModelViewSet(BaseModelViewSet):
    """
    장부 윌간 고정 유입/유출 예정 내역 API
    """
    serializer_class = LedgerMonthlyExpectedItemSerializer
    queryset = LedgerMonthlyExpectedItem.objects.all()
    pagination_class = pagination.LimitOffsetPagination
