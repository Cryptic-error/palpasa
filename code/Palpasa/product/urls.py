
from django.urls import path
from .views import ProductDetailsAPIView

urlpatterns = [
    path('api/product/details/<str:product_id>/', ProductDetailsAPIView.as_view(), name='product-details'),
]