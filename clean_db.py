from core.models import (State, City, Neighborhood, Address, UserType, User, Consortium,
                        ConsortiumParticipation, Category, Color, Metric, Capacity,
                        Product, Sale, SaleProduct, Billing, Payment, SoldProduct)


models = [Payment, Billing, SoldProduct, SaleProduct, Sale,
          Product, Capacity, Metric, Color, Category,
          ConsortiumParticipation, Consortium,
          User, UserType, Address, Neighborhood, City, State]

for model in models:
    model.objects.all().delete()
