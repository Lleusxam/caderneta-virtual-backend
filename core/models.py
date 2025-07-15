from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)


class Address(models.Model):
    number = models.PositiveSmallIntegerField()
    address_line = models.CharField(max_length=100)  # Complemento
    street = models.CharField(max_length=100)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)  # Bairro

    def __str__(self) -> str:
        return f"{self.street} - {self.neighborhood} - {self.address_line}"


class UserType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.type)


class User(models.Model):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)

    def __str__(self) -> str:
        return str(self.name)


class Consortium(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.start_date} - {self.end_date}"


class ConsortiumParticipation(models.Model):
    consortium = models.ForeignKey(Consortium, on_delete=models.CASCADE)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="participations"
    )
    draw_date = models.DateField(default=models.DateField(auto_now_add=True))
    
    def __str__(self) -> str:
        return f"{self.consortium} - {self.client}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)


class Metric(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    capacity = models.FloatField()    
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return str(self.name)


class Sale(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    installments_quantity = models.PositiveSmallIntegerField()
    sold_products = models.ManyToManyField(Product, through='SoldProduct')

    def __str__(self) -> str:
        return f"{self.customer.name} - {self.installments_quantity} - {self.sale_date}"


class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.sale} - {self.product}"


class SoldProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:        
        return f"{self.product} - {self.value:.2f} - {self.sale}"


class Billing(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    total_value = models.FloatField()
    billing_date = models.DateField()
    due_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.sale}"


class Payment(models.Model):
    amount_paid = models.FloatField()
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    discount = models.FloatField()
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.billing}"
