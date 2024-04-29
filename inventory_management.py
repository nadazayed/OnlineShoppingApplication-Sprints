class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_product(self, product_id, new_name, new_price, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.name = new_name
                product.price = new_price
                product.quantity = new_quantity
                print(f"Product with id {product_id} updated successfully.")
                return
        print(f"Product with id {product_id} doesn't exist!")

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product with id {product_id} removed successfully.")
                return
        print(f"Product with id {product_id} doesn't exist!")

    def display_inventory(self):
        for product in self.products:
            print(product.display())
            
