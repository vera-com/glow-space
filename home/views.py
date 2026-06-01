from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def bookings(request):
    return render(request, 'home/bookings.html')
