from django.db import models
from django.utils.timezone import now


# Create your models here.
class Dealership(models.Model):
    _id = models.CharField(max_length=50)
    _rev = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    st = models.CharField(max_length=2)
    address = models.TextField()
    zip = models.CharField(max_length=10)
    lat = models.FloatField()
    long = models.FloatField()
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.short_name} ({self.city}, {self.state})"




class Review(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=255)
    dealership = models.IntegerField()
    review = models.TextField()
    purchase = models.BooleanField()
    purchase_date = models.DateField()
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.car_make} {self.car_model} ({self.car_year})"
# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    carmake_id = models.CharField(max_length=2)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    carmake = models.ForeignKey(CarMake, null= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, primary_key=True)
    id = models.CharField(max_length=2)
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    OTHERS = 'others'
    CAR_CHOICES = [(SEDAN, "Sedan"), (SUV, 'SUV'), (WAGON, 'Wagon'), (OTHERS, 'Others')]
    type = models.CharField(null= False, max_length=20, choices= CAR_CHOICES, default=SEDAN)
    year = models.DateField(null=True)

    def __str__(self):
        return self.name



# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name



# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        # Dealership
        self.dealership = dealership
        # Dealer name
        self.name = name
        # Dealer purchase
        self.purchase = purchase
        # Dealer review
        self.review = review
        # purchase_date
        self.purchase_date = purchase_date
        # car_make
        self.car_make = car_make
        # car_model
        self.car_model = car_model
        # car_year
        self.car_year = car_year
        # sentiment
        self.sentiment = sentiment
        # id
        self.id = id

    def __str__(self):
        return "Dealer name: " +  self.full_name
