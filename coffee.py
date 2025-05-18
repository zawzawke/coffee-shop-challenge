from order import Order

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee must be a string.")
        
        if len(name) < 3:
            raise ValueError("Coffee name should be atleast 3 characters long.")
        self._name = name # its immutabale, has no setter

    @property
    def name(self):
        return self._name
    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)    