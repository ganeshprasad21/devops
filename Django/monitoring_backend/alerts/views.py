# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Alert
from .serializers import AlertSerializer
from metrics.models import Metric

# API to retrieve all alerts
class AlertListView(generics.ListAPIView):
    queryset = Alert.objects.all().order_by("-triggered_at")
    serializer_class = AlertSerializer

# API to check metrics and create alerts
class AlertTriggerView(APIView):
    def post(self, request):
        metric_type = request.data.get("metric_type")
        threshold = float(request.data.get("threshold"))

        # Get the latest metric of the given type
        latest_metric = Metric.objects.filter(metric_type=metric_type).order_by("-timestamp").first()

        if latest_metric and latest_metric.value > threshold:
            # Create an alert
            alert = Alert.objects.create(
                metric_type=metric_type,
                threshold=threshold,
                current_value=latest_metric.value
            )
            return Response({"message": "Alert triggered", "alert_id": alert.id}, status=201)

        return Response({"message": "No alert triggered"}, status=200)
