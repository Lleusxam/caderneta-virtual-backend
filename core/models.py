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
    password = models.TextField()

    def __str__(self) -> str:
        return str(self.name)


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
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    capacity = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return str(self.name)


class Sale(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    on_create = models.DateTimeField(auto_now_add=True)
    installments = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.customer.name} - {self.installments} - {self.on_create}"


class SoldProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.product} - {self.value} - {self.sale}"
