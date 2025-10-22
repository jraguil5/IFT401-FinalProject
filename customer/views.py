from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BrokerageAccount, CustomUser, Transaction, Stock, Order, Trade, Position
from .serializers import BrokerageAccountSerializer, TransactionSerializer, StockSerializer, OrderSerializer, TradeSerializer
from .forms import UserRegistrationForm
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

        current_price = Decimal(stock.current_price)
        total_cost = current_price * Decimal(quantity)

        try:
            with transaction.atomic():
                if trade_type == 'BUY':
                    if user_account.cash_balance < total_cost:
                        return Response({"error": "Not enough cash!"}, status=status.HTTP_400_BAD_REQUEST)
                    
                    user_account.cash_balance -= total_cost
                    user_account.save()

                    position, created = Position.objects.get_or_create(
                        account=user_account,
                        stock=stock,
                        defaults={'quantity': 0}
                    )
                    
                    position.quantity += quantity
                    position.save() 

                    order = Order.objects.create(
                        account=user_account,
                        stock=stock,
                        action='BUY',
                        quantity=quantity,
                        status='Filled'
                    )
                    Trade.objects.create(
                        order=order,
                        executed_price=current_price,
                        executed_qty=quantity,
                    )

                    Transaction.objects.create(
                    account=user_account,
                    transaction_type=trade_type,
                    amount=total_cost
                    )

                    return Response({
                        "message": f"Purchased {quantity} shares of {stock.ticker} at ${current_price}",
                        "new_cash": str(user_account.cash_balance)
                    }, status=status.HTTP_200_OK)

                elif trade_type == 'SELL':
                    try:
                        position = Position.objects.get(account=user_account, stock=stock)
                    except Position.DoesNotExist:
                        return Response({"error": f"You don't own any {stock.ticker}"}, status=status.HTTP_400_BAD_REQUEST)

                    if position.quantity < quantity:
                        return Response({"error": f"Not enough shares to sell!"}, status=status.HTTP_400_BAD_REQUEST)

                    user_account.cash_balance += total_cost
                    user_account.save()
                    
                    position.quantity -= quantity
                    
                    if position.quantity == 0:
                        position.delete()
                    else:
                        position.save()

                    order = Order.objects.create(
                        account=user_account,
                        stock=stock,
                        action='SELL',
                        quantity=quantity,
                        status='Filled'
                    )
                    Trade.objects.create(
                        order=order,
                        executed_price=current_price,
                        executed_qty=quantity,
                    )

                    Transaction.objects.create(
                    account=user_account,
                    transaction_type=trade_type,
                    amount=total_cost
                    )

                    return Response({
                        "message": f"Sold {quantity} shares of {stock.ticker} at ${current_price}",
                        "new_cash": str(user_account.cash_balance)
                    }, status=status.HTTP_200_OK)

                return Response({"error": "Invalid trade type"}, status=status.HTTP_400_OK)

        except Exception as e:
            return Response({"error": "Transaction failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
    
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                CustomUser.objects.create_user(
                    UserName=form.cleaned_data['UserName'],
                    email=form.cleaned_data['email'],
                    FullName=form.cleaned_data['FullName'],
                    Role='CUSTOMER', 
                    password=form.cleaned_data['password']
                )
                messages.success(request, 'Registration successful! You may now sign in.')
                return redirect('login')
            except Exception as e:
                messages.error(request, 'Registration failed. Username or email may already exist.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'customer/registration/register.html', {'form': form})