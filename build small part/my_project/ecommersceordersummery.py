# E-commerce Order Summary
def generate_order_summary():
    customer_name = "John Doe"
    order_id = 12345
    items = [
        {"name": "Laptop", "price": 999.99, "qty": 1},
        {"name": "Mouse", "price": 25.50, "qty": 2},
        {"name": "Keyboard", "price": 75.00, "qty": 1}
    ]
    
    # Calculate totals
    subtotal = sum(item["price"] * item["qty"] for item in items)
    tax_rate = 0.08
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    # Generate receipt
    print(f"{'='*50}")
    print(f"{'ORDER SUMMARY':^50}")
    print(f"{'='*50}")
    print(f"\nCustomer: {customer_name}")
    print(f"Order ID: #{order_id:06d}")
    print(f"\n{'Item':<20} {'Qty':>5} {'Price':>10} {'Total':>10}")
    print(f"{'-'*50}")
    
    for item in items:
        name = item["name"]
        qty = item["qty"]
        price = item["price"]
        line_total = price * qty
        print(f"{name:<20} {qty:>5} ${price:>9.2f} ${line_total:>9.2f}")
    
    print(f"{'-'*50}")
    print(f"{'Subtotal:':<37} ${subtotal:>9.2f}")
    print(f"{'Tax (8%):':<37} ${tax:>9.2f}")
    print(f"{'='*50}")
    print(f"{'TOTAL:':<37} ${total:>9.2f}")
    print(f"{'='*50}")
    
    # Status message with emoji and formatting
    discount_eligible = total > 1000
    print(f"\n{'🎉' if discount_eligible else '📦'} Order Status: "
          f"{'ELIGIBLE FOR DISCOUNT!' if discount_eligible else 'Processing'}")
    
    # Dynamic formatting based on total
    if total > 1000:
        savings = total * 0.10
        final_price = total - savings
        print(f"💰 You save: ${savings:.2f}")
        print(f"✨ Final price: ${final_price:.2f}")

# Run the example
generate_order_summary()