from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BrokerageAccount, Transaction, Stock
from .serializers import BrokerageAccountSerializer, TransactionSerializer, StockSerializer 

def dashboard_view(request):
    return render(request, 'customer/dashboard.html')

class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

class BrokerageAccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BrokerageAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BrokerageAccount.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def trade(self, request):
        data = request.data
        user_account = self.get_queryset().first() 

        try:
            stock = Stock.objects.get(ticker=data.get('ticker'))
            quantity = int(data.get('quantity'))
            trade_type = str(data.get('type', '')).upper()

            # order object to help trace orders?
            
        except (Stock.DoesNotExist, ValueError):
            return Response({"error": "Invalid input."}, status=status.HTTP_400_BAD_REQUEST)

        # current_price = get_stock_price(stock.ticker) 

        if trade_type == 'BUY':
            return Response({"message": f"Successfully processed BUY order for {quantity} shares of {stock.ticker}."}, status=status.HTTP_200_OK)
        elif trade_type == 'SELL':
            return Response({"message": f"Successfully processed SELL order for {quantity} shares of {stock.ticker}."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid transaction type."}, status=status.HTTP_400_BAD_REQUEST)
