# myapp/management/commands/fetch_data.py
import requests
from django.core.management.base import BaseCommand
from home.models import Product

class Command(BaseCommand):
    help = 'Fetch data from API and store in the database'

    def handle(self, *args, **kwargs):
        # Replace 'API_URL' with the actual API endpoint
        api_url = 'https://fakestoreapi.com/products'

        # Fetch data from the API
        response = requests.get(api_url)
        data = response.json()

        # Save data to the database
        for product_data in data:
            Product.objects.create(
                id=product_data['id'],
                title=product_data['title'],
                price=product_data['price'],
                description=product_data['description'],
                category=product_data['category'],
                image=product_data['image'],
                rate=product_data['rating']['rate'],
                count=product_data['rating']['count'],
            )

        self.stdout.write(self.style.SUCCESS('Data fetched and stored successfully.'))
