from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
from djangoapp.models import Dealership
from djangoapp.models import Review
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...
def about(request):
    return render(request,'djangoapp/about.html')

# Create a `contact` view to return a static contact page
#def contact(request):
def contact(request):
    return render(request,'djangoapp/contact.html')


def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # If not, return to login page again
            return render(request, 'djangoapp/index.html', context)
    else:
        return render(request, 'djangoapp/index.html', context)

# ...

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}    
    if request.method == 'GET':
        return render(request,'djangoapp/registration.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            return redirect("djangoapp:login")

# Update the `get_dealerships` view to render the index page with a list of dealerships

def get_dealerships(request):
    if request.method == "GET":
        context = {}
        
        # Get dealers from the local Django database
        context["dealerships"] = Dealership.objects.all()

        # If you want to retrieve specific data, you can filter accordingly, for example:
        # context["dealerships"] = Dealership.objects.filter(state='Texas')

        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...




def get_dealer_details(request, dealer_id):
    context = {}
    if request.method == "GET":
        # Assuming you have a Dealer model
        dealer = get_object_or_404(Dealership, id=dealer_id)
        
        # Assuming you have a Review model with a foreign key to Dealer
        reviews = Review.objects.filter(dealership=dealer.id)
        
        context = {
            "dealer": dealer,
            "reviews": reviews,
        }

        return render(request, 'djangoapp/dealer_details.html', context)




# View to submit a new review
def add_review(request, dealer_id):
    if request.user.is_authenticated:
        if request.method == "GET":
            # Assuming you have a Dealer model
            dealer = get_object_or_404(Dealer, id=dealer_id)
            
            # Assuming you have a CarModel model
            cars = CarModel.objects.all()
            
            context = {
                "cars": cars,
                "dealer": dealer,
            }
            return render(request, 'djangoapp/add_review.html', context)

        if request.method == "POST":
            form = request.POST
            review = dict()
            review["name"] = f"{request.user.first_name} {request.user.last_name}"
            review["dealership"] = dealer_id
            review["review"] = form["content"]
            review["purchase"] = form.get("purchasecheck")
            
            if review["purchase"]:
                purchase_date = form.get("purchasedate")
                if purchase_date:
                    review["purchase_date"] = datetime.strptime(purchase_date, "%m/%d/%Y").isoformat()
            else:
                review["purchase_date"] = None

            car_id = form["car"]
            car = get_object_or_404(CarModel, pk=car_id)
            review["car_make"] = car.car_make.name
            review["car_model"] = car.name
            review["car_year"] = car.year

            # Assuming you have a Review model
            Review.objects.create(**review)

            return redirect("djangoapp:dealer_details", dealer_id=dealer_id)

    else:
        # If user isn't logged in, redirect to login page
        print("User must be authenticated before posting a review. Please log in.")
        return redirect("/djangoapp/login")
