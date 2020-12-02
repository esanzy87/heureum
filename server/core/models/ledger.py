"""
장부 관련 모델
"""
from django.conf import settings
from django.db import models
from .base import BaseModel


class BankAccount(BaseModel):
    """
    Bank Account
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    alias = models.CharField(max_length=200, blank=True)
    bank_name = models.CharField(max_length=40)
    bank_code = models.CharField(max_length=4)
    number =  models.CharField(max_length=20)  # 계좌번호

    class Meta:
        db_table = 'bank_accounts'


class BankAccountTransactionRecord(BaseModel):
    """
    Bank Account Transaction Record
    """
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    transaction_type = models.CharField(max_length=20, blank=True)
    heading = models.CharField(max_length=200, blank=True)
    inflow = models.IntegerField(default=0)
    outflow = models.IntegerField(default=0)
    after_balance_amount = models.IntegerField()
    branch_name = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'bank_account_transaction_records'


class Ledger(BaseModel):
    """
    Ledger
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    alias = models.CharField(max_length=200, blank=True)
    account_started = models.DateTimeField(null=True)
    balance_started = models.IntegerField(default=0)
    bankruptcy_balance = models.IntegerField(default=-1)
    accounts = models.ManyToManyField(BankAccount, blank=True)

    class Meta:
        db_table = 'ledgers'


class LedgerCategory(BaseModel):
    """
    Ledger Category
    """
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    inout_type = models.CharField(max_length=4, choices=(('IN', 'IN'), ('OUT', 'OUT')))
    connected_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'ledger_categories'


class LedgerRecord(BaseModel):
    """
    Ledger Record
    """
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    application_date = models.DateTimeField()
    category = models.ForeignKey(LedgerCategory, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, blank=True)
    inflow = models.IntegerField(default=0)
    outflow = models.IntegerField(default=0)

    class Meta:
        db_table = 'ledger_records'


class LedgerExpectedRecord(BaseModel):
    """
    Ledger Expected Record
    """
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    application_date = models.DateTimeField()
    category = models.ForeignKey(LedgerCategory, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, blank=True)
    inflow = models.IntegerField(default=0)
    outflow = models.IntegerField(default=0)

    class Meta:
        db_table = 'ledger_expected_records'


class LedgerMonthlyExpectedItem(BaseModel):
    """
    Ledger Monthly Expected Item
    """
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE)
    started = models.DateTimeField()
    ended = models.DateTimeField(null=True)
    category = models.ForeignKey(LedgerCategory, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, blank=True)
    inflow = models.IntegerField(default=0)
    outflow = models.IntegerField(default=0)
    date_of_month = models.IntegerField()
    allow_weekend = models.BooleanField(default=False)
    on_weekend_postpone = models.BooleanField(default=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True
    )  # 값 변경 시 히스토리 관리를 위해 이전 버전은 parent에 할당하여 참조하도록 하고 새로운 레코드 생성함.

    class Meta:
        db_table = 'ledger_monthly_expected_items'
