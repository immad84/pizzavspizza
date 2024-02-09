from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductDetailSerializer(serializers.ModelSerializer):
	"""docstring for ProductDetailSerializer"""
	class Meta:
		"""docstring for Meta"""
		model = Product
		fields = [
			"id",
			"product_name", 
			"product_description", 
			"product_price", 
			"product_expiry_date"
		]
			
		
class ProductListSerializer(serializers.ModelSerializer):
	"""docstring for ProductListSerializer"""
	absolute_url = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = [
			"id",
			"product_name", 
			"product_price",
			"absolute_url"
		]

	def get_absolute_url(self, obj):
		return reverse("product_detail_view", args=(obj.pk,))
		