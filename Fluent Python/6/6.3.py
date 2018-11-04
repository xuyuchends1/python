from abc import ABC,abstractmethod
from collections import namedtuple

Customer=namedtuple('Customer','name fidelity')
class LineItem:
    def __init__(self,product,quantity,price):
        self.product=product
        self.quantity=quantity
        self.price=price

    def total(self):
        return self.price*self.quantity

class Order:
    def __init__(self,customer,cart,promotion=None):
        self.customer=customer
        self.cart=cart
        self.promotion=promotion

    def total(self):
        if not hasattr(self,'__total'):
            self.__total=sum(item.total() for item in self.cart)
            return self.__total
    def due(self):
        if self.promotion is None:
            discount=0
        else:
            discount=self.promotion.discount(self)
        return self.total()-discount

def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def bast_promo(order):
    promos=[fidelity_promo,bulk_item_promo,large_order_promo]
    return max(promo(order) for promo in promos)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),  LineItem('apple', 10, 1.5),LineItem('watermellon', 5, 5.0)]
Order(joe, cart, fidelity_promo)
Order(ann, cart, fidelity_promo)
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
Order(joe, banana_cart, bulk_item_promo)
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
Order(joe, long_order, large_order_promo)
o=Order(joe, cart, large_order_promo)

bast_promo(o)