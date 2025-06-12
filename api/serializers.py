from rest_framework import serializers
from core.models import *


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source="state", write_only=True
    )  # Aceita o ID de State para criação

    class Meta:
        model = City
        fields = "__all__"


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class ConsortiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consortium
        fields = "__all__"


class ConsortiumParticipationSerializer(serializers.ModelSerializer):
    consortium = ConsortiumSerializer(read_only=True)
    consortium_id = serializers.PrimaryKeyRelatedField(
        queryset=Consortium.objects.all(), source="consortium", write_only=True
    )  # Aceita o ID de Consortium para criação
    client = UserSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )  # Aceita o ID de User para criação

    class Meta:
        model = ConsortiumParticipation
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = "__all__"



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )  # Aceita o ID de Category para criação
    color = ColorSerializer(read_only=True)
    color_id = serializers.PrimaryKeyRelatedField(
        queryset=Color.objects.all(), source="color", write_only=True
    )  # Aceita o ID de Color para criação
    metric = MetricSerializer(read_only=True)
    metric_id = serializers.PrimaryKeyRelatedField(
        queryset=Metric.objects.all(), source="metric", write_only=True
    )  # Aceita o ID de Metric para criação

    class Meta:
        model = Product
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"


class SoldProductSerializer(serializers.ModelSerializer):
    sale = SaleSerializer(read_only=True)
    sale_id = serializers.PrimaryKeyRelatedField(
        queryset=Sale.objects.all(), source="sale", write_only=True
    )  # Aceita o ID de Sale para criação
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product", write_only=True
    )  # Aceita o ID de Product para criação

    class Meta:
        model = SoldProduct
        fields = "__all__"


class BillingSerializer(serializers.ModelSerializer):
    sale = SaleSerializer(read_only=True)
    sale_id = serializers.PrimaryKeyRelatedField(
        queryset=Billing.objects.all(), write_only=True
    )  # Aceita o ID de Sale para criação

    class Meta:
        model = Billing
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    billing = BillingSerializer(read_only=True)
    billing_id = serializers.PrimaryKeyRelatedField(
        queryset=Billing.objects.all(), source="billing", write_only=True
    )  # Aceita o ID de Billing para criação

    class Meta:
        model = Payment
        fields = "__all__"
