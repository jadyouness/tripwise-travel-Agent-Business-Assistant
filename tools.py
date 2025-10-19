# ================================
# 🛠️ Step 2: Tool Functions
# ================================
import os
import json
import datetime
import requests
from dotenv import load_dotenv

# ✅ Load API keys from .env
load_dotenv()

# =============================================================================
# TOOL 1: Record Customer Interest (Full Trip Info)
# =============================================================================
def record_customer_interest(name, gender, phone, email, destination, start_date, end_date,
                             budget, flight_company, activities, restaurant_type, weather_preferred):
    """
    Records detailed customer travel interest and saves it to a JSON file.
    - All fields are saved as strings to avoid type issues.
    """

    lead_data = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "customer_info": {
            "name": str(name),
            "gender": str(gender),
            "phone": str(phone),
            "email": str(email)
        },
        "trip_details": {
            "destination": str(destination),
            "start_date": str(start_date),
            "end_date": str(end_date),
            "budget": str(budget),
            "flight_company_preference": str(flight_company),
            "preferred_activities": str(activities),
            "restaurant_type": str(restaurant_type),
            "weather_preferred": str(weather_preferred)
        }
    }

    leads_file = "customer_leads.json"

    # ✅ Safely load existing leads or start a new list
    if os.path.exists(leads_file):
        with open(leads_file, 'r', encoding='utf-8') as f:
            try:
                leads = json.load(f)
            except json.JSONDecodeError:
                leads = []
    else:
        leads = []

    # ✅ Append the new lead
    leads.append(lead_data)

    # ✅ Save back to JSON file
    with open(leads_file, 'w', encoding='utf-8') as f:
        json.dump(leads, f, indent=4)

    print(f"✅ Lead recorded: {name} ({email}) - Trip to {destination}")

    return {
        "status": "success",
        "message": f"Thank you {name}! Your travel plan to {destination} has been recorded. Our team will contact you within 24 hours."
    }


# =============================================================================
# TOOL 2: Record Feedback (Unanswered Questions)
# =============================================================================
def record_feedback(question, user_context=""):
    """
    Logs any question the chatbot couldn't answer into unanswered_questions.json.
    """

    feedback_data = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "question": str(question),
        "context": str(user_context),
        "status": "unanswered"
    }

    feedback_file = "unanswered_questions.json"

    # ✅ Safely load existing feedback or start a new list
    if os.path.exists(feedback_file):
        with open(feedback_file, 'r', encoding='utf-8') as f:
            try:
                feedback_list = json.load(f)
            except json.JSONDecodeError:
                feedback_list = []
    else:
        feedback_list = []

    feedback_list.append(feedback_data)

    # ✅ Save feedback list
    with open(feedback_file, 'w', encoding='utf-8') as f:
        json.dump(feedback_list, f, indent=4)

    print(f"📝 Feedback recorded: {question}")

    return {
        "status": "recorded",
        "message": "I’m sorry, I don’t have that information right now. I’ve recorded your question, and our team will review it soon!"
    }


# =============================================================================
# TOOL 3: Weather API Tool (Optional – can skip if testing without weather)
# =============================================================================
def check_weather(city, start_date="", end_date="", preferred="sunny"):
    """
    Returns a 5-day forecast summary from OpenWeather API and checks if preferred weather appears.
    Shows actual conditions with icons.
    """
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "⚠️ Weather API key not found. Please add it to your .env file."

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if "list" not in data:
        return f"⚠️ Could not fetch weather data for {city}. Please check the city name."

    preferred_map = {
        "sunny": "clear",
        "rainy": "rain",
        "cloudy": "clouds",
        "storm": "thunderstorm",
        "snowy": "snow"
    }
    pref = preferred_map.get(preferred.lower(), preferred.lower())

    forecast_lines = []
    match_found = False
    seen_dates = set()

    for entry in data["list"]:
        date = entry["dt_txt"].split(" ")[0]
        condition = entry["weather"][0]["description"]
        main = entry["weather"][0]["main"].lower()

        # Only take one forecast per day
        if date not in seen_dates:
            seen_dates.add(date)
            icon = "☀️" if "clear" in main else "🌧️" if "rain" in main else "☁️" if "cloud" in main else "🌩️"
            forecast_lines.append(f"{date} – {condition.capitalize()} {icon}")

        if pref in main:
            match_found = True

        if len(forecast_lines) >= 5:
            break

    forecast_str = "\n".join(forecast_lines)
    match_msg = (
        f"✅ Your preferred weather (‘{preferred}’) is expected!"
        if match_found
        else f"⚠️ Your preferred weather (‘{preferred}’) is not expected in the next 5 days."
    )

    return f"🌤️ **{city} Weather Forecast (Next 5 Days):**\n{forecast_str}\n\n{match_msg}"
