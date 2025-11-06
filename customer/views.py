import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from .models import BrokerageAccount, CustomUser, Transaction, Stock, Order, Trade, Position
from .serializers import BrokerageAccountSerializer, TransactionSerializer, StockSerializer, OrderSerializer, TradeSerializer
from .forms import UserRegistrationForm
from decimal import Decimal, InvalidOperation
from django.db.models import Max
from django.utils import timezone


def get_next_id(model_class, default_start):
    last_id = model_class.objects.aggregate(Max('id'))['id__max']
    return (last_id or default_start) + 1

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

                    next_order_id = get_next_id(Order, 2000000000)
                    next_trade_id = get_next_id(Trade, 3000000000)
                    next_transaction_id = get_next_id(Transaction, 4000000000)
                    next_position_id = get_next_id(Position, 5000000000)

                    position, created = Position.objects.get_or_create(
                        account=user_account,
                        stock=stock,
                        defaults={'quantity': 0, 'id': next_position_id}  
                    )
                    
                    position.quantity += quantity
                    position.save() 

                    order = Order.objects.create(
                        id=next_order_id,
                        account=user_account,
                        stock=stock,
                        action='BUY',
                        quantity=quantity,
                        status='Filled',
                        created_at=timezone.now(),
                        executed_at=timezone.now(),
                    )

                    Trade.objects.create(
                        id=next_trade_id,
                        order=order,
                        executed_price=current_price,
                        executed_qty=quantity,
                    )

                    Transaction.objects.create(
                    id=next_transaction_id,
                    account=user_account,
                    transaction_type='STOCK_TRADE',
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

                    #  Check if user has enough shares
                    if position.quantity < quantity:
                        return Response({"error": f"Not enough shares to sell!"}, status=status.HTTP_400_BAD_REQUEST)

                    user_account.cash_balance += total_cost
                    user_account.save()
                    
                    position.quantity -= quantity
                    
                    if position.quantity == 0:
                        position.delete()
                    else:
                        position.save()

                    next_order_id = get_next_id(Order, 2000000000)
                    next_trade_id = get_next_id(Trade, 3000000000)
                    next_transaction_id = get_next_id(Transaction, 4000000000)

                    order = Order.objects.create(
                        id=next_order_id,
                        account=user_account,
                        stock=stock,
                        action='SELL',
                        quantity=quantity,
                        status='Filled',
                        created_at=timezone.now(),
                        executed_at=timezone.now(),
                    )

                    Trade.objects.create(
                        id=next_trade_id,
                        order=order,
                        executed_price=current_price,
                        executed_qty=quantity,

                    )

                    Transaction.objects.create(
                    id=next_transaction_id,
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

    @action(detail=False, methods=['post'])
    def deposit(self, request):
        user_account = self.get_queryset().first()
        if not user_account:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)
        
        amount_str = request.data.get('amount')
        
        try:
            amount = Decimal(amount_str)
            if amount <= 0:
                return Response({'error': 'Deposit amount must be greater than $0.00.'}, status=status.HTTP_400_BAD_REQUEST)
        except (InvalidOperation, TypeError):
            return Response({'error': 'Invalid amount format provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                user_account.cash_balance += amount
                user_account.save()
                
                next_transaction_id = get_next_id(Transaction, 4000000000)

                Transaction.objects.create(
                    id=next_transaction_id,
                    account=user_account,
                    transaction_type='DEPOSIT',
                    amount=amount
                )
                
                new_cash_balance = user_account.cash_balance.quantize(Decimal('0.01'))
                
                return Response({
                    "message": f"Successfully deposited ${amount:.2f}.",
                    "new_cash": str(new_cash_balance)
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": "An internal error occurred during deposit."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def withdraw(self, request):
        user_account = self.get_queryset().first()
        if not user_account:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)
        
        amount_str = request.data.get('amount')
        
        try:
            amount = Decimal(amount_str)
            if amount <= 0:
                return Response({'error': 'Withdrawal amount must be greater than $0.00.'}, status=status.HTTP_400_BAD_REQUEST)
        except (InvalidOperation, TypeError):
            return Response({'error': 'Invalid amount format provided.'}, status=status.HTTP_400_BAD_REQUEST)
            
        if user_account.cash_balance < amount:
            return Response({"error": "Insufficient cash balance for withdrawal."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                user_account.cash_balance -= amount
                user_account.save()

                next_transaction_id = get_next_id(Transaction, 4000000000)

                Transaction.objects.create(
                    id=next_transaction_id,
                    account=user_account,
                    transaction_type='WITHDRAW',
                    amount=amount
                )

                new_cash_balance = user_account.cash_balance.quantize(Decimal('0.01'))
                
                return Response({
                    "message": f"Successfully withdrew ${amount:.2f}.",
                    "new_cash": str(new_cash_balance)
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": "An internal error occurred during withdrawal."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
    
def is_admin(user):
    return user.is_staff or user.is_superuser

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser]) 
def admin_create_stock_api(request):
    data = {
        'name': request.data.get('company_name'),
        'ticker': request.data.get('ticker'),
        'current_price': request.data.get('current_price'),
        'float_shares': request.data.get('float_shares'),
    }

    serializer = StockSerializer(data=data)
    if serializer.is_valid():
        try:
            initial_price_value = data['current_price']
            next_stock_id = get_next_id(Stock, 1000000)

            stock_instance = serializer.save(
                id=next_stock_id,
                initial_price=initial_price_value,
                opening_price=initial_price_value,
                day_high=initial_price_value,
                day_low=initial_price_value
            )

            
            return Response({
                "success": True, 
                "message": f"Stock {stock_instance.ticker} created successfully.",
                "ticker": stock_instance.ticker
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": f"Database save failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    first_error_key = next(iter(serializer.errors))
    first_error_message = serializer.errors[first_error_key][0]
    
    return Response({"error": f"{first_error_key.capitalize()}: {first_error_message}"}, 
                    status=status.HTTP_400_BAD_REQUEST)

@user_passes_test(is_admin)
def admin_dashboard_view(request):
    return render(request, 'admin/admin_dashboard.html')

@user_passes_test(is_admin)
def admin_change_market_hours_view(request):
    return render(request, 'admin/admin_change_market_hours.html')

@user_passes_test(is_admin) 
def admin_create_stock_view(request):
    return render(request, 'admin/admin_create_stock.html')


def register_user(request):
    if request.method == 'POST':

        # json for API testing
        if 'application/json' in request.content_type:
            try:
                data = json.loads(request.body.decode('utf-8'))

                username = data.get('UserName') 
                email = data.get('email')
                full_name = data.get('FullName')
                role = data.get('Role', 'CUSTOMER') # Default role if not provided
                password = data.get('password')

                if not all([username, email, full_name, password]):
                    return JsonResponse({"error": "Missing required fields in JSON payload."}, status=400)
                
                with transaction.atomic():
                    CustomUser.objects.create_user(
                        UserName=username,
                        email=email,
                        FullName=full_name,
                        Role=role, 
                        password=password
                    )

                    return JsonResponse({"message": f"User {username} created successfully."}, status=status.HTTP_201_CREATED)
            
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON format."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return JsonResponse({"error": f"Registration failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        else:
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
                    return redirect('sign_in')
                except Exception as e:
                    messages.error(request, 'Registration failed. Username or email may already exist.')
            
            return render(request, 'customer/sign_up.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'customer/sign_up.html', {'form': form})


@login_required
def portfolio_view(request):
    user_account = BrokerageAccount.objects.filter(user=request.user).first()

    if not user_account:
        return render(request, 'customer/portfolio.html', {
            'account': None,
            'positions': [],
            'total_market_value': Decimal('0.00'),
            'total_equity': Decimal('0.00'),
        })
    
    positions = Position.objects.filter(account=user_account).select_related('stock')
    
    total_market_value = Decimal('0.00')
    
    positions_with_value = []
    for p in positions:
        p.market_value = Decimal(p.quantity) * Decimal(p.stock.current_price)
        total_market_value += p.market_value
        positions_with_value.append(p)

    total_equity = user_account.cash_balance + total_market_value if user_account else Decimal('0.00')

    context = {
        'account': user_account,
        'positions': positions_with_value, 
        'total_market_value': total_market_value,
        'total_equity': total_equity,
    }
    return render(request, 'customer/portfolio.html', context)

@login_required
def buy_stock_view(request):
    user_account = BrokerageAccount.objects.filter(user=request.user).first()
    all_stocks = Stock.objects.all().order_by('ticker')
    return render(request, 'customer/buy_stock.html', {'stocks': all_stocks, 'account': user_account})

@login_required
def sell_stock_view(request):
    user_account = BrokerageAccount.objects.filter(user=request.user).first()
    positions = Position.objects.filter(account=user_account).select_related('stock') if user_account else []

    context = {
        'account': user_account,
        'positions': positions
    }
    return render(request, 'customer/sell_stock.html', context)

@login_required
def deposit_cash_view(request):
    user_account = BrokerageAccount.objects.filter(user=request.user).first()
    context = {
        'account': user_account,
    }
    return render(request, 'customer/deposit_cash.html', context)

@login_required
def withdraw_cash_view(request):
    user_account = BrokerageAccount.objects.filter(user=request.user).first()
    context = {
        'account': user_account,
    }
    return render(request, 'customer/withdraw_cash.html', context)

@login_required
def role_based_redirect(request):
    user = request.user
    if user.is_staff or user.is_superuser:
        return redirect('admin_dashboard')
    else:
        return redirect('portfolio')
    
@login_required
def sign_out_user(request):
    logout(request)
    messages.success(request, 'You have been successfully signed out.')
    return redirect('sign_in')