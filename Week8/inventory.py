"""Manage a collection of Product objects, without user input or file I/O."""

from product import Product


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def search_product(self, product_id: str):
        product_id = product_id.strip().upper()
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def update_stock(self, product_id: str, quantity: int) -> bool:
        product = self.search_product(product_id)
        if product is None:
            return False
        product.update_stock(quantity)
        return True

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("------------------------------------------------")
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print("------------------------------------------------")

    def to_list(self) -> list:
        return [product.to_dict() for product in self.__products]
