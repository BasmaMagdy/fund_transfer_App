from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_accounts, name='list_accounts'),
    path('accounts/<int:account_id>/', views.account_info, name='account_info'),
    path('transfer/', views.transfer_funds, name='transfer_funds'),
]
