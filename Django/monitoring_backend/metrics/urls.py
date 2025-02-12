# urls.py
from django.urls import path
from .views import MetricListCreateView

urlpatterns = [
    path("metrics/", MetricListCreateView.as_view(), name="metrics"),
]
