from core.models import *

# Ordem importa para evitar erro de integridade referencial (FKs)
SoldProduct.objects.all().delete()
Sale.objects.all().delete()
Product.objects.all().delete()
Category.objects.all().delete()
Color.objects.all().delete()
Metric.objects.all().delete()

User.objects.all().delete()
UserType.objects.all().delete()
Address.objects.all().delete()
Neighborhood.objects.all().delete()
City.objects.all().delete()
State.objects.all().delete()
