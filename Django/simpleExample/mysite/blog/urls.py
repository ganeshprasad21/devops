from django.urls import path
from . import views  # Import the views file

urlpatterns = [
    path('', views.home, name='home'),  # Calls the home() function when the user visits the page
]
