from django.core.validators import MaxLengthValidator
from django.db import models


class Company(models.Model):
    """
    A class representing a company that sells products.

    This class may be later modified in case of collaboration requests from other companies.

    Attributes:
    - name (str): The name of the company.
    - url (str): The URL of the company's website.

    Example:
    >>> company = Company(name="Example Corp", url="http://www.example.com")
    >>> company.save()
    """

    name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    url = models.TextField()

    def __str__(self):
        return self.name
