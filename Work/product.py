class Product:
    __slots__ = ('name', '_quant', 'price')

    def __init__(self, name, quant, price):
        self.name = name
        self.quant = quant
        self.price = price


    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        self._quant = value

    @property
    def cost(self):
        return self.quant * self.price

    def sell(self, n_units):
        self.quant = self.quant - n_units




