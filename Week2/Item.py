class Item:

    def __init__(self, name, price, quantity):
        self._name = name
        self.set_price(price)
        self.set_quantity(quantity)

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def set_price(self, price):
        if price > 0:
            self._price = price
            # todo - defensive checks

    def set_quantity(self, quantity):
        if quantity >= 0:
            self._quantity = quantity
            # todo - defensive checks

    def buy(self, quantity_to_buy):
        if quantity_to_buy <= self._quantity:
            self._quantity -= quantity_to_buy
            return quantity_to_buy * self._price
        return 0

