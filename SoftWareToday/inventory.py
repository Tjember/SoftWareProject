# inventory.py

class Phone:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

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
        if product.name in self.products:
            # If the product already exists, update the quantity
            self.products[product.name].quantity += product.quantity
        else:
            # If the product is not in the inventory, add it
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

    def check_inventory(self, threshold=5):
        low_stock_products = [product for product in self.products.values() if product.quantity <= threshold]
        return low_stock_products

# Add phone types and their price list
inventory_instance = Inventory()
inventory_instance.add_product(Phone("Samsung Note+", 800, 2))
inventory_instance.add_product(Phone("Iphone X", 1010, 34))
inventory_instance.add_product(Phone("Iphone 11", 1100, 54))
inventory_instance.add_product(Phone("Iphone 12", 1130, 54))
inventory_instance.add_product(Phone("Iphone 13", 1100, 54))
inventory_instance.add_product(Phone("Iphone 14", 1130, 74))
inventory_instance.add_product(Phone("Iphone 15", 1180, 24))
inventory_instance.add_product(Phone("Iphone 11 Pro Max", 1100, 40))
inventory_instance.add_product(Phone("Iphone 12 Pro Max", 1150, 200))
inventory_instance.add_product(Phone("Iphone 13 Pro Max", 120, 10))
inventory_instance.add_product(Phone("Iphone 14 Pro Max", 12500, 21))
inventory_instance.add_product(Phone("Iphone 15 Pro Max", 1400, 300))
inventory_instance.add_product(Phone("Samsung Galaxy 7", 900, 20))
inventory_instance.add_product(Phone("Samsung Galaxy 8", 970, 15))
inventory_instance.add_product(Phone("Samsung Note 10", 1120, 8))
inventory_instance.add_product(Phone("Samsung Galaxy 10", 1050, 50))
inventory_instance.add_product(Phone("Nokia", 1200, 50))
inventory_instance.add_product(Phone("Lenovo", 1000, 45))
# we can add more items here and this is a sample one
