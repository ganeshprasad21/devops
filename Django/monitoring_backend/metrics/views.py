# views.py
from rest_framework import generics
from .models import Metric
from .serializers import MetricSerializer

# API to retrieve all metrics (GET) and create new metrics (POST)
class MetricListCreateView(generics.ListCreateAPIView):
    queryset = Metric.objects.all().order_by("-timestamp")  # Return latest first
    serializer_class = MetricSerializer
