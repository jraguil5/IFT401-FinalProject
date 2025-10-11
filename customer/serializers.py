#convert data into readable JSON for API communication
from rest_framework import serializers
from .models import Portfolio, Transaction, Stock, Holding
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class HoldingSerializer(serializers.ModelSerializer):
    stock_ticker = serializers.ReadOnlyField(source='stock.ticker')
    class Meta:
        model = Holding
        fields = ['id', 'stock_ticker', 'quantity']

class PortfolioSerializer(serializers.ModelSerializer):
    holdings = HoldingSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Portfolio
        fields = ['id', 'user', 'cash_balance', 'holdings']

class TransactionSerializer(serializers.ModelSerializer):
    stock_ticker = serializers.ReadOnlyField(source='stock.ticker')
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('timestamp', 'price_at_transaction')