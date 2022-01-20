from Item import Item


class TaxableItem(Item):

    def __init__(self, name,  price, quantity, tax_rate):
        super().__init__(name,  price, quantity )
        self.set_tax_rate(tax_rate)

    def get_tax_rate(self):
        return self._tax_rate

    def set_tax_rate(self, tax_rate):
        if tax_rate > 1:
            tax_rate /= 100
        self._tax_rate = tax_rate

    def buy(self, quantity_to_buy):
        before_tax = super().buy(quantity_to_buy)
        return before_tax * ( 1 + self._tax_rate )

