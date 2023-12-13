from tkinter import Tk, Label, Entry, Button, Text
from sales import SalesReport
from datetime import datetime

# Create SalesReport instance
sales_report = SalesReport()
transaction_count = 0  # Track the number of transactions

# Function to handle generating sales report based on all transactions
def generate_sales_report():
    global transaction_count
    if transaction_count > 0:
        # Generate sales report by product
        sales_by_product = sales_report.generate_sales_by_product_report()

        # Display sales report in the GUI
        sales_report_display.delete(1.0, 'end')  # Clear previous report
        sales_report_display.insert('end', "Sales Report by Product:\n")
        for product, info in sales_by_product.items():
            sales_report_display.insert('end', f"Product: {product}, Total Quantity Sold: {info['total_quantity']}, Total Amount: ${info['total_amount']}\n")

# Function to handle generating sales report for each transaction
def generate_transaction_report():
    global transaction_count
    # Retrieve user input from the GUI fields
    product_name = product_name_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())

    # Calculate total amount
    total_amount = quantity * price

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
