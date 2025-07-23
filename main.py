import json
import os
from dotenv import load_dotenv
from top_restaurants import get_top_restaurants

def main():
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("GOOGLE_PLACES_API_KEY")

    if not api_key:
        print("API key not found. Please set it in the .env file.")
        return

    city = input("Enter the name of the city: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    top_restaurants = get_top_restaurants(city, api_key)

    if top_restaurants:
        try:
            with open('top_restaurants.json', 'w', encoding='utf-8') as f:
                json.dump(top_restaurants, f, ensure_ascii=False, indent=4)
            print("Top restaurants data saved to 'top_restaurants.json'.")
        except IOError as e:
            print(f"Failed to write file: {e}")

if __name__ == "__main__":
    main()
