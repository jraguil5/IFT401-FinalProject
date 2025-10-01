from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ticker_symbol = models.CharField(max_length=10, unique=True)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    initial_volume = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker_symbol} ({self.name})"
