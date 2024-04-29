class ShopingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)

    def remove_from_cart(self, product_id):
        for product in self.items:
            if product.product_id == product_id:
                self.items.remove(product)
                product.quantity+=1
                print("Item removed from cart.")
                return
        print(f"Product with id {product_id} doesn't exist!")

    def display_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            for item in self.items:
                print(item.display())