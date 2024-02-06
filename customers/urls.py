from django.urls import path
from . import views

urlpatterns = [
	path("customer/create/", views.CustomerCreateAPIView.as_view(),
		name = "CustomerCreateView"),
	path("", views.HomePageView.as_view(), name = "HomeView")
]