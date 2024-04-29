import inventory_management, cart_management, product_management

inventory = inventory_management.Inventory()
cart = cart_management.ShopingCart()
order_id = 0

while True:
    print("-- Online Shopping Application --\n")
    choice = int(input("1. Add Product\n2. Update Product\n3. Remove Product\n4. Display Inventory\n5. Add to Cart\n6. Remove from Cart\n7. Display Cart\n8. Checkout\n"))

    if choice == 1:
        try:
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = product_management.Product(product_id, name, price, quantity)
            inventory.add_product(product)
            print("Product added successfully.")

        except ValueError:
            print("Invalid input. Try again.")
            continue

    elif choice == 2:
        try:
            product_id = input("Enter product ID to update: ")
            new_name = input("Enter new name: ")
            new_price = float(input("Enter new price: "))
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_product(product_id, new_name, new_price, new_quantity)

        except ValueError:
            print("Invalid input. Try again.")
            continue

    elif choice == 3:
        product_id = input("Enter product ID to remove: ")
        inventory.remove_product(product_id)

    elif choice == 4:
        print("\nInventory:")
        inventory.display_inventory()

    elif choice == 5:
        flag = 0
        product_id = input("Enter product ID to add to cart: ")
        for product in inventory.products:
            if product.product_id == product_id:
                if product.quantity > 0:
                    cart.add_to_cart(product)
                    product.quantity-=1
                    print("Product added to cart.")
                    flag = 1
                    break
                else:
                    print("Product is out of stock. Try again later.")
                    flag = 2
        if flag == 0:
            print(f"Product with id {product_id} not found in inventory.")

    elif choice == 6:
        product_id = input("Enter product ID to remove from cart: ")
        cart.remove_from_cart(product_id)

    elif choice == 7:
        print("\nShopping Cart:")
        cart.display_cart()

    elif choice == 8:
        print("Enter shipping details\n")
        name = input("Name: ")
        adr = input("Address: ")
        payment = input("Credit card | Cash on deliver: ")

        print("\n-- Order Summary --")
        print(f"Order id: #{order_id} will be shipped to {adr}\nPayment is successful by {payment} - {name}\n\t\tThank You!\n")
        order_id+=1

        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")