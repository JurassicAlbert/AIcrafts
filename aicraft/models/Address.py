from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models
from django_countries.fields import CountryField


class Address(models.Model):
    """
    A model representing an address for users. A user can have multiple delivery addresses,
    but only one selected as the default for product delivery.

    Attributes:
    - user (User): The user associated with the address.
    - street (str): The street address.
    - city (str): The city.
    - zip_code (str): The ZIP code.
    - is_default_delivery (bool): Indicates whether this address is the default delivery address for the user.

    Example:
    >>> address = Address(user=user_instance, street="123 Main St", city="Cityville", zip_code="12345", is_default_delivery=True)
    >>> address.save()
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    city = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    country = CountryField()
    zip_code = models.CharField("zip code", max_length=8, default="68-100")
    # location = models.PointField(null=True, blank=True) models from django.contrib.gis.db
    is_default_delivery = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name()}'s Address"
