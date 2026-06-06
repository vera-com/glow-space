from django.db import models


class Booking(models.Model):
    SERVICE_CHOICES = [
        ('Facial Treatment', 'Facial Treatment'),
        ('Hair Styling', 'Hair Styling'),
        ('Massage Therapy', 'Massage Therapy'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"
