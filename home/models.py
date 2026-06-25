from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(
     User,
     on_delete=models.CASCADE,
     null=True,
     blank=True,
    )

    SERVICE_CHOICES = [
     ('Facial Treatment', 'Facial Treatment'),
     ('Hair Styling', 'Hair Styling'),
     ('Massage Therapy', 'Massage Therapy'),
     ('Nail Care', 'Nail Care'),
     ('Makeup Session', 'Makeup Session'),
     ('Waxing', 'Waxing'),
     ('Eyebrow Shaping', 'Eyebrow Shaping'),
     ('Body Scrub', 'Body Scrub'),
     ('Bridal Beauty Package', 'Bridal Beauty Package'),
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


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"

    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def subtotal(self):
        return self.product.price * self.quantity
