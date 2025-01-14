import json
from django.core.management.base import BaseCommand
from djangoapp.models import Review

class Command(BaseCommand):
    help = 'Populate the Review model with sample data'

    def handle(self, *args, **options):
        # Sample JSON data (replace this with your actual JSON data)
        json_data = [
            {
                "_id": "459d89f48acfae5cb2d0af0ebe6c1c51",
                "_rev": "1-6d3a316e140863cdb147048888d26051",
                "id": 1,
                "name": "Berkly Shepley",
                "dealership": 1,
                "review": "Total grid-enabled service-desk",
                "purchase": True,
                "purchase_date": "2020-11-07",
                "car_make": "Audi",
                "car_model": "A6",
                "car_year": 2010
            },
            {
                "_id": "459d89f48acfae5cb2d0af0ebe6c21d0",
                "_rev": "1-0cbc084ce570374a1d0c2653ceb254ad",
                "id": 2,
                "name": "Gwenora Zettoi",
                "dealership": 2,
                "review": "Future-proofed foreground capability",
                "purchase": True,
                "purchase_date": "2020-09-17",
                "car_make": "Pontiac",
                "car_model": "Firebird",
                "car_year": 1995
            },
            {
                "_id": "459d89f48acfae5cb2d0af0ebe6c3013",
                "_rev": "1-278e31d48be2f5abc7c9b542cff00208",
                "id": 3,
                "name": "Lion Reames",
                "dealership": 3,
                "review": "Expanded global groupware",
                "purchase": True,
                "purchase_date": "2020-10-10",
                "car_make": "Mazda",
                "car_model": "MX-5",
                "car_year": 2003
            },
            {
                "_id": "459d89f48acfae5cb2d0af0ebe6c3598",
                "_rev": "1-1677bbc642e9673d151d56614ad81963",
                "id": 4,
                "name": "Iorgos Colley",
                "dealership": 3,
                "review": "Optional heuristic software",
                "purchase": False
            },
            {
                "_id": "459d89f48acfae5cb2d0af0ebe6c378c",
                "_rev": "1-7e446087190b20656bad81aeab9242b5",
                "id": 5,
                "name": "Kissee Noirel",
                "dealership": 3,
                "review": "Diverse client-server success",
                "purchase": False
            }
            
            # Add more data as needed
        ]

        # Clear existing data
        Review.objects.all().delete()

        for data in json_data:
            try:
                purchase_date = data['purchase_date']
            except KeyError:
                purchase_date = '2020-01-01'

        for data in json_data:
            try:
                car_make=data['car_make']
            except KeyError:
                car_make = 'Random'

        for data in json_data:
            try:
                car_model=data['car_model']
            except KeyError:
                car_model = 'Random'

        for data in json_data:
            try:
                car_year=data['car_year']
            except KeyError:
                car_year = 2000

        # Populate the database with sample data
        for data in json_data:
            Review.objects.create(
                id=data['_id'],
                name=data['name'],
                dealership=data['dealership'],
                review=data['review'],
                purchase=data['purchase'],
                purchase_date=purchase_date,
                car_make=car_make,
                car_model=car_model,
                car_year=car_year
            )

        self.stdout.write(self.style.SUCCESS('Sample review data has been successfully populated.'))
