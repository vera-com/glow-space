from django.contrib import admin
from .models import Booking, Service, Product


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'service',
        'preferred_date',
        'preferred_time',
        'created_on',
    )

    list_filter = (
        'service',
        'preferred_date',
        'created_on',
    )

    search_fields = (
        'name',
        'email',
        'service',
    )

    ordering = ('-created_on',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )

    search_fields = (
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "available",
        "created_on",
    )

    list_filter = (
        "available",
        "created_on",
    )

    search_fields = (
        "name",
        "description",
    )
