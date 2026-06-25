from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking, Service, Product, Cart, CartItem
from datetime import date, datetime
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home/index.html')


@login_required
def bookings(request):

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        service = request.POST.get("service")
        preferred_date = request.POST.get("preferred_date")
        preferred_time = request.POST.get("preferred_time")

        if (
            not name
            or not email
            or not service
            or not preferred_date
            or not preferred_time
        ):
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
            "%Y-%m-%d %H:%M")

        appointment_time = booking_datetime.time()
        if appointment_time.hour < 9 or appointment_time.hour >= 21:
            messages.error(
                request,
                "Appointments can only be booked between 09:00 and 21:00.")
            return redirect("bookings")

        if booking_datetime < datetime.now():
            messages.error(request, "Please choose a future date and time.")
            return redirect("bookings")

        if Booking.objects.filter(
           preferred_date=preferred_date,
           preferred_time=preferred_time
           ).exists():
            messages.error(
             request,
             "This time slot is already booked. Please choose another time."
            )
            return redirect("bookings")

        if booking_datetime.weekday() == 6:
            messages.error(
             request,
             "Sorry, we are closed on Sundays. Please choose another date."
              )
            return redirect("bookings")

        Booking.objects.create(
            user=request.user,
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
    services = Service.objects.all()

    return render(request, "home/bookings.html", {
         "today": date.today().isoformat(),
         "services": services
         })


@login_required
def appointments(request):
    bookings = Booking.objects.filter(
     user=request.user).order_by(
     "preferred_date",
     "preferred_time"
    )

    return render(
        request,
        "home/appointments.html",
        {"bookings": bookings}
    )


@login_required
def edit_appointment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        service = request.POST.get("service")
        preferred_date = request.POST.get("preferred_date")
        preferred_time = request.POST.get("preferred_time")

        if not name or not email or not preferred_date or not preferred_time:
            messages.error(request, "Please complete all appointment fields.")
            return redirect("edit_appointment", booking_id=booking.id)

        booking_datetime = datetime.strptime(
            f"{preferred_date} {preferred_time}",
            "%Y-%m-%d %H:%M"
        )
        appointment_time = booking_datetime.time()
        if appointment_time.hour < 9 or appointment_time.hour >= 21:
            messages.error(
             request,
             "Appointments can only be booked between 09:00 and 21:00.")
            return redirect("edit_appointment", booking_id=booking.id)

        if booking_datetime <= datetime.now():
            messages.error(request, "Please choose a future date and time.")
            return redirect("edit_appointment", booking_id=booking.id)

        booking.name = name
        booking.email = email
        booking.service = service
        booking.preferred_date = preferred_date
        booking.preferred_time = preferred_time
        booking.save()

        messages.success(request, "Appointment updated successfully.")
        return redirect("appointments")

    return render(
        request,
        "home/edit_appointment.html",
        {"booking": booking, "today":
         date.today().isoformat()}
        )


@login_required
def delete_appointment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Appointment deleted successfully.")
        return redirect("appointments")

    return render(
        request,
        "home/delete_appointment.html",
        {"booking": booking}
    )


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "home/register.html", {"form": form})


def products(request):
    products = Product.objects.filter(available=True)

    context = {
        "products": products,
    }

    return render(request, "home/products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        "home/product_detail.html",
        {"product": product}
    )


@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    return render(
        request,
        "home/cart.html",
        {"cart": cart}
    )


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, "Product added to your cart.")

    return redirect("cart")
