from django.core.validators import MaxLengthValidator
from django.db import models


class Pattern(models.Model):
    name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    code = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], null=True)
    color = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
