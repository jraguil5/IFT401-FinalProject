import random
from decimal import Decimal, ROUND_HALF_UP
from django.core.management.base import BaseCommand
from django.db import transaction, models
from customer.models import Stock, PriceTick 

class Command(BaseCommand):
    help = "Randomly adjust stock prices and create a corresponding PriceTick entry for each."

    def handle(self, *args, **options):
    
    with transaction.atomic():
        stocks = Stock.objects.all()

        if not stocks.exists():
            self.stdout.write(self.style.WARNING(
                "No stocks were found in the database. Maybe you forgot to set the initial data?"
            ))
            return

        try:
            last_tick = PriceTick.objects.aggregate(models.Max("id"))["id__max"]
            next_tick_id = (last_tick or 5000000000) + 1
        except Exception as err:
            self.stderr.write(self.style.ERROR(
                f"Could not fetch max tick ID due to error: {err}. Falling back to default ID start."
            ))
            next_tick_id = 5000000001

        created_ticks = [] 

        for stock in stocks:
            current_price = stock.current_price
            change_factor = Decimal(random.uniform(-0.005, 0.005)) 
            new_price = current_price * (1 + change_factor)

            new_price = max(new_price, Decimal("0.01")).quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

            stock.current_price = new_price
            stock.save()

            tick = PriceTick(
                id=next_tick_id,
                stock=stock,
                price=new_price
            )
            created_ticks.append(tick)
            next_tick_id += 1  

        if created_ticks:
            PriceTick.objects.bulk_create(created_ticks)

        first_id = next_tick_id - len(created_ticks)
        last_id = next_tick_id - 1
        self.stdout.write(self.style.SUCCESS(
            f"Updated {len(stocks)} stocks and created {len(created_ticks)} PriceTicks "
            f"(IDs {first_id} to {last_id})."
        ))

