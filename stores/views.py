from rest_framework import generics
from .models import Pizzaria
from .serializers import PizzariaListSerializer

class PizzariaListAPIView(generics.ListAPIView):
	"""docstring for """
	queryset = Pizzaria.objects.all()
	serializer_class = PizzariaListSerializer
		
	


