from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.utils.translation import gettext_lazy as _

# ==============================================================================
# 1. Custom User Manager
# ==============================================================================

class CustomUserManager(BaseUserManager): 
    """
    Custom manager for the CustomUser model where email and username are the unique identifiers.
    This manager handles the custom required fields (FullName, Role).
    """
    def create_user(self, username, email, FullName, Role, password=None, **extra_fields):
        if not username:
            raise ValueError(_('The given username must be set'))
        
        # Pop standard AbstractUser flags that are set to None in the model definition
        is_active = extra_fields.pop('is_active', True)
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)

        # Instantiate the model with required custom fields
        user = self.model(
            UserName=username,
            email=email, 
            FullName=FullName,
            Role=Role,
            **extra_fields 
        )
        
        if password:
            user.set_password(password)
        
        # Manually set the standard flags
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, FullName, Role, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        # Ensures necessary superuser flags are set before calling create_user
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self.create_user( 
            username=username,
            email=email,
            FullName=FullName,
            Role=Role,
            password=password,
            **extra_fields
        )

# ------------------------------------------------------------------------------
# 2. Custom User Model
# ------------------------------------------------------------------------------

class CustomUser(AbstractUser):
    # Field definitions matching external MySQL schema (BIGINT and db_column)
    UserID = models.BigIntegerField(db_column='UserID', primary_key=True)

    FullName = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)
    UserName = models.CharField(db_column='UserName', unique=True, max_length=50, blank=True, null=True)
    
    # Python field 'email' maps to DB column 'Email'
    email = models.CharField(db_column='Email', unique=True, max_length=100, blank=True, null=True)

    password = models.CharField(db_column='PasswordHash', max_length=255) 
    
    ROLE_CHOICES = [("CUSTOMER", "Customer"), ("ADMIN", "Admin")]
    Role = models.CharField(db_column='Role', max_length=20, 
                            choices=ROLE_CHOICES, 
                            default="CUSTOMER", blank=True, null=True)

    USERNAME_FIELD = 'UserName'
    REQUIRED_FIELDS = ['FullName', 'Role']
    
    # Explicitly assign the custom manager
    objects = CustomUserManager() 

    # Override AbstractUser fields that do not exist in the external database
    username = None 
    last_login = None 
    date_joined = None
    is_superuser = None
    is_staff = None
    is_active = None
    groups = None
    user_permissions = None
    first_name = None 
    last_name = None
    
    class Meta:
        db_table = 'User' 
        # Crucial setting for mapping to an existing database
        managed = False
        
    def __str__(self):
         return self.UserName or str(self.UserID)

# ------------------------------------------------------------------------------
# 3. Stock Model
# ------------------------------------------------------------------------------

class Stock(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='StockID')
    ticker = models.CharField(max_length=10, unique=True, db_column='Ticker')
    name = models.CharField(max_length=100, db_column='CompanyName')
    initial_price = models.DecimalField(max_digits=12, decimal_places=2, db_column='InitialPrice')
    current_price = models.DecimalField(max_digits=12, decimal_places=2, db_column='CurrentPrice')
    opening_price = models.DecimalField(max_digits=12, decimal_places=2, db_column='OpeningPrice')
    day_high = models.DecimalField(max_digits=12, decimal_places=2, db_column='DayHigh')
    day_low = models.DecimalField(max_digits=12, decimal_places=2, db_column='DayLow')
    float_shares = models.BigIntegerField(db_column='FloatShares')
    
    class Meta:
        db_table = 'Stock'
        managed = False
        
    def __str__(self):
        return self.ticker

# ------------------------------------------------------------------------------
# 4. Brokerage Account Model
# ------------------------------------------------------------------------------

class BrokerageAccount(models.Model):
    AccountID = models.BigIntegerField(primary_key=True, db_column='AccountID')
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name="account",
        db_column='UserID'
    )
    cash_balance = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0.00,
        db_column='Balance'
    )
    
    class Meta:
        db_table = 'BrokerageAccount'
        managed = False

# ------------------------------------------------------------------------------
# 5. Price Tick Model
# ------------------------------------------------------------------------------

class PriceTick(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='TickID') 
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='price_ticks', db_column='StockID')
    timestamp = models.DateTimeField(auto_now_add=True, db_column='Timestamp')
    price = models.DecimalField(max_digits=12, decimal_places=2, db_column='Price')
    
    class Meta:
        db_table = 'PriceTick' 
        managed = False
        ordering = ['-timestamp'] 

# ------------------------------------------------------------------------------
# 6. Position Model
# ------------------------------------------------------------------------------

class Position(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='PositionID')
    account = models.ForeignKey(BrokerageAccount, on_delete=models.CASCADE, related_name="positions", db_column='AccountID')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, db_column='StockID')
    quantity = models.BigIntegerField(db_column='Quantity')
    
    class Meta:
        db_table = 'Position' 
        managed = False
        unique_together = ("account", "stock")

# ------------------------------------------------------------------------------
# 7. Transaction Model
# ------------------------------------------------------------------------------

class Transaction(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='TransactionID')
    account = models.ForeignKey(BrokerageAccount, on_delete=models.CASCADE, related_name="transactions", db_column='AccountID')
    
    TRANSACTION_TYPES = [("BUY", "Buy"), ("SELL", "Sell")]
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES, db_column='TransType')
    price_at_transaction = models.DecimalField(max_digits=12, decimal_places=2, db_column='Amount')

    class Meta:
        db_table = 'Transaction'
        managed = False

# ------------------------------------------------------------------------------
# 8. Order Model
# ------------------------------------------------------------------------------

class Order(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='OrderID')
    account = models.ForeignKey(BrokerageAccount, on_delete=models.CASCADE, related_name="orders", db_column='AccountID')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, db_column='StockID')
    
    ORDER_ACTIONS = [("BUY", "Buy"), ("SELL", "Sell")]
    action = models.CharField(max_length=10, choices=ORDER_ACTIONS, db_column='Action')
    quantity = models.BigIntegerField(db_column='Quantity')
    status = models.CharField(max_length=20, db_column='Status')
    created_at = models.DateTimeField(auto_now_add=True, db_column='CreatedAt')
    executed_at = models.DateTimeField(null=True, blank=True, db_column='ExecutedAt')
    
    class Meta:
        db_table = 'Order' 
        managed = False

# ------------------------------------------------------------------------------
# 9. Trade Model
# ------------------------------------------------------------------------------

class Trade(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='TradeID')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="trades", db_column='OrderID')
    executed_price = models.DecimalField(max_digits=12, decimal_places=2, db_column='ExecutedPrice')
    executed_qty = models.BigIntegerField(db_column='ExecutedQty')
    executed_time = models.DateTimeField(auto_now_add=True, db_column='ExecutedTime')
    
    class Meta:
        db_table = 'Trade'
        managed = False

# ------------------------------------------------------------------------------
# 10. Market Schedule Model
# ------------------------------------------------------------------------------

class MarketSchedule(models.Model):
    ScheduleID = models.BigIntegerField(primary_key=True, db_column='ScheduleID') 
    status = models.CharField(max_length=10, db_column='Status')
    open_hour = models.IntegerField(db_column='OpenHour')
    open_minute = models.IntegerField(db_column='OpenMinute')
    close_hour = models.IntegerField(db_column='CloseHour')
    close_minute = models.IntegerField(db_column='CloseMinute')
    holiday = models.BooleanField(default=False, db_column='Holiday')
    
    class Meta:
        db_table = 'MarketSchedule'
        managed = False