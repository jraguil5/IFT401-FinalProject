from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BrokerageAccount, Transaction, Stock
from .serializers import BrokerageAccountSerializer, TransactionSerializer, StockSerializer 


class StockViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing and retrieving stock information."""
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]


class BrokerageAccountViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing and retrieving the user's brokerage account/cash balance."""
    serializer_class = BrokerageAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BrokerageAccount.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def trade(self, request):
        """Custom endpoint to handle buy and sell transactions."""
        data = request.data
        user_account = self.get_queryset().first() 

        # 1. Validate Inputs (stock_ticker, quantity, type)
        try:
            stock = Stock.objects.get(ticker=data.get('ticker'))
            quantity = int(data.get('quantity'))
            trade_type = data.get('type').upper()
        except (Stock.DoesNotExist, ValueError):
            return Response({"error": "Invalid input."}, status=status.HTTP_400_BAD_REQUEST)

        # 2. Get Real-Time Price (Requires Generator App/API Integration)
        # current_price = get_stock_price(stock.ticker) 

        # 3. Execute Transaction Logic (Buy/Sell)
        if trade_type == 'BUY':
            return Response({"message": f"Successfully processed BUY order for {quantity} shares of {stock.ticker}."}, status=status.HTTP_200_OK)
        elif trade_type == 'SELL':
            return Response({"message": f"Successfully processed SELL order for {quantity} shares of {stock.ticker}."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid transaction type."}, status=status.HTTP_400_BAD_REQUEST)
