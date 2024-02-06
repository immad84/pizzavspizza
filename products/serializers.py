from rest_framework import serializers
from .models import Product

class ProductDetailSerializer(serializers.ModelSerializer):
	"""docstring for ProductDetailSerializer"""
	class Meta:
		"""docstring for Meta"""
		model = Product
		fields = ["product_name", "product_description", 
			"product_price", "product_expiry_date"
		]
			
		
class ProductListSerializer(serializers.ModelSerializer):
	"""docstring for ProductListSerializer"""
	class Meta:
		model = Product
		fields = ["product_name", "product_price"]
		