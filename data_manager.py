import requests


class DataManager:
    def __init__(self):
        pass

    def get_data(self):
        get_request_url = "https://api.sheety.co/fdafbfc43b701f05ebcf8e7bcd905632/flightDeals/prices"
        response = requests.get(url=get_request_url)
        response.raise_for_status()
        return response.json()

    def post_data(self, city, code, price):
        post_url = "https://api.sheety.co/fdafbfc43b701f05ebcf8e7bcd905632/flightDeals/prices"
        payload = {
            "price": {
                "city": city,
                "iataCode": code,
                "lowestPrice": price,
            }
        }
        response = requests.post(url=post_url, json=payload)
        response.raise_for_status()
        return response.json()

    def put_data(self, objectid, city, code, price):
        put_url = f"https://api.sheety.co/fdafbfc43b701f05ebcf8e7bcd905632/flightDeals/prices/{objectid}"
        payload = {
            "price": {
                "city": city,
                "iataCode": code,
                "lowestPrice": price,
            }
        }
        response = requests.put(url=put_url, json=payload)
        response.raise_for_status()
        return response.json()
