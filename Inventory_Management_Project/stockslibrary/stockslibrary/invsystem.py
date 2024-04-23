def calculate_total_quantity(product_items):
    """
    Function to calculate the total quantity of products.
    Takes a queryset of product items as input and returns the total quantity.
    """
    total_quantity = sum(product_item.quantity for product_item in product_items)
    return total_quantity