from tkinter import Tk, Label, Entry, Button, Text, Toplevel, messagebox
from sales import SalesReport
from inventory import inventory_instance, Phone  # Import inventory_instance from inventory
from datetime import datetime

# Create SalesReport instance
sales_report = SalesReport()
transaction_count = 0  # Track the number of transactions

# Keep track of out-of-stock items
out_of_stock_items = []

# Function to handle generating sales report based on all transactions
def generate_sales_report():
    global transaction_count, out_of_stock_items
    if transaction_count > 0:
        # Check inventory for low stock or out-of-stock items
        low_stock_products = inventory_instance.check_inventory()

        # Generate sales report by product
        sales_by_product = sales_report.generate_sales_by_product_report()

        # Display sales report in the GUI
        sales_report_display.delete(1.0, 'end')  # Clear previous report
        sales_report_display.insert('end', "Sales Report by Product:\n")
        for product, info in sales_by_product.items():
            # Enhance to display remaining inventory level
            try:
                remaining_inventory = inventory_instance.products[product].quantity
            except KeyError:
                remaining_inventory = "Not available in inventory"
            sales_report_display.insert('end', f"Product: {product}, Total Quantity Sold: {info['total_quantity']}, Total Amount: ${info['total_amount']}, Remaining Inventory: {remaining_inventory}\n")

        # Collect out-of-stock items
        out_of_stock_items = [product for product in low_stock_products if product.quantity == 0]

        # Display out-of-stock items in a summary window
        if out_of_stock_items:
            show_warning_messages(out_of_stock_items)

        # Display remaining inventory in a new window
        show_remaining_inventory()

# Function to display warning messages in a new window
def show_warning_messages(products):
    warning_window = Toplevel(root)
    warning_window.title("Warning: Inventory Status")

    warning_label = Label(warning_window, text="Inventory Status:")
    warning_label.pack()

    for product in products:
        warning_text = f"{product.name}: Quantity available - {product.quantity}"
        warning_message = Label(warning_window, text=warning_text)
        warning_message.pack()

# Function to display remaining inventory in a new window
def show_remaining_inventory():
    remaining_inventory_window = Toplevel(root)
    remaining_inventory_window.title("Remaining Inventory")

    remaining_inventory_label = Label(remaining_inventory_window, text="Remaining Inventory:")
    remaining_inventory_label.pack()

    for product_name, product in inventory_instance.products.items():
        # Display remaining inventory only if the product exists in the inventory
        if product_name in inventory_instance.products:
            remaining_inventory_text = f"{product_name}: {product.quantity}"
            remaining_inventory_message = Label(remaining_inventory_window, text=remaining_inventory_text)
            remaining_inventory_message.pack()

# Function to handle generating sales report for each transaction
def generate_transaction_report():
    global transaction_count
    # Retrieve user input from the GUI fields
    product_name = product_name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    # Validate input
    if not (product_name and quantity and price):
        messagebox.showwarning("Missing Information", "Please enter product name, quantity, and price per unit.")
        return

    # Check if the product exists in the inventory
    if product_name not in inventory_instance.products:
        # Display a warning message
        confirmation = messagebox.askyesno("Product Not Found", f"{product_name} not found in the inventory. Do you want to proceed?")
        if not confirmation:
            return  # Cancel the transaction if the user chooses not to proceed

        # Add the product to the inventory with a default quantity
        default_quantity = 10  # You can adjust this default quantity as needed
        inventory_instance.add_product(Phone(product_name, 0, default_quantity))

    # Check if the quantity is available in the inventory
    try:
        quantity = int(quantity)
        if quantity > inventory_instance.products[product_name].quantity:
            messagebox.showwarning("Insufficient Quantity", f"Insufficient quantity for {product_name} in the inventory.")
            return
    except ValueError:
        messagebox.showwarning("Invalid Quantity", "Please enter a valid quantity.")
        return

    price = float(price)

    # Calculate total amount
    total_amount = quantity * price

    # Deduct the sold quantity from the inventory only if the product exists in the inventory
    if product_name in inventory_instance.products:
        inventory_instance.products[product_name].quantity -= quantity

    # Add the sale to the SalesReport instance with the current date and time
    sales_report.add_sale(product_name, quantity, total_amount, date=datetime.now())

    # Display total amount in the GUI
    transaction_report_display.insert('end', f"Transaction {transaction_count + 1} - Product: {product_name}, Quantity: {quantity}, Total Amount: ${total_amount}\n")
    transaction_count += 1

# Create Tkinter window
root = Tk()
root.title("ABC Business Sales Report")

# GUI elements for input
Label(root, text="Product Name:").pack()
product_name_entry = Entry(root)
product_name_entry.pack()

Label(root, text="Quantity:").pack()
quantity_entry = Entry(root)
quantity_entry.pack()

Label(root, text="Price per unit:").pack()
price_entry = Entry(root)
price_entry.pack()

# Button to add transaction
add_transaction_button = Button(root, text="Add Transaction", command=generate_transaction_report)
add_transaction_button.pack()

# Text area to display transaction details
transaction_report_display = Text(root, height=10, width=50)
transaction_report_display.pack()

# Button to generate sales report
generate_report_button = Button(root, text="Generate Sales Report", command=generate_sales_report)
generate_report_button.pack()

# Text area to display sales report
sales_report_display = Text(root, height=10, width=50)
sales_report_display.pack()

# Run the Tkinter GUI
root.mainloop()
