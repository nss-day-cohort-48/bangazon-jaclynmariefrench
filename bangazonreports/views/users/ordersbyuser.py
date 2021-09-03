from bangazonapi.models.order import Order
import sqlite3
from django.shortcuts import render
from bangazonreports.views import Connection
from datetime import datetime


def orders_by_user(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
                SELECT 
                    o.id as order_id,
                    o.customer_id as customer_id
                FROM bangazon_order as o
                """
            )

            dataset = db_cursor.fetchall()

            orders_by_user = {}

            for row in dataset:
                # Crete a order instance and set its properties
                order = Order()
                order.customer = row["customer"]
                order.payment_type = row["payment_type"]
                order.created_date = row["created_date"]

                # Store the user's id
                uid = row["customer_id"]

                # If the user's id is already a key in the dictionary...
                if uid in orders_by_user:

                    orders_by_user[uid]['order'].append(order)

                else:
                    # Otherwise, create the key and dictionary value
                    orders_by_user[uid] = {}
                    orders_by_user[uid]["id"] = uid

    orders = orders_by_user.values()
    template = "users/list_with_orders.html"
    context = {"user_with_orders": order}
    return render(request, template, context)
