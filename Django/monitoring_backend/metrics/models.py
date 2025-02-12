# models.py
from django.db import models

class Metric(models.Model):
    METRIC_CHOICES = [
        ('CPU', 'CPU Usage'),
        ('Memory', 'Memory Usage'),
        ('Disk', 'Disk Usage'),
        ('Network', 'Network Traffic'),
    ]

    metric_type = models.CharField(max_length=20, choices=METRIC_CHOICES)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_type}: {self.value} at {self.timestamp}"
