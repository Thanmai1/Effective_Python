from typedproperty import typedproperty
from typedproperty import String, Integer, Float

class Product:
    # __slots__ = ('name', '_quant', 'price')
    name = String("name")
    quant = Integer("quant")
    price = Float("price")

    def __init__(self, name, quant, price):
        self.name = name
        self.quant = quant
        self.price = price

    def __repr__(self):
        return f'Product({self.name}, {self.quant}, {self.price})'

    @property
    def cost(self):
        return self.quant * self.price

    def sell(self, n_units):
        self.quant = self.quant - n_units




