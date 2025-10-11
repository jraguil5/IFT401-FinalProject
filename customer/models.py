from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    # Price will be generated externally in generator app

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="portfolio")
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Transaction(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="transactions")
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    transaction_type = models.CharField(max_length=4, choices=[("BUY", "Buy"), ("SELL", "Sell")])
    quantity = models.IntegerField()
    price_at_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

# Represents the stocks held in a portfolio
class Holding(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="holdings")
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ("portfolio", "stock")

