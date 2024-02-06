from django.core.validators import MaxLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])

    def __str__(self):
        return self.name
