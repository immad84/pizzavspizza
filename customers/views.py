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

class HomePageView(TemplateView):
	"""docstring for ClassName"""
	template_name = 'index.html'

	
	

