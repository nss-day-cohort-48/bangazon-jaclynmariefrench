from bangazonreports.views.users.ordersbyuser import orders_by_user
from django.urls import path

urlpatterns = [
    path('reports/userorder', orders_by_user),
]
