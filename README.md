## 📝 Top Restaurants Finder

---

## 🚀 Problem Statement

Develop a Python script that:

1. Prompts the user to enter the name of a city  
2. Retrieves the top 10 restaurants in that city based on food, comparing ratings and reviews through Google search (implemented using Google Places API)  
3. Stores the data in a JSON file, using restaurant names as keys and their ratings, total reviews, and addresses as values

---

## 💡 Approach

1. **Input:** Prompt user for city name  
2. **Validation:** Verify if the city exists using Google Places Find Place API  
3. **Retrieval:** If valid, fetch top 10 restaurants using Places Text Search API  
4. **Storage:** Save results in `top_restaurants.json` with a structured schema  
5. **Edge Cases Handled:**
   - Empty input
   - Invalid city input
   - No internet connection
   - API errors (quota exceeded, invalid key, etc.)
   - No restaurants found in a valid city
   - File write failures

---

## 🔧 Setup Instructions

1. Clone the repository

```bash
git clone <repo-link>
cd top_restaurants_project
```

2. Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.
```

4. Create a .env file and add your Google Places API key:

GOOGLE_PLACES_API_KEY=your_api_key_here

---

## ▶️ How to Run

```bash
python main.py
```

✅ The script will prompt:

```bash
Enter the name of the city:
```

💾 Outputs are saved in top_restaurants.json.

✅ How to Run Tests

```bash
python -m pytest test_get_restaurants.py
```

✔️ Tests include:

    - City validation success and failure
    - Successful restaurant retrieval
    - Invalid city input handling
    - No internet connection handling

---

## ⚠️ Limitations

    Accuracy depends on Google Places data

    Food type filtering (e.g. vegetarian only) is not implemented but can be added as a query parameter enhancement

    Rate limits apply based on your API key quota
---

## 🚀 Possible Improvements

    Implement CLI arguments for food type filters

    Store results in a database for persistent analysis

    Add logging instead of print statements for production readiness

---
## 👨‍💻 Author
Sanjay Rajashekar