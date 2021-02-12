from reviews.models import Review


class ReviewLogic:
    @staticmethod
    def get_all():
        return Review.objects.all()

    @staticmethod
    def filter_by_product(product):
        return Review.objects.filter(product=product)
    
