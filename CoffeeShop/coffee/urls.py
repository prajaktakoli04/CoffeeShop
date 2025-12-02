from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/<int:coffee_id>/', views.order_coffee, name='order'),
]