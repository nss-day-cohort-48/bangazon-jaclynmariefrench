
SELECT 
    o.id as order_id,
    c.id as customer_id,
    a.first_name ||" "|| a.last_name as full_name,
    p.price as product_price
FROM bangazonapi_order as o
    JOIN bangazonapi_customer as c ON o.customer_id = c.id
    JOIN auth_user as a ON c.id = a.id
    JOIN bangazonapi_orderproduct as op ON o.id = op.order_id
    JOIN bangazonapi_product as p ON op.product_id = p.id
GROUP BY o.id;
