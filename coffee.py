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
        