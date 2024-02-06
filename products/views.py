from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductDetailSerializer, ProductListSerializer

# Create your views here.

class ProductCreateView(generics.CreateAPIView):
	"""docstring for ProductCreateView"""
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer

class ProductListView(generics.ListAPIView):
	"""docstring for ProductListView"""
	queryset = Product.objects.all()
	serializer_class = ProductListSerializer

class ProductDetailView(generics.RetrieveAPIView):
	"""docstring for ProductDetailView"""
	lookup_field = "id"
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer

class ProductUpdateView(generics.RetrieveUpdateAPIView):
	"""docstring for ProductUpdateView"""
	lookup_field = "id"
	queryset = Product.objects.all()
	serializer_class = ProductDetailSerializer

class ProductDeleteView(generics.DestroyAPIView):
	"""docstring for ProductDeleteView"""
	lookup_field = "id"
	queryset = Product.objects.all()

		
		
		
		

