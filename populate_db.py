import random
from datetime import date, timedelta
from core.models import (
    State,
    City,
    Neighborhood,
    Address,
    UserType,
    User,
    Consortium,
    ConsortiumParticipation,
    Category,
    Color,
    Metric,
    Product,
    Sale,
    SaleProduct,
    Billing,
    Payment,
    SoldProduct,
)

# STATES
states = [State.objects.create(name=n) for n in ["RN", "PB", "PE", "CE", "BA"]]

# CITIES
cities = []
for state in states:
    for name in ["Natal", "Mossoró", "Caicó"]:
        cities.append(City.objects.create(name=f"{name}-{state.name}", state=state))

# NEIGHBORHOODS
neighborhoods = []
for city in cities:
    for name in ["Centro", "Zona Norte", "Zona Sul"]:
        neighborhoods.append(
            Neighborhood.objects.create(name=f"{name} {city.name}", city=city)
        )

# ADDRESSES
addresses = []
for i in range(20):
    addresses.append(
        Address.objects.create(
            number=100 + i,
            address_line=f"Apto {i+1}",
            street=f"Rua {chr(65+i)}",
            neighborhood=random.choice(neighborhoods),
        )
    )

# USER TYPES
user_types = [
    UserType.objects.create(type=t)
    for t in ["Cliente", "Admin", "Vendedor", "Gerente", "Outro"]
]

# USERS
users = []
for i in range(20):
    users.append(
        User.objects.create(
            user_type=random.choice(user_types),
            name=f"Usuário {i+1}",
            email=f"user{i+1}@exemplo.com",
            phone=f"849999900{i:02}",
            address=random.choice(addresses),
            password="senha123",
        )
    )

# CONSORTIUMS
consortiums = []
for i in range(5):
    start = date.today() - timedelta(days=365)
    end = date.today() + timedelta(days=365)
    consortiums.append(
        Consortium.objects.create(
            name=f"Consórcio {i+1}", start_date=start, end_date=end
        )
    )

# PARTICIPAÇÕES
for cons in consortiums:
    participantes = random.sample(users, 5)
    sorteado = random.choice(participantes)
    for p in participantes:
        ConsortiumParticipation.objects.create(
            consortium=cons, client=p, draw_date=date.today()
        )

# CATEGORIAS, CORES, MÉTRICAS
categorias = [
    Category.objects.create(name=n)
    for n in ["Eletrodoméstico", "Móvel", "Eletrônico", "Veículo", "Outros"]
]
cores = [
    Color.objects.create(name=n)
    for n in ["Branco", "Preto", "Azul", "Vermelho", "Cinza"]
]
metricas = [
    Metric.objects.create(name=n) for n in ["Litros", "Kg", "Unidades", "m²", "cm³"]
]

# PRODUTOS
produtos = []
for i in range(10):
    produtos.append(
        Product.objects.create(
            name=f"Produto {i+1}",
            category=random.choice(categorias),
            color=random.choice(cores),
            capacity=(i + 1) * 10,
            metric=random.choice(metricas),
            price=random.uniform(1.0, 100.0)
        )
    )

# VENDAS
vendas = []
for i in range(10):
    sale_instance = Sale.objects.create(
        customer=random.choice(users),
        installments_quantity=random.choice([1, 3, 6, 12]),
    )
    vendas.append(sale_instance)

    num_products_in_sale = random.randint(1, 3)
    selected_products = random.sample(produtos, min(num_products_in_sale, len(produtos)))

    for product in selected_products:
        SoldProduct.objects.create(
            sale=sale_instance,
            product=product,
        )

# VENDA-PRODUTOS e PRODUTOS-VENDIDOS
for venda in vendas:
    produtos_vendidos = random.sample(produtos, 2)
    for prod in produtos_vendidos:
        SaleProduct.objects.create(sale=venda, product=prod)

# FATURAS
faturas = []
for venda in vendas:
    valor_total = random.uniform(200.0, 2000.0)
    data_fatura = date.today()
    vencimento = data_fatura + timedelta(days=30)
    faturas.append(
        Billing.objects.create(
            sale=venda,
            total_value=valor_total,
            billing_date=data_fatura,
            due_date=vencimento,
        )
    )

# PAGAMENTOS
for fatura in faturas:
    Payment.objects.create(
        amount_paid=fatura.total_value - 10,
        payment_date=fatura.billing_date + timedelta(days=10),
        payment_method="Pix",
        discount=10.0,
        billing=fatura,
    )
