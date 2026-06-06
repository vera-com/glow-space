from django.contrib import admin
from .models import Booking


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
