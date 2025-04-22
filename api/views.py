from rest_framework import generics
from core.models import State
from .serializers import *


# State
class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = "pk"


# City
class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = "pk"


# Neighborhood
class NeighborhoodList(generics.ListCreateAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer


class NeighborhoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    lookup_field = "pk"


# Address
class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = "pk"


# UserType
class UserTypeList(generics.ListCreateAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class UserTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
    lookup_field = "pk"


# User
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"


# Category
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"


# Color
class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    lookup_field = "pk"


# Metric
class MetricList(generics.ListCreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class MetricDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    lookup_field = "pk"


# Product
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


# Sale
class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    lookup_field = "pk"


# SoldProduct
class SoldProductList(generics.ListCreateAPIView):
    queryset = SoldProduct.objects.all()
    serializer_class = SoldProductSerializer


class SoldProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoldProduct.objects.all()
    serializer_class = SoldProductSerializer
    lookup_field = "pk"

