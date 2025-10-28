import random
from decimal import Decimal, ROUND_HALF_UP
from django.core.management.base import BaseCommand
from django.db import transaction, models
from customer.models import Stock, PriceTick

class Command(BaseCommand):
    help = "Update stock prices with random changes"

    def handle(self, *args, **options):
        with transaction.atomic():
            stocks = Stock.objects.all()
            
            if not stocks.exists():
                self.stdout.write("No stocks found")
                return
            
            last_tick = PriceTick.objects.aggregate(models.Max("id"))["id__max"]
            next_tick_id = (last_tick or 5_000_000_000) + 1
            
            ticks = []
            
            for stock in stocks:
                # ±0.5% change
                factor = Decimal(str(random.uniform(-0.005, 0.005)))
                new_price = stock.current_price * (1 + factor)
                new_price = max(new_price, Decimal("0.01")).quantize(Decimal(".01"), rounding=ROUND_HALF_UP)
                
                stock.current_price = new_price
                stock.save(update_fields=["current_price"])
                
                ticks.append(PriceTick(
                    id=next_tick_id,
                    stock=stock,
                    price=new_price
                ))
                next_tick_id += 1
            
            PriceTick.objects.bulk_create(ticks)
            
            self.stdout.write(
                f"Updated {len(stocks)} stocks, created {len(ticks)} ticks"
            )
