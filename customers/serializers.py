from rest_framework import serializers
from .models import Customer
from rest_framework.reverse import reverse

class CustomerDetailSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	absolute_url = serializers.SerializerMethodField()

	class Meta:
		model = Customer
		fields = [
			"customer_firstName",
			"customer_lastName",
			"customer_email",
			"absolute_url",
		]

	def get_absolute_url(self, obj):
		return reverse('CustomerListView')
		