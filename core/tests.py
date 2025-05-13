from django.test import TestCase
from core.models import (
    State, City, Neighborhood, Address,
    UserType, User, Category, Color,
    Metric, Product, Sale, SoldProduct
)


class StateModelTest(TestCase):
    def test_str(self):
        state = State.objects.create(name="Paraná")
        self.assertEqual(str(state), "Paraná")


class CityModelTest(TestCase):
    def test_str(self):
        state = State.objects.create(name="SP")
        city = City.objects.create(name="Campinas", state=state)
        self.assertEqual(str(city), "Campinas")


class NeighborhoodModelTest(TestCase):
    def test_str(self):
        state = State.objects.create(name="RJ")
        city = City.objects.create(name="Niterói", state=state)
        neighborhood = Neighborhood.objects.create(name="Icaraí", city=city)
        self.assertEqual(str(neighborhood), "Icaraí")


class AddressModelTest(TestCase):
    def test_str(self):
        state = State.objects.create(name="MG")
        city = City.objects.create(name="Belo Horizonte", state=state)
        neighborhood = Neighborhood.objects.create(name="Savassi", city=city)
        address = Address.objects.create(
            number=123,
            address_line="Apto 101",
            street="Rua da Paz",
            neighborhood=neighborhood
        )
        self.assertEqual(
            str(address), "Rua da Paz - Savassi - Apto 101"
        )


class UserTypeModelTest(TestCase):
    def test_str(self):
        user_type = UserType.objects.create(type="Cliente")
        self.assertEqual(str(user_type), "Cliente")


class UserModelTest(TestCase):
    def setUp(self):
        state = State.objects.create(name="RS")
        city = City.objects.create(name="Porto Alegre", state=state)
        neighborhood = Neighborhood.objects.create(name="Centro", city=city)
        address = Address.objects.create(
            number=456,
            address_line="Casa",
            street="Av. Independência",
            neighborhood=neighborhood
        )
        user_type = UserType.objects.create(type="Administrador")
        self.user = User.objects.create(
            user_type=user_type,
            name="João Silva",
            email="joao@email.com",
            phone="51999999999",
            address=address,
            password="senha123"
        )

    def test_str(self):
        self.assertEqual(str(self.user), "João Silva")


class CategoryModelTest(TestCase):
    def test_str(self):
        category = Category.objects.create(name="Utensílios")
        self.assertEqual(str(category), "Utensílios")


class ColorModelTest(TestCase):
    def test_str(self):
        color = Color.objects.create(name="Vermelho")
        self.assertEqual(str(color), "Vermelho")


class MetricModelTest(TestCase):
    def test_str(self):
        metric = Metric.objects.create(name="Litros")
        self.assertEqual(str(metric), "Litros")


class ProductModelTest(TestCase):
    def test_str(self):
        category = Category.objects.create(name="Potes")
        color = Color.objects.create(name="Azul")
        metric = Metric.objects.create(name="ml")
        product = Product.objects.create(
            name="Pote Hermético",
            category=category,
            color=color,
            metric=metric,
            capacity=500
        )
        self.assertEqual(str(product), "Pote Hermético")


class SaleModelTest(TestCase):
    
    def setUp(self):
        state = State.objects.create(name="SC")
        city = City.objects.create(name="Florianópolis", state=state)
        neighborhood = Neighborhood.objects.create(name="Trindade", city=city)
        address = Address.objects.create(
            number=321,
            address_line="Sala 2",
            street="Rua das Flores",
            neighborhood=neighborhood
        )
        user_type = UserType.objects.create(type="Cliente")
        self.user = User.objects.create(
            user_type=user_type,
            name="Maria Oliveira",
            email="maria@email.com",
            phone="48999999999",
            address=address,
            password="senha456"
        )

    def test_str(self):
        sale = Sale.objects.create(customer=self.user, installments=3)
        self.assertIn("Maria Oliveira", str(sale))
        self.assertIn("3", str(sale))


class SoldProductModelTest(TestCase):
    def test_str(self):
        category = Category.objects.create(name="Jarras")
        color = Color.objects.create(name="Verde")
        metric = Metric.objects.create(name="ml")
        product = Product.objects.create(
            name="Jarra de Suco",
            category=category,
            color=color,
            metric=metric,
            capacity=2000
        )

        state = State.objects.create(name="BA")
        city = City.objects.create(name="Salvador", state=state)
        neighborhood = Neighborhood.objects.create(name="Barra", city=city)
        address = Address.objects.create(
            number=55,
            address_line="Cobertura",
            street="Rua Atlântica",
            neighborhood=neighborhood
        )
        user_type = UserType.objects.create(type="Cliente")
        user = User.objects.create(
            user_type=user_type,
            name="Carlos Lima",
            email="carlos@email.com",
            phone="71999999999",
            address=address,
            password="senha789"
        )
        sale = Sale.objects.create(customer=user, installments=1)
        sold_product = SoldProduct.objects.create(
            sale=sale, product=product, value=49.90
        )
        self.assertIn("Jarra de Suco", str(sold_product))
        self.assertIn("49.90", str(sold_product))
