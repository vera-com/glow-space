from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking


def home(request):
    return render(request, 'home/index.html')


def bookings(request):

    if request.method == "POST":

        Booking.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            service=request.POST.get("service"),
            preferred_date=request.POST.get("preferred_date"),
            preferred_time=request.POST.get("preferred_time"),
        )
        messages.success(
            request,
            "Your booking request has been submitted successfully."
        )

        return redirect("bookings")

    return render(request, "home/bookings.html")
