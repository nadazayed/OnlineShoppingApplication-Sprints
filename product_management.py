class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    