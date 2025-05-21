from core.models import State, City, Neighborhood, Address, UserType, User, Category, Color, Metric, Product, Sale, SoldProduct
from django.utils import timezone
from random import choice, randint
from decimal import Decimal

# Estados e Cidades
rn = State.objects.create(name="Rio Grande do Norte")
sp = State.objects.create(name="São Paulo")

natal = City.objects.create(name="Natal", state=rn)
serra_negra = City.objects.create(name="Serra Negra do Norte", state=rn)
sao_paulo = City.objects.create(name="São Paulo", state=sp)

# Bairros
bairro1 = Neighborhood.objects.create(name="Centro", city=natal)
bairro2 = Neighborhood.objects.create(name="Zona Norte", city=natal)
bairro3 = Neighborhood.objects.create(name="Zona Rural", city=serra_negra)

# Endereços
end1 = Address.objects.create(number=123, address_line="Ap 101", street="Rua das Flores", neighborhood=bairro1)
end2 = Address.objects.create(number=456, address_line="Casa", street="Av. Brasil", neighborhood=bairro2)
end3 = Address.objects.create(number=789, address_line="Bloco C", street="Rua Principal", neighborhood=bairro3)

# Tipos de usuário
cliente = UserType.objects.create(type="Cliente")
vendedor = UserType.objects.create(type="Vendedor")

# Usuários
u1 = User.objects.create(user_type=cliente, name="João Silva", email="joao@email.com", phone="84999999999", address=end1, password="senha123")
u2 = User.objects.create(user_type=cliente, name="Maria Souza", email="maria@email.com", phone="84988888888", address=end2, password="senha456")
u3 = User.objects.create(user_type=vendedor, name="Carlos Lima", email="carlos@email.com", phone="84977777777", address=end3, password="senha789")

# Categorias
cat1 = Category.objects.create(name="Bebidas")
cat2 = Category.objects.create(name="Alimentos")

# Cores
cor1 = Color.objects.create(name="Vermelho")
cor2 = Color.objects.create(name="Azul")
cor3 = Color.objects.create(name="Verde")

# Métricas
m1 = Metric.objects.create(name="Litros")
m2 = Metric.objects.create(name="Quilos")

# Produtos
prod1 = Product.objects.create(name="Coca-Cola", category=cat1, color=cor1, metric=m1, capacity=2)
prod2 = Product.objects.create(name="Feijão", category=cat2, color=cor3, metric=m2, capacity=1)
prod3 = Product.objects.create(name="Guaraná", category=cat1, color=cor2, metric=m1, capacity=1)

# Vendas
venda1 = Sale.objects.create(customer=u1, on_create=timezone.now(), installments=3)
venda2 = Sale.objects.create(customer=u2, on_create=timezone.now(), installments=1)

# Produtos vendidos
SoldProduct.objects.create(sale=venda1, product=prod1, value=Decimal("8.50"))
SoldProduct.objects.create(sale=venda1, product=prod2, value=Decimal("5.00"))
SoldProduct.objects.create(sale=venda2, product=prod3, value=Decimal("6.75"))
