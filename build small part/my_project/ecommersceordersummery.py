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
    print(f"bill summery{}")