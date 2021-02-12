from shop.models import Product


class ProductLogic:
    @staticmethod
    def get_all():
        return Product.objects.all()
    
    @staticmethod
    def get_by_id(id):
        return Product.objects.get(id=id)
