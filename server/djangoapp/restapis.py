import requests
import json
from django.http import JsonResponse
from .models import CarDealer
from requests.auth import HTTPBasicAuth
from django.views.decorators.csrf import csrf_exempt
from textblob import TextBlob


# Create a `get_request` to make HTTP GET requests
def get_dealers_from_db(**kwargs):
    # You can use **kwargs to pass additional parameters if needed
    # For example, you might use kwargs to filter data based on certain conditions
    dealers = CarDealer.objects.all()
    
    # Convert queryset to a list of dictionaries
    dealers_list = [{'id': dealer.id, 'short_name': dealer.short_name, 'other_field': dealer.state} for dealer in dealers]

    return dealers_list

def get_dealerships(request):
    if request.method == "GET":
        # You can pass additional parameters if needed (e.g., filtering criteria)
        dealerships_data = get_dealers_from_db()
        
        # Return the data as JSON response
        return JsonResponse(dealerships_data, safe=False)

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)

def post_request(request, *args, **kwargs):
    if request.method == "POST":
        try:
            # Assuming the request body contains JSON data
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # Validate and extract data
        short_name = data.get('short_name')
        state = data.get('state')

        # Validate required fields
        if not short_name or not state:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        # Create a new CarDealer instance and save it to the database
        new_dealer = CarDealer(short_name=short_name, state=state)
        new_dealer.save()

        return JsonResponse({'success': 'Dealer added successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list

def get_dealers_from_db(**kwargs):
    results = []
    
    # Retrieve CarDealer objects from the local database
    dealers = CarDealer.objects.all()

    for dealer in dealers:
        # Create a dictionary representation of the CarDealer object
        dealer_dict = {
            "address": dealer.address,
            "city": dealer.city,
            "full_name": dealer.full_name,
            "id": dealer.id,
            "lat": dealer.lat,
            "long": dealer.long,
            "short_name": dealer.short_name,
            "st": dealer.st,
            "zip": dealer.zip,
        }
        results.append(dealer_dict)

    return results


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_reviews_from_db(dealer_id):
    results = []

    # Retrieve reviews for the specified dealer_id from the local database
    reviews = DealerReview.objects.filter(dealer_id=dealer_id)

    for review in reviews:
        # Assuming you have a function analyze_review_sentiments that analyzes sentiment
        sentiment = analyze_review_sentiments(review.review)

        # Create a dictionary representation of the review and sentiment
        review_dict = {
            "review_id": review.id,
            "dealer_id": review.dealer_id,
            "user_name": review.user_name,
            "review": review.review,
            "sentiment": sentiment,
        }
        results.append(review_dict)

    return results

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative

def analyze_review_sentiments(review_text):
    # Create a TextBlob object with the review text
    blob = TextBlob(review_text)

    # Get the sentiment polarity and subjectivity
    sentiment_polarity = blob.sentiment.polarity

    # Determine sentiment based on polarity
    if sentiment_polarity > 0:
        sentiment = "Positive"
    elif sentiment_polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Return the sentiment analysis results
    return {
        "sentiment": sentiment,
        "polarity": sentiment_polarity,
    }
