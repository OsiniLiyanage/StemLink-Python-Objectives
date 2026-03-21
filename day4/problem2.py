def add_item(cart,name,price,qty):
    item= {"name":name,"price":price,"qty":qty}
    cart.append(item)
    print(f"added:{name} (${price:.2f} *{qty})")

def add_bulk_items(cart,items):
    cart.extends(items)
    print(f"extended cart with {len(items)} more items")

def calculate_subtotal(cart):
    item_total = map(lambda item: item["price"] * item["qty"],cart)
    return sum (item_total)

def apply_discount(subtotal,precent):
    discount= subtotal*(precent/100)
    return subtotal-discount

def filter_by_price(cart,min,max):
    filters = filter(
        lambda item:min <= item["price"] <= max,cart
        
    )
    return list (filters)

def sort_cart(cart,by="name"):

    by=="name"

    return cart

def print_recepiet(cart,discount=0):
    print("==== RECEIPT =====")
    subtotal = calculate_subtotal(cart)


def main():
    print("==== SHOPPING CART MANAGER ====")
    cart= []
    print("Adding single items...")
    add_item(cart, "Laptop", 999.99, 1)
    add_item(cart, "Mouse", 25.50, 2)

    print("adding bulk items..")
    bulk_items = [
        {"name": "Keyboard", "price": 89.99, "qty": 1},
        {"name": "Monitor", "price": 299.99, "qty": 1},
        {"name": "Headphones", "price": 79.99, "qty": 1}
    ]
    add_bulk_items(cart,bulk_items)

    print("cart contents(sorted by name):")
    cart_sorted = sort_cart(cart,"name")

    subtotal = calculate_subtotal(cart)
    print(f"subtotal: $ {subtotal:.2f}")
    discountp= 10
    realtotal = apply_discount(subtotal,discountp)
    print(f"discount({discountp}%): - $ {subtotal(discountp/100):.f}")
    print(f"TOTAL:${realtotal:.2f}")

    print("\n===== FILTERED VIEW: Items under $100 =====")


main()