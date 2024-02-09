
from rest_framework import serializers
from .models import Pizzaria
from rest_framework.reverse import reverse

class PizzariaListSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	absolute_url = serializers.SerializerMethodField()

	class Meta:
		"""docstring for Meta"""
		model = Pizzaria
		fields = [
			"id",
			"pizzaria_name",
			"pizzaria_image", 
			"city", 
			"zip_code", 
			"website",
			"absolute_url",
		]

	def get_absolute_url(self, obj):
		return reverse("PizzariaDetailView", args=(obj.pk,))


class PizzariaDetailSerializer(serializers.ModelSerializer):
	"""docstring for PizzariaDetailSerializer"""
	class Meta:
		"""docstring for Meta"""
		model = Pizzaria
		fields = ["id", "pizzaria_name", "street", "city", "state",
		 "zip_code", "phone_number", "website", "description", "pizzaria_image",
		 "email", "active"
		]
		
	

			
	
		