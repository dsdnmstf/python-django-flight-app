from .models import Flight, Reservation
from .serializers import FlightSerializer
from rest_framework import viewsets
from .permissions import IsStuforReadOnly

class FlightView(viewsets.ModelViewSet):  # GET, POST, UPDATE, DELETE
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStuforReadOnly,)


