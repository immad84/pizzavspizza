from rest_framework import serializers
from .models import Pizzaria

class PizzariaListSerializer(serializers.ModelSerializer):
	"""docstring for """
	class Meta:
		"""docstring for ClassName"""
		model = Pizzaria
		fields = ["id", "pizzaria_name", "city", "zip_code"]
			
	
		