import json
from django.core.management.base import BaseCommand
from djangoapp.models import Dealership

class Command(BaseCommand):
    help = 'Populate the Dealership model with sample data'

    def handle(self, *args, **options):
        # Sample JSON data (replace this with your actual JSON data)
        json_data = [
            {
                "_id": "e6440eb3c0aec67832bb3d074cbeb309",
                "_rev": "1-34e7ebd07643af43db578a46ee1d6365",
                "id": 1,
                "city": "El Paso",
                "state": "Texas",
                "st": "TX",
                "address": "3 Nova Court",
                "zip": "88563",
                "lat": 31.6948,
                "long": -106.3,
                "short_name": "Holdlamis",
                "full_name": "Holdlamis Car Dealership"
            },
            {
                "_id": "e6440eb3c0aec67832bb3d074cbeba81",
                "_rev": "1-d1778a396ca8cb0ef2966a9854eb93ee",
                "id": 2,
                "city": "Minneapolis",
                "state": "Minnesota",
                "st": "MN",
                "address": "6337 Butternut Crossing",
                "zip": "55402",
                "lat": 44.9762,
                "long": -93.2759,
                "short_name": "Temp",
                "full_name": "Temp Car Dealership"
            },
            {
                "_id": "e6440eb3c0aec67832bb3d074cbec28c",
                "_rev": "1-cc5d5c13aa879d1cef8253dfa1dce77d",
                "id": 3,
                "city": "Birmingham",
                "state": "Alabama",
                "st": "AL",
                "address": "9477 Twin Pines Center",
                "zip": "35285",
                "lat": 33.5446,
                "long": -86.9292,
                "short_name": "Sub-Ex",
                "full_name": "Sub-Ex Car Dealership"
            },
            {
                "_id": "e6440eb3c0aec67832bb3d074cbed200",
                "_rev": "1-a79013b42c83451d49e7e3aba4a575e3",
                "id": 4,
                "city": "Dallas",
                "state": "Texas",
                "st": "TX",
                "address": "85800 Hazelcrest Circle",
                "zip": "75241",
                "lat": 32.6722,
                "long": -96.7774,
                "short_name": "Solarbreeze",
                "full_name": "Solarbreeze Car Dealership"
            },
            {
                "_id": "e6440eb3c0aec67832bb3d074cbed49e",
                "_rev": "1-c16dcd97a91588c9866814f61ea72751",
                "id": 5,
                "city": "Baltimore",
                "state": "Maryland",
                "st": "MD",
                "address": "93 Golf Course Pass",
                "zip": "21203",
                "lat": 39.2847,
                "long": -76.6205,
                "short_name": "Regrant",
                "full_name": "Regrant Car Dealership"
            }
            # Add more data as needed
        ]

        # Clear existing data
        Dealership.objects.all().delete()

        # Populate the database with sample data
        for data in json_data:
            Dealership.objects.create(
                _id=data['_id'],
                _rev=data['_rev'],
                id=data['id'],
                city=data['city'],
                state=data['state'],
                st=data['st'],
                address=data['address'],
                zip=data['zip'],
                lat=data['lat'],
                long=data['long'],
                short_name=data['short_name'],
                full_name=data['full_name']
            )

        self.stdout.write(self.style.SUCCESS('Sample data has been successfully populated.'))
