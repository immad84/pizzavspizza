from django.db import models

# Create your models here.

class Customer(models.Model):
	"""docstring for ClassName"""
	customer_firstName = models.CharField(max_length = 100, blank = True)
	customer_lastName = models.CharField(max_length = 100, blank = True)
	customer_email = models.EmailField(max_length = 100, blank = True)


	def __str__(self):
		return f"{self.customer_firstName} {self.customer_lastName}"

