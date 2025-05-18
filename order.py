class Order:
    _all = [] #keeps track of all orders

    def __init__(self, customer, coffee, price):
       

        # validations
        from customer import Customer
        from coffee import Coffee
        
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
        Order._all.append(self) #tracks the order instance

        @property
        def price(self):
            return self._price
        
        @property
        def customer(self):
            return self._customer
        
        @property
        def coffee(self):
            return self._coffee
        
        @property
        def price(self):
            return self._price
        
        @classmethod
        def all(cls):
            return cls._all
        