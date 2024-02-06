from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.db import models

from .Product import Product


class Payment(models.Model):
    """
    A model representing a payment for an order.

    Attributes:
    - user (User): The user making the payment.
    - product (Product): The product being purchased.
    - quantity (int): The quantity of the product in the order.
    - payment_type (str): The type of payment (e.g., credit card, PayPal, etc.).
    - is_successful (bool): Indicates whether the payment was successful.

    Example:
    >>> payment = Payment(user=user_instance, product=product_instance, quantity=2, payment_type="Credit Card", is_successful=True)
    >>> payment.save()
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    payment_type = models.CharField(max_length=50, validators=[MaxLengthValidator(50)])
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name()}'s Payment for {self.product.name}"
