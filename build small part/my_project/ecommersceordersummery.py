# E-commerce Order Summary
def generate_order_summary():
    customer_name = "John Doe"
    order_id = 12345
    items = [
        {"name": "Laptop", "price": 999.99, "qty": 1},
        {"name": "Mouse", "price": 25.50, "qty": 2},
        {"name": "Keyboard", "price": 75.00, "qty": 1}
    ]
    
    subtotal = sum(item["price"]* item["qty"] for item in items )
    tax_rate = 0.08
    tax = subtotal * tax_rate
    total = tax + subtotal

    ## generate receipt 
    print(f"{'='*50}")
    print(f"{'Bill summery':^50}")
    print(f"{'-'*50}")
    print(f"\nCustomer: {customer_name}")
    print(f"order_id: #{order_id:06d}")
    print(f"\n{'Item':<20}{'Qty':>5}{'price':>10}{'total':10}")
    
    for item in items:
        name = item["name"]
        qty = item["qty"]
        price = item["price"]
        Line_total = price *qty
        print(f"{name:<20}{qty:}")