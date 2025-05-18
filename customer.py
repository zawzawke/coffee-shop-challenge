from order import Order

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.") 
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})    

       
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        customer_spending = {}

        for order in Order.all:
            if order.coffee == coffee:
                customer = order.customer
                customer_spending[customer] = customer_spending.get(customer, 0) + order.price

        if not customer_spending:
            return None

        return max(customer_spending, key=customer_spending.get)         
    

         


        