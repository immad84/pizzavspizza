from rest_framework import serializers
from .models import Customer

class CustomerDetailSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = Customer
		fields = ["customer_firstName", "customer_lastName", "customer_email"]
	
		