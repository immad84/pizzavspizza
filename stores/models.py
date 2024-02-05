from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Pizzaria (models.Model):
	pizzaria_name = models.CharField(max_length=200, blank=False)
	street = models.CharField(max_length=400, blank=True)
	city = models.CharField(max_length=400, blank=True)
	state = models.CharField(max_length=100, blank=True, null=True)
	zip_code = models.IntegerField(blank=True, default=0)
	phone_number = models.CharField(
		validators=[RegexValidator(regex=r'^\0?\d{9,10}$')],
		max_length=10, blank=True )
	website = models.URLField(max_length=200,blank=True)
	description = models.TextField(blank = True)
	pizzaria_image = models.ImageField(upload_to = 'pizzariaImages', blank = True)
	email = models.EmailField(max_length = 400, blank = True)
	active = models.BooleanField(default = True)

	def __str__(self) :
		return f"{self.pizzaria_name}, {self.city}"