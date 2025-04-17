class Inventory:
    def __init__(self, products):
        self._products = products

    @property
    def total_cost(self):
        return sum( p.cost for p in self._products)

