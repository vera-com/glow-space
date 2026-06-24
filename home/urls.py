from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('bookings/', views.bookings, name='bookings'),
    path("appointments/", views.appointments, name="appointments"),
    path("appointments/edit/<int:booking_id>/",
         views.edit_appointment, name="edit_appointment"),
    path("appointments/delete/<int:booking_id>/",
         views.delete_appointment, name="delete_appointment"),
    path("products/", views.products, name="products"),
    ]
