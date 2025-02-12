# views.py
from rest_framework import generics
from .models import LogEntry
from .serializers import LogEntrySerializer

# API to retrieve all logs (GET) and create new logs (POST)
class LogEntryListCreateView(generics.ListCreateAPIView):
    queryset = LogEntry.objects.all().order_by("-timestamp")  # Show latest logs first
    serializer_class = LogEntrySerializer
