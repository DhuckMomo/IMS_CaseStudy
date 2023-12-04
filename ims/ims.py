class Product:
    def __init__(self, product_id, product_name, product_description, product_price, product_quantity, product_supplier):
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_supplier = product_supplier

    def get_product_id(self):
        return self.product_id

    def get_product_name(self):
        return self.product_name

    def get_product_description(self):
        return self.product_description

    def get_product_price(self):
        return self.product_price

    def get_product_quantity(self):
        return self.product_quantity

    def get_product_supplier(self):
        return self.product_supplier

    def set_product_name(self, name):
        self.product_name = name

    def set_product_description(self, description):
        self.product_description = description

    def set_product_price(self, price):
        self.product_price = price

    def update_product_quantity(self, quantity):
        self.product_quantity += quantity


class Supplier:
    def __init__(self, supplier_id, supplier_name, supplier_contact, supplier_address):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.supplier_contact = supplier_contact
        self.supplier_address = supplier_address

    def get_supplier_id(self):
        return self.supplier_id

    def get_supplier_name(self):
        return self.supplier_name

    def get_supplier_contact(self):
        return self.supplier_contact

    def get_supplier_address(self):
        return self.supplier_address


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __eq__(self, other):
        if not isinstance(other, OrderItem):
            return False
        return self.product == other.product and self.quantity == other.quantity


class Order:
    def __init__(self, order_id, order_date, order_status, order_items):
        self.order_id = order_id
        self.order_date = order_date
        self.order_status = order_status
        self.order_items = order_items

    def get_order_id(self):
        return self.order_id

    def get_order_date(self):
        return self.order_date

    def get_order_status(self):
        return self.order_status

    def get_order_items(self):
        return self.order_items

    def add_order_item(self, product, quantity):
        order_item = OrderItem(product, quantity)
        self.order_items.append(order_item)

    def update_order_status(self, status):
        self.order_status = status


class Inventory:
    def __init__(self, inventory_id, product_id, quantity):
        self.inventory_id = inventory_id
        self.product_id = product_id
        self.quantity = quantity

    def get_inventory_id(self):
        return self.inventory_id

    def get_product_id(self):
        return self.product_id

    def get_quantity(self):
        return self.quantity

    def update_quantity(self, quantity):
        self.quantity += quantity
