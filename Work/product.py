from typedproperty import typedproperty

class Product:
    # __slots__ = ('name', '_quant', 'price')
    name = typedproperty("name", str)
    quant = typedproperty("quant", int)
    price = typedproperty("price", float)

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




