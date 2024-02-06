
from django.urls import path
from . import views

urlpatterns = [
	path("restaurants/", views.PizzariaListAPIView.as_view(),
		name = "PizzariaListView"),
	path("restaurant/<int:id>/", views.PizzariaDetailAPIView.as_view(),
		name = "PizzariaDetailView"),
	path("restaurant/create/", views.PizzariaCreateAPIView.as_view(), 
		name = "PizzariaCreateView"),
	path("restaurant/update/<int:id>", views.PizzariaUpdateAPIView.as_view(),
		name = "PizzariaUpdateView"),
	path("restaurant/delete/<int:id>", views.PizzariaDeleteAPIView.as_view(),
		name = "PizzariaDeleteView")
]