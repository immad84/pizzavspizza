from django.urls import path
from . import views

urlpatterns = [
	path("product/create/", views.ProductCreateView.as_view(),
		name = "product_create_view"),
	path("products/", views.ProductListView.as_view(),
		name = "product_list_view"),
	path("product/<int:id>/", views.ProductDetailView.as_view(),
		name = "product_detail_view"),
	path("product/update/<int:id>", views.ProductUpdateView.as_view(),
		name = "product_update_view"),
	path("product/delete/<int:id>", views.ProductDeleteView.as_view(),
		name = "product_delete_view")
]