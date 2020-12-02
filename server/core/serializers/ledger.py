"""
Serializer classes for ledger models
"""
from rest_framework import serializers
from ..models import (
    BankAccount,
    BankAccountTransactionRecord,
    Ledger,
    LedgerCategory,
    LedgerRecord,
    LedgerExpectedRecord,
    LedgerMonthlyExpectedItem,
)
from .base import BaseModelSerializer

class BankAccountSerializer(BaseModelSerializer):
    """
    Bank Account Serializer
    """
    class Meta:
        model = BankAccount
        fields = '__all__'


class BankAccountTransactionRecordSerializer(BaseModelSerializer):
    """
    Bank Account Transaction Record Serializer
    """
    class Meta:
        model = BankAccountTransactionRecord
        fields = '__all__'


class LedgerSerializer(BaseModelSerializer):
    """
    Ledger Serializer
    """
    class Meta:
        model = Ledger
        fields = '__all__'


class LedgerCategorySerializer(BaseModelSerializer):
    """
    Leger Category Serializer
    """
    class Meta:
        model = LedgerCategory
        fields = '__all__'


class LedgerRecordSerializer(BaseModelSerializer):
    """
    Ledger Record Serializer
    """
    class Meta:
        model = LedgerRecord
        fields = '__all__'


class LedgerExpectedRecordSerializer(BaseModelSerializer):
    """
    Ledger Expected Record Serializer
    """
    class Meta:
        model = LedgerExpectedRecord
        fields = '__all__'


class LedgerMonthlyExpectedItemSerializer(BaseModelSerializer):
    """
    Ledger Monthly Expected Item Serializer
    """
    class Meta:
        model = LedgerMonthlyExpectedItem
        fields = '__all__'
