from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.id')
	product = serializers.ReadOnlyField(source='product.id')

	class Meta:
		model = Review
		fields = '__all__' #['rating', 'advantages', 'disadvantages', 'review']
