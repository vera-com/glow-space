from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from datetime import date, datetime


def home(request):
    return render(request, 'home/index.html')


def bookings(request):

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        service = request.POST.get("service")
        preferred_date = request.POST.get("preferred_date")
        preferred_time = request.POST.get("preferred_time")

        if not name or not email or not preferred_date or not preferred_time:
            messages.error(
                request,
                "Please complete all booking fields."
            )
            return redirect("bookings")
        if preferred_date < str(date.today()):
            messages.error(request, "Please choose today or a future date.")
            return redirect("bookings")
            
        booking_datetime = datetime.strptime(
            f"{preferred_date} {preferred_time}",
            "%Y-%m-%d %H:%M"
        )

        if booking_datetime < datetime.now():
            messages.error(request, "Please choose a future date and time.")
            return redirect("bookings")

        Booking.objects.create(
            name=name,
            email=email,
            service=service,
            preferred_date=preferred_date,
            preferred_time=preferred_time,
        )

        messages.success(
            request,
            "Your booking request has been submitted successfully."
        )

        return redirect("bookings")

    return render(request, "home/bookings.html")
