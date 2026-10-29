"""Represent one product and control changes to its stock."""

import math


class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        if not isinstance(product_id, str) or not product_id.strip():
            raise ValueError("Product ID cannot be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValueError("Price must be a number.")
        if not math.isfinite(price) or price < 0:
            raise ValueError("Price must be a finite, non-negative number.")

        self.__product_id = product_id.strip().upper()
        self.__name = name.strip()
        self.__price = float(price)
        self.update_stock(stock)

    def get_product_id(self) -> str:
        return self.__product_id

    def update_stock(self, quantity: int) -> None:
        """Replace the stock quantity, rather than adding to it."""
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")
        self.__stock = quantity

    def display_information(self) -> None:
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def to_dict(self) -> dict:
        """Return a copy of the product's data for JSON serialization."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }
