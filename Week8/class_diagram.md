# Week 8 UML class diagram

`-` means private; `+` means public. Inventory stores Product objects.

```mermaid
classDiagram
    class Product {
        -str __product_id
        -str __name
        -float __price
        -int __stock
        +__init__(product_id: str, name: str, price: float, stock: int)
        +get_product_id() str
        +update_stock(quantity: int) None
        +display_information() None
        +to_dict() dict
    }
    class Inventory {
        -list~Product~ __products
        +__init__()
        +add_product(product: Product) None
        +search_product(product_id: str) Product_or_None
        +update_stock(product_id: str, quantity: int) bool
        +display_all() None
        +to_list() list
    }
    Inventory "1" o-- "0..*" Product : stores
```

Product owns and validates its data. Inventory manages the collection. The main
program handles input and menu choices; separate functions load and save JSON.
Only dictionaries at the file boundary are serialized; products in memory are objects.
