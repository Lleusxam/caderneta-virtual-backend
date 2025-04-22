from django.urls import path
from . import views


urlpatterns = [
    # State
    path("states/", views.StateList.as_view(), name="state-list"),
    path("states/<int:pk>/", views.StateDetail.as_view(), name="state-detail"),
    # City
    path("cities/", views.CityList.as_view(), name="city-list"),
    path("cities/<int:pk>/", views.CityDetail.as_view(), name="city-detail"),
    # Neighborhood
    path("neighborhoods/", views.NeighborhoodList.as_view(), name="neighborhood-list"),
    path(
        "neighborhoods/<int:pk>/",
        views.NeighborhoodDetail.as_view(),
        name="neighborhood-detail",
    ),
    # Address
    path("addresses/", views.AddressList.as_view(), name="address-list"),
    path("addresses/<int:pk>/", views.AddressDetail.as_view(), name="address-detail"),
    # UserType
    path("user-types/", views.UserTypeList.as_view(), name="usertype-list"),
    path(
        "user-types/<int:pk>/", views.UserTypeDetail.as_view(), name="usertype-detail"
    ),
    # User
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    # Category
    path("categories/", views.CategoryList.as_view(), name="category-list"),
    path(
        "categories/<int:pk>/", views.CategoryDetail.as_view(), name="category-detail"
    ),
    # Color
    path("colors/", views.ColorList.as_view(), name="color-list"),
    path("colors/<int:pk>/", views.ColorDetail.as_view(), name="color-detail"),
    # Metric
    path("metrics/", views.MetricList.as_view(), name="metric-list"),
    path("metrics/<int:pk>/", views.MetricDetail.as_view(), name="metric-detail"),
    # Product
    path("products/", views.ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", views.ProductDetail.as_view(), name="product-detail"),
    # Sale
    path("sales/", views.SaleList.as_view(), name="sale-list"),
    path("sales/<int:pk>/", views.SaleDetail.as_view(), name="sale-detail"),
    # SoldProduct
    path("sold-products/", views.SoldProductList.as_view(), name="soldproduct-list"),
    path(
        "sold-products/<int:pk>/",
        views.SoldProductDetail.as_view(),
        name="soldproduct-detail",
    ),
]
