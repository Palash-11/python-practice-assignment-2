customer_name = input("customer's name: ")

product1_name = input("product 1 name: ")
product1_price = float(input("product 1 price: "))

product2_name = input("product 2 name: ")
product2_price = float(input("product 2 price: "))

product3_name = input("product 3 name: ")
product3_price = float(input("product 3 price: "))

subtotal = product1_price + product2_price + product3_price


if subtotal >= 5000:
    discount_percentage = 20
elif 3000 <= subtotal <= 4999:
    discount_percentage = 10
elif 1000 <= subtotal <= 2999:
    discount_percentage = 5
else:
    discount_percentage = 0

discount_amount = (subtotal * discount_percentage) / 100
final_total = subtotal - discount_amount

print("\n--- Shopping Summary ---")
print(f"Customer Name: {customer_name}")
print(f"1. {product1_name}: {product1_price}")
print(f"2. {product2_name}: {product2_price}")
print(f"3. {product3_name}: {product3_price}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount ({discount_percentage}%): {discount_amount:.2f}")
print(f"Final Total: {final_total:.2f}")