class SalesReport:
    def __init__(self):
        self.sales_data = []

    def add_sale(self, product_name, quantity, total_amount, date=None):
        self.sales_data.append({
            'product_name': product_name,
            'quantity': quantity,
            'total_amount': total_amount
        })

    def generate_sales_by_product_report(self):
        sales_by_product = {}
        for sale in self.sales_data:
            product_name = sale['product_name']
            if product_name not in sales_by_product:
                sales_by_product[product_name] = {
                    'total_quantity': 0,
                    'total_amount': 0
                }
            sales_by_product[product_name]['total_quantity'] += sale['quantity']
            sales_by_product[product_name]['total_amount'] += sale['total_amount']

        return sales_by_product

    def generate_daily_sales_report(self):
        # Placeholder for generating daily sales report
        daily_sales = {}
        # Implement logic to generate daily sales report based on sales_data
        return daily_sales

    def generate_monthly_sales_summary(self):
        # Placeholder for generating monthly sales summary
        monthly_summary = {}
        # Implement logic to generate monthly sales summary based on sales_data
        return monthly_summary

    # Other methods for additional reports...

    def display_sales_report(self, report_type='product'):
        # Display sales report based on report_type
        if report_type == 'product':
            report_data = self.generate_sales_by_product_report()
            # Logic to display sales report by product
            print("Sales Report by Product:")
            for product, info in report_data.items():
                print(f"Product: {product}, Total Quantity Sold: {info['total_quantity']}, Total Amount: ${info['total_amount']}")
