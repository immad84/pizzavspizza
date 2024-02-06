from rest_framework import serializers
from .models import Pizzaria

class PizzariaListSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		"""docstring for Meta"""
		model = Pizzaria
		fields = ["id", "pizzaria_name", "pizzaria_image", "city", "zip_code", "website"]


class PizzariaDetailSerializer(serializers.ModelSerializer):
	"""docstring for PizzariaDetailSerializer"""
	class Meta:
		"""docstring for Meta"""
		model = Pizzaria
		fields = ["id", "pizzaria_name", "street", "city", "state",
		 "zip_code", "phone_number", "website", "description", "pizzaria_image",
		 "email", "active"
		]
		
	

			
	
		