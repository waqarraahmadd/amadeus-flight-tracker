from os import environ

import requests, os
from datetime import datetime, timedelta

class FlightSearch:

    def __init__(self):
        self.API_KEY = os.environ["API_KEY"]
        self.API_SECRET = os.environ["API_SECRET"]
        self.flight_search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    def get_access_token(self):
        access_token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        access_token_body = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET,
        }
        response = requests.post(url=access_token_url, data=access_token_body)
        response.raise_for_status()
        access_token = response.json()["access_token"]
        token_type = response.json()["token_type"]
        return f"{token_type} {access_token}"

    def get_flight_offers(self, token, origin, destination, max_ticket_price):
        all_flights = []
        for days in range(1,2):
            departure_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
            params = {
                "originLocationCode": origin,
                "destinationLocationCode": destination,
                "departureDate": departure_date,
                "adults": 1,
                "maxPrice": max_ticket_price,
                "nonStop": "true"
            }
            headers = {
                "authorization":token
            }
            response = requests.get(url=self.flight_search_url, params=params,headers=headers)
            response.raise_for_status()
            data = response.json()["data"]
            if response.status_code != 200:
                print(f"{response.status_code} {response.text}")
            all_flights.extend(data)
        return all_flights

# t = FlightSearch()
# print(t.get_flight_offers(t.get_access_token(),"LON","LIS",500))