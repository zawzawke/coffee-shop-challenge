from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        if not isinstance(price, float):
            raise TypeError("price must be a float.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 amd 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price # is immutable, has no setter

        @property
        def price(self):
            return self._price
        
        @property
        def customer(self):
            return self._customer
        
        @property
        def coffee(self):
            return self._coffee
        