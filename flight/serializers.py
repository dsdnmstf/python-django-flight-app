from rest_framework import serializers
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "arrival_city",
            "date_of_departure",
            "etd"
        )


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone_number"
        )
class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer()