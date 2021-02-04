from rest_framework import serializers
from shop.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Product
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	class Meta:
		model = Snippet
		fields = ['url', 'id', 'highlight', 'title', 'code',
				  'linenos', 'language', 'style', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'snippets']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = [	'name',
					'cost',
					'description',
					'image',
					'displayed',
					'in_stock',
					'on_sale',
					'discount']
