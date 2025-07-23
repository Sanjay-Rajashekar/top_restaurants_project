import requests

def validate_city(city, api_key):
    """
    Uses Places API Find Place to validate if city exists.
    Returns True if valid, else False.
    """
    endpoint_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        'input': city,
        'inputtype': 'textquery',
        'fields': 'formatted_address',
        'key': api_key
    }

    try:
        response = requests.get(endpoint_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        candidates = data.get("candidates", [])
        if not candidates:
            return False
        return True

    except requests.exceptions.RequestException as err:
        print(f"Validation request failed: {err}")
        return False

def get_top_restaurants(city, api_key):
    """
    Fetches top 10 restaurants for a valid city using Google Places API.
    """
    if not city.strip():
        print("City name cannot be empty.")
        return {}

    # Validate city first
    if not validate_city(city, api_key):
        print("No result found for the given location, please enter the location correctly.")
        return {}

    search_query = f"restaurants in {city}"
    endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {'query': search_query, 'type': 'restaurant', 'key': api_key}

    try:
        response = requests.get(endpoint_url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if 'error_message' in data:
            print(f"API Error: {data['error_message']}")
            return {}

        results = data.get("results", [])
        if not results:
            print(f"No restaurants found in {city}.")
            return {}

        restaurants = {}
        for restaurant in results[:10]:
            name = restaurant.get("name", "N/A")
            rating = restaurant.get("rating", "N/A")
            user_ratings_total = restaurant.get("user_ratings_total", "N/A")
            address = restaurant.get("formatted_address", "N/A")

            restaurants[name] = {
                "rating": rating,
                "total_reviews": user_ratings_total,
                "address": address
            }

        return restaurants

    except requests.exceptions.ConnectionError:
        print("No internet connection. Please check your network and try again.")
        return {}
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
        return {}
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return {}
    except requests.exceptions.RequestException as err:
        print(f"Request failed: {err}")
        return {}
