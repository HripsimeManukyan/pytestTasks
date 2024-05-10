# def calculate_total(items):
#     total_cost = 0
#     for item in items:
#         for i, price in item.items():
#             total_cost += price
#     return total_cost


# def calculate_total(items):
#     total_cost = 0
#     for item, price in items.items():
#         total_cost += price
#     return total_cost




# shopping_cart.py

# def calculate_total(items):
#     total = 0
#     for item, price in items.items():
#         total += price
#     return total

# shopping_cart.py

def calculate_total(items):
    total = 0
    for price in items.values():
        if price < 0:
            raise ValueError("Item price cannot be negative")
        total += price
    return total
