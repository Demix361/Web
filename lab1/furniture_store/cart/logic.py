from cart.models import Cart, CartItem, Order, OrderItem


class CartLogic:
    @staticmethod
    def get_all():
        return Cart.objects.all()
    
    @staticmethod
    def get_by_user(user):
        return Cart.objects.get(user=user)
    
    @staticmethod
    def get_by_id(id):
        return Cart.objects.get(id=id)
        

class CartItemLogic:
    @staticmethod
    def filter_by_cart(cart):
        return CartItem.objects.filter(cart=cart)


class OrderLogic:
    @staticmethod
    def get_all():
        return Order.objects.all()
    
    @staticmethod
    def filter_by_user(user):
        return Order.objects.filter(user=user)


class OrderItemLogic:
    @staticmethod
    def get_all():
        return OrderItem.objects.all()
    
    @staticmethod
    def filter_by_order(order):
        return OrderItem.objects.filter(order=order)
