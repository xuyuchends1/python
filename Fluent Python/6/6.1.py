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

class Promotion(ABC):
    @abstractmethod
    def discount(self,order):
        pass

class FidelityPromo(Promotion):
    def discount(self, order):
        """为积分1000或以上的顾客提供5%折扣"""
        return order.total()*0.05 if order.customer.fidelity>1000 else 0

class BulkItemPromo(Promotion):
    def discount(self,order):
        discount=0
        """单个商品20个以上提供10%"""
        for item in order.cart:
            if item.quantity>=20:
                discount+=item.total*0.01
        return discount

class LargeOrderPromo(Promotion):
    def discount(self,order):
        """订单中的不同商品达到10个或以上打7折"""
        distinct_item={item.product for item in order.cart}
        if len(distinct_item)>=10:
            return order.total()*0.07
        return 0

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),  LineItem('apple', 10, 1.5),LineItem('watermellon', 5, 5.0)]
Order(joe, cart, FidelityPromo())
Order(ann, cart, FidelityPromo())
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
Order(joe, banana_cart, BulkItemPromo())
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
Order(joe, long_order, LargeOrderPromo())
Order(joe, cart, LargeOrderPromo())
