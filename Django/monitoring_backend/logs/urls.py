# urls.py
from django.urls import path
from .views import LogEntryListCreateView

urlpatterns = [
    path("logs/", LogEntryListCreateView.as_view(), name="logs"),
]
