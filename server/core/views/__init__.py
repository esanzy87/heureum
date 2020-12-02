"""
exported view classes and routes of core app
"""
from rest_framework import routers
from .ledger import (
    BankAccountModelViewSet,
    BankAccountTransactionRecordModelViewSet,
    LedgerModelViewSet,
    LedgerCategoryModelViewSet,
    LedgerRecordModelViewSet,
    LedgerExpectedRecordModelViewSet,
    LedgerMonthlyExpectedItemModelViewSet,
)
from .user import (
    RegisterView,
    LoginView,
    MeView,
)


router = routers.DefaultRouter()
router.register(
    'bank-accounts',
    BankAccountModelViewSet,
    basename='bank-account'
)
router.register(
    'bank-account-transaction-records',
    BankAccountTransactionRecordModelViewSet,
    basename='bank-account-transaction-record'
)
router.register(
    'ledgers',
    LedgerModelViewSet,
    basename='ledger'
)
router.register(
    'ledger-categories',
    LedgerCategoryModelViewSet,
    basename='ledger-category'
)
router.register(
    'ledger-records',
    LedgerRecordModelViewSet,
    basename='ledger-record'
)
router.register(
    'ledger-expected-records',
    LedgerExpectedRecordModelViewSet,
    basename='ledger-expected-record'
)
router.register(
    'ledger-monthly-expected-items',
    LedgerMonthlyExpectedItemModelViewSet,
    basename='ledger-monthly-expected-item'
)
