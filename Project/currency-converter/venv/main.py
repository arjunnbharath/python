
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CURRENCYLAYER_API_KEY")



def get_exchange_rates():
    url = "https://api.currencylayer.com/live"

    params = {
        "access_key": API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        if not data.get("success"):
            print("API error:", data.get("error"))
            return None

        return data

    except requests.exceptions.RequestException as error:
        print("Network or HTTP error:", error)
        return None

    except ValueError:
        print("Could not parse the API response.")
        return None

def convert_usd_to_inr(amount, rates):
    rate = rates["quotes"]["USDINR"]
    converted_amount = amount * rate
    return converted_amount


rates = get_exchange_rates()

if rates is not None:
    print("API connected successfully!")

    try:
        amount = float(input("Enter amount in USD: "))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
        else:
            result = convert_usd_to_inr(amount, rates)
            print(f"${amount:.2f} USD = ₹{result:.2f} INR")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

else:
    print("Could not retrieve exchange rates.")
