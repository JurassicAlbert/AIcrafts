from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
from django.db import models


class ProductSize(models.Model):
    """
    A class representing a product size, specifically for shirts in a store.

    Attributes:
    - name (str): The name of the product size.
    - chest_circumference (float): The chest circumference measurement for the size.
    - height (float): The height measurement for the size.
    - person_height (float): An alternative field for specifying a person's height for the size.

    Constraints:
    - The 'name' field must have a minimum length of 1 and a maximum length of 10.
    - The 'chest_circumference', 'height', and 'person_height' fields must be floats with specific minimum and maximum values.

    Example:
    >>> size = ProductSize(name="S", chest_circumference=38.0, height=170.0, person_height=165.0)
    >>> size.save()
    """

    name = models.CharField(default="M", max_length=10, validators=[
        MinLengthValidator(1),
        MaxLengthValidator(10)
    ])

    chest_circumference = models.DecimalField(default=1, max_digits=5, decimal_places=2,
                                              validators=[
                                                  MaxValueValidator(250),
                                                  MinValueValidator(30)
                                              ])

    height = models.DecimalField(default=1, max_digits=5, decimal_places=2,
                                 validators=[
                                     MaxValueValidator(250),
                                     MinValueValidator(30)
                                 ])
    sleeve_height = models.DecimalField(default=1, max_digits=5, decimal_places=2,
                                 validators=[
                                     MaxValueValidator(100),
                                     MinValueValidator(5)
                                 ])

    person_height = models.DecimalField(default=1, max_digits=5, decimal_places=2,
                                        validators=[
                                            MaxValueValidator(250),
                                            MinValueValidator(30)
                                        ])

    def __str__(self):
        return self.name
