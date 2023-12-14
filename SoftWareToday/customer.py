class Customer:
    def __init__(self, name, contact_details):
        self.name = name
        self.contact_details = contact_details
        self.purchase_history = []

    def add_purchase(self, product_name, quantity, total_amount):
        self.purchase_history.append({
            'product_name': product_name,
            'quantity': quantity,
            'total_amount': total_amount
        })

    def display_customer_info(self):
        return f"Name: {self.name}, Contact: {self.contact_details}"

class CustomerDatabase:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.name] = customer

    def remove_customer(self, customer_name):
        if customer_name in self.customers:
            del self.customers[customer_name]
            return True
        return False

    def get_customer_info(self, customer_name):
        if customer_name in self.customers:
            return self.customers[customer_name].display_customer_info()
        return "Customer not found"
