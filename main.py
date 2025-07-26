from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

FLIGHT_SEARCH = FlightSearch()
DATA_MANAGER = DataManager()
NOTIFIER = NotificationManager()

token = FLIGHT_SEARCH.get_access_token()
ORIGIN = "LON"

existing_city_data = DATA_MANAGER.get_data()["prices"]

for row in existing_city_data:
    city = row["city"]
    destination = row["iataCode"]
    cheapest_ticket = int(row["lowestPrice"])
    object_id = row["id"]

    new_flight_data = FLIGHT_SEARCH.get_flight_offers(token=token, origin=ORIGIN, destination=destination,
                                                      max_ticket_price=cheapest_ticket)
    for flights in new_flight_data:
        DATA_ORGANIZER = FlightData(flights)

        if DATA_ORGANIZER.flight_price < float(cheapest_ticket):
            cheapest_ticket = DATA_ORGANIZER.flight_price
            cheapest_flight_id = DATA_ORGANIZER.flight_id
            currency = DATA_ORGANIZER.flight_currency

            response = DATA_MANAGER.put_data(objectid=object_id, city=city, code=destination, price=cheapest_ticket)

            NOTIFIER.send_message(currency=currency,
                                  price=cheapest_ticket,
                                  departure=ORIGIN,
                                  destination=destination,
                                  date=DATA_ORGANIZER.departure_time
                                  )