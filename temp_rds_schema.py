# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brokerageaccount(models.Model):
    accountid = models.BigIntegerField(db_column='AccountID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BrokerageAccount'


class Marketschedule(models.Model):
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    openhour = models.IntegerField(db_column='OpenHour', blank=True, null=True)  # Field name made lowercase.
    openminute = models.IntegerField(db_column='OpenMinute', blank=True, null=True)  # Field name made lowercase.
    closehour = models.IntegerField(db_column='CloseHour', blank=True, null=True)  # Field name made lowercase.
    closeminute = models.IntegerField(db_column='CloseMinute', blank=True, null=True)  # Field name made lowercase.
    holiday = models.IntegerField(db_column='Holiday', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarketSchedule'


class Order(models.Model):
    orderid = models.BigIntegerField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Brokerageaccount, models.DO_NOTHING, db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    stockid = models.ForeignKey('Stock', models.DO_NOTHING, db_column='StockID', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    quantity = models.BigIntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    executedat = models.DateTimeField(db_column='ExecutedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'


class Position(models.Model):
    positionid = models.BigIntegerField(db_column='PositionID', primary_key=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Brokerageaccount, models.DO_NOTHING, db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    stockid = models.ForeignKey('Stock', models.DO_NOTHING, db_column='StockID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.BigIntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Position'
        unique_together = (('accountid', 'stockid'),)


class Pricetick(models.Model):
    tickid = models.BigIntegerField(db_column='TickID', primary_key=True)  # Field name made lowercase.
    stockid = models.ForeignKey('Stock', models.DO_NOTHING, db_column='StockID', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriceTick'


class Stock(models.Model):
    stockid = models.BigIntegerField(db_column='StockID', primary_key=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='Ticker', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    initialprice = models.DecimalField(db_column='InitialPrice', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currentprice = models.DecimalField(db_column='CurrentPrice', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    openingprice = models.DecimalField(db_column='OpeningPrice', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dayhigh = models.DecimalField(db_column='DayHigh', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    daylow = models.DecimalField(db_column='DayLow', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    floatshares = models.BigIntegerField(db_column='FloatShares', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stock'


class Trade(models.Model):
    tradeid = models.BigIntegerField(db_column='TradeID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    executedprice = models.DecimalField(db_column='ExecutedPrice', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    executedqty = models.BigIntegerField(db_column='ExecutedQty', blank=True, null=True)  # Field name made lowercase.
    executedtime = models.DateTimeField(db_column='ExecutedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trade'


class Transaction(models.Model):
    transactionid = models.BigIntegerField(db_column='TransactionID', primary_key=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Brokerageaccount, models.DO_NOTHING, db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    transtype = models.CharField(db_column='TransType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transaction'


class User(models.Model):
    userid = models.BigIntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.CharField(db_column='PasswordHash', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
