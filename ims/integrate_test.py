import unittest
from ims import Product, Supplier, Order, OrderItem, Inventory


class IntegrationTest(unittest.TestCase):
    def test_product_supplier_association(self):

        product = Product(1, "Laptop", "Apple MacBook Pro",
                          1299.99, 10, "Apple")

        self.assertEqual(product.product_supplier, "Apple")

    def test_order_inventory_update(self):

        product = Product(1, "Laptop", "Apple MacBook Pro",
                          1299.99, 10, "Apple")
        inventory = Inventory(1, 1, 10)

        order = Order(1, "2023-10-04", "pending", [OrderItem(product, 2)])

        order.update_order_status("processing")
        self.assertEqual(inventory.quantity, 10)

    def test_supplier_product_information_sync(self):

        product = Product(1, "Laptop", "Apple MacBook Pro",
                          1299.99, 10, "Apple")
        supplier = Supplier(
            1, "Acme Electronics", "support@acme.com", "123 Main St., town, CA 98765")

        supplier.supplier_contact = "newsupport@acme.com"


if __name__ == "__main__":
    from test_ims import ProductTest, SupplierTest, OrderItemTest, OrderTest, InventoryTest
    unittest.main()
