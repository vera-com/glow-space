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
    path("products/<int:product_id>/",
         views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("checkout/",
         views.create_checkout_session, name="create_checkout_session"),
    path("checkout/success/", views.checkout_success, name="checkout_success"),
    path("cart/increase/<int:item_id>/",
         views.increase_cart_item, name="increase_cart_item"),
    path("cart/reduce/<int:item_id>/",
         views.reduce_cart_item, name="reduce_cart_item"),
    path("cart/remove/<int:item_id>/",
         views.remove_cart_item, name="remove_cart_item"),
    path("buy-now/<int:product_id>/", views.buy_now, name="buy_now"),
    ]
