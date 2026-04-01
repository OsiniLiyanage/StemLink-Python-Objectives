amount = float(input("Enter purchase amount: "))

if amount >= 100:
    discount = amount * 0.20
elif amount >= 50:
    discount = amount * 0.10
else:
    discount = 0

final_price = amount - discount

print(f"original price: {amount}")
print(f"discount amount: {discount}")
print(f"final price: {final_price}")