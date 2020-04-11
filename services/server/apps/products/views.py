from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import AllowAny
# from abc import ABC
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


# class ProductBase(ABC):
# 	queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [AllowAny]

# class ProductList(ProductBase, generics.ListCreateAPIView):
#     ...

# product_list = ProductList.as_view()


class Products(viewsets.ReadOnlyModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [AllowAny]
	lookup_field = 'slug'


# products_details = Products.as_view()

