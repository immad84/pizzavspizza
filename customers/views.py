from django.shortcuts import render
from rest_framework import generics
from django.views.generic import TemplateView
from .models import Customer
from .serializers import CustomerDetailSerializer

# Create your views here.

class CustomerCreateAPIView(generics.CreateAPIView):
	"""docstring for ClassName"""
	queryset = Customer.objects.all()
	serializer_class = CustomerDetailSerializer

class CustomerListAPIView(generics.ListAPIView):
	"""docstring for CustomerListAPIView"""
	queryset = Customer.objects.all()
	serializer_class = CustomerDetailSerializer
		

class CustomerDetailAPIView(generics.RetrieveAPIView):
	"""docstring for ClassName"""
	lookup_field = "id"
	queryset = Customer.objects.all()
	serializer_class = CustomerDetailSerializer

class CustomerUpdateAPIView(generics.RetrieveUpdateAPIView):
	"""docstring for ClassName"""
	lookup_field = "id"
	queryset = Customer.objects.all()
	serializer_class = CustomerDetailSerializer

class CustomerDeleteAPIView(generics.DestroyAPIView):
	"""docstring for CustomerDeleteAPIView"""
	queryset = Customer.objects.all()
	lookup_field = "id"
	
class HomePageView(TemplateView):
	"""docstring for ClassName"""
	template_name = 'index.html'

	
	

