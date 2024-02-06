from django.db import models

# Create your models here.

class Product(models.Model):
	"""docstring for Product"""
	product_name = models.CharField(max_length = 100)
	product_description = models.TextField()
	product_price = models.DecimalField(max_digits = 5, decimal_places = 2)
	product_expiry_date = models.DateField(null = True)

