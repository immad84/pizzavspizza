from rest_framework import serializers
from .models import Pizzaria

class PizzariaListSerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		"""docstring for Meta"""
		model = Pizzaria
		fields = ["id", "pizzaria_name", "pizzaria_image", "city", "zip_code", "website"]
	

			
	
		