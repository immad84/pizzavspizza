from django.urls import path
from . import views

urlpatterns = [
	path("customer/create/", views.CustomerCreateAPIView.as_view(),
		name = "CustomerCreateView"),
	path("", views.HomePageView.as_view(), name = "HomeView"),
	path("customer/<int:id>/", views.CustomerDetailAPIView.as_view(),
		name = "CUstomerDetailView"),
	path("customer/update/<int:id>/", views.CustomerUpdateAPIView.as_view(),
		name = "CustomerUpdateView"),
	path("customer/delete/<int:id>/", views.CustomerDeleteAPIView.as_view(),
		name = "CustomerDeleteView"),
	path("customers/", views.CustomerListAPIView.as_view(),
		name = "CustomerListView")
]