from django.urls import path
from . import views

urlpatterns = [
    path('', views.walletsOverview, name='wallets-overview'),
    path('wallet-list/', views.walletList, name='wallet-list'),
    path('wallet-detail/<str:pk>/', views.walletDetail, name='wallet-detail'),
    path('get-prices/<username>', views.get_all_wallet_prices)
]