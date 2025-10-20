from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BrokerageAccount, Transaction, Stock, Order, Trade
from .serializers import BrokerageAccountSerializer, TransactionSerializer, StockSerializer, OrderSerializer, TradeSerializer
from decimal import Decimal

def dashboard_view(request):
    return render(request, 'customer/dashboard.html')

class BrokerageAccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BrokerageAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BrokerageAccount.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def trade(self, request):
        user_account = self.get_queryset().first()
        if not user_account:
            return Response({"error": "Account not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        ticker = request.data.get('ticker')
        trade_type = request.data.get('type', '').upper()
        quantity = request.data.get('quantity')

        try:
            stock = Stock.objects.get(ticker=ticker)
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be positive.")
        except (Stock.DoesNotExist, ValueError):
            return Response({"error": "Invalid stock ticker or quantity"}, status=status.HTTP_400_BAD_REQUEST)

        current_price = stock.current_price
        total_cost = Decimal(current_price) * quantity

        if trade_type == 'BUY':
            if user_account.cash_balance < total_cost:
                return Response({"error": "Not enough cash!"}, status=status.HTTP_400_BAD_REQUEST)
            user_account.cash_balance -= total_cost
            user_account.save()

            order = Order.objects.create(
                account=user_account,
                stock=stock,
                action='BUY',
                quantity=quantity,
                status='Executed'
            )
            Trade.objects.create(
                order=order,
                executed_price=current_price,
                executed_qty=quantity,
            )

            return Response({
                "message": f"Purchased {quantity} shares of {stock.ticker} at ${current_price}.",
                "order_id": order.id
            }, status=200)

        elif trade_type == 'SELL':
            user_account.cash_balance += total_cost
            user_account.save()

            order = Order.objects.create(
                account=user_account,
                stock=stock,
                action='SELL',
                quantity=quantity,
                status='Executed'
            )
            Trade.objects.create(
                order=order,
                executed_price=current_price,
                executed_qty=quantity,
            )

            return Response({
                "message": f"SELL {quantity} shares of {stock.ticker} at ${current_price}.",
                "order_id": order.id
            }, status=200)

        return Response({"error": "Not a valid trade type!"}, status=status.HTTP_400_BAD_REQUEST)

class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(account__user=self.request.user)


class TradeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trade.objects.all().order_by('-executed_time')
    serializer_class = TradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trade.objects.filter(order__account__user=self.request.user)