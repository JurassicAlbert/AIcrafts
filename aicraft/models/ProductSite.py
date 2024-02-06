from django.core.validators import MaxLengthValidator
from django.db import models

from .Product import Product
from .Company import Company
from .ProductSize import ProductSize
from .Pattern import Pattern


class ProductSite(models.Model):
    name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, related_name='sites',
                                     related_query_name='site')
    product_pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, related_name='sites',
                                        related_query_name='site')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
