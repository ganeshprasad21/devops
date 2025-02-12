# models.py
from django.db import models
from metrics.models import Metric

class Alert(models.Model):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    threshold = models.FloatField()
    triggered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.metric.metric_type} at {self.triggered_at} (Threshold: {self.threshold})"
