from django.urls import path

from . import views

urlpatterns = [
    path("product/", views.ProductCreateAPIView.as_view(), name="product-create"),
    path("product/<uuid:pk>/", views.ProductAPIView.as_view(), name='product-modify-edit-delete'),
    path("sell/", views.SellProduct.as_view(), name='sell-product'),
]
