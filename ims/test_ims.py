import unittest
from ims import Product, Supplier, OrderItem, Order, Inventory


class ProductTest(unittest.TestCase):
    def test_product_attributes(self):
        product = Product(1, "Laptop", "Apple MacBook Pro",
                          1299.99, 10, "Apple")
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.product_name, "Laptop")
        self.assertEqual(product.product_description, "Apple MacBook Pro")
        self.assertEqual(product.product_price, 1299.99)
        self.assertEqual(product.product_quantity, 10)
        self.assertEqual(product.product_supplier, "Apple")

    def test_update_product_quantity(self):
        product = Product(1, "Laptop", "Apple MacBook Pro",
                          1299.99, 10, "Apple")
        product.update_product_quantity(5)
        self.assertEqual(product.product_quantity, 15)


class SupplierTest(unittest.TestCase):
    def test_supplier_attributes(self):
        supplier = Supplier(
            1, "Acme Electronics", "support@acme.com", "123 Main St., town, CA 98765")
        self.assertEqual(supplier.supplier_id, 1)
        self.assertEqual(supplier.supplier_name, "Acme Electronics")
        self.assertEqual(supplier.supplier_contact, "support@acme.com")
        self.assertEqual(supplier.supplier_address,
                         "123 Main St., town, CA 98765")


class OrderItemTest(unittest.TestCase):
    def test_order_item_attributes(self):
        product = Product(1, "Laptop", "Apple MacBook Pro",
                          1299.99, 10, "Apple")
        order_item = OrderItem(product, 2)
        self.assertEqual(order_item.product, product)
        self.assertEqual(order_item.quantity, 2)


class OrderTest(unittest.TestCase):
    def test_order_attributes(self):
        order = Order(1, "2023-10-04", "pending", [])
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.order_date, "2023-10-04")
        self.assertEqual(order.order_status, "pending")
        self.assertEqual(order.order_items, [])

    def test_add_order_item(self):
        product = Product(1, "Laptop", "Apple MacBook Pro",
                          1299.99, 10, "Apple")
        order = Order(1, "2023-10-04", "pending", [])
        order.add_order_item(product, 2)
        self.assertEqual(order.order_items, [OrderItem(product, 2)])

    def test_update_order_status(self):
        order = Order(1, "2023-10-04", "pending", [])
        order.update_order_status("processing")
        self.assertEqual(order.order_status, "processing")


class InventoryTest(unittest.TestCase):
    def test_inventory_attributes(self):
        inventory = Inventory(1, 1, 10)
        self.assertEqual(inventory.inventory_id, 1)
        self.assertEqual(inventory.product_id, 1)
        self.assertEqual(inventory.quantity, 10)

    def test_update_quantity(self):
        inventory = Inventory(1, 1, 10)
        inventory.update_quantity(5)
        self.assertEqual(inventory.quantity, 15)


if __name__ == "__main__":
    from test_ims import ProductTest, SupplierTest, OrderItemTest, OrderTest, InventoryTest
    unittest.main()
