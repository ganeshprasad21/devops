# urls.py
from django.urls import path
from .views import AlertListView, AlertTriggerView

urlpatterns = [
    path("alerts/", AlertListView.as_view(), name="alerts"),
    path("alerts/trigger/", AlertTriggerView.as_view(), name="trigger_alert"),
]
