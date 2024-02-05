from django.shortcuts import render
from rest_framework import generics
from .serializers import PizzariaListSerializer
from .models import Pizzaria

# Create your views here.

class PizzariaListAPIView(generics.ListAPIView):
	"""docstring for ClassName"""
	queryset = Pizzaria.objects.all()
	serializer_class = PizzariaListSerializer
	


