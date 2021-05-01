from django.urls import path
from .views import home_view, update_price ,LinkDeleteView

urlpatterns = [
    path('', home_view, name="home"),
    path('delete/<pk>/', LinkDeleteView.as_view(), name="delete"),
    path('update/', update_price, name="update_prices")
]
