from datetime import datetime as dt


class FlightData:

    # This class is responsible for structuring the flight data.

    def __init__(self, flight_data):

        self.flight_id = flight_data["id"]
        self.flight_currency = flight_data["price"]["currency"]
        self.flight_price = float(flight_data["price"]["total"])
        self.raw_departure_time = dt.strptime(flight_data["itineraries"][0]["segments"][0]["departure"]["at"],
                                              "%Y-%m-%dT%H:%M:%S")
        self.departure_time = dt.strftime(self.raw_departure_time, "%Y-%m-%d")
        itinerary = flight_data["itineraries"]
        if len(itinerary) > 1:
            self.raw_return_time = dt.strptime(flight_data["itineraries"][1]["segments"][0]["departure"]["at"],
                                               "%Y-%m-%dT%H:%M:%S")
            self.return_time = dt.strftime(self.raw_return_time, "%Y-%m-%d")
        else:
            self.return_time = None
