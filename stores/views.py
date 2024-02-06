from rest_framework import generics
from .models import Pizzaria
from .serializers import PizzariaListSerializer, PizzariaDetailSerializer


class PizzariaListAPIView(generics.ListAPIView):
	"""docstring for """
	queryset = Pizzaria.objects.all()
	serializer_class = PizzariaListSerializer


class PizzariaDetailAPIView(generics.RetrieveAPIView):
	"""docstring for ClassName"""
	lookup_field = "id"
	queryset = Pizzaria.objects.all()
	serializer_class = PizzariaDetailSerializer


class PizzariaCreateAPIView(generics.CreateAPIView):
	"""docstring for PizzariaCreateAPIView"""
	queryset = Pizzaria.objects.all()
	serializer_class = PizzariaDetailSerializer


	
		
	
		
	


