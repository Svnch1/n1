def bigger_price(n, products):
    sorted_products = sorted(products, key=lambda x: x["price"], reverse=True)
    return sorted_products[:n]

# Example usage:
print(bigger_price(2, [{"name": "wine", "price": 138},
                       {"name": "bread", "price": 100},
                       {"name": "meat", "price": 15},
                       {"name": "water", "price": 1}]))

print(bigger_price(1, [{"name": "pen", "price": 5},
                       {"name": "whiteboard", "price": 170}]))
