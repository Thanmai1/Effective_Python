class Product:
    def __init__(self, name, quant, price):
        self.name = name
        self.quant = quant
        self.price = price

    def cost(self):
        return self.quant * self.price

    def sell(self, n_units):
        self.quant = self.quant - n_units




