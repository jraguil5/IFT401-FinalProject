#convert data into readable JSON for API communication
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import BrokerageAccount, Transaction, Stock, Position

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializes the CustomUser model fields for public display."""
    class Meta:
        model = User
        fields = ('UserID', 'UserName', 'Email', 'FullName')

class StockSerializer(serializers.ModelSerializer):
    """Serializes the Stock model, including all fields."""
    class Meta:
        model = Stock
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    """Serializes a user's stock positions, including the stock ticker."""
    stock_ticker = serializers.ReadOnlyField(source='stock.ticker') 
    class Meta:
        model = Position
        fields = ['id', 'stock_ticker', 'quantity']

class BrokerageAccountSerializer(serializers.ModelSerializer):
    """Serializes the BrokerageAccount, nesting the User and Positions."""
    positions = PositionSerializer(many=True, read_only=True, source='positions') 
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = BrokerageAccount
        fields = ['user', 'cash_balance', 'positions']

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializes the Transaction model. 
    """
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'transaction_type', 'price_at_transaction']
        read_only_fields = ('price_at_transaction',)
        
        