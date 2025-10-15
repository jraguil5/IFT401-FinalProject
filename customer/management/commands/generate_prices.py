import random
from django.core.management.base import BaseCommand
from django.db import transaction, models
from decimal import Decimal, ROUND_HALF_UP

# Import your models
from customer.models import Stock, PriceTick 

class Command(BaseCommand):
    help = 'Generates new random stock prices for all stocks and creates a PriceTick record.'

    def handle(self, *args, **options):
        # All database operations must be inside the transaction block
        with transaction.atomic(): 
            stocks = Stock.objects.all()
            
            if not stocks:
                self.stdout.write(self.style.WARNING("No stocks found to update. Please add initial stock data."))
                return # Exit the command if no stocks are found

            try:
                # Find the current maximum TickID in the table using the imported 'models'
                max_tick_id = PriceTick.objects.all().aggregate(models.Max('id'))['id__max']
                # Start the sequence one greater than the max ID, or a high default if the table is empty
                next_id = (max_tick_id or 5000000000) + 1 
            except Exception as e:
                # Fallback and logging for integrity/connection issues
                self.stderr.write(self.style.ERROR(f"Error determining max TickID: {e}. Using default start ID."))
                next_id = 5000000001

            new_price_ticks = []
            
            for stock in stocks:
                current_price = stock.current_price
                
                # Generate a small, random change percentage 
                change_percent = Decimal(random.uniform(-0.005, 0.005))
                new_price = current_price * (1 + change_percent)
                
                # Ensure price is non-negative and round to 2 decimal places
                new_price = max(new_price, Decimal('0.01')).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
                
                # Update Stock Record (Saves immediately within the atomic block)
                stock.current_price = new_price
                stock.save()
                
                tick = PriceTick(
                    id=next_id,         
                    stock=stock,
                    price=new_price
                )
                new_price_ticks.append(tick)
                next_id += 1 
                
            # Bulk create all PriceTick records
            PriceTick.objects.bulk_create(new_price_ticks)
            
            self.stdout.write(self.style.SUCCESS(
                f'Successfully updated prices for {len(stocks)} stocks and created {len(new_price_ticks)} price ticks (IDs {next_id - len(stocks)} to {next_id - 1}).'
            ))