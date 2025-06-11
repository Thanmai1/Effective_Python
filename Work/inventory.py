from product import Product
from fileparse import parse_csv


class Inventory:
    def __init__(self):
        self._products = []

    def __iter__(self):
        return self._products.__iter__()

    def __len__(self):
        return len(self._products)

    def __getitem__(self, index):
        return self._products[index]

    def __contains__(self, val):
        return any(val == p.name for p in self._products )

    def append(self, prod):
        if not isinstance(prod, Product):
            raise TypeError("Expected a Product instance")
        self._products.append(prod)

    @classmethod
    def from_csv(cls, lines, **opts):
        inv_dicts = parse_csv(lines,
                              select=["name", "quant", "price"],
                              types=[str, int, float],
                              **opts)

        inv_p = [Product(**pr) for pr in inv_dicts]
        inv = cls()
        for pr in inv_p:
            inv.append(pr)

        return inv







    @property
    def total_cost(self):
        return sum( p.cost for p in self._products)

