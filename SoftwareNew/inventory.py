class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def display_product_info(self):
        return f"Name: {self.name}, Description: {self.description}, Price: ${self.price}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            return True
        return False

    def update_product_quantity(self, product_name, new_quantity):
        if product_name in self.products:
            self.products[product_name].update_quantity(new_quantity)
            return True
        return False

    def get_product_info(self, product_name):
        if product_name in self.products:
            return self.products[product_name].display_product_info()
        return "Product not found"
