from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('bookings/', views.bookings, name='bookings'),
    path("appointments/", views.appointments, name="appointments"),
    ]
